H,W = map(int, input().split())
C = []
for _ in range(H):
    C.append(list(input()))

ans = [0]*W
for i in range(H):
    for j in range(W):
        if C[i][j] == '#':
            ans[j]+=1
for i in range(len(ans)):
    ans[i] = str(ans[i])
print(" ".join(ans))