N,M = map(int, input().split())

kx = []
for _ in range(M):
    kx.append(list(map(int, input().split())))
ans = True
flag = True
for i in range(N):
    if i != 0:
        for j in range(N):
            if j != 0:
                flag = False
                for k in range(M):
                    if i in kx[k][1:] and j in kx[k][1:]:
                        flag = True
                        break
                # print(flag, i, j)
                if not flag:
                    ans = False
                    break
            if not flag:
                ans = False
                break

if ans:
    print("Yes")
else:
    print("No")        