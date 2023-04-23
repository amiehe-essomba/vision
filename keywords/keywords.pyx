from keywords   import key_py 

cpdef keys(str language, str termios, unsigned long int n ):
    cdef:
        dict all_keys = key_py.LANG(master = language).LANG(termios = termios, n = n )
        list keys     = all_keys["all_keys"]
        unsigned long int i, j, MAX = 0
        str string, color
        list names  = []
        list colors = []
        dict key_items = {}

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