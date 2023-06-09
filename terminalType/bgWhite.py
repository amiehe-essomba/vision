from configure      import colors, init

def bgWhite(name : str = "monokai"):
    bgWhite = {
        "monokai"   : init.init.bold + colors.bg.rgb(255, 255, 255),
        "orion"     : init.init.bold + colors.bg.rgb(0,0,0), 
        "pegasus"   : init.init.bold + colors.bg.rgb(255, 255, 255),
        "solo"      : init.init.bold + colors.bg.rgb(255, 255, 255), 
        "skyBlue"   : init.init.bold + colors.bg.rgb(255, 255, 255),
        "mirage"    : init.init.bold + colors.bg.rgb(255, 255, 255),
        "material"  : init.init.bold + colors.bg.rgb(255, 255, 255),
        "night"     : init.init.bold + colors.bg.rgb(255, 255, 255), 
        "solarized" : init.init.bold + colors.bg.rgb(255, 255, 255),
        "spectrum"  : init.init.bold + colors.bg.rgb(255, 255, 255),
        "winter"    : init.init.bold + colors.bg.rgb(255, 255, 255),
        "summer"    : init.init.bold + colors.bg.rgb(255, 255, 255), 
        "fall"      : init.init.bold + colors.bg.rgb(255, 255, 255),
        "spring"    : init.init.bold + colors.bg.rgb(255, 255, 255),
        "espresso"  : init.init.bold + colors.bg.rgb(255, 255, 255),
        "darker"    : init.init.bold + colors.bg.rgb(255, 255, 255),
        "ocean"     : init.init.bold + colors.bg.rgb(255, 255, 255),
        "light"     : init.init.bold + colors.bg.rgb(255, 255, 255),
    }
    
    return bgWhite[name]