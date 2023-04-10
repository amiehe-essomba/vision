from getUserInput   import input
from configure      import colors, init, clear, state, screenConfig, moveCursor
from frame          import frame

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
        self.cursorPos          = moveCursor.cursor
        # set termios style (theme ), default value = monokai 
        self.termios            = termios
        
    def VISION(self):
        while True:
            try:
                # get user input
                self.char = input.convert()
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    if self.char is not None: pass 
                    else: pass 
                else: pass 
            except KeyboardInterrupt: pass 
            except IndexError : pass
            

if __name__ == '__main__':
    IDE().VISION()