N = int(input())

flag_4 = True

def temp(n):
    tmp = int(n)%4
    if tmp == 0:
        return 2
    elif tmp == 2:
        global flag_4
        if flag_4:
            flag_4 = False
        return 1
    else:
        return 0

A = list(map(temp, input().split()))
summm = sum(A)
if flag_4 and (summm>=N-1):
    print("Yes")
elif summm >= N:
    print("Yes")
else:
    print("No")