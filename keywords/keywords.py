from keywords   import key_py 

def keys(language : str, termios : str,  n : int ):
    all_keys    = key_py.LANG(master = language).LANG(termios = termios, n = n )
    keys        = all_keys["all_keys"]
    names       = []
    colors      = []
    key_items   = {}
    MAX         = 0

    if language == "unknown" : pass 
    else:
        for i in range( len( keys ) ):
            for string in all_keys[ keys[i] ]["name"]:
                if len(string) > MAX : MAX = len( string )
                else: pass 

                color = all_keys[ keys[i] ]["color"]['values'][0]
                names.append(string)
                colors.append(color)
                key_items[string] = color
                
    return {"names" : names, "colors" : colors}, key_items