import sys 
from frame          import frame
from header         import header
from configure      import init, screenConfig, moveCursor

def postion(x, y, max_x, string = "", COLOR : dict = {}):
    asc                 = frame.frame(custom=True)
    reset               = init.init.reset
    c_bg                = COLOR['bgColor']
    move                = moveCursor.cursor 
    c                   = COLOR['white']
    Input, size         = header.counter( 0 )
    
    sys.stdout.write(move.LEFT(pos=1000))
    sys.stdout.write(
    Input + c_bg + " " * (max_x - (size+2) ) + reset + 
    move.TO(x=max_x, y=y) + c + f"{asc['v']}" +
    move.TO(x=size+1, y=y) + string + 
    move.TO(x=x, y=y) +  reset
    )
    sys.stdout.flush()

def POS(x, y, max_x, string = "", COLOR : dict = {}):
    asc                 = frame.frame(custom=True)
    reset               = init.init.reset
    c_bg                = COLOR['bgColor']
    move                = moveCursor.cursor 
    c                   = COLOR['white']
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
                drop_string : str = "", my_strings : list=[], I : int = 0, LEN : int = 0, 
                idd_select : dict = {"idd" : 0, "index" : 0}, COLOR : dict = {}) :
    # the lastest two line
    max_down            = 2
    # max line on the black screen 
    LINE                = max_y - ( y + max_down + 1)
    # same as LINE
    N                   = max_y-(4+1) 
    # frame used to draw the black screen 
    asc                 = frame.frame(custom=True)
    # set bold characters 
    bold                = init.init.bold
    # reset characters
    reset               = init.init.reset
    # set while color 
    cc                  = COLOR['bgWhite']
    # set bold and black screen 
    c                   = COLOR['fgBlack']
    # set bold and black screen 
    c_bg                = COLOR['bgColor']
    # cursor action 
    move                = moveCursor.cursor 
    # set the identifier 
    cursor              = COLOR["cursorColor"] + reset
    # max elements which can be contained in the white screen
    max_element         = 4 
    # returning string 
    return_string       = ""
    
    if drop_string:
        # all keys and theirs colors 
        all_names, all_colors   = keys['names'].copy(), keys['colors'].copy()
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
            
        # sorting the keys inside the list 
        newNames = sorted(newNames).copy()
                                
        if newNames:
            _IDD_   = idd_select["idd"]
            _INDEX_ = idd_select["index"]
            
            # selecting the number of elements inside the lits 
            if len(  newNames  ) < max_element : pass 
            else: 
                if _IDD_+_INDEX_ < max_element: newNames = newNames[ : max_element]
                else:
                    try: 
                        _newNames_ = newNames[ _INDEX_ : ]
                        if len(_newNames_) >= max_element : newNames = _newNames_[ : max_element]
                        else:  newNames = newNames[-max_element : ] 
                    except IndexError: newNames = newNames[-max_element  : ] 
              
            # border size initialization
            border = 1
            # computing the true border size
            for s in newNames:
                if len(s)  > border: border = len(s)
                else: pass
            # computing the true value of border size, 
            border  += 4
            
            if (max_x - (x+border+2)) > 0 :
                # get return values
                try: return_string = newNames[_IDD_]
                except IndexError: 
                    n = _IDD_
                    while False:
                        n -= 1
                        return_string = newNames[n]          
                
                if LINE > (len(newNames) + 1):
                    #########################################################################
                    postion(x, y+1, max_x, COLOR = COLOR.copy())
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
                        postion(x, y+idd+1, max_x, COLOR = COLOR.copy())
                        # initialization of the the cusror
                        if i == _IDD_:
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
                    postion(x, y+idd+1, max_x , COLOR = COLOR.copy()) 
                    sys.stdout.write(cc+c + f"{asc['dl']}" + f"{asc['h']}" * (border) + f"{asc['dr']}"+ reset + "\n")
                    sys.stdout.flush()
                    #########################################################################
                    postion(x, y, max_x, my_strings[I] , COLOR = COLOR.copy())
                    sys.stdout.write(move.TO(x=x, y=y))
                    
                    # writing keys inside white board
                    for i in range(len(newNames)):
                        sys.stdout.write(
                            move.TO(x=x+1, y=y+i+2) +
                            cc + keys_items[newNames[i]] +
                            init.init.bold + newNames[i] + c + " " * (border - len(newNames[i]))+
                            reset + "\n"
                            )
                        sys.stdout.flush()
                    #########################################################################
                    
                    X, Y = screenConfig.cursor()
                    postion(x, Y, max_x, COLOR = COLOR.copy()) 
                    sys.stdout.write(cc+c + f"{asc['dl']}" + f"{asc['h']}" * (border) + f"{asc['dr']}"+ reset + "\n")
                    sys.stdout.flush()
                    # computing the new cusor postion 
                    NEW_LINE = max_y - (Y+max_down+1)
                    # restoring the screen 
                    if NEW_LINE <= 0: pass 
                    else:
                        for i in range(NEW_LINE):
                            M = Y+i+1
                            try: POS(x, M, max_x, string=my_strings[I+i+1], COLOR = COLOR.copy())
                            except IndexError: POS(x, M, max_x, COLOR = COLOR.copy())
                            sys.stdout.flush()
                    # restoring the true cursor position on the screen
                    sys.stdout.write(move.TO(x=x, y=y))
                    sys.stdout.flush()
                    
                    return None, return_string, len(return_string)
                    #########################################################################
                else:
                    # computing the number of lines could be print on the screen
                    N           = max_y - (4+max_down+1) + 1
                    # computing the number of line which going to be scrolled 
                    delimitor   = ((len(newNames) + 1) - LINE)+2
                    # extracting the data of the main list of data 
                    new_list    = my_strings[ delimitor : ].copy() 
                    
                    # checking the first condition 
                    if N > len(new_list):
                        # when the first condition is respected
                        if (N-len(new_list)) >= (len(newNames)+1) : pass 
                        # when first condition is respected
                        else: 
                            # computing the new delimitor position
                            delimitor += ((len(newNames)+1) - (N - len(new_list))) + 1
                            # getting the new list
                            new_list  = my_strings[ delimitor : ]
                    # checking the second condition 
                    else:
                        # wrunning while loop until the second condition is not respected 
                        while N < len(new_list):
                            delimitor += 1
                            new_list  = my_strings[ delimitor : ].copy()
                        # computing the new delimitor postion 
                        delimitor += ((len(newNames)+1) - (N - len(new_list))) + 1
                        # getting the new list 
                        new_list  = my_strings[ delimitor : ] 
                    
                    # initialization of y postion on 4          
                    Y = 4
                    # moving cursor postion of (x, 4)
                    sys.stdout.write(move.TO(x=0, y=4))
                    sys.stdout.flush()
                    
                    # printing the values stored in new_list from the beginning of screen
                    for i in range(N):
                        try: POS(x, Y, max_x, string=new_list[i], COLOR = COLOR.copy())
                        except IndexError: POS(x, Y, max_x, COLOR = COLOR.copy())
                        sys.stdout.flush()
                        Y += 1
                    
                    # new initialization of y postion on len(new_list)+3
                    Y = len(new_list)+(max_element-1)
                    
                    # drawing the white board 
                    #########################################################################
                    postion(x, Y+1, max_x, COLOR = COLOR.copy())
                    # first line     
                    sys.stdout.write(
                        move.TO(x=x-LEN, y=Y+1) + c_bg + " " * LEN + move.TO(x=x, y=Y+1) + reset + 
                        cc+c + f"{asc['ul']}" + f"{asc['h']}" * (border) + f"{asc['ur']}" +
                        move.TO(x=x+border+2, y=Y+1) + reset + c_bg+ " " * (max_x-x-border-3)
                        + reset + "\n")
                    #########################################################################
                    
                    # middle  lines
                    idd = 0
                    for i in range( len(newNames )+1):
                        idd += 1
                        postion(x, Y+1+idd, max_x, COLOR = COLOR.copy())
                        # initialization of the the cusror
                        if i == _IDD_:
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
                    postion(x, Y+1+idd, max_x, COLOR = COLOR.copy()) 
                    sys.stdout.write(cc+c + f"{asc['dl']}" + f"{asc['h']}" * (border) + f"{asc['dr']}"+ reset + "\n")
                    sys.stdout.flush()
                    #########################################################################
                    #postion(x, Y, max_x, my_strings[I])
                    sys.stdout.write(move.TO(x=x, y=Y))
                    
                    # writing keys inside white board
                    for i in range(len(newNames)):
                        sys.stdout.write(
                            move.TO(x=x+1, y=Y+i+2) +
                            cc + keys_items[newNames[i]] +
                            init.init.bold + newNames[i] + c + " " * (border - len(newNames[i]))+
                            reset + "\n"
                            )
                        sys.stdout.flush()
                        
                    sys.stdout.write(move.TO(x=x, y=Y))
                    sys.stdout.flush()
                    
                    # returning the new y position after scrolling screen
                    return Y, return_string, len(return_string)
            else: return None, "", 0
        else: 
            # if no key was detected by the script 
            # then we just print the values of the list from the cursor 
            # until the end of the line 
            NEW_LINE = max_y - (y+max_down+1)
            if NEW_LINE > 0 :pass 
            else:
                for i in range(NEW_LINE+1):
                    try: POS(x, y+i, max_x, string=my_strings[I+i], COLOR = COLOR.copy())
                    except IndexError: POS(x, y+i, max_x, COLOR = COLOR.copy())
                    sys.stdout.flush()
            # restoring the cursor position    
            sys.stdout.write(move.TO(x=x, y=y))
            sys.stdout.flush()
            
            return None, "", 0
    else:
        # if not drop_string we just 
        # print the values of the list from the cursor until the end of the line 
        NEW_LINE = max_y - (y+max_down+1)
        if NEW_LINE == 0 :pass 
        else:
            for i in range(NEW_LINE+1):
                try: POS(x, y+i, max_x, string=my_strings[I+i], COLOR = COLOR.copy())
                except IndexError: POS(x, y+i, max_x, COLOR = COLOR.copy())
                sys.stdout.flush()
        # restoring the cursor position
        sys.stdout.write(move.TO(x=x, y=y))
        sys.stdout.flush()
        
        return None, "", 0