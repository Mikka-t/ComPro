N,M,X,T,D = map(int, input().split())

start = T-X*D
ylist = []
year = start
ylist.append(year)
for i in range(X):
    year += D
    ylist.append(year)

if M <= X:
    ret = ylist[M]
else:
    ret = ylist[-1]
print(ret)

# N さい Tcm
# X さい stop
# M さい ycm
# 0,1,...,X Dcm



