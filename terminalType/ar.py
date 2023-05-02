from configure      import colors, init
from terminalType   import codeBgColor as CB

def arithmetic(name : str = "monokai"):
    color_fg = colors.fg
    ar = {
        "monokai"   : CB.codeBgColor(name="monokai")    + color_fg.rbg(255, 0, 0),
        "orion"     : CB.codeBgColor(name="orion")      + color_fg.rbg(255, 102, 0), 
        "pegasus"   : CB.codeBgColor(name="pegasus")    + color_fg.rbg(255, 102, 0),
        "solo"      : CB.codeBgColor(name="solo")       + color_fg.rbg(255, 102, 0), 
        "skyBlue"   : CB.codeBgColor(name="skyBlue")    + color_fg.rbg(255, 102, 0),
        "mirage"    : CB.codeBgColor(name="mirage")     + color_fg.rbg(255, 102, 0),
        "material"  : CB.codeBgColor(name="material")   + color_fg.rbg(255, 102, 0),
        "night"     : CB.codeBgColor(name="night")      + color_fg.rbg(255, 102, 0), 
        "solarized" : CB.codeBgColor(name="solarized")  + color_fg.rbg(255, 102, 0),
        "spectrum"  : CB.codeBgColor(name="spectrum")   + color_fg.rbg(255, 102, 0),
        "winter"    : CB.codeBgColor(name="winter")     + color_fg.rbg(255, 102, 0),
        "summer"    : CB.codeBgColor(name="summer")     + color_fg.rbg(255, 102, 0), 
        "fall"      : CB.codeBgColor(name="fall")       + color_fg.rbg(255, 102, 0),
        "spring"    : CB.codeBgColor(name="spring")     + color_fg.rbg(255, 102, 0),
        "espresso"  : CB.codeBgColor(name="espresso")   + color_fg.rbg(255, 102, 0),
        "darker"    : CB.codeBgColor(name="darker")     + color_fg.rbg(255, 102, 0),
        "ocean"     : CB.codeBgColor(name="ocean")      + color_fg.rbg(255, 102, 0),
        "light"     : CB.codeBgColor(name="light")      + color_fg.rbg(255, 102, 0),
    }
    
    return ar[name]