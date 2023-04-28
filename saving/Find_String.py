from configure      import colors, init, clear, state, screenConfig, moveCursor, scroll
from frame          import frame
from getUserInput   import input
from fileType       import fileType as FT
from header         import header 
import sys, platform

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

class FindData:
    def __init__(self):
        # getting max size (max_x, max_y) of the window 
        self.max_x, self.max_y  = screenConfig.cursorMax()
        self._max_x_            = self.max_x 
        self.max_x            //= 2 
        # loading the keywords for moving cursor on a particular region of the screen 
        self.move               = moveCursor.cursor
        # loading keywords for cleaning screen and lines 
        self.clear              = clear.clear
        # border configuration 
        self.acs                = frame.frame(custom=True)
        # loading initialization cursor parameters 
        self.init               = init.init
        # Scroll display down and up
        self.scr                = scroll.scrolled
        # system
        self.system             = platform.system()
         
    def find(self, x :int = 0, y:int = 0, LINE : int = 4, lang : str = "unknown", COLOR : dict = {}):
        
        self.c              = COLOR['white'] 
        self.blink          = self.init.bold + colors.fg.rbg(255, 0, 255)
        self.c_bg           = COLOR['bgColor']  
        self.input          = f"{self.acs['v']} {self.blink}STRING : " + self.init.reset
        self.length         = len("| string : ")
        self.cc             = init.init.bold + colors.fg.rbg(0, 255, 255)
        self.language_type  = "unknown"
        self.color          = COLOR['fgColor'] 
        _input_, _length_   = header.counter(n=0)
        
        
        sys.stdout.write(
            self.move.TO(x=0, y=self.max_y-3) +
            self.clear.screen(0) + 
            self.move.LEFT(pos=1000))
        
        sys.stdout.write(self.c + f"{self.acs['ul']}" + f"{self.acs['h']}" * (self.max_x-2) + f"{self.acs['ur']}" + self.init.reset + "\n")
        
        # getting the cursor coordiantes (x, y)
        self._x_, self._y_ = screenConfig.cursor()
        
        sys.stdout.write(self.move.LEFT(pos=1000))
        sys.stdout.write(
            self.input + self.c_bg + " " * ( self.max_x- (self.length+2) ) + self.init.reset+
            self.move.TO(x=self.max_x, y=self._y_) + self.c + f"{self.acs['v']}" +
            self.move.TO(x=self.length+1, y=self._y_) + self.init.reset  +"\n"
            )
        sys.stdout.write(self.move.LEFT(pos=1000))
        bottom(max_x=self.max_x)
        sys.stdout.write(self.move.TO(x=self.length+1, y=self._y_-2))
        sys.stdout.flush()
        
        # string initialization
        self.string, self.newStr        = "", ""
        # index initialization
        self.i                          = 0
        # when length of screen if higher than self.max_x// 2
        self.counterL, self.counterR    = 0, 0
        # getting the cursor coordiantes (x, y)
        self._x_, self._y_              = screenConfig.cursor()
        self.Y                          = self._y_
        sys.stdout.write(self.move.TO(x=self.length+1, y=self._y_+2))
        sys.stdout.flush()
        
        self._X_, self._y_              = screenConfig.cursor()
        
        while True:
            try:
                self.char = input.convert() 
                if self.char:
                    if self.system in {"Linux", "MacOS"} : pass 
                    elif self.system == "Windows" :
                        _           = self.char[1]
                        self.char   = self.char[0]
                    else: self.char = None
                    if self.char:
                        # <enter> is pressed 
                        if self.char in {10, 13}:
                            self.max_x  = self._max_x_
                            for i in range(2):
                                sys.stdout.write(self.move.LEFT(pos=1000))
                                sys.stdout.write(
                                    _input_ + self.c_bg + " " * (self.max_x - (_length_+2) ) + self.init.reset + 
                                    self.move.TO(x=self.max_x, y=self.Y) + self.c + f"{self.acs['v']}" +
                                    self.move.TO(x=x, y=self.Y) + self.init.reset + "\n"
                                    )
                                self.Y += 1
                            sys.stdout.write(
                                self.move.DOWN(1)+
                                self.move.LEFT(pos=1000)
                                )
                            header.bottom(max_x=self.max_x)
                            sys.stdout.write(self.move.TO(x=x, y=y))
                            
                            break
                        # <ctrl+c> is pressed 
                        elif self.char == 3:
                            self.max_x  = self._max_x_
                            for i in range(2):
                                sys.stdout.write(self.move.LEFT(pos=1000))
                                sys.stdout.write(
                                    _input_ + self.c_bg + " " * (self.max_x - (_length_+2) ) + self.init.reset + 
                                    self.move.TO(x=self.max_x, y=self.Y) + self.c + f"{self.acs['v']}" +
                                    self.move.TO(x=x, y=self.Y) + self.init.reset + "\n"
                                    )
                                self.Y += 1
                            sys.stdout.write(
                                self.move.DOWN(1)+
                                self.move.LEFT(pos=1000)
                                )
                            header.bottom(max_x=self.max_x)
                            sys.stdout.write(self.move.TO(x=x, y=y))
                            break
                        # moving cursor up, down, left, reight
                        elif self.char == 27:
                            if self.system in {"Linux", "MacOs"}: 
                                next1 = input.convert()
                                if   next1 == 91:  next2 = ord(sys.stdin.read(1)) 
                                else: next2 = None
                            elif self.system == "Windows"       :
                                if type(_) is type(list()): next2 = _[0]
                                else: next2 = _
                            else: next2 = None 
                            
                            # move left 
                            if   next2 == 68:
                                if self._x_>= self.length: self._x_ -= 1
                                else: pass 
                                
                                # scroll horizontally string  
                                if self._x_ == self.length -1: 
                                    if self.counterL > 0: 
                                        self.counterL -= 1
                                        self.counterR -= 1
                                    else: pass
                                else: pass
                            #move right
                            elif next2 == 67:
                                if self.counterL == 0:
                                    if self._x_ < ( self.length + self.i-1) : self._x_ += 1
                                    else: pass 
                                else:    
                                    if self._x_< self.max_x - 3:  self._x_ += 1
                                    else: pass 
                                
                                if self._x_ == (self.max_x-2):
                                    # scroll horizontally string  
                                    if self.counterR < len(self.string) : 
                                        self.counterL += 1
                                        self.counterR += 1
                                    else: pass
                                else: pass 
                                
                            else: pass
                        # delecting char <backspace>
                        elif self.char in {8, 127}:
                            if self.i > 0: 
                                self.string = self.string[ : self.i -1] + self.string[self.i : ]
                                self.i          -= 1
                                self._x_        -= 1
                                self.counterL    = 0
                                self.counterR   -= 1
                            else: pass
                        #tabular and space
                        elif self.char in {32, 9} : pass 
                        # another key is pressed 
                        else: 
                            if  self.i < self.max_x - (2 + self.length+1):
                                self.string              = self.string[ : self.i] + chr(self.char) + self.string[self.i : ]
                                self.i                  += 1 
                                self.counterR            = len(self.string)
                                self.counterL            = 0
                                self._x_, self._y_       = screenConfig.cursor()
                            else: 
                                self.string              = self.string[ : self.i] + chr(self.char) + self.string[self.i : ]
                                self.i                  += 1 
                                self.counterL           += 1
                                self.counterR            = len(self.string)
                                
                        sys.stdout.write(self.move.LEFT(pos=1000))
                        sys.stdout.write(self.clear.line(2))
                        sys.stdout.write(
                            self.input + self.c_bg + " " * ( self.max_x - (self.length+2) ) + self.init.reset + 
                            self.move.TO(x=self.max_x, y=self._y_) + self.c + f"{self.acs['v']}" +
                            self.move.TO(x=self.length+1, y=self._y_) + self.c_bg + self.color + self.string[self.counterL : self.counterR]  + self.init.reset +"\n"
                            )
                        sys.stdout.write(self.clear.screen(0))
                        sys.stdout.write(self.move.LEFT(pos=1000))
                        bottom(max_x=self.max_x)
                        sys.stdout.write(self.move.TO(x=self.length+1, y=self._y_))
                        
                        if self.i > 0:  sys.stdout.write(self.move.RIGHT(pos=(self._x_-self.length)) )
                        else: pass 
                        
                        sys.stdout.flush()
                    else: pass 
                else: pass
            except KeyboardInterrupt : 
                self.max_x  = self._max_x_
                for i in range(2):
                    sys.stdout.write(self.move.LEFT(pos=1000))
                    sys.stdout.write(
                        _input_ + self.c_bg + " " * (self.max_x - (_length_+2) ) + self.init.reset + 
                        self.move.TO(x=self.max_x, y=self.Y) + self.c + f"{self.acs['v']}" +
                        self.move.TO(x=x, y=self.Y) + self.init.reset + "\n"
                        )
                    self.Y += 1
                sys.stdout.write(
                    self.move.DOWN(1)+
                    self.move.LEFT(pos=1000)
                    )
                header.bottom(max_x=self.max_x)
                sys.stdout.write(self.move.TO(x=x, y=y))
                break
            
        return self.string