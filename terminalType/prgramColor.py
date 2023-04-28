from configure      import colors, init 
from terminalType   import codeBgColor as CB

def programColor( name : str = "monokai"):
    proColor = {
        "monokai"   : init.init.bold + init.init.blink + CB.codeBgColor(name="monokai")    + colors.fg.rbg(0, 255, 0) ,
        "orion"     : init.init.bold + init.init.blink + CB.codeBgColor(name="orion")      + colors.fg.rbg(153, 153, 255) , 
        "pegasus"   : init.init.bold + init.init.blink + CB.codeBgColor(name="pegasus")    + colors.fg.rbg(153, 153, 255) ,
        "solo"      : init.init.bold + init.init.blink + CB.codeBgColor(name="solo")       + colors.fg.rbg(153, 153, 255) , 
        "skyBlue"   : init.init.bold + init.init.blink + CB.codeBgColor(name="skyBlue")    + colors.fg.rbg(153, 153, 255) ,
        "mirage"    : init.init.bold + init.init.blink + CB.codeBgColor(name="mirage")     + colors.fg.rbg(153, 153, 255) ,
        "material"  : init.init.bold + init.init.blink + CB.codeBgColor(name="material")   + colors.fg.rbg(153, 153, 255) ,
        "night"     : init.init.bold + init.init.blink + CB.codeBgColor(name="night")      + colors.fg.rbg(153, 153, 255) , 
        "solarized" : init.init.bold + init.init.blink + CB.codeBgColor(name="solarized")  + colors.fg.rbg(153, 153, 255) ,
        "spectrum"  : init.init.bold + init.init.blink + CB.codeBgColor(name="spectrum")   + colors.fg.rbg(153, 153, 255) ,
        "winter"    : init.init.bold + init.init.blink + CB.codeBgColor(name="winter")     + colors.fg.rbg(153, 153, 255) ,
        "summer"    : init.init.bold + init.init.blink + CB.codeBgColor(name="summer")     + colors.fg.rbg(153, 153, 255) , 
        "fall"      : init.init.bold + init.init.blink + CB.codeBgColor(name="fall")       + colors.fg.rbg(153, 153, 255) ,
        "spring"    : init.init.bold + init.init.blink + CB.codeBgColor(name="spring")     + colors.fg.rbg(153, 153, 255) ,
        "espresso"  : init.init.bold + init.init.blink + CB.codeBgColor(name="espresso")   + colors.fg.rbg(153, 153, 255) ,
        "darker"    : init.init.bold + init.init.blink + CB.codeBgColor(name="darker")     + colors.fg.rbg(153, 153, 255) ,
        "ocean"     : init.init.bold + init.init.blink + CB.codeBgColor(name="ocean")      + colors.fg.rbg(153, 153, 255) ,
        "light"     : init.init.bold + init.init.blink + CB.codeBgColor(name="light")      + colors.fg.rbg(153, 153, 255) ,
    }
    
    return proColor[name]