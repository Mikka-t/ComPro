import sys
sys.setrecursionlimit(10**6)
N = int(input())
TXAs = []
for _ in range(N):
    TXAs.append(list(map(int, input().split())))

TXAs = sorted(TXAs)

loc = 0
time = 0
weigh_best = 0
i = 0
def foo(i,time,loc,weigh_best):
    if i >= N:
        return [i,time,loc,weigh_best]
    elif abs(TXAs[i][1]-loc) <= abs(TXAs[i][0]-time):
        if i == N-1:
            return foo(i+1,TXAs[i][0],TXAs[i][1],weigh_best+TXAs[i][2])
        elif abs(TXAs[i+1][1]-TXAs[i][1]) <= abs(TXAs[i+1][0]-TXAs[i][0]):
            return foo(i+1,TXAs[i][0],TXAs[i][1],weigh_best+TXAs[i][2])
        else:
            temp1 = foo(i+1,TXAs[i][0],TXAs[i][1],weigh_best+TXAs[i][2])
            temp2 = foo(i+2,TXAs[i+1][0],TXAs[i+1][1],weigh_best+TXAs[i+1][2])
            if temp1[3]>temp2[3]:
                return temp1
            else:
                return temp2
    else:
        return foo(i+1,time,loc,weigh_best)

print(foo(i,time,loc,weigh_best)[3])