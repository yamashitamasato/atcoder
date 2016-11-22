#coding:utf-8
#まだ正解していない
N,K=map(int,raw_input().split())
a=[]
sum=0
ans=[]
a=map(int,raw_input().split())
for i in range(N-K+1):
    for j in range(K):
        sum+=a[i+j]
print(sum)