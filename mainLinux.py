import sys, os 
from getUserInput   import input
from configure      import colors, init, clear, state, screenConfig, moveCursor, scroll
from frame          import frame
from DataBase       import data
from header         import header, formating, counter
from saving         import save, writing
from keywords       import words
import time

class IDE:
    def __init__(self, termios : str = "none", lang : str ="unknown"):
        # border configuration 
        self.acs                = frame.frame(custom=True)
        # loading backgroung color 
        self.color_bg           = colors.bg
        # loading foreground color 
        self.color_fg           = colors.fg
        # loading initialization cursor parameters 
        self.init               = init.init
        # loading keywords for cleaning screen and lines 
        self.clear              = clear.clear
        # save and restore cursor postion 
        self.state              = state 
        # getting max size (max_x, max_y) of the window 
        self.max_x, self.max_y  = screenConfig.cursorMax()
        # getting the cursor coordiantes (x, y)
        self.x, self.y          = screenConfig.cursor()
        # loading the keywords for moving cursor on a particular region of the screen 
        self.move               = moveCursor.cursor
        # scrolling the cursor 
        self.scroll             = scroll.scrolled
        # set termios style (theme ), default value = monokai 
        self.termios            = termios
        # language type 
        self.lang               = lang
        
    def VISION(self, importation : dict = {}, writeData : dict = {}, path : str = "" ):
        # loading external data 
        self.importation            = importation
        #
        self.Data                   = data.base()
        #
        self.indexation             = data.indexation()
        # accounting line
        self.if_line                = 0
        # max lines
        self.if_line_max            = 0
        # move curor up fist time 
        self.key_up_first_time      = True
        # storing key_up_first_time
        self.key_up_id              = False 
        # action to do after one of these commands is pressed 
        # it means UP, DOWN or ENTER is pressed
        self.action                 = None
        # fixing the x-axis border 
        self.border_x_limit         = True 
        # last line 
        self.last_line              = {"last": self.max_y-2, "now" : 0}
        # counter 
        self.np                     = 2
        # writing data in a file
        self.writeData              = writeData
        # bg color 
        self.c_bg                   = self.init.bold + self.color_bg.rgb(10, 10, 10)
        # fg color 
        self.c                      = self.init.bold + self.color_fg.rbg(255, 255, 255)
        # building color 
        self.color                  = self.c_bg + self.c
        # locked the writings 
        self.locked                 = False 
        self.m                      = 0
        # limitation of the last line 
        self.max_down               = 2
        # first line position after the name of the EDITOR 
        self.LINE                   = 4
        ###########################################################
        # initialization 
        self.input, self.size       = header.counter( self.if_line + 1 )
        # get number of line if file is opened 
        self.gama                   = header.title(max_x=self.max_x, max_y=self.max_y, size=self.size, color="white", dataBase=self.Data, 
                                                        data=self.importation, lang=self.lang)
        # get cursor position after printing data 
        self.x, self.y              = screenConfig.cursor()
        ###########################################################
        # counter left and right 
        self.counterL, self.counterR        = 0, 0
        # scroll screen up and down 
        self.scrollUp, self.scrollDown      = 0, 0
        # keyword activated when enter is pressed 
        self.scrollEnter                    = False
        # keyword activated when data is inerting instead of adding 
        self.insert_is_used                 = False
        # counter of scollcreen down 
        self.scrollDown_counter             = 0
        ###########################################################
        # updating the last string cursor coordinates 
        self.Data['x_y'][self.gama]         = (self.x, self.y+self.gama)
        # initialization of line and max_line 
        self.if_line, self.if_line_max      = 0, 0
        # initialization of string 
        self.Data['string']                 = self.Data['string_tabular'][self.if_line]
        # intialization of index of string 
        self.Data['I_S']                    = self.Data['string_tab'][self.if_line]
        # input initiamizatiion 
        self.Data['input']                  = self.Data['liste'][self.if_line]
        # index initialization
        self.Data['index']                  = self.Data['tabular'][self.if_line]
        # get cursor coordinate of the currennt string 
        self.x, self.Y                      = self.Data['x_y'][self.if_line]
        # initialization of list of delecting of data 
        self.Data['get']                    = self.Data['memory'][self.if_line].copy()
        # string customized 
        self.str_                           = self.importation["writing"].copy()
        # unpadting str_
        self.y                              = self.LINE
        #
        self.action                         = "ADD"
        # locked screen 
        self.screenLocked                   = False
        # data copy       
        self.stringCopy                     = None
        self.inputCopy                      = None
        self.getCopy                        = None
        self.xCopy                          = {'x_i' : 0, "x_s" : 0, "pos" : 0}
        self.overwriting                    = False
        ###########################################################
        sys.stdout.write(self.move.TO(self.x, self.y))
        sys.stdout.flush()
        ###########################################################                    
         
        while True:
            # getting max size (max_x, max_y) of the window 
            self._max_x_, self._max_y_  = screenConfig.cursorMax()

            if (self._max_x_ != self.max_x) or (self._max_y_ != self.max_y):
                self._string_ = self.color_bg.red_L + self.color_fg.rbg(255, 255, 255) +"Screen Coordinates have changed" + self.init.reset
                sys.stdout.write(
                    self.clear.screen(pos=2)+ self.move.TO(x=0, y=0)+
                    self._string_ + "\n"
                )
                sys.stdout.flush()
                break
            else: pass 
            
            try:
                # get user input
                self.char = input.convert() 
              
                # break while loop <ctrl+c> = keyboardInterrupt 
                if self.char == 3           :
                    self._string_ = self.color_bg.red_L + self.color_fg.rbg(255, 255, 255) +"KeyboardInterrupt" + self.init.reset
                    sys.stdout.write(
                        self.clear.screen(pos=2)+ self.move.TO(x=0, y=0)+
                        self._string_ + "\n"
                    )
                    return
                
                # saving data <ctrl+s>
                elif self.char == 19        : 
                    if self.screenLocked is False : 
                        if self.writeData['FileName'] is None: 
                            self.writeData["data"] =  self.Data['string_tabular'].copy()
                            self.lang = save.saveData( self.writeData ).build(self.x, self.y, self.lang, self.str_)
                        else: writing.writeInput(self.Data['string_tabular'], self.writeData["FileName"])
                    else: pass
                
                # delecting char <backspace>
                elif self.char in {127, 8}  :
                    if self.screenLocked is False : 
                        if self.Data['get']:
                            self.Data['string']     =  self.Data['string'][ : self.Data["I_S"] - 1] + self.Data['string'][ self.Data["I_S"] : ]
                            self.Data['I_S']       -= 1
                            if type( self.Data['get'][self.Data['I_S']] ) == type(list()):
                                self.Data['input']  =  self.Data['input'][ : self.Data["index"] - 4] + self.Data['input'][ self.Data["index"] : ]
                                self.x                 -= 4
                                self.Data['index']     -= 4
                            else:
                                self.Data['input']      =  self.Data['input'][ : self.Data["index"] - 1] + self.Data['input'][ self.Data["index"] : ]
                                self.x                 -= 1
                                self.Data['index']     -= 1
                            
                            del self.Data['get'][self.Data['I_S']]
                            self.counterL           = 0
                            self.counterR          -= 1
                        else: pass
                    else: pass
                
                # moving cursor up, down, left, right   
                elif self.char == 27        :
                    while True  :
                        #next1, next2  = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)) 
                        next1 = input.convert() 
                        if next1 == 91:
                            next2 = ord(sys.stdin.read(1)) 
                            # move left 
                            if   next2 == 68:
                                if self.Data['I_S'] > 0:
                                    try:
                                        self.Data['I_S']        -= 1
                                        if type(self.Data['get'][self.Data['I_S']]) == type(list()):
                                            self.x              -= 4
                                            self.Data['index']  -= 4
                                        else:
                                            self.x              -= 1
                                            self.Data['index']  -= 1
                                    except IndexError : pass
                                else: pass 
                            # move right
                            elif next2 == 67:
                                if self.x <=  (self.size + len(self.Data['input'])):  
                                    try:
                                        if type(self.Data['get'][self.Data['I_S']]) == type(list()):
                                            self.x              += 4
                                            self.Data['index']  += 4
                                        else:
                                            self.x              += 1
                                            self.Data['index']  += 1
                                        self.Data['I_S']        += 1
                                    except IndexError: pass
                                else: pass 
                            # move up
                            elif next2 == 65:
                                if self.if_line > 0 and self.scrollDown == 0: 
                                    if self.y > self.LINE :   
                                        self.if_line           -= 1 
                                        self.y                 -= 1
                                        self.if_line_max       -= 1
                                        self.input, self.size   = header.counter( self.if_line + 1)
                                        self.Data['string']     = self.Data['string_tabular'][self.if_line]
                                        self.Data['I_S']        = self.Data['string_tab'][self.if_line]
                                        self.Data['input']      = self.Data['liste'][self.if_line]
                                        self.Data['index']      = self.Data['tabular'][self.if_line]
                                        self.x, self.Y          = self.Data['x_y'][self.if_line]
                                        self.Data['get']        = self.Data['memory'][self.if_line].copy()
                                        sys.stdout.write(
                                        self.move.TO(x=self.max_x, y=self.y) +  f"{self.acs['v']}" +
                                        self.move.TO(x=self.x, y=self.y) + self.c_bg  +
                                        self.move.TO(x=self.x, y=self.y) + self.init.reset 
                                        )
                                        sys.stdout.flush()
                                    else:
                                        if self.if_line == 0 : pass 
                                        else: 
                                            self.if_line_max       -= 1
                                            self.if_line           -= 1
                                            self.y                  = self.LINE
                                            self.input, self.size   = header.counter( self.if_line )
                                            self.Data['string']     = self.Data['string_tabular'][self.if_line]
                                            self.Data['I_S']        = self.Data['string_tab'][self.if_line]
                                            self.Data['input']      = self.Data['liste'][self.if_line]
                                            self.Data['index']      = self.Data['tabular'][self.if_line]
                                            self.x, self.Y          = self.Data['x_y'][self.if_line] 
                                            self.Data['get']        = self.Data['memory'][self.if_line].copy()
                                            formating.formating(LINE=self.LINE, data=self.str_, idd=self.if_line_max, max_y=self.max_y-self.max_down+1, max_x=self.max_x) 
                                            sys.stdout.write( self.move.TO(x=self.x, y=self.LINE) + self.init.reset )
                                            sys.stdout.flush()
                                            
                                else: 
                                    if self.scrollDown  > 0 : 
                                        if self.y > self.LINE       : self.y   -= 1 
                                        else: self.y = self.LINE
                                        
                                        self.scrollDown        -= 1
                                        self.if_line_max       -= 1
                                        self.if_line           -= 1
                                        self.input, self.size   = header.counter( self.if_line + 1)
                                        self.Data['string']     = self.Data['string_tabular'][self.if_line]
                                        self.Data['I_S']        = self.Data['string_tab'][self.if_line]
                                        self.Data['input']      = self.Data['liste'][self.if_line]
                                        self.Data['index']      = self.Data['tabular'][self.if_line]
                                        self.x, self.Y          = self.Data['x_y'][self.if_line]
                                        self.Data['get']        = self.Data['memory'][self.if_line].copy()
                                        
                                        if self.y > self.LINE :
                                            sys.stdout.write( self.move.TO(x=self.x, y=self.y) + self.init.reset )
                                            sys.stdout.flush()
                                        else:
                                            formating.formating(LINE=self.LINE, data=self.str_.copy(), max_x=self.max_x, idd=self.scrollDown, 
                                                                                    max_y=self.max_y-self.max_down)
                                            sys.stdout.write( self.move.TO(x=self.x, y=self.LINE) + self.init.reset)
                                            sys.stdout.flush()
                                    else: pass 
                            # move down 
                            elif next2 == 66: 
                                if self.y < self.max_y-(self.max_down+1):
                                    self.y                     += 1
                                    self.if_line               += 1 
                                    self.if_line_max           += 1
                                    self.input, self.size       = header.counter( self.if_line + 1)
                                    try:
                                        self.Data['string']     = self.Data['string_tabular'][self.if_line]
                                        self.Data['I_S']        = self.Data['string_tab'][self.if_line]
                                        self.Data['input']      = self.Data['liste'][self.if_line]
                                        self.Data['index']      = self.Data['tabular'][self.if_line]
                                        self.x, self.Y          = self.Data['x_y'][self.if_line]
                                        self.Data['get']        = self.Data['memory'][self.if_line].copy()
                                    except IndexError:
                                        self.Data['string']     = ""
                                        self.Data['input']      = ""
                                        self.Data['index']      = 0 
                                        self.Data["I_S"]        = 0
                                        self.Data['get']        = []
                                        self.x                  = self.size+1
                                        self.Data['string_tabular'].append(self.Data['string'])
                                        self.Data['string_tab'].append(self.Data['I_S'])
                                        self.Data['liste'].append( self.Data['input'] )
                                        self.Data['tabular'].append( self.Data['index'] )
                                        self.Data['x_y'].append((self.x, self.y))
                                        self.Data['memory'].append(self.Data['get'].copy())
                                        self.str_.append("")
                                    sys.stdout.write( 
                                    self.move.TO(x=self.max_x, y=self.y) +  f"{self.acs['v']}" +
                                    self.move.TO(x=self.x, y=self.y) + self.c_bg +
                                    self.move.TO(x=self.x, y=self.y) + self.init.reset 
                                    )
                                    sys.stdout.flush()
                                else: 
                                    if self.gama > (self.max_y-self.LINE):
                                        if self.scrollDown < self.gama - (self.max_y-self.LINE-self.max_down):
                                            self.scrollDown        += 1
                                            self.if_line_max       += 1
                                            self.if_line           += 1
                                            self.input, self.size   = header.counter( self.if_line + 1)
                                            self.Data['string']     = self.Data['string_tabular'][self.if_line]
                                            self.Data['I_S']        = self.Data['string_tab'][self.if_line]
                                            self.Data['input']      = self.Data['liste'][self.if_line]
                                            self.Data['index']      = self.Data['tabular'][self.if_line]
                                            self.x, self.Y          = self.Data['x_y'][self.if_line]
                                            self.y                  = self.max_y-(self.max_down+1)
                                            self.Data['get']        = self.Data['memory'][self.if_line].copy()
                                            formating.formating(LINE = self.LINE, data=self.str_.copy(), max_x=self.max_x, 
                                                                            idd=self.scrollDown,  max_y=self.max_y-self.max_down)
                                            sys.stdout.write( self.move.TO(x=self.x, y=self.y) + self.init.reset)
                                            sys.stdout.flush()
                                        else: pass
                                    else: pass
                            # <ctrl + up >  or <ctrl + down >
                            elif next2 == 49: 
                                next3, next4, next5 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                                if next5 in {67, 68}: pass
                                # <ctrl+up> is handled 
                                elif next5 == 65: pass 
                                # <ctrl+dow> is handled 
                                elif next5 == 66: pass  
                        elif next1 == 27:
                            next1, next2, next3, next4, next5 = input.outer()
                            if self.screenLocked is False :  self.screenLocked = True
                            else: self.screenLocked = False
                            self.overwriting = False
                        else: 
                            self.overwriting = False
                            if self.screenLocked is False :  self.screenLocked = True
                            else: self.screenLocked = False
                        
                        next1, next2, next3, next4, next5 = 0, 0, 0, 0, 0
                        break
                        
                # when <enter> is pressed  
                elif self.char in {13, 10}  :
                    if self.screenLocked is False : 
                        # moving cursor left 
                        sys.stdout.write(self.move.LEFT(pos=1000))
                        # erasing entire line 
                        sys.stdout.write(self.clear.line(2))
                        # writing string 
                        if self.lang != "unknown" : 
                            __string__, __color__ = words.words(self.Data['input'], self.color, self.lang ).final()
                        else: __string__ = self.Data['input']
                        
                        sys.stdout.write(
                            self.input + self.c_bg + " " * ( self.max_x - (self.size+2) ) + self.init.reset + 
                            self.move.TO(x=self.max_x, y=self.y) + self.c + f"{self.acs['v']}" +
                            self.move.TO(x=self.size+1, y=self.y) + self.c_bg+  __string__ + 
                            self.move.TO(x=self.size+1, y=self.y) + self.init.reset 
                            )
                        
                        #####################################################################################
                        # initializing all variables
                        self.if_line            += 1 
                        self.if_line_max        += 1
                        self.Data['string']      = ""
                        self.Data['input']       = ""
                        self.Data["I_S"]         = 0
                        self.Data["index"]       = 0
                        self.Data['get']         = []
                        self.input, self.size    = header.counter( self.if_line + 1 )
                        self.x                   = self.size + 1
                        ######################################################################################
                        if self.lang != "unknown" : 
                            # changing color or reset color  
                            if __color__["locked"] is False:  
                                self.locked = False
                                self.m      = 0
                            else: 
                                self.color  = __color__["color"]
                                self.locked = True
                                self.m      = __color__["rest"]
                        else: pass
                        
                        #####################################################################################
                        try : 
                            self.Data['string_tabular'][self.if_line]
                            self.Data['string_tabular'].insert(self.if_line, self.Data['string'])
                            self.Data['string_tab'].insert(self.if_line, self.Data['I_S'])
                            self.Data['liste'].insert(self.if_line, self.Data['input'] )
                            self.Data['tabular'].insert(self.if_line, self.Data['index'] )
                            self.Data['x_y'].insert(self.if_line, (self.x, self.y))
                            self.Data['memory'].insert(self.if_line, self.Data['get'])
                            self.str_.insert(self.if_line, self.Data['input'])
                            self.action = "INSERTS"
                        except IndexError:
                            self.Data['string_tabular'].append( self.Data['string'] )
                            self.Data['liste'].append( self.Data['input'] )
                            self.Data['string_tab'].append( self.Data['I_S'] )
                            self.Data['tabular'].append( self.Data['index'] )
                            self.Data['x_y'].append( (self.x, self.y) )
                            self.Data['memory'].append( self.Data['get'] )
                            self.str_.append(self.Data['input'])
                            self.action = "ADD"
                            
                        if self.y < self.max_y-(self.max_down+1): 
                            self.y    += 1
                            if self.action == "ADD" : 
                                sys.stdout.write( 
                                    self.move.TO(x=self.max_x, y=self.y) +  f"{self.acs['v']}" +
                                    self.move.TO(x=self.x, y=self.y) + self.c_bg +
                                    self.move.TO(x=self.x, y=self.y) + self.init.reset 
                                )
                                sys.stdout.flush()
                            else:
                                if len( self.Data['input'] ) >= (self.max_y-(self.LINE+self.max_down)): 
                                    self.scrollUp += 1
                                    formating.formating(LINE=self.LINE, data=self.str_[ : - self.scrollUp ], max_x=self.max_x, idd=self.scrollDown, 
                                                                                max_y=self.max_y-self.max_down)
                                    sys.stdout.write( self.move.TO(x=self.x, y=self.y) + self.init.reset)
                                    sys.stdout.flush()
                                else:
                                    formating.formating(LINE=self.LINE, data=self.str_, max_x=self.max_x, idd=self.scrollDown, 
                                                    max_y=self.max_y-self.max_down, MAX={'x' : self.x, "y" : self.y, "max" : self.if_line})
                                    sys.stdout.write( self.move.TO(x=self.x, y=self.y) + self.init.reset)
                                    sys.stdout.flush()
                        else: 
                            self.y           = self.max_y-(self.max_down+1)
                            self.scrollDown += 1
                            self.scrollUp    = 0
                            
                            formating.formating(LINE=self.LINE, data=self.str_, max_x=self.max_x, idd=self.scrollDown, 
                                                                                max_y=self.max_y-self.max_down)
                            sys.stdout.write( self.move.TO(x=self.x, y=self.y) + self.init.reset)
                            sys.stdout.flush()
                        
                        #####################################################################################
                    else: pass
                
                # indentation Tab
                elif self.char == 9         :
                    if self.screenLocked is False : 
                        if self.Data['index'] < self.max_x - (self.np + self.size+4):  
                            self.tt                  = ' ' * 4
                            self.Data['string']      =  self.Data['string'][ : self.Data["I_S"] ] + chr( self.char ) + self.Data['string'][ self.Data["I_S"] : ]
                            self.Data['input']       =  self.Data['input'][ : self.Data["index"] ] + str( self.tt ) + self.Data['input'][ self.Data["index"] : ]
                            self.Data['index']      += 4
                            self.Data['I_S']        += 1
                            self.x                  += 4
                            self.Data['get'].append([1 for x in range(4)])
                            self.counterR            = len( self.Data['input'] )
                        else: pass 
                    else: pass
                
                #ctrl + q
                elif self.char == 17        :
                    self.Data['I_S']    = 0
                    self.Data['index']  = 0
                    self.x              = self.size + 1
                    
                #ctrl + d 
                elif self.char == 4         : 
                    self.Data['I_S']    = len(self.Data['string'])
                    self.Data['index']  = len(self.Data['input'])
                    self.x              = self.Data['index'] + (self.size + 1)
                
                # maj + d 
                
                elif self.char == 68        :
                    self.Data['string']   = self.Data['string'][self.Data['I_S']]
                    self.Data['input']    = self.Data['input'][self.Data['index']]
                    self.x              = self.Data['index'] + (self.size + 1)
                
                # building scring 
                else: 
                    if self.screenLocked is False : 
                        if self.Data['index'] < self.max_x - (self.size+self.np+1):
                            self.Data['string']      =  self.Data['string'][ : self.Data["I_S"] ] + chr( self.char ) + self.Data['string'][ self.Data["I_S"] : ]
                            self.Data['input']       =  self.Data['input'][ : self.Data["index"] ] + chr( self.char ) + self.Data['input'][ self.Data["index"] : ]
                            self.Data['index']      += 1
                            self.Data['I_S']        += 1
                            self.counterR            = len( self.Data['input'] )
                            self.Data['get'].append(1)
                            self.x                  += 1
                        else : pass
                    else: 
                        if self.overwriting is False:
                            #delecting the line  copied 
                            if   chr(self.char) == "x" : 
                                self.stringCopy         = self.Data['string']
                                self.inputCopy          = self.Data['input'] 
                                self.getCopy            = self.Data['get'].copy() 
                                self.xCopy              = {'x_s' : self.Data['I_S'], "x_i" : self.Data['index'], "pos" : self.x}
                                self.Data['input']      = ""
                                self.Data['string']     = ""
                                self.Data['get']        = [0]
                                self.x                  = (self.size +1)
                            
                            # paste line copied 
                            elif chr(self.char) == "p" :
                                if self.stringCopy is not None : 
                                    self.Data['input']                          = self.inputCopy 
                                    self.Data['string']                         = self.stringCopy
                                    self.x                                      = self.xCopy['pos']
                                    self.Data['index']                          = self.xCopy['x_i']
                                    self.Data['string']                         = self.xCopy['x_s']
                                    self.Data['get']                            = self.getCopy.copy()
                                    
                                    self.Data['string_tabular'][self.if_line]   = self.stringCopy
                                    self.Data['liste'][self.if_line]            = self.inputCopy 
                                    self.Data['string_tab'][self.if_line]       = self.Data['I_S']
                                    self.Data['memory'][self.if_line]           = self.Data['get']
                                    self.Data['tabular'][self.if_line]          = self.Data['index']
                                    self.Data['x_y'][self.if_line]              = (self.x, self.y)
                                    
                                    self.stringCopy, self.inputCopy, self.getCopy     = None, None, None 
                                    self.xCopy                          = {'x_i' : 0, "x_s" : 0, "pos" : 0}
                                else: pass 
                            
                            # copy line of the current line
                            elif chr(self.char) == "c" : 
                                self.stringCopy     = self.Data['string'] 
                                self.inputCopy      = self.Data['input'] 
                                self.getCopy        = self.Data['get'].copy() 
                                self.xCopy          = {'x_s' : self.Data['I_S'], "x_i" : self.Data['index'], "pos" : self.x}
                            
                            # restoring the previous state
                            elif chr(self.char) == "u":
                                pass
                            
                            # delecting string 
                            elif chr(self.char) == "d":
                                if self.if_line < len(self.Data['string_tabular']):   
                                    try:           
                                        del self.Data['string_tabular'][self.if_line] 
                                        del self.Data['string_tab'][self.if_line]  
                                        del self.Data['liste'][self.if_line]          
                                        del self.Data['tabular'][self.if_line]     
                                        del self.Data['memory'][self.if_line]         
                                        del self.Data['x_y'][self.if_line] 
                                        del self.str_[self.if_line]    
                                        
                                        formating.scrollUP(self.str_, self.max_x, self.if_line_max, self.max_y, self.y)
                                        self.if_line        -= 1
                                        self.if_line_max    -= 1
                                    except IndexError: pass 
                                else: pass

                            elif chr(self.char) == "r":
                                self.overwriting = True
                        else:
                            if len(self.Data['string']) > self.Data['I_S']: 
                                sp1 = self.Data['string']
                                sp2 = self.Data['input']
                                
                                self.Data['input']  = ""
                                self.Data['input']  = ""
                                for ii, ss in enumerate( sp1 ):
                                    if ii == self.Data["I_S"]: ss = chr( self.char ) 
                                    else: pass 
                                    self.Data['string'] += ss 
                                
                                for ii, ss in enumerate( sp2 ):
                                    if ii == self.Data["index"]: ss = chr( self.char ) 
                                    else: pass 
                                    self.Data['input'] += ss
                                    
                                self.x                  += 1
                                self.Data['index']      += 1
                                self.Data['I_S']        += 1
                            else : pass

                # moving cursor left 
                sys.stdout.write(self.move.LEFT(pos=1000))
                # erasing entire line 
                sys.stdout.write(self.clear.line(2))
                # writing string 
                if self.lang != "unknown" : 
                    __string__, __color__ = words.words(self.Data['input'], self.color, language = self.lang ).final(locked=self.locked, m = self.m)
                else: __string__ = self.Data['input']
                
                sys.stdout.write(
                    self.input + self.c_bg + " " * ( self.max_x - (self.size+2) ) + self.init.reset + 
                    self.move.TO(x=self.max_x, y=self.y) +  f"{self.acs['v']}" +
                    self.move.TO(x=self.size+1, y=self.y) + self.c_bg+ __string__ + 
                    self.move.TO(x=self.size+1, y=self.y) + self.init.reset 
                    )

                # replace the cussor 
                if self.Data['I_S'] > 0: sys.stdout.write(self.move.TO(self.x, self.y) )
                else: pass 
                
                counter.count(number=self.if_line, x=self.x, y=self.y, max_x=self.max_x, 
                                            max_y=self.max_y-(self.max_down), lang=self.lang, action=self.screenLocked)
                
                sys.stdout.flush()
                
                self.Data['string_tabular'][self.if_line] = self.Data['string']
                self.Data['string_tab'][self.if_line]     = self.Data['I_S']
                self.Data['liste'][self.if_line]          = self.Data['input']   
                self.Data['tabular'][self.if_line]        = self.Data['index']
                self.Data['x_y'][self.if_line]            = (self.x, self.y) 
                self.Data['memory'][self.if_line]         = self.Data['get'].copy() 
                self.str_[self.if_line]                   = __string__ 
                
                
            except KeyboardInterrupt: 
                # breaking whyle loop 
                self._string_ = self.color_bg.red_L + self.color_fg.rbg(255, 255, 255) +"KeyboardInterrupt" + self.init.reset
                sys.stdout.write(
                    self.clear.screen(pos=2)+ self.move.TO(x=0, y=0)+
                    self._string_ + "\n" )
                break
            except IndentationError : pass