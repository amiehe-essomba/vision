import sys 
from configure  import colors, init, clear, state, screenConfig, moveCursor, scroll
from frame      import frame
from header     import checkFile
from header     import add
from keywords   import words

def title(max_x :int = 0, max_y :int = 0, size : int = 0,  color : str = "white",  
                                dataBase : dict = {}, data : dict = {}, lang="unknwon"):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    cc          = init.init.bold + colors.fg.rbg(0, 255, 255)
    string      = "VISION EDITOR V-1.0.0-beta".center(max_x - 2)
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
    
    # position of the first line 
    LINE = y
    
    if not data['input']:
        middle(max_x=max_x, n=max_y-5 ,x=x, y=y, color=color, lang=lang)
        sys.stdout.write(move.LEFT(pos=1000))
        bottom(max_x=max_x, color=color)
        sys.stdout.write(move.TO(x=size+1, y=4))
        sys.stdout.write(action.save)
        N = 0
    else: 
        N, scrolledUp = writingData(max_x=max_x, n=max_y-LINE, x=x, y=y, color=color, dataBase=dataBase, data=data, lang=lang)
        sys.stdout.write(move.LEFT(pos=1000))
        bottom(max_x=max_x, color=color)
        
        if scrolledUp is True: sys.stdout.write(move.UP(pos=3)+move.RIGHT(pos=size))
        else: sys.stdout.write(move.TO(x=size+1, y=LINE))
        
        sys.stdout.write(action.save)
        add.add(dataBase)
        
    sys.stdout.flush()
    
    return N
    
def writingData(max_x: int, n : int, x : int, y : int, color : str = "white", 
                dataBase : dict = {}, data : dict = {}, lang : str = ""):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    move_left   = moveCursor.cursor 
    position    = moveCursor.cursor
    c_bg        = colors.bg.rgb(10, 10, 10)  
    print_data  = data['writing'].copy()
    string      = data['string'].copy()
    Input       = data["input"].copy()
    N           = len(Input)
    
    if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    else: c  = bold + colors.fg.rbg(0, 0, 0)
    input, length       = counter(n=0, color=color)
    scrolledUp          = False 
    _lang_              = bold+init.init.blink+ c_bg + colors.fg.rbg(0, 255, 0)+f"{lang} programm"+colors.fg.rbg(0, 255, 255) + " opened"+ reset 
    magenta             = bold+init.init.blink+ c_bg + colors.fg.rbg(255, 0, 255)+f"{x}, {N}"+ reset 

    for i in range(N-1):
        dataBase['memory'].append( [] )
        dataBase['tabular'].append( [] )
        dataBase['string_tab'].append( [] )
        dataBase['liste'].append( [] )
        dataBase['string_tabular'].append( [] )
        dataBase['x_y'].append( [] )
    
    for i in range(N):
        dataBase['string'], dataBase['input']  = string[i], Input[i]
        dataBase['I_S'], dataBase['index']      = len(string[i]), len(Input[i])
        
        checkFile.check(data=string[i], dataBase=dataBase, x=length+1, y=y, w=i)
        
        if i < n-3 :
            sys.stdout.write(move_left.LEFT(pos=1000))
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset + 
                position.TO(x=max_x, y=y) + c + f"{asc['v']}" +
                position.TO(x=length+1, y=y) + c_bg + print_data[i] + reset + "\n"
                )
        elif i == n -3 :
            sys.stdout.write(move_left.LEFT(pos=1000))
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset + 
                position.TO(x=max_x, y=y) + c + f"{asc['v']}" +
                position.TO(x=length+1, y=y) + c_bg +  print_data[i] + reset + "\n"
                )
        else: pass
        y += 1
    
    if N > (n-2): 
        scrolledUp = True
        sys.stdout.write(
            input + c_bg + " " * (max_x - (length+2) ) + reset + 
            position.TO(x=max_x, y=n+2) + c + f"{asc['v']}" +
            position.TO(x=x, y=n+2) + reset + position.TO(x=length+2, y=n+2)+ _lang_+
            position.TO(x=max_x-10, y=n+2) + magenta + position.DOWN(1)
            )
    elif N == (n-2):
        scrolledUp = True
        h = 2
        for i in range(h):
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset + 
                position.TO(x=max_x, y=y) + c + f"{asc['v']}" +
                position.TO(x=x, y=y) + reset + "\n" 
                )
            y += 1
        sys.stdout.write(position.TO(x=length+2, y=y-1)+ _lang_+
            position.TO(x=max_x-10, y=y-1) + magenta +  position.DOWN(1)
        )
    else:
        n -= (N+1)
        for i in range(n):
            sys.stdout.write(move_left.LEFT(pos=1000))
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset + 
                position.TO(x=max_x, y=y) + c + f"{asc['v']}" +
                position.TO(x=x, y=y) + reset + "\n" if i != n-1 else ""
                )
            y += 1

        sys.stdout.write(
            input + c_bg + " " * (max_x - (length+2) ) + reset + 
            position.TO(x=max_x, y=y) + c + f"{asc['v']}" +
            position.TO(x=x, y=y) + reset
            )
        sys.stdout.write(position.TO(x=length+2, y=y-1)+ _lang_+
            position.TO(x=max_x-10, y=y-1) + magenta + 
            position.TO(x=max_x, y=y-1) + c + f"{asc['v']}" + position.DOWN(1)
        )
    
    return N, scrolledUp

