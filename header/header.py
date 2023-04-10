import os  
import sys 
from configure  import colors, init, clear, state, screenConfig, moveCursor
from frame      import frame

def head():
    if os.name == "nt":
        from ctypes         import windll

        clear_line = clear.clear.line(pos=0)
        move_left  = moveCursor.cursor.LEFT(pos=1000)
        
        k  = windll.kernel32
        k.SetConsoleMode( k.GetStdHandle(-11), 7)
        # clear entire line
        sys.stdout.write(clear_line)
        # move cursor left
        sys.stdout.write(move_left)
        # print the input value

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
    sys.stdout.write(c + f"{asc['vl']}" + f"{asc['h']}" * 7 + f"{asc['m1']}" +  
                         f"{asc['h']}"*(max_x - 10) + f"{asc['vr']}" + reset + "\n")

    # currently cursor position (x, y)    
    x, y = screenConfig.cursor()
    
    middle(max_x=max_x, n=max_y-5 ,x=x, y=y, color=color)
    sys.stdout.write(move.LEFT(pos=1000))
    bottom(max_x=max_x, color=color)
    sys.stdout.write(move.TO(x=size+1, y=5))
    sys.stdout.write(action.save)
    sys.stdout.flush()

def middle(max_x: int, n : int, x : int, y : int, color : str = "white"):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    move_left   = moveCursor.cursor 
    position    = moveCursor.cursor
    c_bg        = colors.bg.rgb(10, 10, 10)
    
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

def counter(n :int , color : str = "white"):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold    
    reset       = init.init.reset
    length      = len(str(n))
    max_x       = 5
    space       = " " * (max_x - length)
    cc          = bold + colors.fg.rbg(255, 153, 204)
    if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    else: c = bold + colors.fg.rbg(0, 0, 0)
    
    if (max_x - length) >= 0:  s       = f"{c}{asc['v']}[{space}{cc}{n}{c}]{asc['v']}{reset} "
    else:  s = ""

    return s, len(f"[{space}{n}]   ")

def bottom(max_x :int = 0, color : str = "white"):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold    
    reset       = init.init.reset
    
    if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    else: c = bold + colors.fg.rbg(0, 0, 0)
    
    sys.stdout.write(
        c + f"{asc['dl']}" + f"{asc['h']}" * 7 + 
        f"{asc['m2']}" + f"{asc['h']}" * (max_x - 10) + 
        f"{asc['dr']}" + reset + "\n"
        )