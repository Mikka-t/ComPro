from itertools import product

N,M = map(int, input().split())
C = []
A = []
for _ in range(M):
    C.append(int(input()))
    A.append(list(map(int, input().split())))

Asub = []
for i in range(M):
    tmp = "0b"
    ind = 0
    for j in range(N):
        if ind == C[i]:
            tmp += "0"
        else:
            if A[i][ind]-1 == j:
                tmp += "1"
                ind += 1
            else:
                tmp += "0"
    Asub.append(int(tmp,0))

tar = pow(2,N)-1
count = 0
for pro in product((0, 1), repeat=M):
    tmp = 0
    for i in range(M):
        if pro[i]:
            tmp = tmp | Asub[i]
        # print(bin(tmp))
        if tmp == tar:
            count += 1
            break
print(count)