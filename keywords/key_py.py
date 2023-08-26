from configure  import colors

def case() -> list :
    lower_case = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    upper_case = lower_case.upper().split()

    return upper_case

def pseudo() -> list:
    ext     = "psp"
    psp     = ["MT", 'GTH', "SPRINK", 'MT_GIA']
    func    = ["BLYP", "PBE", "B3LYP", "HSE", "PBE0", "BLYP2"]
    all_psp = []
    strin   = ""

    for i, s in enumerate(case()):
        for j, ss in enumerate(psp):
            for k, sss in enumerate( func):
                string = s + "_" + ss + "_" + ss + "." + ext
                all_psp.append(string)
    
    return all_psp

class LANG:
    def __init__(self, master) -> None:
        self.master     = master
        self.c          = {"color_name" : [], 'values' : []}
    def LANG(self, termios : str = "monokai",  n : int = 0):
        if    self.master == "python"   : return LANG(self.master).PY(termios=termios)
        elif  self.master == "mamba"    : return LANG(self.master).MAMBA(termios=termios, n = n)
        elif  self.master == "c"        : return LANG(self.master).C(termios=termios)
        elif  self.master == "c++"      : return LANG(self.master).C(termios=termios)
        elif  self.master == "cpmd"     : return LANG(self.master).CPMD(termios=termios)
        elif  self.master == "cython"   : return LANG(self.master).CYTHON(termios=termios)
        else: pass

    def PY(self, termios : str = "monokai"):
        data = {}
        keys = []

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        data['types']               = {"name" : ['int', 'float', 'complex', "str", "dict", "set", "tuple", "list", "bool", "self"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data["constructor"]         = {"name" : ['__init__', '__name__'], "color" : self.c}

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(15,100,150)]}
        data['class_and_func']      = {"name" : ['def', "class", "super"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}  
        data['iner']                = {"name" : ["lambda", "map", "filter", "print", "raise", "assert", "range",  "ord", "chr",
                                                "async", "type", "input", "round", "del"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data["loop"]                = {"name" : ["while", "with", "for", "yield"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data['cond']                = {"name" : ['if', "elif", "else", "try", "except", "finaly"], "color" : self.c } 

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        names                       = ['break', "cancel", "exit", "continue", "quit", "next", "pass"]
        data['stop']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        names                       = [ "local", "global",  "return", "open", "close", "readline", "write", "read", "readlines"]
        data['global']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        data['arguments']           = {"name" : ["args", "kwargs", "other", "all", "any"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(204,153,255)]} 
        data["bool_func"]           = {"name" : ["True", "False", "None", "NULL"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data['logical']             = {"name" : ['and', 'or'], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data["bolean"]              = {"name" : ['==', "<=", ">=", "!=", "in", "is", "not in", "not", "-=", "//="
                                                    "+=", "/=", "**=", "%=", "*=", "->"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 0, 0)]}
        data["loading"]             = {"name" : ['from',  "import", "as"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 204, 0)]}
        data['exceptions']          = {"name" : [ "Exception", "UnicodeEncodeError",
                                        "UnboundLocalError", "UnicodeDecodeError", "UnicodeError", "UnicodeTranslateError", "UnicodeWarning",
                                        "UserWarning", "ArithmeticError", "AssertionError", "AttributeError", "BaseException", "BlockingIOError",
                                        "BrokenPipeError", "BufferError", "BytesWarning", "ConnectionResetError", "ChildProcessError", "ConnectionError",
                                        "ConnectionRefusedError", "ConnectionAbortedError", "DeprecationWarning", "EnvironmentError", "EOFError",
                                        "FileExistsError","FileNotFoundError","FloatingPointError","FutureWarning","GeneratorExit",
                                        "ImportError","ImportWarning","IndentationError","IndexError","InterruptedError","IOError","IsADirectoryError",
                                        'KeyError', "KeyboardInterrupt", "LookupError", "MemoryError","ModuleNotFoundError",
                                        "NameError","NotADirectoryError","NotImplemented","NotImplementedError", "OSError","OverflowError",
                                        "PendingDeprecationWarning", "PermissionError", "ProcessLookupError",
                                        "RecursionError","ReferenceError","ResourceWarning","RuntimeError","RuntimeWarning",
                                        "StopAsyncIteration", "StopIteration", "SyntaxError", "SystemError", "SystemExit","SyntaxWarning",
                                        "TabError", "TimeoutError", "TypeError", "ValueError", "Warning", "WindowsError", "ZeroDivisionError"
                                        ], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data["magic_method"]        = {"name" : ["__add__", "__sub__", "__mul__", "__truediv__", "__floordiv__", "__mod__", 
                                        "__pow__", "__and__", "__xor__", "__or__", "__radd__", "__le__", '__lt__', "__gt__", "__eq__",
                                        "__ne__", "__ge__", "__len__", "__getitem__", '__setitem__', '__delitem__', '__iter__', '__contains__',
                                        '__call__', '__str__'
                                        ] , "color" : self.c }

        keys                        = list(data.keys())
        data['all_keys']            = keys.copy()

        return data.copy()

    def CYTHON(self, termios : str = "monokai"):
        
        data = {}
        keys = []

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        names                       = ['int', 'float', 'complex', "str", "dict", "set", "tuple", "list",  "self",
                                        "unsigned", "signed", "long", "double", "size_t", "bint", "struct", "const", "readonly", "public"]
        data['types']               = {"name" : names , "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data["constructor"]         = {"name" : ['__init__', '__name__', "__cinit__", "property", "typedef"], "color" : self.c}

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}
        data['class_and_func']      = {"name" : ['def', "class", "super"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,105,75)]}
        data['cython_def']          = {"name" : ["cdef", "cpdef"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}  
        data['iner']                = {"name" : ["lambda", "map", "filter", "print", "raise", "assert", "range",  
                                                "ord", "chr", "gil", "nogil", "inline",
                                                "async", "type", "input", "round", "del"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data["loop"]                = {"name" : ["while", "with", "for", "yield"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data['cond']                = {"name" : ['if', "elif", "else", "try", "except", "finaly"], "color" : self.c } 

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        names                       = ['break', "cancel", "exit", "continue", "quit", "next", "pass"]
        data['stop']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        names                       = [ "local", "global",  "return", "open", "close", "readline", "write", "read", "readlines"]
        data['global']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        data['arguments']           = {"name" : ["args", "kwargs", "other", "all", "any"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(204,153,255)]} 
        data["bool_func"]           = {"name" : ["True", "False", "None", "NULL"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data['logical']             = {"name" : ['and', 'or'], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data["bolean"]              = {"name" : ['==', "<=", ">=", "!=", "in", "is", "not in", "not", "-=", "//="
                                                    "+=", "/=", "**=", "%=", "*=", "->"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 0, 0)]}
        data["loading"]             = {"name" : ['from',  "import", "as", "cimport", "extern", "include"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 204, 0)]}
        data['exceptions']          = {"name" : [ "Exception", "UnicodeEncodeError",
                                        "UnboundLocalError", "UnicodeDecodeError", "UnicodeError", "UnicodeTranslateError", "UnicodeWarning",
                                        "UserWarning", "ArithmeticError", "AssertionError", "AttributeError", "BaseException", "BlockingIOError",
                                        "BrokenPipeError", "BufferError", "BytesWarning", "ConnectionResetError", "ChildProcessError", "ConnectionError",
                                        "ConnectionRefusedError", "ConnectionAbortedError", "DeprecationWarning", "EnvironmentError", "EOFError",
                                        "FileExistsError","FileNotFoundError","FloatingPointError","FutureWarning","GeneratorExit",
                                        "ImportError","ImportWarning","IndentationError","IndexError","InterruptedError","IOError","IsADirectoryError",
                                        'KeyError', "KeyboardInterrupt", "LookupError", "MemoryError","ModuleNotFoundError",
                                        "NameError","NotADirectoryError","NotImplemented","NotImplementedError", "OSError","OverflowError",
                                        "PendingDeprecationWarning", "PermissionError", "ProcessLookupError",
                                        "RecursionError","ReferenceError","ResourceWarning","RuntimeError","RuntimeWarning",
                                        "StopAsyncIteration", "StopIteration", "SyntaxError", "SystemError", "SystemExit","SyntaxWarning",
                                        "TabError", "TimeoutError", "TypeError", "ValueError", "Warning", "WindowsError", "ZeroDivisionError"
                                        ], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data["magic_method"]        = {"name" : ["__add__", "__sub__", "__mul__", "__truediv__", "__floordiv__", "__mod__", 
                                        "__pow__", "__and__", "__xor__", "__or__", "__radd__", "__le__", '__lt__', "__gt__", "__eq__",
                                        "__ne__", "__ge__", "__len__", "__getitem__", '__setitem__', '__delitem__', '__iter__', '__contains__',
                                        '__call__', '__str__'
                                        ] , "color" : self.c }

        keys                        = list(data.keys())
        data['all_keys']            = keys.copy()

        return data.copy()
    
    def MAMBA(self, termios : str = "monokai",  n: int = 0):
    
        data = {}
        keys = []
        names


        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        names                       = ['int', 'float', 'list', 'tuple', 'bool', 'cplx', 'dict', 'string', 'any', 'none', 'range', 'ndarray', 'table'
                                        "p_int", "p_float", "n_int", "n_float", "self"]
        data['types']               = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data["constructor"]         = {"name" : ['initialize'], "color" : self.c}

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}
        data['class_and_func']      = {"name" : ['def', "class", "func", "lambda"], "color" : self.c }


        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}  
        names                       = ['integer', 'float', 'string', 'complex', 'type', 'list', 'tuple', 'boolean', 'dictionary',
                                        'length', 'range', 'ansi', 'rand', 'GetLine', 'scan_test', 'min', 'max', 'fopen', 'floor', "print", "scan",
                                        'License', 'help', 'matrix1', 'sget', 'GetFuncNames', 'GetClassNames', 'merge', "prompt", "delete" ]
        data['inter']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data["loop"]                = {"name" : ["while", "with", "for"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        names                       = ['if', "elif", "else", "try", "except", "finaly", "unless", "until", "switch", "case", "default",  "begin"]
        data['cond']                = {"name" : names, "color" : self.c }

        if n == 0:
            self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        else: self.c                    = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]} 
        names                       = ["end"]
        data['end']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        data['general']                = {"name" : [ "local", "global", "return", "open",  
                                            "close", "readline", "write", "read", "readlines"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        data['stop']                = {"name" : ['break', "exit", "continue", "pass", "next"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(204,153,255)]} 
        data["bool_func"]           = {"name" : ["True", "False", "None" ], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data['logical']             = {"name" : ['and', 'or', "only", "&&", "||"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data["bolean"]              = {"name" : ['==', "<=", ">=", "!=", "in", "is", "not in", "not", "->", "-=", 
                                                    "+=", "/=", "^=", "%=", "*=", "?"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 0, 0)]}
        data["loading"]             = {"name" : ['from',  "module", "load", "as", "save"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 204, 0)]}
        data['exceptions']          = {"name" : ['NameError', "TypeError", "ArithmeticError", "AttributeError", "EOFError", "FileNotFoundError", 
                                                    "ImportError", "IndentationError","IndexError", "IOError", 'KeyError', "KeyboardInterrupt",
                                                    "MemoryError", "ModuleNotFoundError", "NameError", "OSError","OverflowError",
                                                    "SyntaxError", "SystemError",   "ValueError",   "ZeroDivisionError", 'DirectoryNotFoundError', 
                                                    'DomainError', 'FileError', 'ModuleLoadError', 'FileModeError', 'EncodingError', 'DecodingError', 
                                                    'UnicodeError', 'CircularLoadingError', 'FileNameError' 
                                        ], "color" : self.c }

        keys                        = list(data.keys())
        data['all_keys']            = keys.copy()

        return data.copy()

    def C(self, termios : str = "monokai"):
        data = {}
        keys = []

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        names                       = ['int', 'float',  "auto", "double", "char", "long", "signed", "unsigned", "struct", 
                                        "static", "short", "public", "private", "protected", "bool", "const", "mutable", "union",
                                         ]
        data['types']               = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data["constructor"]         = {"name" : ['void', "std", "main"], "color" : self.c}

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}
        data['class_and_func']      = {"name" : [ "class"], "color" : self.c }   

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}  
        names                       = ['new', 'delete', 'enum',  "goto", "friend", "inline" , "namespace", 
                                        "operator", "register", "volatile", "sizeof", "throw", "this", "cout", "endl", "cin"]
        data['iner']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data["loop"]                = {"name" : ["while", "do", "for" ], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        names                       = ['if',   "else", "try", "switch", "case", "default", "catch"]
        data['cond']                = {"name" : names, "color" : self.c }  

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data['general']             = {"name" : [ "return", "using", "typedef", "typeid", "typename", "virtual", 
                                                "extern", "explicit", "template"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        data['stop']                = {"name" : ['break', "continue" ], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(204,153,255)]} 
        data["bool_func"]           = {"name" : ["true", "false", "NULL" ], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data['logical']             = {"name" : ['&&', '||', "!"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        names                       = ['==', "<=", ">=", "!=", "in", "not in", "not", "+=", "-=", "%=", "/=", "*=", "?"]
        data["bolean"]              = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 0, 0)]}
        data["loading"]             = {"name" : ['include', "define"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 204, 0)]}
        data['exceptions']          = {"name" : ['logic_error', "exception", "bad_alloc", "bad_cast", "bad_exception", "bad_typeid", 
                                                    "invalid_argument", "length_error","out_of_range", "runtime_error", 'overflow_error', "range_error",
                                                    "underflow_error", "runtime_error"  ], "color" : self.c }

        keys                        = list(data.keys())
        data['all_keys']            = keys.copy()

        return data.copy()

    def CPMD(self, termios : str = "monokai"):
        data = {}
        keys = []
       
        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        names                       = ["CPMD", "CONTROL", "SYSTEM", "POTENTIAL", "PARAMETERS", "PRINT", "ATOMS",
                                            "RESTART", "CONSTRAINTS", "THERMOSTAT", "BAROSTAT", "CELL_OPT", "GEO_OPT", "INFO", "END", "DFT", "VDW"]
        data['types']               = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        names                       = ['OPTIMIZE', "WAVEFUNCTION", "INITIALIZE", "MOLECULAR", "DYNAMICS", "CP", "COORDINATES", "RESTFILES", "RESTART", "LATEST",
                                        "VELOCITIES", "ACCUMULATORS", "NOSEP", "NOSEE", "LASTES", "QUENCH", "ELECTRONS", "BO", "ANNEALING", 
                                        "IONS", "TIMESTEP", "EMASS", "MAXSTEP", "ENERGIES", "FORCES", "STORE", "PCG", "MINIMIZE", "STRESS",
                                        "TENSOR", "CONVERGENCE", "ORBITALS", "NOSE", "TRAJECTORY", "SAMPLE", "XYZ", "SUBTRACT", "COMVEL", "ROTVEL",
                                        "MEMORY", "BIG", "REAL", "SPACE", "WFN", "KEEP", "DISTRIBUTE", "FNL", "ON", "WANNIER", "TYPE", "VANDERBILT",
                                        "SD", "JACOBI", "OPTIMIZATION", "PARAMETER"] 
        _names_                     = [x.lower() for x in names]
        data["CPMD_UPPER"]          = {"name" : names, "color" : self.c}
        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        data['CPMD_LOWER']          = {"name" : _names_, "color" : self.c }


        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}
        names                       = ["FUNCTIONAL", "PBE", "BLYP", "B3LYP", "PBE0", "HSE", "GCC-CUTOFF"]
        _names_                     = [x.lower() for x in names]
        data['DFT_UPPER']           = {"name" : names, "color" : self.c }   
        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(204,153,255)]} 
        data["DFT_LOWER"]           = {"name" : _names_, "color" : self.c }


        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}  
        names                       = ["ANGSTROM", "BOHR", "ATMIC", "UNIT", "SYMMETRY","CELL", "CUTOFF"]
        _names_                     = [x.lower() for x in names]
        data['SYSTEM_UPPER']        = {"name" : names, "color" : self.c }
        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data['SYSTEM_LOWER']        = {"name" : _names_, "color" : self.c }


        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        names                       = ["CORRECTION", "VERSION", "FRAGMENT", "BOND", "TOLERANCE","CELL", "CUTOFF"]
        _names_                     = [x.lower() for x in names]
        data["VWD_UPPER"]           = {"name" : names, "color" : self.c }
        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data['VDW_LOWER']           = {"name" : _names_, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 25, 10)]}
        names                       = ["LMAX", "LOC", "KLEINMAN", "BYLANDER"]
        _names_                     = [x.lower() for x in names]
        data['ATOMS_UPPER']         = {"name" : names, "color" : self.c }  
        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 204, 0)]}
        data['ATOMS_LOWER']         = {"name" : _names_, "color" : self.c }  

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(90, 75, 75)]}
        data['PSEUDO']              = {"name" : pseudo(), "color" : self.c }  

        keys                        = list(data.keys())
        data['all_keys']            = keys.copy()

        return data.copy()