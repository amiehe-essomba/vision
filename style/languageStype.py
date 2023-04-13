def comment( name : str = "python"):
    if name in ['mamba', "python", "bash"]  : return '#'
    elif name in ['fortran']                : return "!"
    elif name in ['c', 'c++']               : return "//"
    else: return None
    
def ouput( name : str = "python"):
    if name in ['mamba', "python"]  : return '->'
    else: return None
    
def deco( name : str = "python"):
    if name in ['mamba', "python"]  : return '@'
    else: return None