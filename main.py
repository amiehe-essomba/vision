import sys, os 
from getUserInput   import input
from configure      import colors, init, clear, state, screenConfig, moveCursor
from frame          import frame
from DataBase       import data
from header         import header

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
        self.max_x, self.max_y  = screenConfig.get_win_ter()
        # getting the cursor coordiantes (x, y)
        self.x, self.y          = screenConfig.cursor()
        # loading the keywords for moving cursor on a particular region of the screen 
        self.move               = moveCursor.cursor
        # set termios style (theme ), default value = monokai 
        self.termios            = termios
        
    def VISION(self):
        self.Data                   = data.base()
        self.indexation             = data.indexation()
        # accounting line
        self.if_line                = 0
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
        
        ###########################################################
        self.input, self.size = header.counter( self.if_line )
        header.title(max_x=self.max_x, max_y=self.max_y, size=self.size, color="white")
        ###########################################################
        
        while True:
            # getting max size (max_x, max_y) of the window 
            self._max_x_, self._max_y_  = screenConfig.get_win_ter()
            
            try:
                # get user input
                self.char = input.convert()
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    if self.char is not None: pass 
                    else: pass 
                else: pass 
            except KeyboardInterrupt: 
                # breaking whyle loop 
                self._string_ = self.color_bg.red_L + self.color_fg.rbg(255, 255, 255) +"KeyboardInterrupt" + self.init.reset
                sys.stdout.write(
                    self.clear.screen(pos=2)+ self.move.TO(x=0, y=0)+
                    self._string_ + "\n"
                )
                break
            except IndexError : pass
            

if __name__ == '__main__':
    IDE().VISION()