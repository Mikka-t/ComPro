N=int(input())
S = input()
W = list(map(int, input().split()))

human=[]
for i in range(N): 
    human.append([W[i],int(S[i])])
human.sort()

for i in range(N):
    if i == 0:
        human[i].append(1-human[i][1]) #child is 1
        human[i].append(human[i][1]) #adult is 1
    elif human[i][1] == 0:
        human[i].append(human[i-1][2]+1)
        human[i].append(human[i-1][3])
    elif human[i][1] == 1:
        human[i].append(human[i-1][2])
        human[i].append(human[i-1][3]+1)
ans = 0
i = 0
while i < len(human):
    flag = 0
    if i < len(human)-1:
        if human[i][0]==human[i+1][0]:
            flag = 1
    if flag != 1:
        temp = human[i][2]+(human[-1][3]-human[i][3])
        if temp>ans:
            ans = temp
    i += 1
if human[-1][3] > ans:
    ans = human[-1][3]
elif human[-1][2] > ans:
    ans = human[-1][2]
print(ans)












# W: 体重
# S: adult or child N人 1がおとな0子供
# 体重X未満子供
# Xをさだめて正しく判定できる人数の最大値