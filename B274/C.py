N = int(input())
A = list(map(int, input().split()))

ans = [0]*(2*N+2)
for i in range(N):
    ans[2*(i+1)] = ans[A[i]] + 1
    ans[2*(i+1)+1] = ans[A[i]] + 1    
for i in range(1,len(ans)):
    print(ans[i])