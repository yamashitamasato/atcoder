W, H = map(int, raw_input().split())
c=1
mod = 10**9+7
for i in range(1,H):
    c=c*(i+W-1)*pow(i,mod-2,mod)%mod
    print(c*(i+W-1))
    print(pow(i,mod-2,mod))
print(c)