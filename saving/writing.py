
def writeInput(dataFile: list , FileName : str):
    with open(FileName, "w") as file:
        for i, string in enumerate(dataFile): 
            if i != len(dataFile)-1: file.write(f"{string}\n")
            else: file.write(f"{string}")
            
    file.close()
    
def BLACK_M(WRITE : list = [], lang : str = "unknown", history : dict = {}, COLOR : dict = {},):
    from keywords       import words

    # building color 
    color                  = COLOR['fgColor']
    # locking string 
    locked                 = False 
    # storing data      
    LIST                   = []
    m, idd                 = 0, 0
    cmt                    = COLOR['cmtColor']
    no_cmt                 = color
    
    if WRITE:
        for string in WRITE :
            tab = tabular(string, lang)
            if locked is False:
                locked, idd         = keys(tab, lang, string)
                _string_            = string.replace("\t", " " * 4)
                __line__, __color__ = words.words(string=_string_, color=color, language=lang ).final(locked=locked, m=m, n=idd, COLOR=COLOR.copy())
                
                history["color"].append(color)
                history["m"].append(m)
                history['n'].append(idd)
                history['locked'].append(locked)
                
                if locked is True: color = cmt 
                else: color = no_cmt
            else:
                _open_                  = OPEN(tab, lang, locked)
                if _open_ is None: pass
                else:
                    for s in _open_: 
                        locked = STR(s, string )
                _string_            = string.replace("\t", " " * 4)
                __line__, __color__ = words.words(string=_string_, color=color, language=lang ).final(locked=locked, m=m, n=idd)
                
                history["color"].append(color)
                history["m"].append(m)
                history['n'].append(idd)
                history['locked'].append(locked)
                
                if locked is True: color = cmt 
                else: color = no_cmt
                    
            LIST.append(__line__)
            
    else: pass 

    return LIST        
    
def tabular(string : str, lang: str = ""):
    # tabular initialization
    count   = 0
    # locking 
    locaked = False 
    
    if lang in ["python", "mamba", "c++", "c"]:
        if string: 
            for i, s in enumerate(string):
                if string[0] == '\t': 
                    if locaked is False:
                        if i == 0: 
                            count += 1 
                        else:
                            if string[count - 1] == "\t" : count += 1 
                            else: break 
                    else: pass
                else: locaked = True 
        else: pass 
    else: pass 
    
    return count 

def keys(count : int = 0, lang : str='', string : str = ""):
    key_found = False 
    idd       = 0
    
    if string: 
        if lang == 'cpmd':
            if    string[count : 5+count] == "&INFO": key_found = True 
            else: pass 
        elif lang == 'mamba':
            if   string[count : 5+count] == "begin"   : key_found = True 
            elif string[count : 5+count] == "class"   : idd = 1
            elif string[count : 3+count] == "def"     : idd = 1
            elif string[count : 4+count] == "func"    : idd = 1
            else: pass
        elif lang == "python":
            if   string[count : 3] == '"""'   : key_found = True 
            elif string[count : 3] == "'''"   : key_found = True 
            else: pass 
        else: pass
    else: pass 
    
    return key_found, idd

def OPEN(count : int , lang : str, locked : bool = False):
    
    if locked is False : return None
    else:
        if   lang == "mamba"    : return ["\t"*count + "end", "\t"*count + "save" ]
        elif lang == "cpmd"     : return ["\t"*count + "&END"]
        elif lang == "python"   : return ["\t"*count + '"""']
        else: return None
        
def STR(STR : str, string : str):
    open = True 
    
    try:
        if string[:len(STR)] == STR: open = False
    except IndexError: pass
    
    return open