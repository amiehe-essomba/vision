import sys , os 
from configure  import colors, init, clear, state, screenConfig, moveCursor, scroll
from frame      import frame
from header     import header

def formating(LINE : int = 4, data : list = [], x : int = 0, y : int = 0, size : int=  0, max_x : int = 0, idd : int = 0):
    move        = moveCursor.cursor
    N           = 7
    Y           = LINE
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    move_left   = moveCursor.cursor 
    position    = moveCursor.cursor
    c_bg        = colors.bg.rgb(10, 10, 10)  
    c           = bold + colors.fg.rbg(255, 255, 255)
    input, length       = header.counter(n=0)
    sys.stdout.write(move.TO(x=size, y=LINE) )

    for i in range(N):
        i += idd
        sys.stdout.write(move.LEFT(pos=1000) + clear.clear.line(2))
        sys.stdout.write(
            input + c_bg + " " * (max_x - (size+2) ) + reset + 
            move.TO(x=max_x, y=Y) + c + f"{asc['v']}" +
            move.TO(x=size+1, y=Y) + data[i] + reset + "\n"
            )
        Y += 1
        sys.stdout.flush()