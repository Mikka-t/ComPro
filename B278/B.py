H,M = map(int, input().split())

H = "{0:02d}".format(H)
M = "{0:02d}".format(M)


A = int(H[0])
B = int(H[1])
C = int(M[0])
D = int(M[1])

while True:
    if(int(str(A)+str(C))<24 and int(str(B)+str(D))<60):
        ans = str(int(str(A)+str(B)))+" "+str(int(str(C)+str(D)))
        break
    else:
        if D!=9:
            D+=1
        else:
            if C!=5:
                C+=1
                D=0
            else:
                if A==2 and B==3:
                    A=0
                    B=0
                    C=0
                    D=0
                elif A==2 and B!=3:
                    B+=1
                    C=0
                    D=0
                elif B!=9:
                    B+=1
                    C=0
                    D=0
                else:
                    A+=1
                    B=0
                    C=0
                    D=0
print(ans)
                    