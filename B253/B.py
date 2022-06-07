H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(input())
koma = [[0,0],[0,0]]
count = 0
for i in range(H):
    for j in range(W):
        if (S[i][j]=="o"):
            koma[count][0]=i
            koma[count][1]=j
            count+=1
        if count == 2:
            break
    if count==2:
        break
ans=0
ans+=abs(koma[0][0]-koma[1][0])
ans+=abs(koma[0][1]-koma[1][1])
print("{}".format(ans))