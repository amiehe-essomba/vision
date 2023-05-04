from configure      import colors, init
from terminalType   import codeBgColor as CB

def cursorColor(name : str = "monokai"):
    cursorColor = {
        "monokai"   : CB.codeBgColor(name="monokai")    + colors.fg.rbg(255,255,0) + chr(9664),
        "orion"     : CB.codeBgColor(name="orion")      + colors.fg.rbg(0,255,0) + chr(9664),
        "pegasus"   : CB.codeBgColor(name="pegasus")    + colors.fg.rbg(255,255,255) + chr(9664),
        "solo"      : CB.codeBgColor(name="solo")       + colors.fg.rbg(0,0,0) + chr(9664),
        "skyBlue"   : CB.codeBgColor(name="skyBlue")    + colors.fg.rbg(255,0,255) + chr(9664),
        "mirage"    : CB.codeBgColor(name="mirage")     + colors.fg.rbg(40,120,60) + init.init.rapid_blink + chr(9664),
        "material"  : CB.codeBgColor(name="material"),
        "night"     : CB.codeBgColor(name="night"), 
        "solarized" : CB.codeBgColor(name="solarized"),
        "spectrum"  : CB.codeBgColor(name="spectrum"),
        "winter"    : CB.codeBgColor(name="winter"),
        "summer"    : CB.codeBgColor(name="summer"), 
        "fall"      : CB.codeBgColor(name="fall"),
        "spring"    : CB.codeBgColor(name="spring"),
        "espresso"  : CB.codeBgColor(name="espresso"),
        "darker"    : CB.codeBgColor(name="darker"),
        "ocean"     : CB.codeBgColor(name="ocean"),
        "light"     : CB.codeBgColor(name="light"),
    }
    
    return cursorColor[name]