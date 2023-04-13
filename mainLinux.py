import sys, os 
from getUserInput   import input
from configure      import colors, init, clear, state, screenConfig, moveCursor, scroll
from frame          import frame
from DataBase       import data
from header         import header
from saving         import save, writing
from keywords       import words

class IDE:
    def __init__(self, termios : str = "monokai"):
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
        
    def VISION(self):
        self.Data                   = data.base()
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
        self.np                     = 0
        # writing data in a file
        self.writeData              = {"data" : [], "FileName" : None, "action" : False}
        # bg color 
        self.c_bg                   = self.init.bold + self.color_bg.rgb(10, 10, 10)
        # fg color 
        self.c                      = self.init.bold + self.color_fg.rbg(255, 255, 255)
        ###########################################################
        self.input, self.size       = header.counter( self.if_line + 1 )
        header.title(max_x=self.max_x, max_y=self.max_y, size=self.size, color="white")
        self.x, self.y              = screenConfig.cursor()
        ###########################################################
        self.counterL, self.counterR        = 0, 0
        self.scrollUp, self.scrollDown      = 0, 0
        self.scrollEnter                    = False
        ###########################################################
        self.Data['x_y'].append((self.x, self.y))
        ###########################################################                    
        
        while True:
            # getting max size (max_x, max_y) of the window 
            self._max_x_, self._max_y_  = screenConfig.cursorMax()
            
            try:
                # get user input
                self.char = input.convert() 
                # break while loop <ctrl+c> = keyboardInterrupt 
                if self.char == 3:
                    self._string_ = self.color_bg.red_L + self.color_fg.rbg(255, 255, 255) +"KeyboardInterrupt" + self.init.reset
                    sys.stdout.write(
                        self.clear.screen(pos=2)+ self.move.TO(x=0, y=0)+
                        self._string_ + "\n"
                    )
                    return
                
                # saving data <ctrl+s>
                elif self.char == 19: 
                    if self.writeData['FileName'] is None: save.saveData(self.writeData).build(self.x, self.y)
                    else: writing.writeInput(self.writeData['data'], self.writeData['FileName'])
                
                # delecting char <backspace>
                elif self.char in {127, 8}:
                    if self.Data["I_S"] > 0:
                        self.Data['string']     =  self.Data['string'][ : self.Data["I_S"] - 1] + self.Data['string'][ self.Data["I_S"] : ]
                        self.Data['I_S']       -= 1
                        if type( self.Data['get'][self.Data['I_S']] ) == type(list()):
                            for i in range(4):
                                self.Data['input']  =  self.Data['input'][ : self.Data["index"] - 1] + self.Data['input'][ self.Data["index"] : ]
                                self.x                 -= 1
                                self.Data['index']     -= 1
                        else:
                            self.Data['input']      =  self.Data['input'][ : self.Data["index"] - 1] + self.Data['input'][ self.Data["index"] : ]
                            self.x                 -= 1
                            self.Data['index']     -= 1
                        
                        del self.Data['get'][self.Data['I_S']]
                        self.counterL           = 0
                        self.counterR          -= 1
                    else: pass
                
                # moving cursor up, down, left, right   
                elif self.char == 27:
                    next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
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
                        if self.x <=  (self.size + len(self.Data['input'])): #( self.size + self.Data["I_S"] - 1) : 
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
                        if self.if_line > 0:
                            self.if_line           -= 1 
                            self.y                 -= 1
                            self.if_line_max       -= 1
                            self.input, self.size   = header.counter( self.if_line + 1)
                            self.Data['string']     = self.Data['string_tabular'][self.if_line]
                            self.Data['I_S']        = self.Data['string_tab'][self.if_line]
                            self.Data['input']      = self.Data['liste'][self.if_line]
                            self.Data['index']      = self.Data['tabular'][self.if_line]
                            self.x, self.y          = self.Data['x_y'][self.if_line]

                            sys.stdout.write(
                            self.move.TO(x=self.max_x, y=self.y) +  f"{self.acs['v']}" +
                            self.move.TO(x=self.x, y=self.y) + self.c_bg+self.Data['string'] + 
                            self.move.TO(x=self.x, y=self.y) + self.init.reset 
                            )
                            sys.stdout.flush()
                        else: pass  
                    # move down 
                    elif next2 == 66: 
                        if self.y < self.max_y-3:
                            self.y                     += 1
                            self.if_line               += 1 
                            self.if_line_max           += 1
                            self.input, self.size       = header.counter( self.if_line + 1)
                            try:
                                self.Data['string']     = self.Data['string_tabular'][self.if_line]
                                self.Data['I_S']        = self.Data['string_tab'][self.if_line]
                                self.Data['input']      = self.Data['liste'][self.if_line]
                                self.Data['index']      = self.Data['tabular'][self.if_line]
                                self.x, self.y          = self.Data['x_y'][self.if_line]
                            except IndexError:
                                ####################################################
                                self.Data['string_tabular'][self.if_line-1] = self.Data['string']
                                self.Data['string_tab'][self.if_line-1]     = self.Data['I_S']
                                self.Data['liste'][self.if_line-1]          = self.Data['input']   
                                self.Data['tabular'][self.if_line-1]        = self.Data['index']
                                self.Data['x_y'][self.if_line-1]            = (self.x, self.y-1)        
                                #####################################################
                                self.Data['string']     = ""
                                self.Data['input']      = ""
                                self.Data['index']      = 0 
                                self.Data["I_S"]        = 0
                                self.x                  = self.size+1
                                self.Data['string_tabular'].append(self.Data['string'])
                                self.Data['string_tab'].append(self.Data['I_S'])
                                self.Data['liste'].append( self.Data['input'] )
                                self.Data['tabular'].append( self.Data['index'] )
                                self.Data['x_y'].append((self.x, self.y))
                                
                            sys.stdout.write( 
                            self.move.TO(x=self.max_x, y=self.y) +  f"{self.acs['v']}" +
                            self.move.TO(x=self.x, y=self.y) + self.c_bg+self.Data['string'] + 
                            self.move.TO(x=self.x, y=self.y) + self.init.reset 
                            )
                            sys.stdout.flush()
                        else: pass
                    # <ctrl + up >  or <ctrl + down >
                    elif next2 == 49: 
                        next3, next4, next5 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                        if next5 in {67, 68}: pass
                        # <ctrl+up> is handled 
                        elif next5 == 65: pass 
                        # <ctrl+dow> is handled 
                        elif next5 == 66: pass  
                        
                # when <enter> is pressed  
                elif self.char in {13, 10}:
                    # moving cursor left 
                    sys.stdout.write(self.move.LEFT(pos=1000))
                    # erasing entire line 
                    sys.stdout.write(self.clear.line(2))
                    # writing string 
                    sys.stdout.write(
                        self.input + self.c_bg + " " * ( self.max_x - (self.size+2) ) + self.init.reset + 
                        self.move.TO(x=self.max_x, y=self.y) + self.c + f"{self.acs['v']}" +
                        self.move.TO(x=self.size+1, y=self.y) + self.c_bg+self.Data['string'] + 
                        self.move.TO(x=self.size+1, y=self.y) + self.init.reset 
                        )
                    #####################################################################################
                    # storing string
                    self.Data['string_tabular'].append( self.Data['string'] )
                    # storing input
                    self.Data['liste'].append( self.Data['input'] )
                    # saving index
                    self.Data['string_tab'].append( self.Data['I_S'] )
                    # storing index
                    self.Data['tabular'].append( self.Data['index'] )
                    # saving cursor coordinates(x,y)
                    self.Data['x_y'].append( (self.x, self.y) )
                    #####################################################################################
                    # initializing all variables
                    self.if_line        += 1 
                    self.if_line_max    += 1
                    self.Data['string'] = ""
                    self.Data['input']  = ""
                    self.Data["I_S"]    = 0
                    self.Data["index"]  = 0
                    self.input, self.size = header.counter( self.if_line + 1 )
                    ######################################################################################
                    
                    if self.y < (self.max_y-3 ):
                        self.y += 1
                        self.x = self.size + 1
                        sys.stdout.write(self.move.TO(x=self.x, y=self.y))
                    else: 
                        self.scrollUp   += 1
                        self.x           = self.size + 1
                        self.scrollEnter = True
                        sys.stdout.write( self.scroll.UP(1) )
                        sys.stdout.flush()
                # indentation Tab
                elif self.char == 9:
                    self.tt                  = ' ' * 4
                    self.Data['string']      =  self.Data['string'][ : self.Data["I_S"] ] + chr( self.char ) + self.Data['string'][ self.Data["I_S"] : ]
                    self.Data['input']       =  self.Data['input'][ : self.Data["index"] ] + str( self.tt ) + self.Data['input'][ self.Data["index"] : ]
                    self.Data['index']      += 4
                    self.Data['I_S']        += 1
                    self.x                  += 4
                    self.Data['get'].append([1 for x in range(4)])
               
                # building scring 
                else: 
                    self.Data['string']      =  self.Data['string'][ : self.Data["I_S"] ] + chr( self.char ) + self.Data['string'][ self.Data["I_S"] : ]
                    self.Data['input']       =  self.Data['input'][ : self.Data["index"] ] + chr( self.char ) + self.Data['input'][ self.Data["index"] : ]
                    self.Data['index']      += 1
                    self.Data['I_S']        += 1
                    self.x                  += 1
                    self.Data['get'].append(1)
                # moving cursor left 
                sys.stdout.write(self.move.LEFT(pos=1000))
                # erasing entire line 
                sys.stdout.write(self.clear.line(2))
                # writing string 
                sys.stdout.write(
                    self.input + self.c_bg + " " * ( self.max_x - (self.size+2) ) + self.init.reset + 
                    self.move.TO(x=self.max_x, y=self.y) +  f"{self.acs['v']}" +
                    self.move.TO(x=self.size+1, y=self.y) + self.c_bg+
                    words.words(self.Data['input'], self.c, "python" ).final() + 
                    self.move.TO(x=self.size+1, y=self.y) + self.init.reset 
                    )

                # replace the cussor 
                if self.Data['I_S'] > 0: sys.stdout.write(self.move.RIGHT(pos=(self.x)) )
                else: pass 
                
                sys.stdout.write( self.move.TO(y=self.max_y-2, x=self.size) )
                
                if self.scrollUp == 0:
                    header.line(x=self.x, y=self.y, max_x=self.max_x, max_y=self.max_y-2)
                else:
                    header.line(x=self.x, y=self.y , max_x=self.max_x, max_y=self.max_y-2,scrollUp=self.scrollUp)
                    if self.scrollEnter is True:
                        sys.stdout.write(self.move.DOWN(2)+self.move.LEFT(1000))
                        header.bottom(self.max_x)
                        sys.stdout.write(self.move.TO(x=self.x, y=self.y))
                        self.scrollEnter = False
                    else: self.scrollEnter = False
                sys.stdout.flush()
                
            except KeyboardInterrupt: 
                # breaking whyle loop 
                self._string_ = self.color_bg.red_L + self.color_fg.rbg(255, 255, 255) +"KeyboardInterrupt" + self.init.reset
                sys.stdout.write(
                    self.clear.screen(pos=2)+ self.move.TO(x=0, y=0)+
                    self._string_ + "\n" )
                break
            except NameError : pass
            

if __name__ == '__main__':
    sys.stdout.write(clear.clear.screen(2))
    IDE().VISION()