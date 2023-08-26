import os, sys

if (sys.platform == "win32"): pass 
else:  import  termios, tty

def decoding_string():
    import msvcrt 
    number = None
    s, idd = [], 0

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            s.append(key)
            if s[0] == b'\x00':
                try: 
                    if s[1] : break
                except IndexError: pass
            else: break    
   
    return s

def windows( ):
    s = decoding_string()
    number = None 

    if len(s) == 1:
        try:
            s = s[0].decode("utf-8")
            try:
                if ord(s) not in {72, 75, 77, 80}:
                    number =  [ord(s), None]
                else:
                    if   ord(s) == 72 : number = [27, [65, 0]]
                    elif ord(s) == 80 : number = [27, [66, 0]]
                    elif ord(s) == 75 : number = [27, [68, 0]]
                    elif ord(s) == 77 : number = [27, [67, 0]]
            except TypeError: 
                #<ctrl+n>
                if   s == "\x0e":  number =  [14, None]
                #<ctrl+d>
                elif s == "\x04":  number =  [4,  None]
                #<ctrl+a>
                elif s == "\x01":  number =  [17, None]
                #<ctrl+g>
                elif s == "\x07":  number =  [20, None]
                #<ctrl+l>
                elif s == "\x0c":  number =  [12, None]
                #<ctrl+s>
                elif s == "\x13":  number =  [19, None]
                #rest 
                else:  number =  [None, None]
        except UnicodeDecodeError:  number =  [None, None]
    else:
        if s[0] in [b'\x00']:
            
            s = s[1].decode("utf-8")
            #up
            if   s == "H" : number = [27, [65, 0]]
            #down
            elif s == "P" : number = [27, [66, 0]]
            #left
            elif s == "K" : number = [27, [68, 0]]
            #right
            elif s == "M" : number = [27, [67, 0]]
            #<ctrl+right>
            elif s == "t" : number = [27, [49, 65]]
            #<ctrl+left>
            elif s == "s" : number = [27, [49, 66]]
        else: number =  [None, None]
        
    return number
 
def linux():
    #import termios, sys, tty

    fd              = sys.stdin.fileno()
    old_settings    = termios.tcgetattr( fd )
    try:
        tty.setraw(sys.stdin)
        ch = ord( sys.stdin.read(1) )
    finally: termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

def convert():
    if os.name == "nt": return windows()
    else: return linux()
    
def inter():
    char1, char2, char3, char4, char5 = 0, 0, 0, 0, 0
    while True:
        char1 = convert() 
        if char1 == 91: 
            char2 = ord(sys.stdin.read(1)) 
            if char2 == 49:
                char3, char4, char5 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
            else: pass 
        elif char1 == 27:
            char1, char2, char3, char4, char5 = outer()
        else: pass 
        
        break
    return [char1, char2, char3, char4, char5]

def outer():
    char1, char2, char3, char4, char5 = 0, 0, 0, 0, 0
    while True:
        char1 = convert() 
        if char1 == 91: 
            char2 = ord(sys.stdin.read(1)) 
            if char2 == 49:
                char3, char4, char5 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
            else: pass 
        elif char1 == 27:
            char1, char2, char3, char4, char5 = inter()
        else: pass 
        
        break
    return [char1, char2, char3, char4, char5]

def win_inter():
    char1, char2, char3, char4, char5 = 0, 0, 0, 0, 0
    while True:
        char1 = convert() 
        if char1:
            _     = char1[1]
            char1 = char1[0]
            if char1 is not None:
                if char1 == 27:
                    if _ is None: char1, char2, char3, char4 = win_outer()
                    else:
                        char2, char3 = _
                else: pass
            else: pass 
        else: pass
        break
    
    return [char1, char2, char3, char4]

def win_outer():
    char1, char2, char3, char4, char5 = 0, 0, 0, 0, 0
    while True:
        char1 = convert() 
        if char1:
            _     = char1[1]
            char1 = char1[0]
            if char1 is not None:
                if char1 == 27:
                    if _ is None: char1, char2, char3, char4 = win_inter()
                    else:
                        char2, char3 = _
                else: pass
            else: pass 
        else: pass
        break
    
    return [char1, char2, char3, char4]

if __name__ == "__main__":
    while True:
        try:
            s = convert()
            if s:
                _ = s[1]
            else: pass 
            
            #print(s)
        except KeyboardInterrupt: break
        