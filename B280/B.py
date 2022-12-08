N = int(input())
S = list(map(int, input().split()))

for i in range(N):
    if i==0:
        A = [S[i]]
    else:
        A.append(S[i]-sum(A))
A =map(str,A)
print(" ".join(A))