from setuptools import setup, find_packages

VERSION = '0.01' 
DESCRIPTION = 'Control SAP by python program'
LONG_DESCRIPTION = 'Control SAP by python program'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pyautosap", 
        version=VERSION,
        author="LIU YUAN",
        author_email="Yuan.LIU7@cn.bosch.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        url = 'https://github.boschdevcloud.com/LYU3CGD4/pyautosap',
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'pyautosap'],
        classifiers= [
            "Development Status :: 1 - Alpha",
            "Intended Audience :: Education",
            ' Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: Microsoft :: Windows'
        ]
)