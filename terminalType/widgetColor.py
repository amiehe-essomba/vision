from configure      import colors, init
from terminalType   import codeBgColor as CB

def widgetColor(name : str = "monokai"):
    widgetColor = {
        "monokai"   : CB.codeBgColor(name="monokai")    + init.init.bold + colors.fg.rbg(255, 255, 255),
        "orion"     : CB.codeBgColor(name="orion")      + init.init.bold + colors.fg.rbg(100, 150, 103),
        "pegasus"   : CB.codeBgColor(name="pegasus")    + init.init.bold + colors.fg.rbg(100, 150, 203),
        "solo"      : CB.codeBgColor(name="solo")       + init.init.bold + colors.fg.rbg(0, 150, 20), 
        "skyBlue"   : CB.codeBgColor(name="skyBlue")    + init.init.bold + colors.fg.rbg(0, 200, 50),
        "mirage"    : CB.codeBgColor(name="mirage"),
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
    
    return  widgetColor[name]