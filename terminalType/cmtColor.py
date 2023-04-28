from configure      import colors 
from terminalType   import codeBgColor as CB

def commentColor( name : str = "monokai"):
    cmtColor = {
        "monokai"   : CB.codeBgColor(name="monokai")    + colors.fg.rbg(153, 153, 255) ,
        "orion"     : CB.codeBgColor(name="orion")      + colors.fg.rbg(153, 153, 255) , 
        "pegasus"   : CB.codeBgColor(name="pegasus")    + colors.fg.rbg(153, 153, 255) ,
        "solo"      : CB.codeBgColor(name="solo")       + colors.fg.rbg(153, 153, 255) , 
        "skyBlue"   : CB.codeBgColor(name="skyBlue")    + colors.fg.rbg(153, 153, 255) ,
        "mirage"    : CB.codeBgColor(name="mirage")     + colors.fg.rbg(153, 153, 255) ,
        "material"  : CB.codeBgColor(name="material")   + colors.fg.rbg(153, 153, 255) ,
        "night"     : CB.codeBgColor(name="night")      + colors.fg.rbg(153, 153, 255) , 
        "solarized" : CB.codeBgColor(name="solarized")  + colors.fg.rbg(153, 153, 255) ,
        "spectrum"  : CB.codeBgColor(name="spectrum")   + colors.fg.rbg(153, 153, 255) ,
        "winter"    : CB.codeBgColor(name="winter")     + colors.fg.rbg(153, 153, 255) ,
        "summer"    : CB.codeBgColor(name="summer")     + colors.fg.rbg(153, 153, 255) , 
        "fall"      : CB.codeBgColor(name="fall")       + colors.fg.rbg(153, 153, 255) ,
        "spring"    : CB.codeBgColor(name="spring")     + colors.fg.rbg(153, 153, 255) ,
        "espresso"  : CB.codeBgColor(name="espresso")   + colors.fg.rbg(153, 153, 255) ,
        "darker"    : CB.codeBgColor(name="darker")     + colors.fg.rbg(153, 153, 255) ,
        "ocean"     : CB.codeBgColor(name="ocean")      + colors.fg.rbg(153, 153, 255) ,
        "light"     : CB.codeBgColor(name="light")      + colors.fg.rbg(153, 153, 255) ,
    }
    
    return cmtColor[name]