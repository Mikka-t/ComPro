N,K=map(int, input().split())
A = list(map(int, input().split()))

# how many K-1 in N-1 ?
ans = -(-(N-1)//(K-1))
print(ans)