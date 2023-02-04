import copy
N,K = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
lr = []
for _ in range(Q):
    lr.append(list(map(int, input().split())))

Ad = [0]*N
Ad[0] = A[0]
for i in range(1,N):
    Ad[i] = A[i] - A[i-1]
print(A)
print(Ad)
for i in range(Q):
    l,r = lr[i][0], lr[i][1]
    Atemp = Ad[l-1:r]
    Atemp[0] = A[l-1]
    temp = Atemp[-1]
    flag = True
    print(Atemp)
    print(A[r-1])
    if (A[r-1-(K-1)] - sum(Atemp[-2*K+1:-K])) + A[r-1] == 0:
        print("Yes") 
    else:
        print("No")       





















"""

Ad = copy.deepcopy(A)
temp = Ad[0]
for i in range(N-K): 
    for j in range(K-1):
        Ad[i+j+1] -= Ad[i]

Ad2 = [0]*N
temp = 0
for i in range(N):
    temp += Ad[i]
    Ad2[i] = temp

print(A)
print(Ad)
print(Ad2)
"""

"""

# katei: kno baisuu nara ii suuretsu
print(A)
print(Ad)
for i in range(Q):
    query = lr[i]
    tempA = Ad[query[0]-1:query[1]]
    print(tempA)
    if query[0] != 1:
        sumA = tempA[-1] - (query[1]-query[0])*Ad[query[0]-1-1]
        
        for a in range(len(tempA)):
            tempA[a] = tempA[a]-Ad[query[0]-1-1]
        print(tempA)
    else:
        sumA = tempA[-1]

    if sumA % K == 0:
        print("Yes")
    else:
        print("No")
"""

