from configure      import colors, init
from terminalType   import codeBgColor as CB
from terminalType   import codeFgColor as CF

def codeColors(name : str = "monokai"):
    codeColor = {
        "monokai"   : CB.codeBgColor(name="monokai")    + CF.codeFgColor(name="monokai"),
        "orion"     : CB.codeBgColor(name="orion")      + CF.codeFgColor(name="orion"), 
        "pegasus"   : CB.codeBgColor(name="pegasus")    + CF.codeFgColor(name="pegasus"),
        "solo"      : CB.codeBgColor(name="solo")       + CF.codeFgColor(name="solo"), 
        "skyBlue"   : CB.codeBgColor(name="skyBlue")    + CF.codeFgColor(name="skyBlue"),
        "mirage"    : CB.codeBgColor(name="mirage")     + CF.codeFgColor(name="mirage"),
        "material"  : CB.codeBgColor(name="material")   + CF.codeFgColor(name="material"),
        "night"     : CB.codeBgColor(name="night")      + CF.codeFgColor(name="night"),
        "solarized" : CB.codeBgColor(name="solarized")  + CF.codeFgColor(name="solarized"),
        "spectrum"  : CB.codeBgColor(name="spectrum")   + CF.codeFgColor(name="spectrum"),
        "winter"    : CB.codeBgColor(name="winter")     + CF.codeFgColor(name="winter"),
        "summer"    : CB.codeBgColor(name="summer")     + CF.codeFgColor(name="summer"), 
        "fall"      : CB.codeBgColor(name="fall")       + CF.codeFgColor(name="fall"),
        "spring"     : CB.codeBgColor(name="spring")     + CF.codeFgColor(name="spring"),
        "espresso"  : CB.codeBgColor(name="espresso")   + CF.codeFgColor(name="espresso"),
        "darker"    : CB.codeBgColor(name="darker")     + CF.codeFgColor(name="darker"),
        "ocean"     : CB.codeBgColor(name="ocean")      + CF.codeFgColor(name="ocean"),
        "light"     : CB.codeBgColor(name="light")      + CF.codeFgColor(name="light"),
    }
    
    return codeColor[name]