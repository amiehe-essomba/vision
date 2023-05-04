from configure      import colors, init

def codeBgColor(name : str = "monokai"):
    codeBgColor = {
        "monokai"   : init.init.bold + colors.bg.rgb(0, 0, 0),
        "orion"     : colors.bg.rgb(255,255,255), 
        "pegasus"   : init.init.bold + colors.bg.rgb(100, 100, 125),
        "solo"      : init.init.bold + colors.bg.rgb(140, 200, 60), 
        "skyBlue"   : init.init.bold + colors.bg.rgb(60, 255, 200),
        "mirage"    : init.init.bold + colors.bg.rgb(120, 60, 50),
        "material"  : init.init.bold + colors.bg.rgb(145, 145, 220),
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