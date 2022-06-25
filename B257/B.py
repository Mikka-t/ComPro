N,K,Q=map(int, input().split())

A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(Q):
    if A[L[i]-1]==N:
        pass
    else:
        if A[L[i]-1]==A[-1]:
            A[L[i]-1]+=1
        elif A[L[i]]-A[L[i]-1]>1:
            A[L[i]-1]+=1
    A.sort()

ans = ""
for i in range(K):
    ans+=str(A[i])
    if i != K-1:
        ans+=" "
print(ans)














# 1 2 3 ,,,N
# i番目の駒はマスAi
# Q回
# 