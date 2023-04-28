import os, sys
import platform
import mainLinux
import mainWin
import webbrowser
from configure      import colors, init
from configure	    import clear, moveCursor
from pathlib		import Path
from fileType	    import fileType as FT
from fileType	    import readfile as RT
from configure      import screenConfig, colors, init
from keywords       import key_py
from images         import * 
from style          import style, languageStyle 
from terminalType   import Terminal

def open_graven_web():
        webbrowser.open(url='https://github.com/amiehe-essomba/vision')
        
def visionEditor( ):
    """
    # bg color 
    fgBlack                 = init.init.bold + colors.fg.rbg(10, 10, 10)
    # bg color 
    bgWhite                 = init.init.bold + colors.bg.rgb(255, 255, 255)
    # bg color 
    codeBgColors            = init.init.bold + colors.bg.rgb(0, 0, 0)
    # fg color 
    codeFgColors            = init.init.bold + colors.fg.rbg(255,255,255)
    # building color 
    codeColors              = codeBgColors + init.init.bold + colors.fg.rbg(255, 255, 255)
    # widget color 
    widgetColors            = codeBgColors + init.init.bold + colors.fg.rbg(255, 255, 255)
    #keyword found color 
    KeyColor                = init.init.bold + colors.bg.rgb(200, 200, 0) + init.init.bold + colors.fg.rbg(255, 255, 255)
    # comment color 
    commentColor            = codeBgColors  + colors.fg.rbg(153, 153, 255) 
    #string color 
    strColor                = codeBgColors + colors.bg.rgb(100, 100, 100) + colors.fg.rbg(255, 153, 20)
    #title color            
    titleColor              = init.init.bold + colors.fg.rbg(0, 255, 0)
    #program color 
    proColor                = init.init.bold+init.init.blink+ codeBgColors + colors.fg.rbg(0, 255, 0)
    #col and raw color 
    ColRawColor             = init.init.bold+init.init.blink+ codeBgColors + colors.fg.rbg(255, 100, 255)
    #opened, closed
    openedColor             = init.init.bold+init.init.blink+ codeBgColors + colors.fg.rbg(0, 255, 255)
    #cursor color 
    cursorColor             = codeBgColors + colors.fg.rbg(255,0,0)+chr(9664)
    # colors used 
    COLOR                   = {
        "fgColor"   : codeColors, 
        "bgColor"   : codeBgColors, 
        "wColor"    : widgetColors, 
        "keyColor"  : KeyColor,
        "cmtColor"  : commentColor,
        "strColor"  : strColor, 
        "white"     : codeFgColors,
        "titleColor": titleColor,
        "proColor"  : proColor,
        "CRColor"   : ColRawColor,
        "openedColor" :openedColor,
        "cursorColor" : cursorColor, 
        "bgWhite"   : bgWhite, 
        "fgBlack"   : fgBlack 
        }
    """
    
    
    # get root path 
    root	                = os.path.abspath(os.curdir)
    # path parent
    s                       = Path(__file__).resolve().parents[2]
    # get system name
    system                  = platform.system()
    # get arguments 
    arg	                    = sys.argv
    # coustomized terminal 
    terminal                = "monokai"
    #colors used
    COLOR = Terminal.termianlConfig(name = terminal)
    # get screen coordinate (x_max, y_max)
    max_x, max_y            = screenConfig.cursorMax()
    # set color 
    color                   = colors.fg.rbg(255,0,0) + init.init.bold+init.init.blink
    reset                   = init.init.reset
    c_bg                    = colors.bg.white_L
    
    # initilization of writeData
    writeData               = {"data" : [], "FileName" : None, "action" : False}
    data				    = {"writing" : [""], "string" : [""], "input" : [], "color" : {"color" : [color], "m" : [0], "n" : [0], "locked": [False]}}
    #
    locked                  = False
    

    if system in ['Windows', "Linux", "MacOS"]: 
        if   len(arg) == 1 :  termios, language   = "none", "unknown"
        elif len(arg) == 2 : 
            if arg[1]: 
                ext = FT.file(arg[1])
                if ext is not None : 
                    termios, language = terminal, ext
                    if system == "Windows" :  name = root + f"\\{arg[1]}"
                    else:  name = root + f"/{arg[1]}"
                    try:
                        if os.stat(name).st_size != 0 :  data = RT.readFile(fileName=name, termios=termios, language=language, COLOR=COLOR.copy())
                        else:  pass
                    except FileNotFoundError : pass 
                   
                    writeData["FileName"]   = arg[1]
                    writeData["data"]	    = data['string'].copy()
                    writeData["action"]	    = True     
                else: termios, language = "none", "unknown"
            else : termios, language = "none", "unknown"
        elif len(arg) == 3 : 
            locked = True
            if arg[1] == "--ide":
                if arg[2] in ['-v', 'version']:
                    string = f" {colors.fg.rbg(0,0,255)}VISION IDE {colors.fg.rbg(255,0,0)}version {colors.fg.rbg(0,0,0)}1.0.1 beta"
                    print(c_bg + string + reset)
                elif arg[2] in ['-a', 'author']:
                    string = f" {colors.fg.rbg(0,0,255)}VISION IDE {colors.fg.rbg(255,0,0)}author : {colors.fg.rbg(0,0,0)}Dr. Iréné Amiehe-Essomba"
                    print(c_bg + string + reset)
                elif arg[2] in ['-g', 'github']:
                    open_graven_web()
                else: 
                    r = colors.fg.rbg(255,0,0)
                    b = colors.fg.rbg(0,0,255)
                    g = colors.fg.rbg(0,255,0)
                    string = f"vision --ide [argument]\n{r}argument {b}in {g}[-a, author, -v, version, -g, github]{reset}\n"
                    print(string + reset)
            else:
                r = colors.fg.rbg(255,0,0)
                b = colors.fg.rbg(0,0,255)
                g = colors.fg.rbg(0,255,0)
                string = f"vision --ide [argument]\n{r}argument {b}in {g}[-a, author, -v, version, -g, github]{reset}\n"
                print(string + reset)
        else:
            r = colors.fg.rbg(255,0,0)
            b = colors.fg.rbg(0,0,255)
            g = colors.fg.rbg(0,255,0)
            string = f"vision --ide [argument]\n{r}argument {b}in {g}[-a, author, -v, version, -g, github]{reset}\n"
            print(string + reset)
            locked = True 
            
        if locked is False:
            if max_x > 50:
                if max_y > 20 :
                    if   system == "Windows"	: mainWin.IDE(termios=termios, lang=language, COLOR=COLOR.copy()).VISION(importation=data, writeData =  writeData, path = root)
                    elif system == "Linux"	    : mainLinux.IDE(termios=termios, lang=language, COLOR=COLOR.copy()).VISION(importation=data, writeData =  writeData, path = root)
                    else: 
                        string = f" VISION is not distributed for {system} platform "
                        print(c_bg + color + string + reset)
                else: 
                    string = f" Increase the width of screen at least 20  : width = {max_y} "
                    print(c_bg + color + string + reset)
            else:
                string = f" Increase the height of screen at least 50 : height = {max_x} "
                print(c_bg + color + string + reset)
        else: pass
    else: 
        string = f" VISION is not distributed for {system} platform "
        print(c_bg + color + string + reset)
    
   
if __name__ == '__main__':
    sys.stdout.write(clear.clear.screen(2)+moveCursor.cursor.TO(0,0))
    sys.stdout.flush()
    visionEditor()