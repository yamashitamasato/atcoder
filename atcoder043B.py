S=list(str(raw_input()))
res=[]
for i in  S:
    if(i=="B"):
        if(len(res)>0):
            res.pop()
    else:
        res.append(i)
print ''.join(res)