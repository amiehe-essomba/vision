from pynput import mouse
from getUserInput   import input
import sys

def on_scroll(x, y, dx, dy):
    traiter_mouvement(x, y, dx, dy)

def traiter_mouvement(x, y, dx, dy):
    # Faites quelque chose avec les valeurs de x, y, dx et dy
    print(dy, dx)

#with mouse.Listener(on_scroll=on_scroll) as listener:
#    listener.join()
    
"""_summary_
while True:
                try:
                    char1 = input.convert() 
                    if char1 == 91: 
                        next2 = ord(sys.stdin.read(1)) 
                        next1 = char1
                        if next2 == 49:
                            next3, next4, next5 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                    elif char1 == 27:
                        next11, next23 = ord(sys.stdin.read(1)) , ord(sys.stdin.read(1)) 
                    else: pass
                    break
                except KeyboardInterrupt: break
                except EOFError: break
"""

def R():
    next1, next2,  next3, next4, next5 = 0, 0, 0, 0, 0
    data = []
    while True:
        try:
            char = input.convert() 
    
            if char == 27:
                while True:
                    next1 = input.convert() 
                    if next1 == 91: 
                        next2 = ord(sys.stdin.read(1)) 
                        if next2 == 49:
                            next3, next4, next5 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                    elif next1 == 27:
                        data = outer()
                    else: pass
                    break
                
            elif char == 3: break
            
            print([char, next1, next2, next3, next4, next5])
            print(data)
            data = [] 
            next1, next2,  next3, next4, next5 = 0, 0, 0, 0, 0
        except KeyboardInterrupt: break
        except EOFError: break
    
    
def outer():
    char1, char2, char3, char4, char5 = 0, 0, 0, 0, 0
    while True:
        char1 = input.convert() 
        if char1 == 91: 
            char2 = ord(sys.stdin.read(1)) 
            if char2 == 49:
                char3, char4, char5 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
            else: pass 
        elif char1 == 27:
            char1, char2, char3, char4, char5 = inter()
        else: pass 
        
        break
    return [char1, char2, char3, char4, char5]
            
def inter():
    char1, char2, char3, char4, char5 = 0, 0, 0, 0, 0
    while True:
        char1 = input.convert() 
        if char1 == 91: 
            char2 = ord(sys.stdin.read(1)) 
            if char2 == 49:
                char3, char4, char5 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
            else: pass 
        elif char1 == 27:
            char1, char2, char3, char4, char5 = outer()
        else: pass 
        
        break
    return [char1, char2, char3, char4, char5]
            
if __name__ == '__main__':
    R()