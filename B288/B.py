N,K = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

Ssub = sorted(S[:K])
for i in Ssub:
    print(i)