import sys, os 
from getUserInput   import input
from configure      import colors, init, clear, state, screenConfig, moveCursor, scroll
from frame          import frame
from DataBase       import data
from header         import header, formating, counter
from saving         import save, writing, Find_String
from keywords       import words
import time
from AUTO           import buildString as BS
from keywords       import keywords as KW
from AUTO           import KEYS

class IDE:
    def __init__(self, termios : str = "none", lang : str = "unknown", COLOR : dict = {}):
        
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
        # color parameter 
        self.COLOR              = COLOR.copy()
        
    def VISION(self, importation : dict = {}, writeData : dict = {}, path : str = ""):
        """_summary_

        Args:
            importation (dict, optional): _description_. Defaults to {}.
            writeData (dict, optional): _description_. Defaults to {}.
            path (str, optional): _description_. Defaults to "".
        """
        # loading external data 
        self.importation                    = importation
        
        # initialization of data 
        self.Data                           = data.base()
        # 
        self.indexation                     = data.indexation()
        # accounting line
        self.if_line                        = 0
        # max lines
        self.if_line_max                    = 0
        # move curor up fist time 
        self.key_up_first_time              = True
        # storing key_up_first_time
        self.key_up_id                      = False 
        # action to do after one of these commands is pressed 
        # it means UP, DOWN or ENTER is pressed
        self.action                         = None
        # fixing the x-axis border 
        self.border_x_limit                 = True 
        # last line 
        self.last_line                      = {"last": self.max_y-2, "now" : 0}
        # counter 
        self.np                             = 2
        # writing data in a file
        self.writeData                      = writeData
        # bg color 
        self.c_bg                           = self.COLOR["bgColor"] 
        # fg color 
        self.c                              = self.COLOR["fgColor"] 
        # building color 
        self.color                          = self.COLOR["fgColor"] 
        # locked the writings 
        self.locked                         = False 
        # 
        self.m                              = 0
        self.max_down                       = 2
        self.LINE                           = 4
        ###########################################################
         # initialization 
        self.input, self.size               = header.counter( self.if_line + 1 )
        # get number of line if file is opened 
        self.gama                           = header.title(max_x=self.max_x, max_y=self.max_y, size=self.size, color="white", dataBase=self.Data, 
                                                        data=self.importation, lang=self.lang, COLOR=self.COLOR.copy())
        # get cursor position after printing data 
        self.x, self.y                      = screenConfig.cursor()
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
        ###########################################################
        # data copy       
        self.stringCopy                     = None
        self.inputCopy                      = None
        self.getCopy                        = None
        self.xCopy                          = {'x_i' : 0, "x_s" : 0, "pos" : 0}
        self.overwriting                    = False
        self.differentStates                = {
            "index" : 0,
            "data"  : {}
        }
        self.histotyOfColors                = self.importation["color"].copy()
        ##########################################################
        self.no_cmt                         = self.COLOR["fgColor"] 
        self.cmt                            = self.COLOR["cmtColor"] 
        self.conservingColor                = self.COLOR["fgColor"]
        self.color                          = self.COLOR["fgColor"]
        ###########################################################
        self.idd_select                     = 0
        self.index_select                   = 0
        self.str_select                     = False
        self.QUOTE                          = ""
        ###########################################################
        self.find_string                    = ""
        self.string_find_is_found           = False
        ###########################################################
        sys.stdout.write(self.move.TO(self.x, self.y))
        sys.stdout.flush()
        ########################################################### 
        
        while True:
            # getting max size (max_x, max_y) of the window at each time
            self._max_x_, self._max_y_  = screenConfig.cursorMax()
            if (self._max_x_ != self.max_x) or (self._max_y_ != self.max_y):
                self._string_ = self.color_bg.red_L + self.color_fg.rbg(255, 255, 255) +"Screen Coordinates have changed" + self.init.reset
                sys.stdout.write(
                    self.clear.screen(pos=2)+ self.move.TO(x=0, y=0)+
                    self._string_ + "\n"
                )
                sys.stdout.flush()
                return
            else: pass 
            
            try:
                # get user input
                self.char = input.convert()
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    if self.char is not None: 
                        
                        # <ctrl+a>
                        if   self.char == 1         :
                            # checking firstly is the screen is locked
                            if self.screenLocked is False : 
                                # delecting characters on the left side of the cursor
                                if self.Data['input']:
                                    self.Data['input']  = self.Data['input'][self.Data['index'] : ]
                                    self.Data['string'] = self.Data['string'][self.Data['I_S'] : ]
                                    self.x              = (self.size + 1)
                                    self.get            = []
                                    if self.Data['string']:
                                        for ss in self.Data['string']:
                                            if ss == '\t': self.get.append([1 for x in range(4)])
                                            else: self.get.append(1)
                                    else: pass
                                    sys.stdout.write(self.move.TO(x=self.x, y=self.y))
                                    sys.stdout.flush()
                                else: pass
                            else: pass
                    
                        # breaking whyle loop 
                        elif self.char == 3         :
                            self._string_ = self.color_bg.red_L + self.color_fg.rbg(255, 255, 255) +"KeyboardInterrupt" + self.init.reset
                            sys.stdout.write(
                                self.clear.screen(pos=2)+ self.move.TO(x=0, y=0)+
                                self._string_ + "\n"
                            )
                            return

                        # <ctrl+z>
                        elif self.char == 26        :
                            # checking firstly is the screen is locked
                            if self.screenLocked is False : 
                                # delecting characters from the cursor at the end of the line
                                if self.Data['input']:
                                    self.Data['input']  = self.Data['input'][ : self.Data['index']]
                                    self.Data['string'] = self.Data['string'][ : self.Data['I_S']]
                                    self.x              = len(self.Data["input"]) + (self.size + 1)
                                    self.get            = []
                                    if self.Data['string']:
                                        for ss in self.Data['string']:
                                            if ss == '\t': self.get.append([1 for x in range(4)])
                                            else: self.get.append(1)
                                    else: pass
                                    sys.stdout.write(self.move.TO(x=self.x, y=self.y))
                                    sys.stdout.flush()
                                else: pass
                            else: pass
                        
                        # saving data <ctrl+s>
                        elif self.char == 19        : 
                            if self.screenLocked is False : 
                                if self.writeData['FileName'] is None: 
                                    self.histotyOfColors   = {"m" : [], "n" : [], "color" : [], "locked" : []}
                                    self.writeData["data"] =  self.Data['string_tabular'].copy()
                                    self.lang = save.saveData( self.writeData ).build(self.x, self.y, self.lang, self.str_, 
                                                                    history = self.histotyOfColors, COLOR=self.COLOR.copy())
                                else: writing.writeInput(self.Data['string_tabular'], self.writeData["FileName"])
                                self.differentStates['data'] = {
                                    self.differentStates['index'] : {
                                        'string_tabular'        : self.Data['string_tabular'].copy(),
                                        'string_tab'            : self.Data['string_tab'].copy(),
                                        "liste"                 : self.Data['liste'].copy() , 
                                        'tabular'               : self.Data['tabular'].copy(),
                                        "x_y"                   : self.Data['x_y'].copy(),
                                        'memory'                : self.Data['memory'].copy(),
                                        "str"                   : self.str_.copy(),
                                        "now_x_y"               : [self.x, self.y].copy(),
                                        "string"                : self.Data['string'],
                                        "input"                 : self.Data['input'],
                                        "I_S"                   : self.Data['I_S'],
                                        "index"                 : self.Data['index'],
                                        "if_line"               :  self.if_line
                                        }
                                }
                                self.differentStates['index'] += 1
                            else: pass
                            
                        # adding a new line on top <ctrl+o>
                        elif self.char == 15        : 
                            # checking first is the screen is not locked 
                            if self.screenLocked is False :
                                self.Data['string']      = ""
                                self.Data['input']       = ""
                                self.Data["I_S"]         = 0
                                self.Data["index"]       = 0
                                self.Data['get']         = []
                                self.x                   = self.size + 1
                                
                                self.Data['string_tabular'].insert(self.if_line, self.Data['string'])
                                self.Data['string_tab'].insert(self.if_line, self.Data['I_S'])
                                self.Data['liste'].insert(self.if_line, self.Data['input'] )
                                self.Data['tabular'].insert(self.if_line, self.Data['index'] )
                                self.Data['x_y'].insert(self.if_line, (self.x, self.y))
                                self.Data['memory'].insert(self.if_line, self.Data['get'])
                                self.str_.insert(self.if_line, self.Data['input'])
                                
                                self.histotyOfColors['color'].insert(self.if_line, self.color)
                                self.histotyOfColors['m'].insert(self.if_line, 0)
                                self.histotyOfColors['n'].insert(self.if_line, 0)
                                self.histotyOfColors['locked'].insert(self.if_line, self.locked)
                                
                                formating.scrollUP(self.str_, self.max_x, self.if_line_max, self.max_y, self.y, COLOR=self.COLOR.copy())
                                
                                self.if_line_max        += 1
                                self.if_line            += 1
                            else: pass
                        
                        # selecting <ctrl+n>
                        elif self.char == 14        :
                            # checking first is the screen is not locked 
                            if self.screenLocked is False : 
                                # selecting a keyword from the proposed list 
                                self.str_select = True
                            else: pass
                    
                        # clear screen  <ctrl+l>
                        elif self.char == 12        :
                            self.Data['string']             = ""
                            self.Data['input']              = ""
                            self.Data["I_S"]                = 0
                            self.Data["index"]              = 0
                            self.Data['get']                = []
                            self.x                          = self.size + 1
                            self.y                          = self.LINE
                            ####################################################
                            self.Data['string_tabular']     = [""]
                            self.Data['string_tab']         = [0]
                            self.Data['liste']              = [""]    
                            self.Data['tabular']            = [0]
                            self.Data['x_y']                = [(self.x, self.y)]
                            self.Data['memory']             = [[]]
                            self.str_                       = ['']
                            self.if_line_max                = 0
                            self.if_line                    = 0
                            ####################################################
                            self.histotyOfColors['color']   = [self.color]
                            self.histotyOfColors['m']       = [0]
                            self.histotyOfColors['n']       = [0]
                            self.histotyOfColors['locked']  = [False]
                            ####################################################
                            self.Data['drop_idd'],self.Data['str_drop_down'] = 0, ""
                            ####################################################
                            
                            formating.scrollUP(self.str_, self.max_x, self.if_line_max, self.max_y, self.y, COLOR=self.COLOR.copy())
                    
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
                        
                        #<ctrl+x>
                        elif self.char == 24        :
                            # checking first is the screen is not locked 
                            if self.screenLocked is False : 
                                # clear lines from the cursor at the end of the screen
                                if self.if_line == len(self.Data['string_tabular']) : pass
                                else:
                                    for ii in range(self.if_line+1, len(self.Data['string_tabular'])):
                                        self.Data['string_tabular'][ii] = ""
                                        self.Data['string_tab'][ii]     = 0
                                        self.Data['liste'][ii]          = ""  
                                        self.Data['tabular'][ii]        = 0
                                        self.Data['x_y'][ii]            = (self.size+1, self.y) 
                                        self.Data['memory'][ii]         = []
                                        self.str_[ii]                   = ""  
                                    formating.WritingDown(x=self.x, y=self.y, max_x=self.max_x, max_y=self.max_y, COLOR=self.COLOR.copy()) 
                            else: pass 

                        #<ctrl+u>
                        elif self.char == 21        :
                            # checking first is the screen is not locked 
                            if self.screenLocked is False : 
                                # clear lines from the cursor at the beginning of screen
                                if self.if_line == len(self.Data['string_tabular']) : pass
                                else:
                                    for ii in range(0, self.if_line):
                                        self.Data['string_tabular'][ii] = ""
                                        self.Data['string_tab'][ii]     = 0
                                        self.Data['liste'][ii]          = ""  
                                        self.Data['tabular'][ii]        = 0
                                        self.Data['x_y'][ii]            = (self.size+1, self.y) 
                                        self.Data['memory'][ii]         = []
                                        self.str_[ii]                   = ""  
                                    formating.WritingUp(x=self.x, y=self.y, max_x=self.max_x, max_y=self.max_y, COLOR=self.COLOR.copy()) 
                            else: pass
                        
                        # moving cursor up, down, left, right   
                        elif self.char == 27        :
                            if type(_) is type(list()): next1 = _[0]
                            else: next1 = _
                            
                            if next1 in {68, 67, 66, 65, 49} :
                                # move left 
                                if   next1 == 68:
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
                                elif next1 == 67:
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
                                elif next1 == 65:
                                    if self.if_line > 0 and self.scrollDown == 0 : 
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
                                            self.move.TO(x=self.x, y=self.y) + self.c_bg + 
                                            self.move.TO(x=self.x, y=self.y) + self.init.reset 
                                            )
                                            sys.stdout.flush()
                                        else:
                                            if self.if_line == 0 : pass 
                                            else: 
                                                if self.if_line > 0 :
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
                                                    formating.formating(LINE=self.LINE, data=self.str_, idd=self.if_line_max, 
                                                                    max_y=self.max_y-self.max_down+1, max_x=self.max_x, COLOR=self.COLOR.copy()) 
                                                    sys.stdout.write( self.move.TO(x=self.x, y=self.LINE) + self.init.reset )
                                                    sys.stdout.flush()
                                                else: pass
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
                                                sys.stdout.write( self.move.TO(x=self.x, y=self.y) + self.init.reset)
                                                sys.stdout.flush()
                                            else:
                                                formating.formating(LINE=self.LINE, data=self.str_.copy(), max_x=self.max_x, idd=self.scrollDown, 
                                                                                    max_y=self.max_y-self.max_down, COLOR=self.COLOR.copy())
                                                sys.stdout.write( self.move.TO(x=self.x, y=self.LINE) + self.init.reset)
                                                sys.stdout.flush()
                                        else: pass 
                                # move down 
                                elif next1 == 66: 
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
                                            self.histotyOfColors["color"].append(self.conservingColor)
                                            self.histotyOfColors['m'].append(0)
                                            self.histotyOfColors['locked'].append(False)
                                            self.histotyOfColors['n'].append(0)
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
                                                                idd=self.scrollDown,  max_y=self.max_y-self.max_down, COLOR=self.COLOR.copy())
                                                sys.stdout.write( self.move.TO(x=self.x, y=self.y) + self.init.reset)
                                                sys.stdout.flush()
                                            else: pass
                                        else: pass
                                # ctrl-up is handled
                                elif next1 == 49:
                                    if self.Data['string'] : 
                                        next2 =  _[1]
                                        if next2 in {67, 68}: pass # ctrl-up, ctrl-down is handled 
                                        # ctrl-right is handled 
                                        elif next2 == 65:
                                            if len(self.Data['string']) > self.Data['I_S']: 
                                                newString =  self.Data['string'][self.Data['I_S']].upper()
                                                self.Data['string'] = self.Data['string'][ : self.Data['I_S']]  + newString  + \
                                                    self.Data['string'][self.Data['I_S'] + 1 : ] 
                                                newString =  self.Data['input'][self.Data['index']].upper()
                                                self.Data['input']  = self.Data['input'][ : self.Data['index']] + newString  + \
                                                    self.Data['input'][self.Data['index'] + 1 : ] 
                                                self.x                  += 1
                                                self.Data['index']      += 1
                                                self.Data['I_S']        += 1
                                            else: pass
                                        # ctrl-left is handled 
                                        elif next2 == 66: 
                                            if self.Data['I_S'] > 0: 
                                                self.x                  -= 1
                                                self.Data['index']      -= 1
                                                self.Data['I_S']        -= 1
                                                newString =  self.Data['string'][self.Data['I_S']].lower()
                                                self.Data['string'] = self.Data['string'][ : self.Data['I_S']]  + newString + \
                                                    self.Data['string'][self.Data['I_S'] + 1 : ] 
                                                newString =  self.Data['input'][self.Data['index']].lower()
                                                self.Data['input']  = self.Data['input'][ : self.Data['index']] + newString + \
                                                    self.Data['input'][self.Data['index'] + 1 : ] 
                                            else: pass
                                        else: pass
                                        self.char = _[1]
                                    else: pass
                            elif next1 is None:
                                next1, ext2, nex3, next4 = input.win_outer()
                                if self.screenLocked is False :  self.screenLocked = True
                                else: self.screenLocked = False
                                self.overwriting        = False
                            else: 
                                self.overwriting        = False
                                if self.screenLocked is False :  self.screenLocked = True
                                else: self.screenLocked = False
                            next1, next2, next3, next4, next5 = 0, 0, 0, 0, 0
                                     
                        # when <enter> is pressed  
                        elif self.char in {13, 10}  :
                            # creating or inserting a new line line on the bottom of the current line
                            if self.screenLocked is False : 
                                # moving cursor left 
                                sys.stdout.write(self.move.LEFT(pos=1000))
                                # erasing entire line 
                                sys.stdout.write(self.clear.line(2))
                                # writing string 
                                self.color  = self.histotyOfColors['color'][self.if_line]
                                self.m      = self.histotyOfColors['m'][self.if_line]
                                self.nn     = self.histotyOfColors['n'][self.if_line]
                                self.locked = self.histotyOfColors['locked'][self.if_line]
                                if self.lang != "unknown" : 
                                    __string__, __color__ = words.words(self.Data['input'][ : self.Data['index'] ], self.color, 
                                            self.lang ).final(locked=self.locked, m=self.m, n=self.nn, COLOR=self.COLOR.copy())     
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
                                self.Data['string']      = self.Data['string'][self.Data['I_S'] : ]#""
                                self.Data['input']       = self.Data['input'][self.Data['index'] : ] #""
                                self.Data['get']         = self.Data["get"][self.Data['I_S'] : ]#[]
                                self.input, self.size    = header.counter( self.if_line + 1 )
                                #####################################################################################
                                
                                try : 
                                    self.Data['string_tabular'][self.if_line]
                                    self.Data['string_tabular'].insert(self.if_line, self.Data['string'][: self.Data['I_S']])
                                    self.Data['string_tab'].insert(self.if_line, self.Data['I_S'])
                                    self.Data['liste'].insert(self.if_line, self.Data['input'][ : self.Data['index']] )
                                    self.Data['tabular'].insert(self.if_line, self.Data['index'] )
                                    self.Data['x_y'].insert(self.if_line, (self.x, self.y))
                                    self.Data['memory'].insert(self.if_line, self.Data['get'][: self.Data['I_S']])
                                    self.str_.insert(self.if_line, self.Data['input'][ : self.Data['index']])
                                    self.action = "INSERTS"
                                    
                                    if self.histotyOfColors['locked'][self.if_line-1] is True: self.locked = True 
                                    else: pass 
                                    
                                    self.histotyOfColors['color'].insert(self.if_line, self.color)
                                    self.histotyOfColors['m'].insert(self.if_line, self.m)
                                    self.histotyOfColors['n'].insert(self.if_line, self.nn)
                                    self.histotyOfColors['locked'].insert(self.if_line, self.locked)
                                except IndexError:
                                    self.Data['string_tabular'].append( self.Data['string'][ : self.Data['I_S'] ] )
                                    self.Data['liste'].append( self.Data['input'][ : self.Data['index'] ] )
                                    self.Data['string_tab'].append( self.Data['I_S'] )
                                    self.Data['tabular'].append( self.Data['index'] )
                                    self.Data['x_y'].append( (self.x, self.y) )
                                    self.Data['memory'].append( self.Data['get'][ : self.Data['I_S'] ] )
                                    self.str_.append(self.Data['input'][ : self.Data['index']])
                                    self.action = "ADD"
                                    
                                    self.histotyOfColors['color'].append(self.color)
                                    self.histotyOfColors['m'].append(self.m)
                                    self.histotyOfColors['n'].append(self.nn)
                                    self.histotyOfColors['locked'].append(self.locked)
                                    
                                ######################################################################
                                self.Data["I_S"]         = 0
                                self.Data["index"]       = 0
                                self.x                   = self.size + 1
                                ######################################################################
                                
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
                                                                    max_y=self.max_y-self.max_down, COLOR=self.COLOR.copy())
                                            sys.stdout.write( self.move.TO(x=self.x, y=self.y) + self.init.reset)
                                            sys.stdout.flush()
                                        else:
                                            formating.formating(LINE=self.LINE, data=self.str_, max_x=self.max_x, idd=self.scrollDown, 
                                                            max_y=self.max_y-self.max_down, MAX={'x' : self.x, "y" : self.y, "max" : self.if_line}
                                                            , COLOR=self.COLOR.copy())
                                            sys.stdout.write( self.move.TO(x=self.x, y=self.y) + self.init.reset)
                                            sys.stdout.flush()
                                else: 
                                    self.y           = self.max_y-(self.max_down+1)
                                    self.scrollDown += 1
                                    self.scrollUp    = 0
                                    
                                    formating.formating(LINE=self.LINE, data=self.str_, max_x=self.max_x, idd=self.scrollDown, 
                                                                    max_y=self.max_y-self.max_down, COLOR=self.COLOR.copy())
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
                                else: pass 
                            else: pass
                        
                        #ctrl + a
                        elif self.char == 17        :
                            self.Data['I_S']    = 0
                            self.Data['index']  = 0
                            self.x              = self.size + 1

                        #<ctrl + r>
                        elif self.char == 18        :
                            #used for finding a particular string on the screen 
                            if self.screenLocked is True:
                                self.find_string = Find_String.FindData().find(x=self.x, y=self.y, LINE=self.LINE, lang=self.lang, COLOR=self.COLOR.copy())
                            else: pass 
                    
                        #ctrl + d 
                        elif self.char == 4         : 
                            self.Data['I_S']    = len(self.Data['string'])
                            self.Data['index']  = len(self.Data['input'])
                            self.x              = self.Data['index'] + (self.size + 1)
                    
                        # building scring 
                        else: 
                            if self.screenLocked is False : 
                                if self.Data['index'] < self.max_x - (self.size+self.np+1):
                                    self.Data['string']      =  self.Data['string'][ : self.Data["I_S"] ] + chr( self.char ) + self.Data['string'][ self.Data["I_S"] : ]
                                    self.Data['input']       =  self.Data['input'][ : self.Data["index"] ] + chr( self.char ) + self.Data['input'][ self.Data["index"] : ]
                                    self.Data['index']      += 1
                                    self.Data['I_S']        += 1
                                    self.x                  += 1
                                    self.counterR            = len( self.Data['input'] )
                                    self.Data['get'].append(1)
                                else: pass 
                            else:
                                if self.overwriting is False:
                                    #delecting the line  copied 
                                    if   chr(self.char) == "x"  : 
                                        self.stringCopy         = self.Data['string']
                                        self.inputCopy          = self.Data['input'] 
                                        self.getCopy            = self.Data['get'].copy() 
                                        self.xCopy              = {'x_s' : self.Data['I_S'], "x_i" : self.Data['index'], "pos" : self.x}
                                        self.Data['input']      = ""
                                        self.Data['string']     = ""
                                        self.Data['get']        = [0]
                                        self.x                  = (self.size +1)
                                    
                                    # paste line copied 
                                    elif chr(self.char) == "p"  :
                                        if self.stringCopy is not None : 
                                            self.Data['input']                          = self.inputCopy 
                                            self.Data['string']                         = self.stringCopy
                                            self.x                                      = self.xCopy['pos']
                                            self.Data['index']                          = self.xCopy['x_i']
                                            self.Data['I_S']                            = self.xCopy['x_s']
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
                                    elif chr(self.char) == "c"  : 
                                        self.stringCopy     = self.Data['string'] 
                                        self.inputCopy      = self.Data['input'] 
                                        self.getCopy        = self.Data['get'].copy() 
                                        self.xCopy          = {'x_s' : self.Data['I_S'], "x_i" : self.Data['index'], "pos" : self.x}

                                    # restoring the previous state
                                    elif chr(self.char) == "u"  :
                                        keys = list(self.differentStates['data'].keys())
                                        if keys: 
                                            self.Data['string_tabular'] = self.differentStates['data'][self.differentStates['index']-1]['string_tabular'].copy()
                                            self.Data['string_tab']     = self.differentStates['data'][self.differentStates['index']-1]['string_tab'].copy()
                                            self.Data['liste']          = self.differentStates['data'][self.differentStates['index']-1]['liste'].copy()  
                                            self.Data['tabular']        = self.differentStates['data'][self.differentStates['index']-1]['tabular'].copy()
                                            self.Data['x_y']            = self.differentStates['data'][self.differentStates['index']-1]['x_y'].copy()
                                            self.Data['memory']         = self.differentStates['data'][self.differentStates['index']-1]['memory'].copy()
                                            self.str_                   = self.differentStates['data'][self.differentStates['index']-1]['str'].copy()
                                            self.if_line                = self.differentStates['data'][self.differentStates['index']-1]['if_line']
                                            self.Data['string']         = self.differentStates['data'][self.differentStates['index']-1]['string']
                                            self.Data['input']          = self.differentStates['data'][self.differentStates['index']-1]['input']
                                            self.Data['I_S']            = self.differentStates['data'][self.differentStates['index']-1]['I_S']
                                            self.Data['index']          = self.differentStates['data'][self.differentStates['index']-1]['index']
                                            self.x, self.y              = self.differentStates['data'][self.differentStates['index']-1]['now_x_y'].copy()
                                            self.if_line_max            = self.if_line
                                            if self.str_ : 
                                                formating.RestoringSTring(max_x=self.max_x, max_y=self.max_y,LINE=self.LINE, 
                                                                    WRITE=self.str_, x = self.x, y = self.y, COLOR=self.COLOR.copy())
                                            else: pass 
                                            
                                            del self.differentStates['data'][ self.differentStates['index']-1]
                                            self.differentStates['index'] -= 1
                                        else: pass
                                    
                                    # delecting string 
                                    elif chr(self.char) == "d"  :
                                        if self.if_line < len(self.Data['string_tabular']):   
                                            try:           
                                                self.Data['string_tabular'] = self.Data['string_tabular'][ : self.if_line] + self.Data['string_tabular'][self.if_line+1 : ] + ['']
                                                self.Data['string_tab']     = self.Data['string_tab'][ : self.if_line]  + self.Data['string_tab'][self.if_line +1 : ] + [0]
                                                self.Data['liste']          = self.Data['liste'][: self.if_line] + self.Data['liste'][self.if_line+1 : ] + ['']      
                                                self.Data['tabular']        = self.Data['tabular'][ : self.if_line] + self.Data['tabular'][self.if_line+1 : ] + [0]      
                                                self.Data['memory']         = self.Data['memory'][ : self.if_line] + self.Data['memory'][self.if_line+1 : ] + [[]]        
                                                self.Data['x_y']            = self.Data['x_y'][ : self.if_line] + self.Data['x_y'][self.if_line+1 : ] + [(self.size+1, len(self.Data['memory']))]
                                                self.str_                   = self.str_[ : self.if_line] + self.str_[self.if_line+1 : ] + ['']    
                                                
                                                formating.scrollUP(self.str_, self.max_x, self.if_line_max, self.max_y, self.y, COLOR=self.COLOR.copy())
                                                
                                                self.Data['input']                          = self.Data['liste'][self.if_line]
                                                self.Data['string']                         = self.Data['string_tabular'][self.if_line]
                                                self.x, self.Y                              = self.Data['x_y'][self.if_line]
                                                self.Data['index']                          = self.Data['tabular'][self.if_line] 
                                                self.Data['I_S']                            = self.Data['string_tab'][self.if_line]
                                                self.Data['get']                            = self.Data['memory'][self.if_line]
                                            except IndexError: pass 
                                        else: pass
                                    
                                    # overwrite the string activation key
                                    elif chr(self.char) == "r"  :
                                        self.overwriting = True
                                else:
                                    if len(self.Data['string']) > self.Data['I_S']: 
                                        if self.Data['string']:
                                            self.Data['string'] = self.Data['string'][ : self.Data['I_S']]  + chr( self.char ) + \
                                                self.Data['string'][self.Data['I_S'] + 1 : ] 
                                            self.Data['input']  = self.Data['input'][ : self.Data['index']] + chr( self.char ) + \
                                                self.Data['input'][self.Data['index'] + 1 : ] 
                                        else: 
                                            self.Data['string'] = self.Data['string'][ : self.Data['I_S']]  + chr( self.char ) + \
                                                self.Data['string'][self.Data['I_S'] : ] 
                                            self.Data['input']  = self.Data['input'][ : self.Data['index']] + chr( self.char ) + \
                                                self.Data['input'][self.Data['index'] : ]
                                            self.Data['get'].append(1)
                                        self.x                  += 1
                                        self.Data['index']      += 1
                                        self.Data['I_S']        += 1
                                        self.counterR            = len( self.Data['input'] )
                                    else : 
                                        if self.Data['index'] < self.max_x - (self.size+self.np+1):
                                            self.Data['string']      = self.Data['string'][ : self.Data["I_S"] ] + chr( self.char ) + \
                                                self.Data['string'][ self.Data["I_S"] : ]
                                            self.Data['input']       = self.Data['input'][ : self.Data["index"] ] + chr( self.char ) + \
                                                self.Data['input'][ self.Data["index"] : ]
                                            self.Data['index']      += 1
                                            self.Data['I_S']        += 1
                                            self.x                  += 1
                                            self.counterR            = len( self.Data['input'] )
                                            self.Data['get'].append(1)
                                        else: pass
                                        
                        # moving cursor left 
                        sys.stdout.write(self.move.LEFT(pos=1000))
                        # erasing entire line 
                        sys.stdout.write(self.clear.line(2))
                        # writing string 
                        self.color  = self.histotyOfColors['color'][self.if_line]
                        self.m      = self.histotyOfColors['m'][self.if_line]
                        self.nn     = self.histotyOfColors['n'][self.if_line]
                        self.locked = self.histotyOfColors['locked'][self.if_line]
                    
                        if self.lang != "unknown" : 
                            __string__, __color__ = words.words(self.Data['input'], self.color, language = self.lang ).final(locked=self.locked, 
                                                m = self.m, n=self.nn, COLOR=self.COLOR.copy())
                        else:  __string__, __color__ = self.Data['input'], {}
                        
                        sys.stdout.write(
                            self.input + self.c_bg + " " * ( self.max_x - (self.size+2) ) + self.init.reset + 
                            self.move.TO(x=self.max_x, y=self.y) +  f"{self.acs['v']}" +
                            self.move.TO(x=self.size+1, y=self.y) + self.c_bg+ __string__ + 
                            self.move.TO(x=self.size+1, y=self.y) + self.init.reset 
                            )

                        # replace the cussor 
                        if self.Data['I_S'] > 0: sys.stdout.write(self.move.TO(self.x, self.y) )
                        else: pass 
                        
                        #########################################################################################################
                        self.Data['drop_idd'], self.Data['str_drop_down'], self.a, self.b = BS.string( self.Data['input'], self.Data['index']-1 )
                        _, _, self._a, self._b = BS.string( self.Data['string'], self.Data['I_S']-1 )
                        #########################################################################################################
                        
                        sys.stdout.flush()           
                        
                        self.Data['string_tabular'][self.if_line] = self.Data['string']
                        self.Data['string_tab'][self.if_line]     = self.Data['I_S']
                        self.Data['liste'][self.if_line]          = self.Data['input']   
                        self.Data['tabular'][self.if_line]        = self.Data['index']
                        self.Data['x_y'][self.if_line]            = (self.x, self.y) 
                        self.Data['memory'][self.if_line]         = self.Data['get'].copy() 
                        self.str_[self.if_line]                   = __string__ 
                        
                        #########################################################################################################
                        #########################################################################################################
                        
                        self.color   = self.no_cmt 
                        """
                        tab = writing.tabular(self.Data['string'], self.lang)
                        
                        if self.locked is False:         
                            self.locked, self.nn                  = writing.keys(tab, self.lang, self.Data['string'])
                            if self.locked is True: self.color    = self.cmt 
                            else: self.color = self.no_cmt
                        else:
                            _open_                                = writing.OPEN(tab, self.lang, self.locked)
                            if _open_ is None: pass
                            else:
                                for s in _open_: 
                                    self.locked =  writing.STR(s, self.Data['string'])
                            
                            if  self.locked is True: self.color   = self.cmt 
                            else: self.color = self.no_cmt
                        """
                        
                        self.histotyOfColors['color'][self.if_line] = self.color
                        self.histotyOfColors['m'][self.if_line]     = self.m 
                        self.histotyOfColors['n'][self.if_line]     = self.nn
                        self.histotyOfColors['locked'][self.if_line]= self.locked
                        ########################################################################################################
                        if self.lang != "unknown":
                            self.KEYS, self.keys_items = KW.keys(language=self.lang, termios=self.termios, n=self.nn)
                            self.alpha, self._STR_, self.beta = KEYS.auto(x=self.x, y=self.y,max_x=self.max_x, max_y=self.max_y, 
                                    keys=self.KEYS.copy(), keys_items=self.keys_items, drop_string=self.Data['str_drop_down'], 
                                    my_strings=self.str_, I=self.if_line,  LEN=self.Data['index'], 
                                    idd_select={"idd" : self.idd_select, "index" : self.index_select}, COLOR=self.COLOR.copy())
                            if self.alpha is None: pass
                            else: self.y = self.alpha
                            
                            if self.str_select is True: 
                                if self._STR_ :
                                    self.Data['input']  = self.Data['input'][ : self.a] + self._STR_ +  self.Data['input'][self.b : ]
                                    self.Data['string'] = self.Data['string'][ : self._a] + self._STR_ +  self.Data['string'][self._b : ]
                                    self.Data['I_S']   += self.beta-1
                                    self.Data['index'] += self.beta-1
                                    for k in range(self.beta-1):
                                        self.Data['get'].append(1)
                                    self.idd_select, self.index_select, self.str_select  = 0, 0, False
                                    __string__, __color__ = words.words(self.Data['input'], self.color, 
                                            language = self.lang ).final(locked=self.locked, m = self.m, n=self.nn, COLOR=self.COLOR.copy())
                                    
                                    # moving cursor left 
                                    sys.stdout.write(self.move.LEFT(pos=1000))
                                    # erasing entire line 
                                    sys.stdout.write(self.clear.line(2))
                                    # writing string 
                                    sys.stdout.write(
                                        self.input + self.c_bg + " " * ( self.max_x - (self.size+2) ) + self.init.reset + 
                                        self.move.TO(x=self.max_x, y=self.y) +  f"{self.acs['v']}" +
                                        self.move.TO(x=self.size+1, y=self.y) + self.c_bg+ __string__ + 
                                        self.move.TO(x=self.size+1, y=self.y) + self.init.reset 
                                        )
                                    self.x             += self.beta-1 
                                    sys.stdout.write(self.move.TO(x=self.x, y=self.y))
                                    sys.stdout.flush()
                                    
                                    self.Data['string_tabular'][self.if_line] = self.Data['string']
                                    self.Data['string_tab'][self.if_line]     = self.Data['I_S']
                                    self.Data['liste'][self.if_line]          = self.Data['input']   
                                    self.Data['tabular'][self.if_line]        = self.Data['index']
                                    self.Data['x_y'][self.if_line]            = (self.x, self.y) 
                                    self.Data['memory'][self.if_line]         = self.Data['get'].copy() 
                                    self.str_[self.if_line]                   = __string__ 
                                else: pass
                            else: pass
                        else: pass
                        #########################################################################################################  
                        counter.count(number=self.if_line, x=self.x, y=self.y, max_x=self.max_x, 
                                max_y=self.max_y-(self.max_down), lang=self.lang, action=self.screenLocked, COLOR=self.COLOR.copy()) 
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
            