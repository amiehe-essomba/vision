def ascii(char :str ):
    if   char == '<=' : return chr(8804)
    elif char == '>=' : return chr(8805)
    elif char == '/'  : return chr(247)
    elif char == '!=' : return chr(8800)
    elif char == '->' : return chr(8594)
    elif char == '||' : return chr(9553)
    elif char == '==' : return chr(9552)*2
    else: return char 
 
		
def frame(custom : bool = False):
    if custom is False:
        up_l, up_r = chr(9556), chr(9559)
        down_l, down_r = chr(9562), chr(9565)
        med1, med2, med3 = chr(9574), chr(9577), chr(9580)
        ver, hor = chr(9553), chr(9552)
        vl, vr = chr(9568), chr(9571)

        f = {'ul':up_l, 'ur':up_r, 'dl':down_l, 'dr':down_r, 'm1':med1,'m2':med2, 'm3':med3, 'v':ver, 'h':hor, 'vl':vl, 'vr': vr}
    else:
        up_l, up_r = chr(9487), chr(9491)
        down_l, down_r = chr(9495), chr(9499)
        med1, med2, med3 = chr(9523), chr(9531), chr(9547)
        ver, hor = chr(9475), chr(9473)
        vl, vr = chr(9507), chr(9515)

        f = {'ul':up_l, 'ur':up_r, 'dl':down_l, 'dr':down_r, 'm1':med1,'m2':med2, 'm3':med3, 'v':ver, 'h':hor, 'vl':vl, 'vr': vr}

    return f