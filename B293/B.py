N = int(input())
X = list(map(int, input().split()))

mask = [False]*N

for i in range(N):
    if mask[i] == False:
        mask[X[i]-1] = True
not_called = []
for i in range(N):
    if mask[i] == False:
        not_called.append(i+1)
not_called.sort()
print(len(not_called))
print(" ".join([str(x) for x in not_called]))
