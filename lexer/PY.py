
class PY:
    def __init__(self, string : str) :
        self.string     = string 
    
    def PY(self, is_opned : bool, identical : str = ""):
        self.stringLeft, self.stringRight = "", ""
        self.char, self.locked = "", False
        self.index, self.r_id, self.l_id  = 0, 0, 0
        self.jump_id = 0
        self.open, self.close = False, False 
        
        if self.string:
            for i, s in enumerate( self.string ):
                if i >= self.jump_id:
                    if s in {"'", '"'}:
                        if self.char : pass 
                        else: 
                            self.char, self.l_id = s, i
                            self.stringLeft += s
                            
                        if not self.char: self.stringLeft += s
                        else:
                            if s == self.char:
                                if self.locked is False:
                                    if len(self.stringLeft) < 3:  self.stringLeft += self.char
                                    else:
                                        self.open = True
                                        if not self.stringRight: self.r_id = i 
                                        else: pass 
                                        self.stringRight += self.char
                                        self.locked = True 
                                else: 
                                    if len(self.stringRight) < 3 : 
                                        self.stringRight += self.char
                                        
                                        if len(self.stringRight) == 3: 
                                            self.close, self.index = True, i
                                            break
                                        else: pass 
                                    else: pass
                            else:
                                if len(self.stringLeft) == 3:
                                    self.open = True
                                    if self.locked is True: self.stringRight, self.locked, self.close = "", True, False
                                    else: self.locked = True 
                                else:
                                    self.stringLeft = ""
                                    self.locked     = False
                                    self.char       = ""
                                    self.l_id       = 0
                    else:
                        if len(self.stringLeft) == 3 :
                            self.open = True
                            if self.locked is True :  self.stringRight, self.locked, self.close = "", True, False 
                            else: self.locked = True 
                        else:
                            self.stringLeft = ""
                            self.locked     = False 
                else: pass 
        else: pass
          

        if len(self.stringLeft) == 3: pass 
        else: self.char, self.l_id = '', 0
             
        try: 
            if is_opned is False:  
                if self.index != 0: self.rest = self.string[self.index+1 : ]
                else: self.rest = ""
            else:
                if self.open is True: self.rest = self.string[self.l_id + 3 : ]
                else:  self.rest = ""
        except IndexError: self.rest = ""
        
        try: 
            if is_opned is False: self.string_before = self.string[ : self.l_id ]
            else: self.string_before = ""
        except IndexError : self.string_before = ""
        
        try: 
            if is_opned is False:  
                if self.index != 0 :   self.locked_s = self.string[self.l_id : self.index+1]
                else: self.locked_s = self.string[ self.l_id  : ]
            else:
                if self.open is True: self.locked_s = self.string[ : self.l_id + 3 ]
                else: self.locked_s = self.string
        except IndexError : self.locked_s = ""
        
        if is_opned is False: pass 
        else:
            if self.open is True :
                if self.char == identical: self.close = True 
                else: pass
            else: 
                if self.open is False:  self.open = is_opned 
                else: pass
            
        data =  {
            "OPENED"    : self.open, 
            "CLOSED"    : self.close, 
            'STARTED'   : self.l_id, 
            "ENDED"     : self.index, 
            "CHAR"      : self.char, 
            "REST"      : self.rest,
            "BEFORE"    : self.string_before,
            "LOCKED_S"  : self.locked_s
            }
        
        return data 
    

def STRING_PROCESSING(string : str = "", is_opened : bool = False, char : str = ""):
    returning   = PY(string).PY(is_opened, char)
    close       = returning["CLOSED"]
    open        = returning["OPENED"]
    
    if open is True:
        if close is True : is_opened = False 
        else: is_opened = True
    else: is_opened = False
    
    returning["IS_OPENED"] = is_opened
    
    return returning    