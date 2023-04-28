from configure      import colors, init

def codeBgColor(name : str = "monokai"):
    codeBgColor = {
        "monokai"   : init.init.bold + colors.bg.rgb(0, 0, 0),
        "orion"     : init.init.bold + colors.bg.rgb(0, 0, 0), 
        "pegasus"   : init.init.bold + colors.bg.rgb(0, 0, 0),
        "solo"      : init.init.bold + colors.bg.rgb(0, 0, 0), 
        "skyBlue"   : init.init.bold + colors.bg.rgb(0, 0, 0),
        "mirage"    : init.init.bold + colors.bg.rgb(0, 0, 0),
        "material"  : init.init.bold + colors.bg.rgb(0, 0, 0),
        "night"     : init.init.bold + colors.bg.rgb(0, 0, 0), 
        "solarized" : init.init.bold + colors.bg.rgb(0, 0, 0),
        "spectrum"  : init.init.bold + colors.bg.rgb(0, 0, 0),
        "winter"    : init.init.bold + colors.bg.rgb(0, 0, 0),
        "summer"    : init.init.bold + colors.bg.rgb(0, 0, 0), 
        "fall"      : init.init.bold + colors.bg.rgb(0, 0, 0),
        "spring"    : init.init.bold + colors.bg.rgb(0, 0, 0),
        "espresso"  : init.init.bold + colors.bg.rgb(0, 0, 0),
        "darker"    : init.init.bold + colors.bg.rgb(0, 0, 0),
        "ocean"     : init.init.bold + colors.bg.rgb(0, 0, 0),
        "light"     : init.init.bold + colors.bg.rgb(0, 0, 0),
    }

    return codeBgColor[name]