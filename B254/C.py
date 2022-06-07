N,K = map(int, input().split())

dist = N-K

A = list(map(int, input().split()))

for i in range(min(dist+1,K)):
    #print(i)
    length = (len(A)-i-1)//K
    B = [A[i+x*K] for x in range(length+1)]
    B.sort()
    #print(B)
    for x in range(length+1):
        A[i+x*K]=B[x]
count = 0
#print(A)
for i in range(len(A)-1):
    if A[i]>A[i+1]:
        count = 1
if count == 1:
    print("No")
else:
    print("Yes")