N,Q = map(int, input().split())
S = input()

shift = 0
for i in range(Q):
    q,x = map(int, input().split())
    if q == 1:
        shift += x
    elif q == 2:
        print(S[(x-1-shift)%N])