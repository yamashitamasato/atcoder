N=int(input())
i=0
a=int(input())
while i< N-1:
    b=int(input())
    if a> b:
        a=b
    i+=1
print(a)