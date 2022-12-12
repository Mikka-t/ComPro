def exEuclid(a,b):
    A = [a,b] # a0, a1
    X = [1,0] # x0, x1
    Y = [0,1] # y0, y1
    while A[1]:
        q = A[0]//A[1]
        A[0], A[1] = A[1], A[0]%A[1]
        X[0], X[1] = X[1], X[0]-q*X[1]
        Y[0], Y[1] = Y[1], Y[0]-q*Y[1]
    return [A[0], X[0], Y[0]]

def inv(a,n):
    return exEuclid(a,n)[1] % n

N = int(input())
A = list(map(int, input().split()))

# sosuu
q = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
qlen = len(q)
q2 = [0]*qlen
for i in range(qlen):
    q2[i] = pow(q[i],2)

DP = {}
"""
sosuu = []
gousei = []
for a in A:
    if a not in q:
        gousei.append(a)
    else:
        sosuu.append(a)
"""
for a in range(len(A)):
    if A[a] not in DP:
        DP[A[a]] = [a]
    else:
        DP[A[a]].append(a)
flag = True
count = 0
while flag:
    count_prev = count
    for i in range(N):
        for j in DP:
            if i not in DP[j]:
                for l in DP[j]:
                    num = A[i]*A[DP[j][l]]
                    if num not in DP:
                        DP[num] = [i]
                        count += 1
                    else:
                        DP[num].append(i)
    if count_prev == count:
        flag = False

ans = 0
for i in q2:
    if i in DP:
        ans += i*DP[i]
print(ans)