

N = int(input())
LR = []
for i in range(N):
    LR.append(list(map(int, input().split())))

LR.sort()
ans = []
temp_s = LR[0][0]
temp_e = LR[0][1]

for i in range(N):
    if temp_e < LR[i][0]:
        ans.append([temp_s,temp_e])
        temp_s = LR[i][0]
        temp_e = LR[i][1]
    elif temp_e < LR[i][1]:
        temp_e = LR[i][1]
ans.append([temp_s,max(temp_e, LR[N-1][1])])

for a in range(len(ans)):
    temp = list(map(str, ans[a]))
    print(" ".join(temp))
