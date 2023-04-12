class scrolled:
    # scrollUp
    def UP(n : int):
        s = u"\u001b[" + f"{n}" + "S"
        return s
    def DOWN(n : int ):
        # scrollDown 
        s = u"\u001b[" + f"{n}" + "T"
        return s
    