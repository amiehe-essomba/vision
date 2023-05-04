def fgC(r, g, b):
    return  f"\u001b[38;2;{r};{g};{b}m"

def bgC(r, b, g):
    return f"\u001b[48;2;{r};{g};{b}m"

def reset():
    return u"\u001b[0m"  

if __name__ == "__main__":
    re = reset()
    
    for i in range(5):
        h = fgC(150, 250, 200) + " abc " * 10 + re 
        print(h)
    
    """
    for r in range(255):
        for g in range(255):
            for b in range(255):
                if r == g  and r != b:
                    s = color(r, g, b) + "hello" + re 
                    print(s, r, g, b)
    """