def check(data, dataBase, x, y, w):
    idd = 0
    for s in data:
        if s == '\t': 
            idd += 4
            dataBase['get'].append([x for x in range(4)])
        else:
            idd += 1
            dataBase['get'].append(1)
            
    dataBase['memory'][w]           = dataBase['get'] 
    dataBase['tabular'][w]          = dataBase['index']
    dataBase['string_tab'][w]       = dataBase['I_S']
    dataBase['liste'][w]            = dataBase['input']
    dataBase['string_tabular'][w]   = dataBase['string'] 
    dataBase['x_y'][w]              = (x+idd, y)
    
    dataBase['string']  = ""
    dataBase['input']   = "" 
    dataBase['I_S']     = 0
    dataBase["index"]   = 0 
    dataBase['get']     = []
    
    