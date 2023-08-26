from configure      import colors, init

def codeFgColor(name : str = "monokai"):
    codeFgColor = {
        "monokai"   : init.init.bold + colors.fg.rbg(255,255,255),
        "orion"     : init.init.bold + colors.fg.rbg(255,100,255),
        "pegasus"   : init.init.bold + colors.fg.rbg(255,255,255),
        "solo"      : init.init.bold + colors.fg.rbg(255,255,255),
        "skyBlue"   : init.init.bold + colors.fg.rbg(255,255,255),
        "mirage"    : init.init.bold + colors.fg.rbg(255,255,255),
        "material"  : init.init.bold + colors.fg.rbg(255,255,255),
        "night"     : init.init.bold + colors.fg.rbg(255,255,255),
        "solarized" : init.init.bold + colors.fg.rbg(255,255,255),
        "spectrum"  : init.init.bold + colors.fg.rbg(255,255,255),
        "winter"    : init.init.bold + colors.fg.rbg(255,255,255),
        "summer"    : init.init.bold + colors.fg.rbg(255,255,255),
        "fall"      : init.init.bold + colors.fg.rbg(255,255,255),
        "spring"    : init.init.bold + colors.fg.rbg(255,255,255),
        "espresso"  : init.init.bold + colors.fg.rbg(255,255,255),
        "darker"    : init.init.bold + colors.fg.rbg(255,255,255),
        "ocean"     : init.init.bold + colors.fg.rbg(255,255,255),
        "light"     : init.init.bold + colors.fg.rbg(255,255,255),
    }
    
    return codeFgColor[name]