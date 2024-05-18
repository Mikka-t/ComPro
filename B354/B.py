N = int(input())
chal = []
T = 0
for i in range(N):
    chal.append(list(input().split()))
    T += int(chal[-1][1])

chal = sorted(chal)
ans = chal[T%N][0]
print(ans)

