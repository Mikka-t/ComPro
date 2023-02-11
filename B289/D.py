N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

from collections import defaultdict

DP = [False]*(X+1)
DP[0] = True
Bdict = defaultdict(lambda:False)
for b in B:
    Bdict[b] = True

for i in range(X+1):
    if DP[i] and not Bdict[i]:
        for j in range(N):
            nextstep = i+A[j]
            if nextstep < X+1:
                DP[nextstep] = True

if DP[X]:
    print("Yes")
else:
    print("No")