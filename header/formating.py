import sys 
from configure  import init, clear, moveCursor 
from frame      import frame
from header     import header

def formating(LINE : int = 4, data : list = [], max_x : int = 0, idd : int = 0, max_y : int = 0, MAX  = None, COLOR : dict = {}):
    move        = moveCursor.cursor
    N           = max_y-(LINE+1) 
    Y           = LINE
    asc         = frame.frame(custom=True)
    reset       = init.init.reset
    c_bg        = COLOR['fgColor'] 
    c           = COLOR['white'] 
    input, length       = header.counter(n=0, COLOR=COLOR)
    sys.stdout.write(move.TO(x=length, y=LINE) )

    if MAX is None:
        for i in range(N):
            i += idd
            sys.stdout.write(move.TO(x=length+1, y=Y) + move.LEFT(pos=1000) + clear.clear.line(2))
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset +
                move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
                move.TO(x=length+1, y=Y) + c_bg + data[i]  + reset 
                )
            Y += 1
        sys.stdout.flush()
    else:
        
        Y = MAX['y']
        line = N - Y +  (LINE+1)
        if len(data[MAX['max'] : ]) <  line :
            sys.stdout.write( move.TO(MAX['x'], MAX['y']) )
            for i in range(MAX['max'], len(data)):
                sys.stdout.write(move.LEFT(pos=1000) + clear.clear.line(2))
                sys.stdout.write(
                    input + c_bg + " " * (max_x - (length+2) ) + reset + 
                    move.TO(x=max_x, y=Y) + c + f"{asc['v']}" +
                    move.TO(x=length+1, y=Y) + c_bg+ data[i] + reset + "\n"
                    )
                Y += 1
                sys.stdout.flush()
        else:
            sys.stdout.write( move.TO(MAX['x'], MAX['y']) )
            for i in range(line ):
                i += MAX['max'] 
                sys.stdout.write(move.LEFT(pos=1000) + clear.clear.line(2))
                sys.stdout.write(
                    input + c_bg + " " * (max_x - (length+2) ) + reset + 
                    move.TO(x=max_x, y=Y) + c + f"{asc['v']}" +
                    move.TO(x=length+1, y=Y) + c_bg+ data[i] + reset +"\n"
                    )
                Y += 1
                sys.stdout.flush()

def scrollUP(data : list = [], max_x : int = 0, idd : int = 0, max_y : int = 0, y : int = 0, COLOR : dict = {}):
    move        = moveCursor.cursor
    N           = max_y-(y+1) 
    Y           = y
    asc         = frame.frame(custom=True)
    reset       = init.init.reset
    c_bg        = COLOR['fgColor'] 
    c           = COLOR['white'] 
    input, length       = header.counter(n=0)
    sys.stdout.write(move.TO(x=length, y=Y) )
    
    if data[idd : ] : 
        for i in range(N):
            i += idd
            sys.stdout.write(move.TO(x=length+1, y=Y) + move.LEFT(pos=1000) + clear.clear.line(2))
            try:
                sys.stdout.write(
                    input + c_bg + " " * (max_x - (length+2) ) + reset +
                    move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
                    move.TO(x=length+1, y=Y) + c_bg + data[i]  + reset 
                    )     
            except IndexError:
                sys.stdout.write(
                    input + c_bg + " " * (max_x - (length+2) ) + reset +
                    move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
                    move.TO(x=length+1, y=Y) + c_bg + reset 
                    )
            Y += 1
            sys.stdout.flush()
    else: pass
    
def ClearScreen(max_x : int = 0, max_y : int = 0, LINE : int = 4, COLOR :dict = {}):
    move        = moveCursor.cursor
    N           = max_y-(LINE+1) 
    Y           = LINE
    asc         = frame.frame(custom=True)
    reset       = init.init.reset
    c_bg        = COLOR['fgColor'] 
    c           = COLOR['white'] 
    input, length       = header.counter(n=0)
    sys.stdout.write(move.TO(x=length, y=Y) )
    
    for i in range(N):
        sys.stdout.write(move.TO(x=length+1, y=Y) + move.LEFT(pos=1000) + clear.clear.line(2))
        sys.stdout.write(
            input + c_bg + " " * (max_x - (length+2) ) + reset +
            move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
            move.TO(x=length+1, y=Y) + c_bg + "" + reset +"\n"
            )
        Y += 1
        sys.stdout.flush()
        
    sys.stdout.write(move.TO(x=length+1, y=LINE))
    sys.stdout.flush()
    
def RestoringSTring(max_x : int = 0, max_y : int = 0, LINE : int = 4, WRITE : list = [], y : int = 0, x : int = 0, COLOR : dict = {} ):
    ClearScreen(max_x=max_x, max_y=max_y, LINE=LINE)
    move        = moveCursor.cursor
    N           = max_y-(LINE+1) 
    Y           = LINE
    asc         = frame.frame(custom=True)
    reset       = init.init.reset
    c_bg        = COLOR['fgColor'] 
    c           = COLOR['white'] 
    input, length       = header.counter(n=0)
    sys.stdout.write(move.TO(x=length, y=Y) )
    
    line = y - LINE
    
    for i in range(N):
        sys.stdout.write(move.TO(x=length+1, y=Y) + move.LEFT(pos=1000) + clear.clear.line(2))
        try:
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset +
                move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
                move.TO(x=length+1, y=Y) + c_bg + WRITE[i] + reset 
                )
        except IndexError:
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset +
                move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
                move.TO(x=length+1, y=Y) + c_bg + reset 
                )
        Y += 1
        sys.stdout.flush()
            
    sys.stdout.write(move.TO(x=x, y=y))
    sys.stdout.flush()
    
def WritingDown(x :int = 0, y : int = 0, max_x : int = 0, max_y : int = 0, LINE : int = 4, COLOR : dict = {}):
    move        = moveCursor.cursor
    N           = max_y-(LINE+1) 
    Y           = LINE
    asc         = frame.frame(custom=True)
    reset       = init.init.reset
    c_bg        = COLOR['fgColor'] 
    c           = COLOR['white'] 
    input, length       = header.counter(n=0)
    sys.stdout.write(move.TO(x=length, y=Y) )
    
    for i in range(N):
        if Y > y:
            sys.stdout.write(move.TO(x=length+1, y=Y) + move.LEFT(pos=1000) + clear.clear.line(2))
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset +
                move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
                move.TO(x=length+1, y=Y) + c_bg + "" + reset +"\n"
                )
            sys.stdout.flush()
        else: pass
        Y += 1 
    sys.stdout.write(move.TO(x=x, y=y))
    sys.stdout.flush()
    
def WritingUp(x :int = 0, y : int = 0, max_x : int = 0, max_y : int = 0, LINE : int = 4, COLOR : dict = {}):
    move        = moveCursor.cursor
    N           = max_y-(LINE+1) 
    Y           = LINE
    asc         = frame.frame(custom=True)
    reset       = init.init.reset
    c_bg        = COLOR['fgColor'] 
    c           = COLOR['white'] 
    input, length       = header.counter(n=0)
    sys.stdout.write(move.TO(x=length, y=Y) )
    
    for i in range(N):
        if Y < y:
            sys.stdout.write(move.TO(x=length+1, y=Y) + move.LEFT(pos=1000) + clear.clear.line(2))
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset +
                move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
                move.TO(x=length+1, y=Y) + c_bg + "" + reset +"\n"
                )
            sys.stdout.flush()
        else: pass
        Y += 1 
    sys.stdout.write(move.TO(x=x, y=y))
    sys.stdout.flush()