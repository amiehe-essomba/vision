from configure      import colors, init
from terminalType   import codeBgColor as CB

def B(name : str = "monokai"):
    color_fg = colors.fg
    ar = {
        "monokai"   : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "orion"     : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "pegasus"   : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "solo"      : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            }, 
        "skyBlue"   : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "mirage"    : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "material"  : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "night"     : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            }, 
        "solarized" : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "spectrum"  : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "winter"    : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "summer"    : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            }, 
        "fall"      : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "spring"    : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "espresso"  : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "darker"    : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "ocean"     : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
        "light"     : {
            "("     : CB.codeBgColor(name="monokai")    + color_fg.rbg(0, 255, 0),
            "["     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 0),
            "{"     : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 255, 153), 
            },
    }
    
    return ar[name]