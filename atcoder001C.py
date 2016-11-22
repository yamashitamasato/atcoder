def wind(size):
    H=11.25
    if(H<=size and (H*3)>size):
        return("NNE")
    elif((H*3)<=size and (H*5)>size):
        return("NE")
    elif((H*5)<=size and (H*7)>size):
        return("ENE")
    elif((H*7)<=size and (H*9)>size):
        return("E")
    elif((H*9)<=size and (H*11)>size):
        return("ESE")
    elif((H*11)<=size and (H*13)>size):
        return("SE")
    elif((H*13)<=size and (H*15)>size):
        return("SSE")
    elif((H*15)<=size and (H*17)>size):
        return("S")
    elif((H*17)<=size and (H*19)>size):
        return("SSW")
    elif((H*19)<=size and (H*21)>size):
        return ("SW")
    elif((H*21)<=size and (H*23)>size):
        return ("WSW")
    elif((H*23)<=size and (H*25)>size):
        return ("W")
    elif((H*25)<=size and (H*27)>size):
        return ("WNW")
    elif((H*27)<=size and (H*29)>size):
        return ("NW")
    elif((H*29)<=size and (H*31)>size):
        return ("NNW")
    else:
        return ("N")

def power(Dis):
    if(Dis>=0 and Dis<=2):
        return (0)
    elif(Dis>=3 and Dis<=15):
        return (1)
    elif(Dis>=16 and Dis<=33):
        return (2)
    elif(Dis>=34 and Dis<=54):
        return (3)
    elif(Dis>=55 and Dis<=79):
        return (4)
    elif(Dis>=80 and Dis<=107):
        return (5)
    elif(Dis>=108 and Dis<=138):
        return (6)
    elif(Dis>=139 and Dis<=171):
        return (7)
    elif(Dis>=172 and Dis<=207):
        return (8)
    elif(Dis>=208 and Dis<=244):
        return (9)
    elif(Dis>=245 and Dis<=284):
        return (10)
    elif(Dis>=285 and Dis<=326):
        return (11)
    elif(Dis>=327):
        return (12)

Deg,Dis=map(int, raw_input().split())

Dir=wind(Deg/10.0)
Dis=Dis/6.0
W=power(round(Dis))
if(W==0):
    Dir = "C"
print Dir,W