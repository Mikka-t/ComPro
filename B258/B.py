

N = int(input())
A = []
maxlist = []
maxnum = 0
for i in range(N):
    temp = str(input())
    templist=[]
    for ind in range(len(temp)):
        templist.append(int(temp[ind]))
    A.append(templist)
    for j in range(N):
        if A[i][j]>maxnum:
            maxnum = A[i][j]
            maxlist = [[i,j]]
        elif A[i][j] == maxnum:
            maxlist.append([i,j])


dirlist = [[-1,1],[0,1],[1,1] ,[-1,0],[1,0] ,[-1,-1],[0,-1],[1,-1]]

ansnum = 0
for maxs in maxlist:
    for dir in dirlist:
        ans = ""
        for i in range(N):
            ans+=str(A[(maxs[0]+dir[0]*i)%N][(maxs[1]+dir[1]*i)%N])
        if ansnum < int(ans):
            ansnum = int(ans)

print(ansnum)