from pywinauto.application import Application
import os
import re
import time
import win32gui,win32com.client

class sap():
    def __init__(self,path):
        self.app = Application().connect(path=path)


    def foreground_window(self,window_title):
        hwnd = win32gui.FindWindow(None, window_title)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(hwnd)
    

    def get_Info_bar(self,textbarFile):
        '''
        Get the content of information bar at the bottom left corner.
        :param textbarFile: path of txt file
        :return: content of information bar at the bottom left corner
        '''
        app=self.app['SAP_FRONTEND_SESSION']
        d = app.child_window(class_name_re = 'Afx:[\s\S]*?0000:8:0001000\d{1}:00000010:00000000')
        d.print_control_identifiers(filename=textbarFile)
        textList=[]
        with open(textbarFile) as FileObj: 
            for line in FileObj: 
                textList.append(line)
        text=re.findall('title="([\s\S]*?)",',''.join(textList))
        if len(text)==0:
            return None
        elif len(text)>1:
            raise ValueError('have multiple text from info bar.')
        else:
            return text[0]


    def get_FRONTEND_SESSION_title(self,txtFile):
        '''
        This will only return one title of SAP window
        Note: FRONTEND_SESSION is a calss of SAP
        :param textbarFile: path of txt fileS
        '''
        app=self.app['SAP_FRONTEND_SESSION']
        app.print_control_identifiers(depth=1,filename=txtFile)
        text=[]
        with open(txtFile) as FileObj: 
            for line in FileObj:  
                text=re.findall('title="([\s\S]*?)"',line)      
                if len(text) ==1:
                    break
        if len(text)==0:
            return None
        elif len(text)>1:
            raise ValueError('get multiple FRONTEND_SESSION window name!!!')
        else:
            return text[0]


    def check_easyAccess(txtFile):
        systemTitle=sap.get_FRONTEND_SESSION_title(txtFile)
        if 'Easy Access' in systemTitle:
            time.sleep(1)
            return True
        else:
            return False

    def check_popOut_window(self,systemTitle):
    
        window_list = self.app.windows()
        filtered_list=[]
        for window in window_list:
            if window.friendly_class_name()=='Dialog' and window.is_dialog()==True and window.owner()!=None and window.element_info.visible==True:
                if window.owner().element_info.name==systemTitle :
                    filtered_list.append(window)
        
        if len(filtered_list)==0:
            return None
        elif len(filtered_list)>1:
            raise ValueError('get multiple pop-out window !!!')
        else:
            return filtered_list[0]


    def click_topWindow_button(self,DialogTitle,buttonTitle):
        button=self.app[DialogTitle][buttonTitle]
        button.click()


    def screen_shot(self,path,img_name):
        win = self.app['SAP_FRONTEND_SESSION']
        self.foreground_window(win.element_info.name)
        win.capture_as_image().save(r'' + path + os.sep + img_name  +'.png')

def load_window(path):
    app_obj=sap(path)
    return app_obj



