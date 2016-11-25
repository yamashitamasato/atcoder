import math
xa,ya,xb,yb,xc,yc=map(int,raw_input().split())
a=math.sqrt(((xa-xb)**2)+((ya-yb)**2))
b=math.sqrt(((xb-xc)**2)+((yb-yc)**2))
c=math.sqrt(((xc-xa)**2)+((yc-ya)**2))
S=(a+b+c)/2
T=math.sqrt(S*(S-a)*(S-b)*(S-c))
print (T)