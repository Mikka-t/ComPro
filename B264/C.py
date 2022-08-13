H1,W1 = map(int, input().split())
A = []
for _ in range(H1):
    A.append(list(map(int, input().split())))

B = []
ifs = []
H2,W2 = map(int, input().split())
for _ in range(H2):
    temp = list(map(int, input().split()))
    B.append(temp)
for i in range(W1):
    for j in range(H1):
        if A[j][i]==B[0][0]:
            ifs.append([j,i])

flag = False
flag2 = True

for index in ifs:
    B_j = 0
    for j in range(H1-index[0]):
        # 1行分
        B_i = 0
        i_s = []
        flag2 = True
        for i in range(W1-index[1]):
            if A[index[0]+j][index[1]+i]==B[B_j][B_i]:
                B_i += 1
                i_s.append(index[1]+i)
                if B_i >= W2:
                    break

    
    
        if B_j != 0 and B_i >= W2:
            if prev_i_s != i_s:
                flag2 = False

        if B_i >= W2 and flag2:
            B_j += 1
            prev_i_s = i_s
            if B_j >= H2:
                break

    if B_j >= H2 and flag2:
        flag = True
        break

if H1 < H2 or W1 < W2:
    flag = False

if flag:
    print("Yes")
else:
    print("No")

# Aの列と行をいくらでも消してBにする
