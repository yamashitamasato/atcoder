import math
n,x = map(int, raw_input().split())
if math.ceil(n/2.0)< x:
    print(n-x)
else:
    print(x-1)
