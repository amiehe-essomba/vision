from saving         import save

def string(string, idd ):
    str_ = ""
    try:
        if string: 
            if string[idd] in save.case(): 
                _id_ = idd 
                newString = string[ : idd]
                while _id_ > 0:
                    _id_ -= 1 
                    if string[_id_] in save.case(): pass 
                    else: break
            
                str_ = string[_id_ : idd]
                return (len(str_), str_)
            
            elif string[idd+1] in save.case():
                for s in string[idd +1: ] :
                    if s in save.case():
                        str_ += s
                    else: break
                return (len(str_, str_))
            elif string[idd-1] in save.case():
                _id_ = idd 
                newString = string[ : idd]
                while _id_ > 0:
                    _id_ -= 1 
                    if string[_id_] in save.case(): pass 
                    else: break
            
                str_ = string[_id_ : idd]
                return (len(str_), str_)
            else: return (0, "")
        else: return (0, "")
    except IndexError: return (0, "")