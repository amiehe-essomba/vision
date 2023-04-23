import sys 
from frame          import frame
from header         import header
from configure      import colors, init, clear, state, screenConfig, moveCursor, scroll

def postion(x, y, max_x, string = ""):
    asc                 = frame.frame(custom=True)
    reset               = init.init.reset
    c_bg                = init.init.bold + colors.bg.rgb(10,10,10)
    move                = moveCursor.cursor 
    c                   = init.init.bold + colors.fg.rbg(255,255,255)
    Input, size         = header.counter( 0 )
    
    sys.stdout.write(move.LEFT(pos=1000))
    sys.stdout.write(
    Input + c_bg + " " * (max_x - (size+2) ) + reset + 
    move.TO(x=max_x, y=y) + c + f"{asc['v']}" +
    move.TO(x=size+1, y=y) + string + 
    move.TO(x=x, y=y) +  reset
    )
    sys.stdout.flush()

def POS(x, y, max_x, string = ""):
    asc                 = frame.frame(custom=True)
    reset               = init.init.reset
    c_bg                = init.init.bold + colors.bg.rgb(10,10,10)
    move                = moveCursor.cursor 
    c                   = init.init.bold + colors.fg.rbg(255,255,255)
    Input, size         = header.counter( 0 )
    
    sys.stdout.write(move.LEFT(pos=1000))
    sys.stdout.write(
    Input + c_bg + " " * (max_x - (size+2) ) + reset + 
    move.TO(x=max_x, y=y) + c + f"{asc['v']}" +
    move.TO(x=size+1, y=y) + string + 
    move.TO(x=x, y=y) +  reset+"\n"
    )
    sys.stdout.flush()

def auto(x : int, y : int, max_y : int, max_x : int, keys : dict = {}, keys_items: int = 1, 
                        drop_string : str = "", my_strings : list=[], I : int = 0, LEN : int = 0) :
    
    max_down            = 2
    LINE                = max_y - ( y + max_down + 1)
    N                   = max_y-(4+1) 
    asc                 = frame.frame(custom=True)
    bold                = init.init.bold
    reset               = init.init.reset
    cc                  = colors.bg.rgb(255,255,255)
    c                   = init.init.bold + colors.fg.rbg(10,10,10)
    c_bg                = init.init.bold + colors.bg.rgb(10,10,10)
    move                = moveCursor.cursor 
    cursor              = c_bg+ colors.fg.rbg(255,0,0)+chr(10999)+reset
    
    if drop_string:
        # all keys and theirs colors 
        all_names, all_colors   = keys['names'], keys['colors']
        # creating of the new lists for storing the sorting keys and colors respectively
        newNames, newColors     = [], []
        # computing the length of the drop_string 
        index                   = len(drop_string)
        
        for i, string in enumerate( all_names ) : 
            # finding if key exist 
            try:
                if drop_string == string[ : index ]:
                    # string new tring
                    newNames.append( string ) 
                    # strring associated color           
                    newColors.append( all_colors[ i ] )
                else: pass 
            except IndexError: pass
        
        if newNames:
            if len(  newNames  ) < 4 : pass 
            else: newNames = newNames[ : 4]
            
            # border size initialization
            border = 1
            # computing the true border size
            for s in newNames:
                if len(s)  > border: border = len(s)
                else: pass
            # computing the true value of border size, 
            border  += 1
            # sorting the keys inside the list 
            newNames = sorted(newNames)
            
            if LINE > len(newNames):
                #########################################################################
                postion(x, y+1, max_x)
                # first line     
                sys.stdout.write(
                    move.TO(x=x-LEN, y=y+1) + c_bg + " " * LEN + move.TO(x=x, y=y+1) + reset + 
                    cc+c + f"{asc['ul']}" + f"{asc['h']}" * (border) + f"{asc['ur']}" +
                    move.TO(x=x+border+2, y=y+1) + reset + c_bg+ " " * (max_x-x-border-3)
                    + reset + "\n")
                #########################################################################
                # middle  lines
                idd = 0
                for i in range( len(newNames )+1):
                    idd += 1
                    postion(x, y+idd+1, max_x)
                    # initialization of the the cusror
                    if i == 0:
                        sys.stdout.write( 
                            cc+c + f"{asc['v']}"  + bold + cc +  
                            " " * (border) + cc+c + f"{asc['v']}" + 
                            cursor + reset + "\n"
                            )
                    # remove cursor
                    else:
                        sys.stdout.write( 
                            cc+c + f"{asc['v']}"  + bold + cc +  
                            " " * (border) + cc+c + f"{asc['v']}" + 
                            reset + "\n"
                        )
                    sys.stdout.flush()
                #########################################################################
                # third line
                postion(x, y+idd+1, max_x) 
                sys.stdout.write(cc+c + f"{asc['dl']}" + f"{asc['h']}" * (border) + f"{asc['dr']}"+ reset + "\n")
                sys.stdout.flush()
                #########################################################################
                postion(x, y, max_x, my_strings[I])
                sys.stdout.write(move.TO(x=x, y=y))
                
                # writing keys inside white board
                for i in range(len(newNames)):
                    sys.stdout.write(
                        move.TO(x=x+1, y=y+i+2) +
                        keys_items[newNames[i]] +
                        init.init.bold + newNames[i] + c + " " * (border - len(newNames[i]))+
                        reset + "\n"
                        )
                    sys.stdout.flush()
                #########################################################################
                X, Y = screenConfig.cursor()
                postion(x, Y, max_x) 
                sys.stdout.write(cc+c + f"{asc['dl']}" + f"{asc['h']}" * (border) + f"{asc['dr']}"+ reset + "\n")
                sys.stdout.flush()
                # computing the new cusor postion 
                NEW_LINE = max_y - (Y+max_down+1)
                # restoring the screen 
                if NEW_LINE <= 0: pass 
                else:
                    for i in range(0,NEW_LINE+1):
                        M = Y+i
                        try: POS(x, M, max_x, string=my_strings[I+i+1])
                        except IndexError: POS(x, M, max_x)
                        sys.stdout.flush()
                # restoring the true cursor position on the screen
                sys.stdout.write(move.TO(x=x, y=y))
                sys.stdout.flush()
                #########################################################################
            else: pass
        else: 
            # if no key was detected by the script 
            # then we just print the values of the list from the cursor 
            # until the end of the line 
            NEW_LINE = max_y - (Y+max_down+1)
            if NEW_LINE > 0 :pass 
            else:
                for i in range(NEW_LINE-1):
                    try: POS(x, y+i, max_x, string=my_strings[I+i])
                    except IndexError:postion(x, y+i, max_x)
                    sys.stdout.flush()
            # restoring the cursor position    
            sys.stdout.write(move.TO(x=x, y=y))
            sys.stdout.flush()
    else:
        # if not drop_string we just 
        # print the values of the list from the cursor until the end of the line 
        NEW_LINE = max_y - (y+max_down+1)
        if NEW_LINE == 0 :pass 
        else:
            for i in range(NEW_LINE):
                try: POS(x, y+i, max_x, string=my_strings[I+i])
                except IndexError: postion(x, y+i, max_x)
                sys.stdout.flush()
        # restoring the cursor position
        sys.stdout.write(move.TO(x=x, y=y))
        sys.stdout.flush()