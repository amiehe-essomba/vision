from keywords       import words
from configure      import colors, init

def readFile(fileName, termios : str , language :  str ):
    # bg color 
    c_bg                   = init.init.bold + colors.bg.rgb(10, 10, 10)
    # fg color 
    c_fg                   = init.init.bold + colors.fg.rbg(255, 255, 255)
    # building color 
    color                  = c_bg + c_fg
    # storing data 
    data                   = {"writing" : [], "string" : [], "input" : []}
    locked                 = False 
    m                      = 0
    
    with open(fileName) as file:
        for line in file.readlines():  
            if line[-1] == '\n': line = line[:-1]
            else: pass
            if termios == "none": 
                data["writing"].append( line.replace("\t", " " * 4) )
                data["input"].append( line.replace("\t", " " * 4) )
                data["string"].append( line)
            else:
                __line__, __color__ = words.words(string=line.replace("\t", " " * 4), color=color, language=language ).final(locked=locked, m=m)
                data["writing"].append( __line__ )
                data["input"].append( line.replace("\t", " " * 4) )
                data["string"].append( line.replace(" " * 4, '\t') )
                #######################################
                # changing color or reset color  
                if __color__["locked"] is False:  
                    locked = False
                    m      = 0
                else: 
                    color  = __color__["color"]
                    locked = True
                    m      = __color__["rest"]
                #######################################
    file.close()
    return data 

def transform(fileName, termios : str , language :  str ):
    # bg color 
    c_bg                   = init.init.bold + colors.bg.rgb(10, 10, 10)
    # fg color 
    c_fg                   = init.init.bold + colors.fg.rbg(255, 255, 255)
    # building color 
    color                  = c_bg + c_fg
    # storing data 
    data                   = {"writing" : [], "string" : [], "input" : []}
    locked                 = False 
    m                      = 0
    
    with open(fileName) as file:
        for line in file.readlines():  
            if line[-1] == '\n': line = line[:-1]
            else: pass
            if termios == "none": 
                data["writing"].append( line.replace("\t", " " * 4) )
                data["input"].append( line.replace("\t", " " * 4) )
                data["string"].append( line)
            else:
                __line__, __color__ = words.words(string=line.replace("\t", " " * 4), color=color, language=language ).final(locked=locked, m=m)
                data["writing"].append( __line__ )
                data["input"].append( line.replace("\t", " " * 4) )
                data["string"].append( line.replace(" " * 4, '\t') )
                #######################################
                # changing color or reset color  
                if __color__["locked"] is False:  
                    locked = False
                    m      = 0
                else: 
                    color  = __color__["color"]
                    locked = True
                    m      = __color__["rest"]
                #######################################
    file.close()
    return data 