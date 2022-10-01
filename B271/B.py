N,Q = map(int, input().split())
arr = []
que = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
for _ in range(Q):
    que.append(list(map(int, input().split())))

for i in range(Q):
    print(arr[que[i][0]-1][que[i][1]])