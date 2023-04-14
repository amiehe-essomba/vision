from configure  import colors

cdef class LANG:
    cdef public :
        str master 
    cdef:
        dict c
    def __cinit__(self, master) -> None:
        self.master     = master
        self.c          = {"color_name" : [], 'values' : []}
    cpdef LANG(self, str termios = "monokai"):
        if    self.master == "python": return LANG(self.master).PY(termios=termios)
        elif  self.master == "mamba" : return LANG(self.master).MAMBA(termios=termios)
        else: pass

    cdef PY(self, str termios = "monokai"):
        cdef :
            dict data = {}
            list keys = []

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        data['types']               = {"name" : ['int', 'float', 'complex', "str", "dict", "set", "tuple", "list", "bool"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data["constructor"]         = {"name" : ['__init__', '__name__', "__cinit__"], "color" : self.c}

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}
        data['class_and_func']      = {"name" : ['def', "class", "super"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}  
        data['iner']                = {"name" : ["lambda", "map", "filter", "print", "raise", "assert", "range", 
                                                "async", "type", "input", "round", "del"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data["loop"]                = {"name" : ["while", "with", "for", "yield"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data['cond']                = {"name" : ['if', "elif", "else", "try", "except", "finaly"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        names                       = ['break', "cancel", "exit", "continue", "quit", "next"]
        data['stop']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        names                       = [ "self", "local", "global",  "return", "open", "close", "readline", "write", "read", "readlines"]
        data['global']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        data['arguments']           = {"name" : ["args", "kwargs", "other", "all", "any"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(204,153,255)]} 
        data["bool_func"]           = {"name" : ["True", "Flase", "None", "NULL"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data['logical']             = {"name" : ['and', 'or'], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data["bolean"]              = {"name" : ['==', "<=", ">=", "!=", "in", "not in", "not", "->"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 0, 0)]}
        data["loading"]             = {"name" : ['from',  "import", "as"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 204, 0)]}
        data['exceptions']          = {"name" : ['NameError', "TypeError", "Exception", "UnicodeEncodeError",
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

    cdef MAMBA(self, str termios = "monokai"):
        cdef :
            dict data = {}
            list keys = []
            list names


        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        names                       = ['int', 'float', 'list', 'tuple', 'bool', 'cplx', 'dict', 'string', 'any', 'none', 'range', 'ndarray', 'table'
                                        "p_int", "p_float", "n_int", "n_float"]
        data['types']               = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data["constructor"]         = {"name" : ['initialize'], "color" : self.c}

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}
        data['class_and_func']      = {"name" : ['def', "class", "func", "lambda"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}  
        names                       = ['integer', 'float', 'string', 'complex', 'type', 'list', 'tuple', 'boolean', 'dictionary',
                                        'length', 'range', 'ansi', 'rand', 'GetLine', 'scan_test', 'min', 'max', 'fopen', 'floor', 
                                        'License', 'help', 'matrix1', 'sget', 'GetFuncNames', 'GetClassNames', 'merge', "prompt, delete"]
        data['iner']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data["loop"]                = {"name" : ["while", "with", "for", "end"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        names                       = ['if', "elif", "else", "try", "except", "finaly", "unless", "until", "switch", "case", "default", "end", "begin"]
        data['cond']                = {"name" : names, "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data['general']                = {"name" : ["self", "local", "global", "return", "open", 
                                            "close", "readline", "write", "read", "readlines"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        data['stop']                = {"name" : ['break', "exit", "continue", "pass", "next"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(204,153,255)]} 
        data["bool_func"]           = {"name" : ["True", "Flase", "None" ], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data['logical']             = {"name" : ['and', 'or', "only"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data["bolean"]              = {"name" : ['==', "<=", ">=", "!=", "in", "not in", "not", "->"], "color" : self.c }

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