N,Q=map(int,raw_input().split())
ans=[0]*N
for i in range(Q):
    L,R,T=map(int,raw_input().split())
    for position in range(L-1,R):
        ans[position]=T
for anser in ans:
    print(anser)