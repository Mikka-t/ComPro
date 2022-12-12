import sys

sys.setrecursionlimit(200000000)
N,X,Y = map(int, input().split())
UV = []
for _ in range(N+1):
    UV.append([0])
for _ in range(N-1):
    U,V = map(int, input().split())
    UV[U].append(V)
    UV[V].append(U)
#print(UV)
def dfs(now, flag, ans, parent):
    children = UV[now]
    for i in children:
        if i == Y:
            flag = True
            ans.append(i)
            #print("found")
            return [i,flag,ans]
        else:
            if i == 0 or i == parent:
                pass
            else:
                ret = dfs(i,flag,ans,now)
                if ret != None:
                    if ret[1]:
                        ans = ret[2]
                        ans.append(i)
                        return [ret[0],ret[1],ans]

ret = dfs(X,False,[],0)
if ret != None:
    ret[2].append(X)
else:
    ret = [0,True,[X]]
st = ""
if ret[1]:
    for i in ret[2]:
        st = " " + str(i) + st
print(st[1:])