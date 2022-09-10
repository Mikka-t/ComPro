S = input()
T = input()
flag = True
if len(S) > len(T):
    flag = False
else:
    for i in range(len(S)):
        if T[i] != S[i]:
            flag = False
            break
if flag:
    print("Yes")
else:
    print("No")