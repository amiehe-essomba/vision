import os , sys 
from configure  import colors, init, clear, moveCursor 
from frame      import frame
from header     import header

def count(number : int , x : int , y : int , max_x : int, max_y : int, lang : str = 'python', action : bool = False):
    move                = moveCursor.cursor
    asc                 = frame.frame(custom=True)
    bold                = init.init.bold
    reset               = init.init.reset
    c_bg                = colors.bg.rgb(10, 10, 10)  
    c                   = bold + colors.fg.rbg(255, 255, 255)
    _lang_              = bold+init.init.blink+ c_bg + colors.fg.rbg(0, 255, 0)+f"{lang} programm"+ reset 
    magenta             = bold+init.init.blink+ c_bg + colors.fg.rbg(255, 0, 255)+f"{x}, {number+1}"+ reset 
    if action is False:
        _opened_        = bold+init.init.blink+ c_bg + colors.fg.rbg(0, 255, 255)+f" opened"+ reset 
    else: _opened_        = bold+init.init.blink+ c_bg + colors.fg.rbg(0, 255, 255)+f" locked"+ reset 
    
    input, length         = header.counter(n=0)

    #sys.stdout.write()
    sys.stdout.write(
        move.TO(x=length+2, y=max_y) + move.LEFT(pos=1000) + clear.clear.line(2)+
        input + c_bg + " " * (max_x - (length+2) ) + reset + 
        move.TO(x=max_x, y=max_y) + c + f"{asc['v']}" +
        move.TO(x=length+1, y=max_y) +  move.TO(x=length+2, y=max_y) + 
        _lang_ + _opened_ + 
        move.TO(x=max_x-10, y=max_y) + magenta + 
        move.TO(x=x, y=y) + reset
        )
    sys.stdout.flush()