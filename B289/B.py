
N,M = map(int, input().split())
A = list(map(int, input().split()))

ans = []
ind = 0
tmp = []
for i in range(N):
    if ind == len(A):
        break
    else:
        if A[ind]-1 == i:
            if len(tmp) == 0:
                tmp.append(A[ind])
            tmp.append(A[ind]+1)
            ind += 1
            # print(tmp)
        else:
            ans = ans + tmp[::-1]
            if len(tmp) == 0:
                ans.append(i+1)
            tmp = []
            # print(tmp)
if len(tmp) != 0:
    ans = ans + tmp[::-1]
if len(ans) != N:
    ans = ans + list(range(len(ans)+1,N+1))
ans = [str(x) for x in ans]
print(" ".join(ans))