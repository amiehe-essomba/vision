from configure      import colors, init
from terminalType   import bgWhite, cmtColor, codeBgColor, codeColor, codeFgColor, ColRawColor, strColor
from terminalType   import cursorColor, fgBlack, openColor, prgramColor, titleColor, widgetColor 
from terminalType   import op, ar, bracket, number

def termianlConfig( name : str = "monokai"):
    """_summary_

    Args:
        name (str, optional): _description_. Defaults to "monokai".

    Returns:
        _type_: _description_
    """
    # bg color 
    fgBlack_                = fgBlack.fgColor(name = name) 
    # bg color 
    bgWhite_                = bgWhite.bgWhite(name = name) 
    # bg color 
    codeBgColors_           = codeBgColor.codeBgColor(name = name) 
    # fg color 
    codeFgColors_           = codeFgColor.codeFgColor(name = name) 
    # building color 
    codeColors_             = codeColor.codeColors(name = name) 
    # widget color 
    widgetColors_           = widgetColor.widgetColor(name = name)  
    #keyword found color 
    KeyColor                = init.init.bold + colors.bg.rgb(200, 200, 0) + init.init.bold + colors.fg.rbg(255, 255, 255)
    # comment color 
    commentColor_           = cmtColor.commentColor(name = name)  
    #string color 
    strColor_               = strColor.stringColor(name = name)  
    #title color            
    titleColor_             = titleColor.titleColor(name = name)  
    #program color 
    proColor_               = prgramColor.programColor(name = name)  
    #col and raw color 
    ColRawColor_            = ColRawColor.ColRawColor(name = name)  
    #opened, closed
    openedColor_            = openColor.openColor(name = name) 
    #cursor color 
    cursorColor_            = cursorColor.cursorColor(name = name)  
    # colors used 
    COLOR                   = {
        "fgColor"       : codeColors_, 
        "bgColor"       : codeBgColors_, 
        "wColor"        : widgetColors_, 
        "keyColor"      : KeyColor,
        "cmtColor"      : commentColor_,
        "strColor"      : strColor_, 
        "white"         : codeFgColors_,
        "titleColor"    : titleColor_,
        "proColor"      : proColor_,
        "CRColor"       : ColRawColor_,
        "openedColor"   : openedColor_,
        "cursorColor"   : cursorColor_, 
        "bgWhite"       : bgWhite_, 
        "fgBlack"       : fgBlack_, 
        'op'            : op.operators(name = name),
        "ar"            : ar.arithmetic(name = name),
        "bracket"       : bracket.B(name = name),
        "num"           : number.number( name = name)
        }


    return COLOR

