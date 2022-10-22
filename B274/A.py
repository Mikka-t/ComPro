A,B = map(int, input().split())

S = B/A
flag=True
S = str(S)
if len(str(S))>=5:
    if int(str(S)[5]) >=5:
        print(str(S)[:4]+str(int(str(S)[4])+1))
        flag = False
    else:
        flag=False
        print(str(S)[:4]+str(int(str(S)[4])))
if flag:
    
    print(str(S).ljust(5,"0"))