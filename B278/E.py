
H,W,N,h,w = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

loc = {}
for i in range(H):
    for j in range(W):
        tar = A[i][j]
        if tar not in loc:
            loc[tar] = []
        loc[tar].append([i,j])


ans = [[0]*(W-w+1) for _ in range(H-h+1)]
for k in range(0, H-h+1):
    for l in range(0, W-w+1):
        ans_temp = 0
        for i in loc:
            for j in range(len(loc[i])):
                loc_temp = loc[i][j]
                loc_temp0 = loc_temp[0]
                loc_temp1 = loc_temp[1]
                if loc_temp0<k or k+h-1<loc_temp0 or loc_temp1<l or l+w-1<loc_temp1:
                    ans_temp += 1
                    break
        ans[k][l] = str(ans_temp)

for i in range(len(ans)):
    print(" ".join(ans[i]))