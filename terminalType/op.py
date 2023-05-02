from configure      import colors, init
from terminalType   import codeBgColor as CB

def operators(name : str = "monokai"):
    op = {
        "monokai"   : CB.codeBgColor(name="monokai")    + colors.fg.rbg(255, 102, 0),
        "orion"     : CB.codeBgColor(name="orion")      + colors.fg.rbg(255, 102, 0), 
        "pegasus"   : CB.codeBgColor(name="pegasus")    + colors.fg.rbg(255, 102, 0),
        "solo"      : CB.codeBgColor(name="solo")       + colors.fg.rbg(255, 102, 0), 
        "skyBlue"   : CB.codeBgColor(name="skyBlue")    + colors.fg.rbg(255, 102, 0),
        "mirage"    : CB.codeBgColor(name="mirage")     + colors.fg.rbg(255, 102, 0),
        "material"  : CB.codeBgColor(name="material")   + colors.fg.rbg(255, 102, 0),
        "night"     : CB.codeBgColor(name="night")      + colors.fg.rbg(255, 102, 0),
        "solarized" : CB.codeBgColor(name="solarized")  + colors.fg.rbg(255, 102, 0),
        "spectrum"  : CB.codeBgColor(name="spectrum")   + colors.fg.rbg(255, 102, 0),
        "winter"    : CB.codeBgColor(name="winter")     + colors.fg.rbg(255, 102, 0),
        "summer"    : CB.codeBgColor(name="summer")     + colors.fg.rbg(255, 102, 0),
        "fall"      : CB.codeBgColor(name="fall")       + colors.fg.rbg(255, 102, 0),
        "spring"    : CB.codeBgColor(name="spring")     + colors.fg.rbg(255, 102, 0),
        "espresso"  : CB.codeBgColor(name="espresso")   + colors.fg.rbg(255, 102, 0),
        "darker"    : CB.codeBgColor(name="darker")     + colors.fg.rbg(255, 102, 0),
        "ocean"     : CB.codeBgColor(name="ocean")      + colors.fg.rbg(255, 102, 0),
        "light"     : CB.codeBgColor(name="light")      + colors.fg.rbg(255, 102, 0),
    }
    
    return op[name]