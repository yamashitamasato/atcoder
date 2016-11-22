S=list(input())
T=list(input())
atcoder=['a','t','c','o','d','e','r']
for i in range(len(S)):
    if S[i] == T[i]:
        pass
    else:
        if S[i]=='@':
            if T[i] in atcoder:
                pass
            else:
                print("You will lose")
                exit()
        elif T[i]=='@':
            if S[i] in atcoder:
                pass
            else:
                print("You will lose")
                exit()
        else:
            print("You will lose")
            exit()
print("You can win")