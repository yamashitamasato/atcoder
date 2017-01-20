A=[]
listA=[]
N=int(input())
for i in range(0,N):
    A.append(int(input()))
listA=list(set(A))
listA.sort()
print(listA.pop(-2))