from configure  import colors, init
from style      import style, languageStyle 
from keywords   import key_py 
cdef list case():
    lower_case = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    upper_case = lower_case.upper().split()
    
    return lower_case.split()+upper_case+['_']

cdef class words:
    cdef public :
        str string 
        str color 
        str language
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
        dict LANG 

    def __cinit__(self, string, color, language = "python" ):
        self.string         = string 
        self.color          = color 
        self.LANG           = key_py.LANG("").PY(termiso = "monokai")
        self.language       = language
        self.counter        = 0
        self.newS           = ""
        self.ss             = ""
        self.active         = False
        self.count          = {"init" : 0, "sys" : []}
        self.c              = init.init.bold+colors.fg.rbg(255, 153, 204)
        self.cc             = init.init.bold+self.color
        self.cmt            = languageStyle.comment(name=self.language)
        self.comment        = [ self.cmt ]

    cdef keywords(self, unsigned long long int n = 0, bint locked = False, dict count = {'int' : 0, 'sys' : []}, str b_ = ''):
        cdef :
            str newString  = ""
            bint active    = False
            unsigned long long int i, j
            list my_list   = count['sys']
            str bold       = b_+init.init.bold
            list keys      = self.LANG["all_keys"]
            bint isFound   = False
            str s 
            list chars = ['+', '-', '*', '^', '%', '/', '<', '>', '=', '!', '|', '&', '?', "~", "[","]",'{','}', "(", ")", '.', ':', '$', '@']
            list num = [str(x) for x in range(10)]
            list comment   = [ languageStyle.comment(name=self.language) ]

        self.counter = count['int']

        if locked is False: 
            for i in range(len(keys)):
                if self.string in self.LANG[ keys[i] ]["name"]:
                    if self.counter % 2 == 0: newString += bold + self.LANG[ keys[i] ]["color"] + self.string + init.init.reset
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
                               newString += style.config().main(char=s, language="python", cmt=s) 
                            elif s in self.num:
                                if i == 0:
                                    try: 
                                        if self.string[1] in case(): newString += self.bold + self.color + s + init.init.reset
                                        else: newString += style.config().main(char=s, language="python", cmt=s)
                                    except IndexError: newString += style.config().main(char=s, language="python", cmt=s)
                                else:
                                    if self.string[i - 1] in case(): newString += self.bold + self.color + s + init.init.reset
                                    else: newString += style.config().main(char=s, language="python", cmt=s)
                            elif s in self.comment:
                                newString += style.config().main(char=s, language="python", cmt=s)
                                if self.string[ 0 ] not in [ "'", '"']: active = True
                                else: active = False
                            elif s  in {"'", '"'}:
                                newString += style.config().main(char=s, language="python", cmt=s)
                                my_list.append(s)
                                self.counter += 1
                            else: newString += bold + self.color + s + init.init.reset
                        else: newString += bold+colors.fg.rbg(153, 153, 255) + s + init.reset
                    else:
                        newString += bold + colors.fg.rbg(255, 153, 204) + s + init.init.reset
                        if my_list[0] == s: self.counter, self.my_list = 0, []
                        else: pass
        else: newString = self.color + self.string + init.init.reset

        count['int'] = self.counter
        count['sys'] = my_list.copy()

        return newString

    cpdef final(self, unsigned long long n = 0, bint locked = False, bint blink = False, bint code_w = False):
        cdef:
            str b_, s 
            unsigned long  long int i, j 
          
        if blink is False : b_ = ""
        else : b_ = init.init.blink

        if locked is False:
            for i , s in enumerate(self.string ):
                if self.count['int'] % 2 == 0: self.color = init.init.bold+self.cc 
                else: self.cc = self.c 

                if s not in [' ']:
                    if s in case()+[str(x) for x in range(10)]:
                        self.ss += s 
                        if i < len(self.string)-1: pass 
                        else:
                            if self.ss: self.newS +=  words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                            else: pass  
                    else:
                        if s in self.comment:
                            self.ss += s 
                            if i < len( self.string ) - 1: pass 
                            else:
                                if self.ss: self.newS +=  words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                else: pass 
                        elif s in ['"', "'"]:
                            self.ss += s 
                            if i < len( self.string ) - 1: pass 
                            else:
                                if self.ss:  self.newS += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                else:  pass
                        elif s == "-":
                            if self.language in ['python', "mamba"]:
                                try:
                                    if self.string[i+1] == '>': 
                                        self.ss += s
                                        if i < len( self.string ) - 1: pass 
                                        else: self.newS += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                    else: 
                                        self.newS   += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                        self.newS   += words(s, self.color).keywords(n=n,locked=locked, count=self.count, b_=b_)
                                        self.ss     = ""
                                except IndexError: 
                                    self.newS   += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                    self.newS   += words(s, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                    self.ss      = ""
                            else: 
                                self.newS   += words(s, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                self.ss      = ""
                        elif s == ">":
                            if self.language in ['python', "mamba"]: 
                                if i == 0:
                                    self.newS   += words(s, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                    self.ss      = ""
                                else:
                                    try:
                                        if self.string[i-1] in ['-']:
                                            self.ss += s 
                                            if i < len(self.string)-1: pass 
                                            else: self.newS += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                        else: 
                                            self.ss     += s
                                            self.newS   += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                            self.ss     = ""
                                    except IndexError: 
                                        self.newS   += words(s, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_) 
                                        self.ss      = ""
                            else: 
                                self.newS   += words(s, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_) 
                                self.ss      = ""
                        else:
                            if self.ss:
                                if self.cmt in self.ss:
                                    self.ss += s
                                    if i < len(self.string) - 1: pass
                                    else:
                                        if self.ss: self.newS += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                        else:  pass
                                else:
                                    self.newS   += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                    self.newS   += words(s, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                    self.ss      = ''
                            else :
                                self.newS   += words(s, self.color).keywords(n=n,locked=locked, count=self.count, b_=b_)
                                self.ss      = ''
                else:
                    if self.ss :
                        if self.cmt in self.ss:
                            self.ss += ' '
                            if i < len(self.string) - 1:  pass
                            else:
                                if self.ss:  self.newS += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                                else:  pass
                        else:
                            if self.count['int'] % 2 == 0: self.color = self.cc
                            else: self.color = self.c

                            self.newS   += words(self.ss, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)
                            if code_w is False: self.newS   += ' '
                            else: self.newS   += self.cc + ' '
                            self.ss     = ''
                    else:
                        if code_w is False: self.newS   += ' '
                        else: self.newS   += self.cc + ' '
                        self.ss      = ''

        else: self.newS = words(self.string, self.color).keywords(n=n, locked=locked, count=self.count, b_=b_)

        return self.newS