# delecting screen and line 
class clear:
    clear       = u"\u001b[" + "2J"
    # line
    def line( pos : int ):
        # 2 = entire line
        # 1 = from the cursor to start of line
        # 0 = from the cursor to end of line
        clearline   = u"\u001b[" + f"{pos}" + "K"
        return clearline
    # creen 
    def screen(pos : int ):
        # 0 = clears from cursor until end of screen,
        # 1 = clears from cursor to beginning of screen
        # 2 = clears entire screen
        # 3 = erasing recording line 
        clearScreen = u"\u001b[" + f"{pos}" + "J"
        return clearScreen 