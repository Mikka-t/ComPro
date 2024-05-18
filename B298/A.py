N = int(input())
S=input()

isOK = False
isNG = False
for i in range(N):
    if S[i] == "o":
        isOK=True
    elif S[i] == "x":
        isNG=True

if isOK and (not isNG):
    print("Yes")
else:
    print("No")
