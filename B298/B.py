N = int(input())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))

A1 = A
A2, A3, A4 = [[-1]*N for _ in range(N)], [[-1]*N for _ in range(N)], [[-1]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        a = A[i][j]
        A2[N-1-j][i] = a
        A3[N-1-i][N-1-j] = a
        A4[j][N-1-i] = a

isa1, isa2, isa3, isa4 = True, True, True, True
for i in range(N):
    for j in range(N):
        b = B[i][j]
        a1 = A[i][j]
        a2 = A2[i][j]
        a3 = A3[i][j]
        a4 = A4[i][j]

        if b == 0 and a1 == 1:
            isa1 = False
            #print(i,j)
        if b == 0 and a2 == 1:
            isa2 = False
            #print(i,j)
        if b == 0 and a3 == 1:
            isa3 = False
            #print(i,j)
        if b == 0 and a4 == 1:
            isa4 = False
            #print(i,j)
        
        if not isa1 and not isa2 and not isa3 and not isa4:
            break
    
    if not isa1 and not isa2 and not isa3 and not isa4:
        break
    
#for i in range(N):
#    print("".join([str(x) for x in A2[i]]))
#for i in range(N):
#    print("".join([str(x) for x in A3[i]]))
#for i in range(N):
#    print("".join([str(x) for x in A4[i]]))

#print(isa1, isa2, isa3, isa4)

if not isa1 and not isa2 and not isa3 and not isa4:
    print("No")
else:
    print("Yes")