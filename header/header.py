import sys 
import platform
from configure  import colors, init, state, screenConfig, moveCursor
from frame      import frame
from header     import checkFile
from header     import add


def title(max_x :int = 0, max_y :int = 0, size : int = 0,  color : str = "white",  
                                dataBase : dict = {}, data : dict = {}, lang="unknwon", COLOR : dict={}):
    system      = platform.system()
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    cc          = COLOR['titleColor']
    ball        = chr(9898)
    string      = f"{ball}{ball} VISION EDITOR {ball}{ball}".center(max_x - 6)
    _string_    = f"VISION EDITOR".center(max_x - 2)
    move        = moveCursor.cursor 
    action      = state.save
    c           = COLOR['white']
    
    if system in {"Linux", "Macos"}:
        # first line 
        sys.stdout.write(c + f"{asc['ul']}" + f"{asc['h']}" * (max_x-2) + f"{asc['ur']}" + reset + "\n")
        # second line 
        sys.stdout.write(c + f"{asc['v']}"  + bold + cc +  string + c + f"{asc['v']}" + reset + "\n" )
        # third line 
        sys.stdout.write(c + f"{asc['vl']}" + f"{asc['h']}" * 7 + f"{asc['h']}" +  
                            f"{asc['h']}"*(max_x - 10) + f"{asc['vr']}" + reset+ "\n")
    else:
        # first line 
        sys.stdout.write(move.LEFT(1000)+c + f"{asc['ul']}" + f"{asc['h']}" * (max_x-2) + f"{asc['ur']}" + reset +"\n")
        # second line 
        sys.stdout.write(move.LEFT(1000)+c + f"{asc['v']}"  + cc + bold + _string_+reset  + f"{asc['v']}" + reset + "\n")
        # third line 
        sys.stdout.write(move.LEFT(1000)+c + f"{asc['vl']}" + f"{asc['h']}" * 7 + f"{asc['h']}" +  
                            f"{asc['h']}"*(max_x - 10) + f"{asc['vr']}" + reset +"\n")

    # currently cursor position (x, y)    
    x, y = screenConfig.cursor()
    
    # position of the first line 
    LINE = y
                                                                                                                                                             
    if not data['input']:
        middle(max_x=max_x, n=max_y-5 ,x=x, y=y, color=color, lang=lang, COLOR=COLOR.copy())
        sys.stdout.write(move.LEFT(pos=1000))
        bottom(max_x=max_x, color=color, COLOR=COLOR.copy())
        sys.stdout.write(move.TO(x=size+1, y=4))
        sys.stdout.write(action.save)
        N = 0
    else: 
        N, scrolledUp = writingData(max_x=max_x, n=max_y-LINE, x=x, y=y, color=color, dataBase=dataBase, 
                                        data=data, lang=lang, COLOR=COLOR.copy())
        sys.stdout.write(move.LEFT(pos=1000))
        bottom(max_x=max_x, color=color, COLOR=COLOR.copy())
        
        if scrolledUp is True: sys.stdout.write(move.UP(pos=3)+move.RIGHT(pos=size))
        else: sys.stdout.write(move.TO(x=size+1, y=LINE))
        
        sys.stdout.write(action.save)
        add.add(dataBase)
        
    sys.stdout.flush()
    
    return N
    
def writingData(max_x: int, n : int, x : int, y : int, color : str = "white", 
                dataBase : dict = {}, data : dict = {}, lang : str = "", COLOR : dict={}):
    asc                 = frame.frame(custom=True)
    bold                = init.init.bold
    reset               = init.init.reset
    move_left           = moveCursor.cursor 
    position            = moveCursor.cursor
    c_bg                = COLOR['bgColor'] 
    print_data          = data['writing'].copy()
    string              = data['string'].copy()
    Input               = data["input"].copy()
    N                   = len(Input)
    c                   = COLOR["white"]
    input, length       = counter(n=0, color=color, COLOR=COLOR.copy())
    scrolledUp          = False 
    _lang_              = f"{COLOR['proColor']}{lang} program"+f"{COLOR['openedColor']} opened"+ reset 
    magenta             = f"{COLOR['CRColor']}{x}, {N}"+ reset 

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

def middle(max_x: int, n : int, x : int, y : int, color : str = "white", lang : str = "unknown", COLOR : dict = {}):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold
    reset       = init.init.reset
    move_left   = moveCursor.cursor 
    position    = moveCursor.cursor
    c_bg        = COLOR['bgColor']
    c           = COLOR['white']  
    _lang_      = f"{COLOR['proColor']}{lang} program"+f"{COLOR['openedColor']} opened"+ reset 
    magenta     = f"{COLOR['CRColor']}{1}, {1}"+ reset 
    
    input, length = counter(n=0, color=color, COLOR=COLOR.copy())
    
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
    
def counter(n :int , color : str = "white", COLOR : dict = {}):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold    
    reset       = init.init.reset
    length      = len(str(n))
    max_x       = 5
    c           = COLOR['white']
    
    #if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    #else: c = bold + colors.fg.rbg(0, 0, 0)
    
    if (max_x - length) >= 0:  s       = f"{c}{asc['v']}{reset} "
    else:  s = ""

    return s, len("  ")

def bottom(max_x :int = 0, color : str = "white", COLOR : dict = {}):
    asc         = frame.frame(custom=True)
    bold        = init.init.bold    
    reset       = init.init.reset
    c           = COLOR['white']
    #if color == "white": c   = bold + colors.fg.rbg(255, 255, 255)
    #else: c = bold + colors.fg.rbg(0, 0, 0)
    
    sys.stdout.write(
        c + f"{asc['dl']}" + f"{asc['h']}" * 7 + 
        f"{asc['h']}" + f"{asc['h']}" * (max_x - 10) + 
        f"{asc['dr']}" + reset + "\n"
        )

