from configure  import colors

cdef class LANG:
    cdef public :
        str master 
    cdef:
        dict c
    def __cinit__(self, master) -> None:
        self.master     = master
        self.c          = {"color_name" : [], 'values' : []}
    cpdef dict PY(self, str termios = "monokai"):
        cdef :
            dict data = {}
            list keys = []


        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153, 153, 255)]}
        data['cmt']                 = {"name" : "#" , "color" : self.c}

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        data['types']               = {"name" : ['int', 'float', 'complex', "str", "dict", "set", "tuple", "list", "bool"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(25,165,200)]}
        data["constructor"]         = {"name" : ['__init__', '__name__', "__cinit__"], "color" : self.c}

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}
        data['class_and_func']      = {"name" : ['def', "class", "super"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255,165,0)]}  
        data['iner']                = {"name" : ["lambda", "map", "filter", "print", "raise", "assert", "range"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data["loop"]                = {"name" : ["while", "with", "for", "yield"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(51, 102, 255)]}
        data['cond']                = {"name" : ['if', "elif", "else", "try", "except", "finaly"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(153,204,0)]}
        data['stop']                = {"name" : ['break', "cancel", "exit", "continue", "self", "local", "global", "quit", "return", "open", 
                                            "close", "readline", "write", "read", "readlines"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(240,128,128)]}
        data['arguments']           = {"name" : ["args", "kwargs", "other", "all", "any"], "color" : self.c }

        self.cancel                 = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(204,153,255)]} 
        data["bool_func"]           = {"name" : ["True", "Flase", "None", "NULL"], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data['logical']             = {"name" : ['and', 'or'], "color" : self.c }

        self.c                      = {"color_name" : ["monokai"], 'values' : [colors.fg.rbg(255, 102, 0)]}
        data["bolean"]              = {"name" : ['==', "<=", ">=", "!=", "in", "not in", "not", "->"], "color" : self.c }

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
        keys = list(data.keys())

        data['all_keys'] = keys.copy()


        return data.copy()