import sys , os 
from configure  import colors, init, clear, moveCursor 
from frame      import frame
from header     import header

def formating(LINE : int = 4, data : list = [], max_x : int = 0, idd : int = 0, max_y : int = 0, MAX  = None):
    move        = moveCursor.cursor
    N           = max_y-(LINE+1) 
    Y           = LINE
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    c_bg        = colors.bg.rgb(10, 10, 10)  
    c           = bold + colors.fg.rbg(255, 255, 255)
    input, length       = header.counter(n=0)
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
            

def scrollUP(data : list = [], max_x : int = 0, idd : int = 0, max_y : int = 0, y : int = 0):
    move        = moveCursor.cursor
    N           = max_y-(y+1) 
    Y           = y
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    c_bg        = colors.bg.rgb(10, 10, 10)  
    c           = bold + colors.fg.rbg(255, 255, 255)
    input, length       = header.counter(n=0)
    sys.stdout.write(move.TO(x=length, y=Y) )
    
    if data[idd : ] : 
      
        if len(data[idd : ]) > N :
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
            for i in range(N):
                sys.stdout.write(move.TO(x=length+1, y=Y) + move.LEFT(pos=1000) + clear.clear.line(2))
                if i < len(data[idd : ]) : 
                    i += idd
                    sys.stdout.write(
                        input + c_bg + " " * (max_x - (length+2) ) + reset +
                        move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
                        move.TO(x=length+1, y=Y) + c_bg + data[i]  + reset 
                        )
                else:
                    i += idd
                    sys.stdout.write(
                        input + c_bg + " " * (max_x - (length+2) ) + reset +
                        move.TO(x=max_x, y=Y) + c + f"{asc['v']}" + 
                        move.TO(x=length+1, y=Y) + c_bg + reset 
                        )
                Y += 1
            sys.stdout.flush()
    else: pass