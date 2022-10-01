import sys

sys.setrecursionlimit(2000)

N,S = map(int, input().split())
ab = []
for _ in range(N):
    ab.append(list(map(int, input().split())))

ans = ""
sum = 0
step = [0]*N
i = 0
flag = False
while not flag:
    print(step)
    print(i)
    if step[i] == 0:
        step[i]=1
        ans = ans+"H"
        sum += ab[i][0]
        i+=1
        if i == N:
            if sum == S:
                flag = True
                break
            i -= 1
            ans = ans[:-1]
            sum -= ab[i][0]
            

    elif step[i] == 1:
        step[i] = 2
        ans = ans+"T"
        sum += ab[i][1]
        i+=1
        if i == N:
            if sum == S:
                flag = True
                break
            i -= 1
            ans = ans[:-1]
            sum -= ab[i][1]
    elif step[i] == 2 and i == 0:
        break
    elif step[i]==2:
        count = i
        while count < N:
            step[count]=0
            count += 1
        i -= 1
        ans = ans[:-1]
        sum -= ab[i+1]

if flag:
    print("Yes")
    print(ans)
else:
    print("No")