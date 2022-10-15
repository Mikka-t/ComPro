N = int(input())
A = list(map(int, input().split()))
As = sorted(list(set(A)))
# A = sorted(A)
Ac = {}
Ac[As[-1]] = 0
for i in range(len(As)-1):
    Ac[As[-2-i]] = Ac[As[-1-i]] + 1
ans = [0]*N
for i in range(N):
    ans[Ac[A[i]]] += 1
for i in ans:
    print(i)


