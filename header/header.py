import os  
import sys 
from configure  import colors, init, clear, state, screenConfig, moveCursor
from frame      import frame


def title(max_x :int = 0, max_y :int = 0, size : int = 0,  color : str = "white"):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    cc          = init.init.bold + colors.fg.rbg(0, 255, 255)
    string      = "VISION EDITOR V-1.0.0".center(max_x - 2)
    move        = moveCursor.cursor 
    action      = state.save
    blink       = init.init.blink+init.init.underline
    
    if color == "white": c   = colors.fg.rbg(255, 255, 255)
    else: c = colors.fg.rbg(0, 0, 0)
    
    # first line     
    sys.stdout.write(c + f"{asc['ul']}" + f"{asc['h']}" * (max_x-2) + f"{asc['ur']}" + reset + "\n")
    # second line 
    sys.stdout.write(c + f"{asc['v']}"  + bold + cc +  string + c + f"{asc['v']}" + reset + "\n")
    # third line 
    sys.stdout.write(c + f"{asc['vl']}" + f"{asc['h']}" * 7 + f"{asc['h']}" +  
                         f"{asc['h']}"*(max_x - 10) + f"{asc['vr']}" + reset + "\n")

    # currently cursor position (x, y)    
    x, y = screenConfig.cursor()
    
    middle(max_x=max_x, n=max_y-5 ,x=x, y=y, color=color)
    sys.stdout.write(move.LEFT(pos=1000))
    bottom(max_x=max_x, color=color)
    sys.stdout.write(move.TO(x=size+1, y=6))
    sys.stdout.write(action.save)
    sys.stdout.flush()

def middle(max_x: int, n : int, x : int, y : int, color : str = "white"):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    move_left   = moveCursor.cursor 
    position    = moveCursor.cursor
    c_bg        = colors.bg.rgb(10, 10, 10)
    magenta     = bold+init.init.blink+ c_bg + colors.fg.rbg(255, 0, 255)+"1, 1"+ reset   
    
    if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    else: c = bold + colors.fg.rbg(0, 0, 0)
    
    for i in range(n-1):
        i += 1
        input, length = counter(n=i, color=color)
        
        sys.stdout.write(move_left.LEFT(pos=1000))
        sys.stdout.write(
            input + c_bg + " " * (max_x - (length+2) ) + reset + 
            position.TO(x=max_x, y=y) + c + f"{asc['v']}" +
            position.TO(x=x, y=y) + reset + "\n"
            )
        y += 1
    sys.stdout.write(
        position.TO(x=max_x-10, y=y-2) + magenta +  position.TO(x=x, y=y-1) 
    )
    
def counter(n :int , color : str = "white"):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold    
    reset       = init.init.reset
    length      = len(str(n))
    max_x       = 5
    if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    else: c = bold + colors.fg.rbg(0, 0, 0)
    
    if (max_x - length) >= 0:  s       = f"{c}{asc['v']}{reset} "
    else:  s = ""

    return s, len("  ")

def bottom(max_x :int = 0, color : str = "white"):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold    
    reset       = init.init.reset
    
    if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    else: c = bold + colors.fg.rbg(0, 0, 0)
    
    sys.stdout.write(
        c + f"{asc['dl']}" + f"{asc['h']}" * 7 + 
        f"{asc['h']}" + f"{asc['h']}" * (max_x - 10) + 
        f"{asc['dr']}" + reset + "\n"
        )

def line(x : int, y : int, max_x : int, max_y : int, scrollUp : int = 0):
    """
    This block is used to set column and row of the cusror a each time 
    on the terminal 
    
    x       = is the currently row of the cursor 
    y       = is the currently column of the cursor 
    x_max   = width of the screen 
    y_max   = height of the screen 
    """
    position        = moveCursor.cursor
    reset           = init.init.reset
    input, length   = counter(n=1)
    asc             = frame.frame(custom=True)
    c_bg            = colors.bg.rgb(10, 10, 10)
    magenta         = init.init.bold + init.init.blink + c_bg + colors.fg.rbg(255, 0, 255) + f"{x-2}, {y+scrollUp-5}" + reset
    c               = init.init.bold + colors.fg.rbg(255, 255, 255)
    size            = len(f"{x-2}, {y+scrollUp-5}")
    
    sys.stdout.write(
        position.LEFT(pos=1000) + clear.clear.line(2)
        )
    sys.stdout.write(
        input + c_bg + " " * (max_x - (length+2) ) + reset + 
        position.TO(x=max_x, y=max_y) + c + f"{asc['v']}" +
        position.TO(x=x, y=max_y) + reset
        )
    if size <= 6:
        sys.stdout.write(
            position.TO(x=max_x-10, y=max_y) + magenta +  position.TO(x=x, y=y) 
        )
    else:
        n = size - 6
        sys.stdout.write(
            position.TO(x=max_x-10-n, y=max_y) + magenta +  position.TO(x=x, y=y) 
        )
    sys.stdout.flush()