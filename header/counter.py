import sys 
from configure  import colors, init, clear, moveCursor 
from frame      import frame
from header     import header

def count(number : int , x : int , y : int , max_x : int, max_y : int, lang : str = 'python', action : bool = False, COLOR : dict = {}):
    move                = moveCursor.cursor
    asc                 = frame.frame(custom=True)
    bold                = init.init.bold
    reset               = init.init.reset
    c_bg                = COLOR['fgColor'] 
    c                   = COLOR['white'] 
    _lang_              = COLOR['proColor']+f"{lang} program"+ reset 
    magenta             = COLOR["CRColor"]+f"{x-2}, {number+1}"+ reset 
    if action is False: _opened_        = f"{COLOR['openedColor']} opened"+ reset 
    else:               _opened_        = f"{COLOR['openedColor']} locked"+ reset 
    input, length         = header.counter(n=0, COLOR=COLOR.copy())

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