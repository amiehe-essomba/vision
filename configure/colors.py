# Forgeground colors 
class fg:
    black       = u"\u001b[30m"
    red         = u"\u001b[31m"
    green       = u"\u001b[32m"
    yellow      = u"\u001b[33m"
    blue        = u"\u001b[34m"
    magenta     = u"\u001b[35m"
    cyan        = u"\u001b[36m"
    white       = u"\u001b[37m"
    black_L     = u"\u001b[30;1m"
    red_L       = u"\u001b[31;1m"
    green_L     = u"\u001b[32;1m"
    yellow_L    = u"\u001b[33;1m"
    blue_L      = u"\u001b[34;1m"
    magenta_M   = u"\u001b[35;1m"
    cyan_L      = u"\u001b[36;1m"
    white_L     = u"\u001b[1m"+f"\u001b[38;2;{255};{255};{255}m"

    def rbg(r, g, b): 
        return f"\u001b[38;2;{r};{g};{b}m"

# Background colors
class bg:
    black       = u"\u001b[40m"
    red         = u"\u001b[41m"
    green       = u"\u001b[42m"
    yellow      = u"\u001b[43m"
    blue        = u"\u001b[44m"
    magenta     = u"\u001b[45m"
    cyan        = u"\u001b[46m"
    white       = u"\u001b[47m"
    black_L     = u"\u001b[40;1m"
    red_L       = u"\u001b[41;1m"
    green_L     = u"\u001b[42;1m"
    yellow_L    = u"\u001b[43;1m"
    blue_L      = u"\u001b[44;1m"
    magenta_L   = u"\u001b[45;1m"
    cyan_L      = u"\u001b[46;1m"
    white_L     = u"\u001b[47;1m"

    def rgb(r, g, b): 
        return f"\u001b[48;2;{r};{g};{b}m"