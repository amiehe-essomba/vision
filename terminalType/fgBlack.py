from configure      import colors, init
from terminalType   import codeBgColor as CB

def fgColor(name : str = "monokai"):
    Color = {
        "monokai"   : init.init.bold + colors.fg.rbg(0, 0, 0),
        "orion"     : init.init.bold + colors.fg.rbg(0, 255, 0),
        "pegasus"   : init.init.bold + colors.fg.rbg(255, 0, 0),
        "solo"      : init.init.bold + colors.fg.rbg(0, 0, 255), 
        "skyBlue"   : init.init.bold + colors.fg.rbg(0, 255, 255),
        "mirage"    : init.init.bold + colors.fg.rbg(255, 255, 0),
        "material"  : init.init.bold + colors.fg.rbg(255, 0, 255),
        "night"     : init.init.bold + colors.fg.rbg(0, 0, 0),
        "solarized" : init.init.bold + colors.fg.rbg(0, 0, 0),
        "spectrum"  : init.init.bold + colors.fg.rbg(0, 0, 0),
        "winter"    : init.init.bold + colors.fg.rbg(0, 0, 0),
        "summer"    : init.init.bold + colors.fg.rbg(0, 0, 0),
        "fall"      : init.init.bold + colors.fg.rbg(0, 0, 0),
        "spring"    : init.init.bold + colors.fg.rbg(0, 0, 0),
        "espresso"  : init.init.bold + colors.fg.rbg(0, 0, 0),
        "darker"    : init.init.bold + colors.fg.rbg(0, 0, 0),
        "ocean"     : init.init.bold + colors.fg.rbg(0, 0, 0),
        "light"     : init.init.bold + colors.fg.rbg(0, 0, 0),
    }
    
    return Color[name]