N,K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
taka = 0
ao = 0
num = N
max = A.pop(-1)
nowT = True
while num > 0:
    if  max > num:
        if len(A)>0:
            max = A.pop(-1)
        else:
            num = -1
            break
    else:
        if nowT:
            taka += max
            num -= max
            nowT = not nowT
        else:
            num -= max
            nowT = not nowT
print(taka)









"""
    else:
        syou = num//max
        num =num%max
        if syou%2 == 0:
            taka+=(max*(syou//2))
            ao+=(max*(syou//2))
        elif syou%2 == 1:
            taka+=(max*(syou//2))
            ao+=(max*(syou//2))
            if nowT:
                taka += max
            else:
                ao += max
            nowT = not nowT
        """
#print(taka)