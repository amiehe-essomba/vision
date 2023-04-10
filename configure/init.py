# cursor state 
class init:
    # reset cursor state
    reset       = u"\u001b[0m"  
    # text bold                                
    bold        = u"\u001b[1m"
    # text italic 
    italic      = u"\u001b[3m"
    # underline text 
    underline   = u"\u001b[4m"
    # make cursor and text blink 
    blink       = u"\u001b[5m"
    # same to blink
    rapid_blink = u"\u001b[6m"
    # change the fg and bg 
    reverse     = u"\u001b[7m"
    # hiding text when user is typing 
    hide        = u"\u001b[8m"
    # putting bar on the text 
    bare        = u"\u001b[9m"
    # dounle underline 
    double_underline= u"\u001b[21m"
    # make color more intense
    high_intensity  = u"\u001b[22m"
    # unknown 
    eyes            = u"\u001b[25m"
    # removing the reverse when is set 
    remove_reverse  = u"\u001b[27m"
    # link github 
    link        = u"\u001b[8;;https://github.com/amiehe-essomba ST"