N,M = map(int, input().split())
ABCD = []
for _ in range(M):
    ABCD.append(list(input().split()))

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #parent
        self.rank = [0 for _ in range(n)] #root_length
        
    #search the root x belongs
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    #merge groups x and y belong
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        
    #are x and y in the same group?
    def same(self, x, y):
        return self.find(x) == self.find(y)
# cant divide
# useful for making group

uni = UnionFind(2*N)
# 2*i本目のロープについて、2*iが赤、2*i+1が青
for i in range(N):
    uni.unite(2*i, 2*i+1)
for i in range(M):
    A = 2 * (int(ABCD[i][0])-1)
    C = 2 * (int(ABCD[i][2])-1)
    if ABCD[i][1] == "B":
        A+=1
    if ABCD[i][3] == "B":
        C+=1
    uni.unite(A,C)

dic = {}
for i in range(M):
    prev = "".join(ABCD[i][:2])
    lat = "".join(ABCD[i][2:])
    dic[prev] = lat
    dic[lat] = prev

from collections import defaultdict
mask = defaultdict(lambda: [])
for i in range(N):
    ind = 2*i
    mask[uni.find(ind)].append(i+1)
X,Y = 0,0
for key in mask:
    lo = mask[key]
    # print(lo)
    temp = str(lo[0])+"R"
    flag = False
    while temp in dic:
        temp = dic[temp]
        #print(temp)
        if temp == str(lo[0])+"B":
            flag = True
            break
        if temp[-1] =="R":
            temp = temp[:-1]+"B"
        elif temp[-1] == "B":
            temp = temp[:-1]+"R"
    if flag:
        X+=1
    else:
        Y+=1


print(X,Y)
