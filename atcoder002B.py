n=input()
char_list=list(n.lower())
ans=''
list=['a','i','u','e','o']
for i in char_list:
    if i not in list:
        ans+=i
print(ans)