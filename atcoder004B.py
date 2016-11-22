a=input()
a+=(' ')
a+=input()
a+=(' ')
a+=input()
a+=(' ')
a+=input()
j=0
mas=a.split(' ')
mas.reverse()
for i in mas:
    if j<3:
        print (i+" ",end="")
        j+=1
    else:
        print(i)
        j=0
exit()