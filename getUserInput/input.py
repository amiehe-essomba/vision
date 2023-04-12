import os, sys

if (sys.platform == "win32"): pass 
else:  import  termios, tty

def decoding_string():
    import msvcrt 
    s = []   
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
            try: number =  [ord(s), None]
            except TypeError: 
                if   s == "\x0e":
                    number =  [14, None]
                elif s == "\x04":
                    number =  [4,  None]
                elif s == "\x01":
                    number =  [17, None]
                elif s == "\x0c":
                    number =  [12, None]
                else:  
                    number =  [None, None]
        except UnicodeDecodeError: number =  [None, None]
    else:
        if s[0] in [b'\x00']:
            s = s[1].decode("utf-8")
            if   s == "H" : number = [27, [65, 0]]
            elif s == "P" : number = [27, [66, 0]]
            elif s == "K" : number = [27, [68, 0]]
            elif s == "M" : number = [27, [67, 0]]
            elif s == "t" : number = [27, [49, 65]]
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