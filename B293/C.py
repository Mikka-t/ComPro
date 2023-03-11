H,W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

arr = [0]*(H-1) + [1]*(W-1)

ans = 0

for y in range(pow(2,(H+W-2))+1):
    x = bin(y)[2:]
    #print(x)
    temp = len(x)
    while temp < (H-1)+(W-1):
        x = "0"+x
        temp = len(x)
    sum1 = 0
    sum0 = 0
    for test in x:
        if test == "1":
            sum1+=1
        if test == "0":
            sum0+=1
    if sum1 != W-1:
        continue
    if sum0 != H-1:
        continue
    #print(x)
    temp = set([A[0][0]])
    now = [0,0]
    for i in x:
        if i == "0":
            now[0]+=1
        if i == "1":
            now[1]+=1
        # print(now, x)
        if A[now[0]][now[1]] not in temp:
            if (now[0] != H-1) or (now[1] != W-1):
                temp.add(A[now[0]][now[1]])
            elif now[0] == H-1 and now[1] == W-1:
                ans += 1
        else:
            break
print(ans)

