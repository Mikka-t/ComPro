H,W = map(int, input().split())
S=[]
count = 0
for _ in range(H):
    S.append(input())
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            count += 1
print(count)