from configure      import colors, init

class config:
    def __init__(self, termios : str = "monokai"):
        # set style 
        self.termios            = termios
        # loading backgroung color 
        self.color_bg           = colors.bg
        # loading foreground color 
        self.color_fg           = colors.fg
        # loading initialization cursor parameters 
        self.init               = init.init
 
    def main(self, char : str = "=", language : str = "python", cmt : str = "", cc : str = "", color: str = ""):
        self.return_char  = ""
        
        if char and char != cmt:
            if   char in {'<', '>', '=', '!', '|', '&', '?', "~"}   : self.return_char =  config(self.termios).operators(char=char, language=language, cc=cc)
            elif char in {'+', '-', '*', '^', '%', '/'}             : self.return_char =  config(self.termios).arithmetic(char=char, language=language,cc=cc)
            elif char in {"'", '"'}                                 : self.return_char =  config(self.termios).quote(char=char, language=language,cc=cc, color=color)
            elif char in {str(x) for x in range(10)}                : self.return_char =  config(self.termios).number(char=char, language=language,cc=cc)
            elif char in {"[","]",'{','}', "(", ")"}                : self.return_char =  config(self.termios).bracket(char=char, language=language,cc=cc)
            elif char in {"@", "$"}                                 : self.return_char =  config(self.termios).decorators(char=char, language=language,cc=cc)
            elif char in {":", "."}                                 : self.return_char =  config(self.termios).dots(char=char, language=language,cc=cc)
            else                                                    : self.return_char =  config(self.termios).rest(char=char, language=language,cc=cc)
        elif char and char == cmt: 
            self.return_char =  config(self.termios).comment(char=char, language=language, cc=cc)
        else: pass 
        
        return self.return_char
    
    def operators(self, char: str = "=", language : str = "mamba", cc : str = "")      :
        # initialization 
        self.text = ""
        
        if language in ['python', 'mamba',  "c", "c++"] : 
            # default text color white 
            if   self.termios == "monokai":  self.text = self.init.bold+cc+self.color_fg.rbg(255, 102, 0) + char + self.init.reset
            elif self.termios == "orion"  :  self.text = self.init.bold+cc+self.color_fg.rbg(255, 102, 0) + self.init.blink+ char + self.init.reset
        else: pass 
        
        return self.text
    
    def arithmetic(self, char: str = "+", language : str = "mamba", cc : str = "")     :
        # initialization 
        self.text = ""
        
        if language in ['python', 'mamba',  "c", "c++"] : 
            # default text color white 
            if   self.termios == "monokai":  self.text = self.init.bold+cc+self.color_fg.rbg(255, 0, 0) + char + self.init.reset
            elif self.termios == "orion"  :  self.text = self.init.bold+cc+self.color_fg.rbg(255, 0, 0) + self.init.blink+ char + self.init.reset
        else: pass 
        
        return self.text
    
    def quote(self, char: str = "'", language : str = "mamba", cc : str = "", color: str = "")          :
        # initialization 
        self.text = ""
        
        if language in ['python', 'mamba', "c", "c++"] : 
            # default text color white 
            if not color:
                if   self.termios == "monokai":  self.text = self.init.bold+cc+self.color_fg.rbg(255, 153, 204) + char + self.init.reset
                elif self.termios == "orion"  :  self.text = self.init.bold+cc+self.color_fg.rbg(255, 153, 204) + self.init.blink+ char + self.init.reset
            else: 
                if   self.termios == "monokai":  self.text = color + char + self.init.reset
                elif self.termios == "orion"  :  self.text = color +  self.init.blink+ char + self.init.reset
        else: pass 
        
        return self.text
    
    def number(self, char: str = "1", language : str = "mamba", cc : str = "")         :
        # initialization 
        self.text = ""
        
        if language in ['python', 'mamba', "c", "c++"] : 
            # default text color white 
            if   self.termios == "monokai":  self.text = self.init.bold+cc+self.color_fg.rbg(255, 0, 255) + char + self.init.reset
            elif self.termios == "orion"  :  self.text = self.init.bold+cc+self.color_fg.rbg(255, 0, 255) + self.init.blink+ char + self.init.reset
        else: pass 
        
        return self.text
    
    def comment(self, char: str = "#", language : str = "mamba", cc : str = "")        :
        # initialization 
        self.text = ""
        
        if language in ['python', 'mamba', "c", "c++"] : 
            # default text color white 
            if language in ['c', 'c++']: self.c = self.init.bold+cc+self.color_fg.rbg(255, 0, 0)
            else: self.c = self.init.bold+cc+self.color_fg.rbg(153, 153, 255)
            
            if   self.termios == "monokai":  self.text = self.c + char + self.init.reset
            elif self.termios == "orion"  :  self.text = self.c + self.init.blink+ char + self.init.reset
        else: pass 
        
        return self.text
    
    def bracket(self, char: str = "(", language : str = "mamba", cc : str = "")        :
        # initialization 
        self.text = ""
        
        if language in ['python', 'mamba',"c", "c++"] : 
            # default text color white 
            if   self.termios == "monokai":  
                if char in ['(', ')']: self.text = self.init.bold+cc+self.color_fg.rbg(0, 255, 0) + char + self.init.reset
                if char in ['[', ']']: self.text = self.init.bold+cc+self.color_fg.rbg(255, 255, 0) + char + self.init.reset
                if char in ['{', '}']: self.text = self.init.bold+cc+self.color_fg.rbg(255, 255, 153) + char + self.init.reset
            elif self.termios == "orion"  :  self.text = self.init.bold+cc+self.color_fg.rbg(153, 153, 255) + self.init.blink+ char + self.init.reset
        else: pass 
        
        return self.text
    
    def decorators(self, char: str = "@", language : str = "mamba", cc : str = "")     :
        # initialization 
        self.text = ""
        
        if language in ['python', 'mamba'] : 
            # default text color white 
            if   self.termios == "monokai":  
                if char == "$"  :  self.text = self.init.bold+cc+self.color_fg.rbg(50, 102, 255) + char + self.init.reset
                if char == "@"  :  self.text = self.init.bold+cc+self.color_fg.rbg(0, 255, 255) + char + self.init.reset
            elif self.termios == "orion"  :  self.text = self.init.bold+cc+self.color_fg.rbg(0, 255, 255) + self.init.blink+ char + self.init.reset
        else: pass 
        
        return self.text
    
    def dots(self, char: str = ":", language : str = "mamba", cc : str = "")           :
        # initialization 
        self.text = ""
        
        if language in ['python', 'mamba', "c", "c++"] : 
            # default text color white 
            if   self.termios == "monokai":  
                if char == ":"  :  self.text = self.init.bold+cc+self.color_fg.rbg(255, 255, 153) + char + self.init.reset
                if char == "."  :  self.text = self.init.bold+cc+self.color_fg.rbg(0, 102, 204) + char + self.init.reset
            elif self.termios == "orion"  :  self.text = self.init.bold+cc+self.color_fg.rbg(0, 255, 255) + self.init.blink+ char + self.init.reset
        else: pass 
        
        return self.text
    
    def rest(self, char: str = ":", language : str = "mamba", cc : str = "")           :
        # initialization 
        self.text = ""
        
        if language in ['python', 'mamba', "c", "c++"] : 
            # default text color white 
            if   self.termios == "monokai":  self.text = self.init.bold+cc+self.color_fg.rbg(255, 255, 255) + char + self.init.reset
            elif self.termios == "orion"  :  self.text = self.init.bold+cc+self.color_fg.rbg(255, 255, 255) + self.init.blink+ char + self.init.reset
        else: pass 
        
        return self.text
    
    