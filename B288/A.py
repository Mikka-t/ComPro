N = int(input())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))

for ab in AB:
    print(sum(ab))
