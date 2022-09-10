N = int(input())
P = list(map(int, input().split()))
dist = [0]*N
for i in range(N):
    dist[abs(P[i]-i)]+=1
ans = 0
count = 0
for i in range(len(dist)-2):
    count = dist[i]+dist[i+1]+dist[i+2]
    if count >ans:
        ans = count
count = dist[-1]+dist[0]+dist[1]
if count >ans:
        ans = count
print(ans)


