import PyInstaller.__main__ 
import os
import platform


def path_ico():
    # get ico image 
    error  = None 
    system = platform.system()
    #system  = os.uname()[0]
    if system == "Linux":
        return os.path.abspath(os.curdir)+"/images/logo-png.png"
    elif system == 'Windows':
        return os.path.abspath(os.curdir)+"\\images\\logo-png.png"
    else: pass

path = path_ico()
if path is None: print(path)
else:
    data = os.path.abspath(os.curdir)+'/Library/*;.'
    data_info = os.path.abspath(os.curdir)+'/README.md;CONTRIBUTING.md;Tools.md;CODE.md'
    PyInstaller.__main__.run([
        "vision.py",
        '--onefile',
        '--console',
        '-c',
        '--clean',
        '--nowindowed',
        f"--icon={path}",   
    ])
    