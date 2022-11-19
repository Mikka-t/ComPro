N = int(input())
A = list(map(int, input().split()))
Q = int(input())
wipe = False
isWiped = {}
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        wipe = True
        wipe_num = q[1]
        isWiped = {}
    elif q[0] == 2:
        if wipe and isWiped.get(q[1]-1,True):
            A[q[1]-1] = wipe_num + q[2]
            isWiped[q[1]-1] = False
        else:
            A[q[1]-1] += q[2]
    elif q[0] == 3:
        if wipe and isWiped.get(q[1]-1,True):
            print(wipe_num)
        else:
            print(A[q[1]-1])
