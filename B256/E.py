N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))

Count = 0
for i in range(N):
    if i+1 == X[X[X[i]-1]-1]:
        Count += min(C[i],C[X[i]-1],C[X[X[i]-1]-1])
print(Count)
Count = Count//3
print(Count)