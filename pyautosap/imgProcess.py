import pyautogui
import win32gui, win32com.client
import numpy
import cv2


def window_match(TargetImg,className=None,windowName=None,offset_x=0,offset_y=0, debug=False):
    '''
    The function will take a screenshot of a window and compare with Target image.
    
    '''
    if className==None and windowName==None:
        raise Exception('Function need a className or windowName')
    
    #Get window handle
    hwnd = win32gui.FindWindow(className,windowName)
    #foreground the window
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)
    #get window size and position
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    #Take screenshot and save as matrix
    screenImg = pyautogui.screenshot(region=[left,top, right-left ,bottom-top])
    #convert to numpy array
    screenImg = numpy.asarray(screenImg)

    img = cv2.imread(TargetImg,1)
    h,w,c=img.shape
    res = cv2.matchTemplate(screenImg,img,cv2.TM_CCOEFF_NORMED)
    print(len(res))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #calculate abslout position on screen
    abs_x= left + max_loc[0] + w/2 +offset_x
    abs_y= top + max_loc[1] + h/2 + offset_y
    

    if debug:
        debug_img = cv2.cvtColor(screenImg, cv2.COLOR_RGB2BGR)
        top_left = max_loc #top left corner
        bottom_right = (top_left[0] + w, top_left[1] + h) #bottom right corner
        cv2.rectangle(debug_img,top_left, bottom_right, (0,0,255), 2)
        cv2.line(debug_img,(int(max_loc[0] + w/2) , int(max_loc[1] + h/2)),(int(max_loc[0] + w/2 +offset_x),int(max_loc[1] + h/2 + offset_y)),(0,0,255), 2)
        cv2.imshow('Debug Mode', debug_img)
        cv2.waitKey(0)
        return

    pyautogui.moveTo(abs_x,abs_y)