def middle(max_x: int, n : int, x : int, y : int, color : str = "white", lang : str = "unknown"):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    move_left   = moveCursor.cursor 
    position    = moveCursor.cursor
    c_bg        = colors.bg.rgb(10, 10, 10)
    magenta     = bold+init.init.blink+ c_bg + colors.fg.rbg(255, 0, 255)+"1, 1"+ reset   
    _lang_        = bold+init.init.blink+ c_bg + colors.fg.rbg(0, 255, 0)+f"{lang} programm"+ colors.fg.rbg(0, 255, 255) + " opened" + reset 
    
    if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    else: c = bold + colors.fg.rbg(0, 0, 0)
    
    input, length = counter(n=0, color=color)
    
    for i in range(n+1): 
        sys.stdout.write(move_left.LEFT(pos=1000))
        sys.stdout.write(
            input + c_bg + " " * (max_x - (length+2) ) + reset + 
            position.TO(x=max_x, y=y) + c + f"{asc['v']}" +
            position.TO(x=x, y=y) + reset + "\n"
            )
        y += 1
    sys.stdout.write(
        position.TO(x=max_x-10, y=y-2) + magenta + 
        position.TO(x=length+2, y=y-2) + _lang_ + 
        position.TO(x=x, y=y-1) 
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

def line(x : int, y : int, max_x : int, max_y : int, scrollUp : int = 0, lang : str = "unknwon"):
    """
    This block is used to set column and row of the cusror a each time 
    on the terminal 
    
    x       = is the currently row of the cursor 
    y       = is the currently column of the cursor 
    x_max   = width of the screen 
    y_max   = height of the screen 
    """
    bold            = init.init.bold
    position        = moveCursor.cursor
    reset           = init.init.reset
    input, length   = counter(n=1)
    asc             = frame.frame(custom=True)
    c_bg            = colors.bg.rgb(10, 10, 10)
    magenta         = init.init.bold + init.init.blink + c_bg + colors.fg.rbg(255, 0, 255) + f"{x-2}, {y+scrollUp-3}" + reset
    c               = init.init.bold + colors.fg.rbg(255, 255, 255)
    size            = len(f"{x-2}, {y+scrollUp-5}")
    _lang_          = bold+init.init.blink+ c_bg + colors.fg.rbg(0, 255, 0)+f"{lang} programm"+ reset 
    
    sys.stdout.write(
        position.LEFT(pos=1000) + clear.clear.line(2)
        )
    sys.stdout.write(
        input + c_bg + " " * (max_x - (length+2) ) + reset + 
        position.TO(x=max_x, y=max_y) + c + f"{asc['v']}" +
        position.TO(x=x, y=max_y) + reset
        )
    if size <= 6:
        sys.stdout.write(position.TO(x=length+2, y=max_y)+ _lang_+
            position.TO(x=max_x-10, y=max_y) + magenta +  position.TO(x=x, y=y) 
        )
    else:
        n = size - 6
        sys.stdout.write(position.TO(x=length+2, y=max_y)+ _lang_+
            position.TO(x=max_x-10-n, y=max_y) + magenta +  position.TO(x=x, y=y) 
        )
    sys.stdout.flush()
        
def Insert(data, x : int, y : int, max_x : int, max_y : int, lang : str = "unknwon", Color : str ="", locked : bool=False, m : int = 0, line : int=0):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    move_left   = moveCursor.cursor 
    position    = moveCursor.cursor
    c_bg        = colors.bg.rgb(10, 10, 10) 
    N           = len(data)
    color       = "white"
    X, Y        = x, y
    magenta     = bold+init.init.blink+ c_bg + colors.fg.rbg(255, 0, 255)+f"1, {line+1}"+ reset 
    _lang_      = bold+init.init.blink+ c_bg + colors.fg.rbg(0, 255, 0)+f"{lang} programm"+ reset  
    
    if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    else: c = bold + colors.fg.rbg(0, 0, 0)
    scrollUp        = 0
    input, length   = counter(n=0, color=color)
    
    for i in range(N):
        __line__, __color__ = words.words(string=data[i], color=Color, language=lang ).final(locked=locked, m=m)
        sys.stdout.write(position.LEFT(pos=1000))
        sys.stdout.write(
            input + c_bg + " " * (max_x - (length+2) ) + reset + 
            position.TO(x=max_x, y=Y+i) + c + f"{asc['v']}" +
            position.TO(x=length+1, y=Y+i) + c_bg + __line__ + 
            position.TO(x=length+1, y=Y+i)+reset+'\n' if i != N-1 else ""
            )
        #######################################
        # changing color or reset color  
        if __color__["locked"] is False:  
            locked = False
            m      = 0
        else: 
            Color  = __color__["color"]
            locked = True
            m      = __color__["rest"]
        #######################################
        XX, YY = screenConfig.cursor()
        
        if YY <= max_y-3: 
            n = (max_y-3)-YY + 2
            for i in range(n):
                i -= 1 
                sys.stdout.write(move_left.LEFT(pos=1000))
                sys.stdout.write(
                    input + c_bg + " " * (max_x - (length+2) ) + reset + 
                    position.TO(x=max_x, y=YY+i) + c + f"{asc['v']}" +
                    position.TO(x=x, y=YY+i) + reset + "\n" if  i != n-1 else "" 
                    )
            XX, YY = screenConfig.cursor()
            sys.stdout.write(move_left.LEFT(pos=1000))
            sys.stdout.write(
                input + c_bg + " " * (max_x - (length+2) ) + reset + 
                position.TO(x=max_x, y=YY) + c + f"{asc['v']}" +
                position.TO(x=max_x-10, y=YY) + magenta + 
                position.TO(x=length+2, y=YY) + _lang_ 
                + reset 
                )
        else: pass
                
def subTitle(max_x:int, x:int, y:int, lang : str="", scrollUp : int = 0):
    bold            = init.init.bold
    position        = moveCursor.cursor
    reset           = init.init.reset
    input, length   = counter(n=1)
    asc             = frame.frame(custom=True)
    c_bg            = colors.bg.rgb(10, 10, 10)
    magenta         = init.init.bold + init.init.blink + c_bg + colors.fg.rbg(255, 0, 255) + f"{x-2}, {y+scrollUp-5}" + reset
    c               = init.init.bold + colors.fg.rbg(255, 255, 255)
    magenta     = bold+init.init.blink+ c_bg + colors.fg.rbg(255, 0, 255)+f"{x}, {y}"+ reset 
    _lang_        = bold+init.init.blink+ c_bg + colors.fg.rbg(0, 255, 0)+f"{lang} programm"+ reset  
    
    sys.stdout.write(
    input + c_bg + " " * (max_x - (length+2) ) + reset + 
    position.TO(x=max_x, y=y) + c + f"{asc['v']}" +
    position.TO(x=length+1, y=y) + reset
    )
    sys.stdout.write(position.TO(x=length+2, y=y)+ _lang_+
        position.TO(x=max_x-10, y=y) + magenta +  position.TO(x=x, y=y)+'\n'+position.LEFT(1000)
    )
    sys.stdout.flush()