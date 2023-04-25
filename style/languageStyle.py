def comment( name : str = "python"):
    if   name in ['mamba', "python", "bash", "cython"]    : return {"name" : '#'}
    elif name in ['fortran']                    : return {"name" : "!"}
    elif name in ['c', 'c++']                   : return {"name" : "//"}
    elif name in ['cpmd']                       : return {"name" : "#"}
    else                                        : return {"name" : None}
    
def mul_cmt(name : str = "python"):
    if   name in ["python", "cython"]     : return {"name" : ['"""', '"""']}
    elif name in ["c", "c++"]   : return {"name" : ['/*', '*/']}
    else: return {"name" : None}
    
def ouput( name : str = "python"):
    if name in ['mamba', "python", "cython"]  : return {"name" : '->'}
    else: return {"name" : None}
    
def decorator( name : str = "python"):
    if name in ['mamba', "python", "cython"]  : return {"name" : '@'}
    else: return {"name" : None}
    
def delimitor(name : str = "python"):
    if name in ['mamba', "python", "cython"]  : return {"name" : ":"}
    elif name in ['c', "c++", "cython"]       : return {"name" : ";"}
    else: return {"name" : None}
    
def characters(name : str = "python"):
    if   name in ["python", "cython"]     : return {"name" : ['+', '-', '*', '%', '/', '<', '>', '=', '!', '|', '&', "~", "[","]",'{','}', "(", ")", '.']}
    elif name in ['mamba']      : return {"name" : ['+', '-', '*', '%', '/', '<', '>', '=', '!', '|', '&', "~", "[","]",'{','}', "(", ")", '.', "$", "?"]}
    elif name in ['c', "c++"]   : return {"name" : ['+', '-', '*', '%', '<', '>', '=', '!', '|', '&', "~", "[","]",'{','}', "(", ")", '.', ";", "#"]}
    elif name in ["cpmd"]       : return {"name" : ['+', '-', '*', '%', '/', '<', '>', '=', '!', '|', '&', "~", "[","]",'{','}', "(", ")", '.', ";"]}
    else: return {"name" : ['+', '-', '*', '%', '/', '<', '>', '=', '!', '|', '&', "~", "[","]",'{','}', "(", ")", '.', "$", ";", ":"]}
    
