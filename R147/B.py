N = int(input())
P = list(map(int, input().split()))

thres = N//2
ans = ""
noodd = 0
noeve = 0
count = 0


for i in range(N):
    if i%2 == 0:
        if P[i]%2 == 0:
            noodd += 1
    else:
        if P[i]%2 == 1:
            noeve += 1

temp_tar = 1
for _1 in range(noodd):
    flag = True
    while flag:
        for j in range(N-1):
            # print(P)
            if (j%2==1 and P[j]%2==1 and P[j+1]%2==0) or (j%2==0 and P[j]%2==0 and P[j+1]%2==1):
                ans+=f"A {j+1}\n"
                count += 1
                temp = P[j]
                P[j] = P[j+1]
                P[j+1] = temp
                flag = False
                break
        if flag:
            index = P.index(temp_tar)
            if index+2>N-1:
                temp_tar = (temp_tar + 2)%thres + 2 
            else:
                temp = P[index]
                P[index] = P[index+2]
                P[index+2] = temp
                ans += f"B {index+1}\n"
                count += 1
                temp_tar = (temp_tar + 2)%thres + 3

# odd
i = 0
while i < (N//2 + N%2):
    # print(P)
    # print(i)
    target = 2*i + 1
    # print(target)
    index = P.index(target)
    # print(index)
    if index != target-1:
        temp = P[index]
        P[index] = P[index-2]
        P[index-2] = temp
        ans += f"B {index-2+1}\n"
        count += 1
    else:
        i += 1

# even
i = 0
while i < N//2:
    target = 2*i+2
    index = P.index(target)
    if index != target-1:
        temp = P[index]
        P[index] = P[index-2]
        P[index-2] = temp
        ans += f"B {index-2+1}\n"
        count += 1
    else:
        i += 1

print(count)
print(ans)


