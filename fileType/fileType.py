def file(FileName : str = ""):
    
    # get extension
    ext = FileName.split(".")
    if len(ext) >= 2:
        ext = ext[-1]
        
        # python extention 
        if   ext == "py"            : return "python"
        # R extension 
        elif ext in ['r', "R"]      : return "r"
        # black mamba extention 
        elif ext == "bm"            : return "mamba"
        # c extention 
        elif ext == "c"             : return "c"
        # c++ extention 
        elif ext == "cpp"           : return "c++"
        # car-parrinello MD extention 
        elif ext in ["in", "ou"]    : return "cpmd"
        # java script extention 
        elif ext == "js"            : return "javascript"
        # cython extention 
        elif ext == "pyx"           : return "cython"
        # extention is not recognized 
        else: return None 
    else:
        # extention is not found 
        return None 
    
    
    