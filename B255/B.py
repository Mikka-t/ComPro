
N,K = map(int, input().split())
A = list(map(int, input().split()))
human = []
for i in range(N):
    human.append( list(map(int, input().split())) )

R = 0
for i in range(N):
    if i+1 not in A:
        # no torches
        temp2 = float('inf')
        for j in range(K):
            # distance^2 to every torches
            temp = pow(human[i][0] - human[A[j]-1][0],2)+pow(human[i][1] - human[A[j]-1][1],2)
            if temp2 > temp:
                temp2 = temp # biggest r^2
        if R < temp2:
            R = temp2
print(pow(R,1/2))
            
    
            

