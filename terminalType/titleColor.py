from configure      import colors, init

def titleColor(name : str = "monokai"):
    titleColor = {
        "monokai"   : init.init.bold + colors.fg.rbg(0, 255, 0),
        "orion"     : init.init.bold + colors.fg.rbg(255, 255, 0),
        "pegasus"   : init.init.bold + colors.fg.rbg(100, 255, 0),
        "solo"      : init.init.bold + colors.fg.rbg(0, 255, 100), 
        "skyBlue"   : init.init.bold + colors.fg.rbg(25, 255, 25),
        "mirage"    : init.init.bold + colors.fg.rbg(255, 255, 255),
        "material"  : init.init.bold + colors.fg.rbg(0, 0, 0),
        "night"     : init.init.bold + colors.fg.rbg(0, 255, 0),
        "solarized" : init.init.bold + colors.fg.rbg(0, 255, 0),
        "spectrum"  : init.init.bold + colors.fg.rbg(0, 255, 0),
        "winter"    : init.init.bold + colors.fg.rbg(0, 255, 0),
        "summer"    : init.init.bold + colors.fg.rbg(0, 255, 0),
        "fall"      : init.init.bold + colors.fg.rbg(0, 255, 0),
        "spring"    : init.init.bold + colors.fg.rbg(0, 255, 0),
        "espresso"  : init.init.bold + colors.fg.rbg(0, 255, 0),
        "darker"    : init.init.bold + colors.fg.rbg(0, 255, 0),
        "ocean"     : init.init.bold + colors.fg.rbg(0, 255, 0),
        "light"     : init.init.bold + colors.fg.rbg(0, 255, 0),
    }
    
    return titleColor[name]