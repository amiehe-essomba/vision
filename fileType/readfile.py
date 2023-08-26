from keywords       import words
from saving         import writing
from configure      import screenConfig

def readFile(fileName: str, termios : str , language :  str, COLOR : dict  = {}):
    # building color 
    color                  = COLOR["fgColor"] 
    # storing data 
    data                   = {"writing" : [], "string" : [], "input" : [], "color" : {"m" : [], "n" : [], "color" : [], "locked" : []}}
    # locked string to set it as a comment line 
    locked                 = False 
    # initialization
    m, idd                 = 0, 0
    cmt                    = COLOR['cmtColor']
    no_cmt                 = color
    colorList              = []
    end                    = False
    # getting max size (max_x, max_y) of the window 
    max_x, max_y           = screenConfig.cursorMax()
    n                      = 5
    error                  = None
    index                  = 0
    try:
        with open(fileName) as file:
            for line in file.readlines(): 
                index += 1 
                if line[-1] == '\n': line = line[:-1]
                else: pass
                
                tab = writing.tabular(line, language)
                if locked is False:
                    line = line.replace("\t", " " * 4) 
                    if len(line) > (max_x-n):
                        #line = line[:(max_x-n)]
                        #__line__, __color__ = words.words(string=line, color=color, 
                        #            language=language ).final(locked=locked, m=m, n=idd, blink=False, 
                        #                                        code_w=False, COLOR=COLOR.copy())
                        error = f'line {index} has more characters than {max_x}'
                        break
                    else:
                        __line__, __color__ = words.words(string=line, color=color, 
                                    language=language ).final(locked=locked, m=m, n=idd, blink=False, 
                                                                code_w=False, COLOR=COLOR.copy())
                    data["writing"].append( __line__ )
                    data["input"].append( line.replace("\t", " " * 4) )
                    data["string"].append( line.replace(" " * 4, '\t') )
                    data["color"]["color"].append(color)
                    data["color"]["m"].append(m)
                    data["color"]['n'].append(idd)
                    data["color"]['locked'].append(locked)     
                    
                    locked, idd         = writing.keys(tab, language, line)
                    if locked is True: color = cmt 
                    else: color = no_cmt
                else: 
                    _open_                  = writing.OPEN(tab, language, locked)
                    if _open_ is None: pass
                    else:
                        for s in _open_:
                            locked = writing.STR(s, line )
                    
                    if termios == "none": 
                        data["writing"].append( line.replace("\t", " " * 4) )
                        data["input"].append( line.replace("\t", " " * 4) )
                        data["string"].append( line)
                    else:
                        line = line.replace("\t", " " * 4) 
                        if len(line) > (max_x-n):
                            line = line[:(max_x-n)]                      
                            __line__, __color__ = words.words(string=line, color=color, 
                                            language=language ).final(locked=locked, m=m, n=idd, blink=False, code_w=False, COLOR=COLOR.copy())
                        else:
                            __line__, __color__ = words.words(string=line, color=color, 
                                            language=language ).final(locked=locked, m=m, n=idd, blink=False, code_w=False, COLOR=COLOR.copy())
                        data["writing"].append( __line__ )
                        data["input"].append( line.replace("\t", " " * 4) )
                        data["string"].append( line.replace(" " * 4, '\t') )
                        data["color"]["color"].append(color)
                        data["color"]["m"].append(m)
                        data["color"]['n'].append(idd)
                        data["color"]['locked'].append(locked)

                    if locked is True: color = cmt 
                    else: color = no_cmt                 
        file.close()
    except FileNotFoundError: 
        data = {"writing" : [""], "string" : [""], "input" : [""], "color" : {"color" : [color], "m" : [0], "n" : [0], "locked" : [False]}}
        
    data["color"]["color"].append(color)
    data["color"]["m"].append(m)
    data["color"]['n'].append(idd)
    data["color"]['locked'].append(locked)
    data["writing"].append('')
    
    return data, error

