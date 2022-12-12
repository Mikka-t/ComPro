from math import sqrt, ceil
N,M = map(int, input().split())

movable = []

ans = [[-1]*N for i in range(N)]
counted = [[0,0]]
next_counted = []
count = 1
ans[0][0] = 0

ranges = []
for i in range(ceil(sqrt(M))+1):
    for j in range(ceil(sqrt(M))+1):
        if pow(i,2)+pow(j,2) == M:
            ranges.append([i,j])
            ranges.append([-i,j])
            ranges.append([i,-j])
            ranges.append([-i,-j])
# print(ranges)
while True:
    # print(ans)
    for now in counted:
        for move in ranges:
            i = now[0]+move[0]
            j = now[1]+move[1]
            if 0<=i and i<N and 0<=j and j<N:
                if ans[i][j] == -1:
                    ans[i][j] = ans[now[0]][now[1]] + 1
                    count += 1
                    next_counted.append([i,j])
    counted = next_counted
    next_counted = []
    if len(counted)==0:
        break

for bruh in ans:
    bruhbruh = list(map(str,bruh))
    print(" ".join(bruhbruh))


                


