from configure      import colors 
from terminalType   import codeBgColor as CB

def stringColor( name : str = "monokai"):
    strColor = {
        "monokai"   : CB.codeBgColor(name="monokai")    + colors.bg.rgb(100, 100, 100) + colors.fg.rbg(255, 153, 20) ,
        "orion"     : CB.codeBgColor(name="orion")      + colors.fg.rbg(0, 200, 50) , 
        "pegasus"   : CB.codeBgColor(name="pegasus")    + colors.fg.rbg(150, 200, 200) ,
        "solo"      : CB.codeBgColor(name="solo")       + colors.fg.rbg(150, 60, 200) , 
        "skyBlue"   : CB.codeBgColor(name="skyBlue")    + colors.fg.rbg(150, 250, 200) ,
        "mirage"    : CB.codeBgColor(name="mirage")     + colors.fg.rbg(15, 153, 255) ,
        "material"  : CB.codeBgColor(name="material")   + colors.fg.rbg(153, 200, 255) ,
        "night"     : CB.codeBgColor(name="night")      + colors.fg.rbg(200, 153, 25) , 
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
    
    return strColor[name]