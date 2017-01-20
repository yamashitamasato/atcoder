dict={}
N=int(input())
for i in  range(0,N):
    S=raw_input()
    if S in dict:

        dict[S]=dict[S]+1
    else:
        dict.update({S:1})
print (max([(v,k) for k,v in dict.items()])[1])