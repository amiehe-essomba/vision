from configure  import colors, init
from style      import style, languageStyle 
from keywords   import key_py 

cdef list case():
    lower_case = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    upper_case = lower_case.upper().split()
    
    return lower_case.split()+upper_case+['_']

cdef list CHARS():
    cdef:
        list names =  ['+', '-', '*', '^', '%', '/', '<', '>', '=', 
                        '!', '|', '&', '?', "~", "[","]",'{','}', 
                        "(", ")", '.', ':', '$', '@']

    return names

cdef class words:
    cdef public :
        str string 
        str color 
        str language
        str  termios
    cdef:
        unsigned long long int counter
        str  newS        
        str  ss          
        bint active   
        dict count      
        str  c           
        str  cc          
        str  cmt         
        list comment  
        str  decorator, delimitor
        list chars 
        list mul_cmt
        dict LANG

    def __cinit__(self, string, color, language,  termios = "monokai" ):
        self.string         = string 
        self.color          = color 
        self.language       = language
        self.termios        = termios
        self.newS           = ""
        self.ss             = ""
        self.active         = False
        self.cmt            = languageStyle.comment(name=self.language)["name"]
        self.comment        = [ self.cmt ]
        self.decorator      = languageStyle.decorator(name=self.language)['name']
        self.delimitor      = languageStyle.delimitor(name=self.language)['name']
        self.chars          = languageStyle.characters(name=self.language)['name']
        self.mul_cmt        = languageStyle.mul_cmt(name=self.language)['name']
        self.LANG           = {}
        
        
    cdef keywords(self, unsigned long long int n = 0, bint locked = False, dict count = {'int' : 0, 'sys' : []}, str b_ = '', dict COLOR = {}):
        self.LANG  = key_py.LANG(master = self.language).LANG(termios = self.termios, n = n)
        cdef :
            str newString   = ""
            bint active     = False
            unsigned long long int i, j
            list my_list    = count['sys'].copy()
            str bold        = b_+init.init.bold
            list keys       = self.LANG["all_keys"]
            bint isFound    = False
            str s , cc      = COLOR['fgColor'] 
            list num        = [str(x) for x in range(10)]
            unsigned long int c_idd = 0
            
       
        self.counter = count['int']

        if locked is False: 
            for i in range(len(keys)):
                if self.string in self.LANG[ keys[i] ]["name"]:
                    if self.counter % 2 == 0: newString += bold + cc + self.LANG[ keys[i] ]["color"]['values'][0] + self.string + init.init.reset
                    else: newString += bold + self.color + self.string + init.init.reset
                    isFound = True
                    break
                else: pass
            
            if isFound is True: pass
            else:
                for i, s in enumerate(self.string):
                    if self.counter % 2 == 0:
                        if active is False: 
                            if s in self.chars:
                               newString += style.config().main(char=s, language=self.language, cmt="", cc=cc, COLOR=COLOR.copy()) 
                            elif s in num:
                                if i == 0:
                                    try: 
                                        if self.string[1] in case(): newString += bold + cc + self.color + s + init.init.reset
                                        else: newString += style.config().main(char=s, language=self.language, cmt="", cc=cc)
                                    except IndexError: newString += style.config().main(char=s, language=self.language, cmt="", cc=cc)
                                else:
                                    if self.string[i - 1] in case(): newString += bold + cc + self.color + s + init.init.reset
                                    else: newString += style.config().main(char=s, language=self.language, cmt="",cc=cc)
                            elif s in self.comment:
                                newString += style.config().main(char=s, language=self.language, cmt=s, cc=cc, COLOR=COLOR.copy())
                                if self.string[ 0 ] not in [ "'", '"']: active = True
                                else: active = False
                            elif s in {"'", '"'}:
                                newString += style.config().main(char=s, language=self.language, cmt="", cc=cc, COLOR=COLOR.copy())
                                my_list.append(s)
                                self.counter += 1
                            elif s == self.delimitor: 
                                newString += bold + cc + colors.fg.rbg(255, 200, 50) + s + init.init.reset
                            elif s == self.decorator: 
                                newString += bold + cc + colors.fg.rbg(10, 255, 50) + s + init.init.reset
                            elif s == "/":
                                if self.language in ['c++', 'c']:
                                    try:
                                        if self.string[i+1] == "/" :
                                            newString += style.config().main(char=s, language=self.language, cmt=s, cc=cc)
                                            active = True
                                        else:  newString += style.config().main(char=s, language="mamba", cmt="", cc=cc)
                                    except IndexError: newString += style.config().main(char=s, language=self.language, cmt="", cc=cc)
                                else: newString += style.config().main(char=s, language="mamba", cmt="", cc=cc) 
                            else: newString += bold + cc + self.color + s + init.init.reset
                        else: newString += bold+cc+COLOR['cmtColor']  + s + init.init.reset
                    else:
                        newString += bold + cc + COLOR['strColor'] + s + init.init.reset
                        if my_list[0] == s: self.counter, my_list = 0, []
                        else: pass
        else: newString = cc + self.color + self.string + init.init.reset

        count['int'] = self.counter
        count['sys'] = my_list.copy()

        return newString
    
    cpdef final(self, unsigned long long n = 0, bint locked = False, bint blink = False, bint code_w = False, 
                                        unsigned long long int m = 0, dict COLOR  = {}, str QUOTE = ""):
        cdef:
            str b_, s 
            unsigned long  long int i, j 
            unsigned long long int quote = 0
            str _cmt_           = COLOR['cmtColor']    
            str _init_          = COLOR['fgColor']   
            str str_color       = COLOR['cmtColor']
            dict color_return   = {"color" : self.color, "locked" : False, "rest" : 0, "init" : _init_, "quote" : ""}
            bint string_locked  = False
            str cmt_str         = ""
            str python_str      = ""
            dict  __dic__ 
            str __string__
            
        self.c              = COLOR['strColor'] 
        self.cc             = self.color  
        self.count          = {"int" : 0, "sys" : [], "c" : 0}

        if blink is False : b_ = ""
        else : b_ = init.init.blink

        if locked is False:
            for i , s in enumerate(self.string ):
                if i >= quote:
                    if self.count['int'] % 2 == 0: self.color = init.init.bold+self.cc 
                    else: self.color = self.c 

                    if s not in [' ']:
                        if s in case()+[str(x) for x in range(10)]:
                            self.ss += s 
                            cmt_str  = ""
                            if i < len(self.string)-1: pass 
                            else:
                                if self.ss: self.newS +=  words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                                            count=self.count, b_=b_, COLOR=COLOR.copy())
                                else: pass  
                        else:
                            if   s in self.comment  :
                                cmt_str  = ""
                                self.ss += s 
                                if i < len( self.string ) - 1: pass 
                                else:
                                    if self.ss: self.newS +=  words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                        count=self.count, b_=b_,COLOR=COLOR.copy())
                                    else: pass 
                            elif s in ['"', "'"]    :
                                self.ss   += s 
                                if self.language in ['python', "cython"]: 
                                    if s == "'": 
                                        if not cmt_str: cmt_str += s 
                                        else:
                                            if '"' not in cmt_str : cmt_str += s 
                                            else : cmt_str = ""

                                    elif s == '"' : 
                                        if not cmt_str: cmt_str += s 
                                        else:
                                            if "'" not in cmt_str : cmt_str += s 
                                            else : cmt_str = ""
    
                                    if cmt_str in ['"""', "'''"] : 
                                        string_locked = True 
                                        color_return = {"color" : str_color, "locked" : False, "rest" : 0, 'init' : _init_, "quote" : cmt_str[0]}
                                        
                                        if i != len(self.string)-1 :
                                            for d, _s_ in enumerate(self.string[i + 1 : ]):
                                                if _s_ == s: python_str += s 
                                                else:
                                                    if not python_str : pass
                                                    else:  break
                                            
                                            if len(python_str) >= 3: quote = d + i + 1
                                            else: quote = 0

                                            self.newS += words(self.ss[ : -len(cmt_str)], self.color, language=self.language).keywords(n=n, locked=locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy())
                                            
                                            if quote > 0 :
                                                self.newS += words(cmt_str+self.string[i+1 : quote], str_color, language=self.language).keywords(n=n, locked=string_locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy())
                                                color_return = {"color" : self.color, "locked" : False, "rest" : 0, 'init' : _init_, "quote" : cmt_str[0]}
                                        
                                                try:
                                                    __string__, __dic__ = words(self.string[quote : ], str_color, language=self.language).final(n=n, locked=locked, 
                                                                    m=m, COLOR=COLOR.copy())
                                                    self.newS += __string__
                                                    break
                                                except IndexError: break
                                            else:
                                                self.newS += words(cmt_str+self.string[i+1 : ], str_color, language=self.language).keywords(n=n, locked=string_locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy())
                                                break
                                            
                                            self.ss,  cmt_str , python_str  = "", "", ""
                                        else:
                                            if self.ss[ :-3 ]:
                                                self.newS += words(self.ss[ :-3 ], self.color, language=self.language).keywords(n=n, locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                            else: pass 
                                            self.newS += words(cmt_str, str_color, language=self.language).keywords(n=n, locked=string_locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy())
                                            self.ss = ""
                                            break
                                    else:
                                        if i < len( self.string ) - 1: pass 
                                        else: 
                                            if i < len( self.string ) - 1: pass 
                                            else:
                                                color_return = {"color" : _init_, "locked" : False, "rest" : 0, 'init' : _init_, "quote" : ""}
                                                if self.ss:  
                                                    self.newS += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy())
                                                    self.ss=""
                                                else:  pass
                                
                                else:
                                    if i < len( self.string ) - 1: pass 
                                    else:
                                        if self.ss:  self.newS += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                        else:  pass
                            elif s == "-"           :
                                cmt_str  = ""
                                if self.language in ['python', "mamba", "cython"]:
                                    try:
                                        if self.string[i+1] == '>': 
                                            self.ss += s
                                            if i < len( self.string ) - 1: pass 
                                            else: self.newS += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                        count=self.count, b_=b_, COLOR=COLOR.copy())
                                        else: 
                                            self.newS   += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                            self.newS   += words(s, self.color, language=self.language).keywords(n=n,locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                            self.ss     = ""
                                    except IndexError: 
                                        self.newS   += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                        self.newS   += words(s, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                        self.ss      = ""
                                else: 
                                    self.newS   += words(s, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                    self.ss      = ""
                            elif s == "<"           :
                                self.ss += s
                                cmt_str  = ""
                                if self.language in ['c', "c++"]:
                                    if i < len(self.string) - 1: pass
                                    else:
                                        if self.ss: self.newS += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                        else:  pass
                                else: 
                                    if i < len(self.string) - 1: pass
                                    else:
                                        if self.ss: self.newS += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                        else:  pass
                            elif s == ">"           :
                                cmt_str  = ""
                                if self.language in ['python', "mamba", "cython"]: 
                                    if i == 0:
                                        self.newS   += words(s, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                        self.ss      = ""
                                    else:
                                        try:
                                            if self.string[i-1] in ['-']:
                                                self.ss += s 
                                                if i < len(self.string)-1: pass 
                                                else: self.newS += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy())
                                            else: 
                                                self.ss     += s
                                                self.newS   += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy())
                                                self.ss     = ""
                                        except IndexError: 
                                            self.newS   += words(self.s, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy()) 
                                            self.ss      = ""
                                elif self.language in ['c', "c++"]:
                                    self.ss += s
                                    if self.ss[0] == '<':
                                        
                                        self.newS   += words(self.ss, _cmt_, language=self.language).keywords(n=n, locked=True, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy()) 
                                        self.ss      = ""
                                    else:
                                        self.newS   += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy()) 
                                        self.ss      = ""
                                else: 
                                    self.ss     += s
                                    self.newS   += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                                count=self.count, b_=b_,COLOR=COLOR.copy()) 
                                    self.ss      = ""
                            else                    :
                                cmt_str  = ""
                                if self.ss:
                                    if self.cmt in self.ss:
                                        self.ss += s
                                        if i < len(self.string) - 1: pass
                                        else:
                                            if self.ss: self.newS += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                    count=self.count, b_=b_,COLOR=COLOR.copy())
                                            else:  pass
                                    else:
                                        self.newS   += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                        count=self.count, b_=b_,COLOR=COLOR.copy())
                                        self.newS   += words(s, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                        count=self.count, b_=b_,COLOR=COLOR.copy())
                                        self.ss      = ''
                                else :
                                    if s == '/':
                                        if self.language in {"c++", "c"}:
                                            self.ss += s 
                                            if i < len(self.string) - 1: pass
                                            else:
                                                if self.ss: self.newS += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                                count=self.count, b_=b_,COLOR=COLOR.copy())
                                                else:  pass
                                        else:
                                            self.newS   += words(s, self.color, language=self.language).keywords(n=n,locked=locked, 
                                            count=self.count, b_=b_,COLOR=COLOR.copy())
                                            self.ss      = ''
                                    else:
                                        self.newS   += words(s, self.color, language=self.language).keywords(n=n,locked=locked, 
                                        count=self.count, b_=b_,COLOR=COLOR.copy())
                                        self.ss      = ''
                    else:
                        cmt_str  = ""
                        if self.ss :
                            if self.cmt in self.ss:
                                self.ss += ' '
                                if i < len(self.string) - 1:  pass
                                else:
                                    if self.ss:  self.newS += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                        count=self.count, b_=b_,COLOR=COLOR.copy())
                                    else:  pass
                            else:
                                if self.count['int'] % 2 == 0: self.color = self.cc
                                else: self.color = self.c

                                self.newS   += words(self.ss, self.color, language=self.language).keywords(n=n, locked=locked, 
                                    count=self.count, b_=b_,COLOR=COLOR.copy())
                                if code_w is False: self.newS   += self.cc + ' '
                                else: self.newS   += self.cc + ' '
                                self.ss     = ''
                        else:
                            if code_w is False: self.newS   += self.cc + ' '
                            else: self.newS   += self.cc + ' '
                            self.ss      = ''
                else: self.ss = ""
        else:
            self.newS = words(self.string, self.color, language=self.language).keywords(n=n, locked=locked, 
                    count=self.count, b_=b_,COLOR=COLOR.copy())

        return self.newS, color_return
        