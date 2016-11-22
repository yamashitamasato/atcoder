w=list(str(raw_input()))
lib=list(set(w))
res="Yes"
for i in range(0,len(lib)):
    if(w.count(lib[i])%2==1):
        res="No"
print(res)