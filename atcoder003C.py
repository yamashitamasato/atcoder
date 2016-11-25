N,K =map(int,raw_input().split())
R=[]
R=map(int,raw_input().split())
R.sort(reverse=True)
rate=0.0
select=R[0:K]
for i in range(0,K):
    rate=(rate+select.pop())/2
print rate