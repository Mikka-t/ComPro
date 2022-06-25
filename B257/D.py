
# i から j に飛ぶときの距離/ジャンプ台パワーがjump,Sがこれより大きければいい

import math
N = int(input())
INF = float('inf')
cost = []
jumps = [[INF]*N for _ in range(N)]

for i in range(N):
    x,y,p = map(int, input().split())
    cost.append([x,y,p])
for i in range(N):
    for j in range(N):
        if i != j:
            jumps[i][j] = (abs(cost[i][0]-cost[j][0])+abs(cost[i][1]-cost[j][1])) / cost[i][2]
            # i to j
        else:
            jumps[i][j] = 0

# for i in range(N):
#     print(jumps[i])



def warshall_floyd(d, V): 
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], max(d[i][k] , d[k][j]))
    
    return d
# d[i][j] to get the path between i and j

D = warshall_floyd(jumps, N)

costie = INF
for i in range(N):
    temp = max(D[i])
    # print(temp)
    if costie > temp:
        costie = temp
print(math.ceil(costie))
# for i in range(N):
#     print(D[i])






# 2点の距離/始点のパワーPi <= S
# 2点のコストがこれ、有向
# 適切なジャンプ台からどのジャンプ台にも行けるようにする　どこか1台からでもいけたらそれでいい