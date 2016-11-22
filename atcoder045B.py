Sa=list(str(raw_input()))
Sb=list(str(raw_input()))
Sc=list(str(raw_input()))
state="a"
while True:
    if state=="a":
        if (len(Sa) == 0):
            break
        else:
            state=Sa.pop(0)

    elif state=="b":
        if (len(Sb) == 0):
            break
        else:
            state=Sb.pop(0)
    elif state=="c":
        if (len(Sc) == 0):
            break
        else:
            state=Sc.pop(0)
print(state.upper())
