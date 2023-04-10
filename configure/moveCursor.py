# moving cursor on a partuclar region of the screen
class cursor:
    move = u"\u001b[?12h"

    def __init__(self):
        pass
    # moving cursor up 
    def UP( pos: int ):
        up          = u"\u001b[" + str( pos ) + "A"
        return up
    # moving cursor down 
    def DOWN( pos: int ):
        down        = u"\u001b[" + str( pos ) + "B"
        return down  
    # moving cursor right 
    def RIGHT( pos: int ):
        right       = u"\u001b[" + str( pos ) + "C"
        return right
    # moving cursor left
    def LEFT(pos: int):
        left        = u"\u001b[" + str( pos ) + "D"
        return left
    # moving cursor on the x and y axis of th scren
    def TO(x:int, y:int):
        to          = u"\u001b[" +  str( y ) +";" + str(x) + "H"
        return to

class line:
    # next line 
    nextline = u"\u001b[1E"
    # previous line 
    prevline = u"\u001b[1F"