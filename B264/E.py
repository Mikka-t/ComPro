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



N,M,E = map(int, input().split())
UVs = []
for _ in range(E):
    UVs.append(list(map(int, input().split())))
Q = int(input())
Xs = []
for _ in range(Q):
    Xs.append(int(input()))

revUVs = []
for i in range(E):
    if i not in Xs:
        revUVs.append(UVs[i])

revans = []

Uni = UnionFind(N+M+1)
for UV in revUVs:
    Uni.unite(UV[0],UV[1])

count = 0
for i in range(N):
    for j in range(M):
        if Uni.same(i,j):
            count += 1
            break
revans.append(count)

for i in range(Q):
    wire = UVs[Xs[-(i+1)]-1]
    if Uni.same(wire[0],wire[1]):
        revans.append(revans[-1])
    else:
        Uni.unite(wire[0],wire[1])
        count = 0
        for i in range(N):
            for j in range(M):
                if Uni.same(i,j):
                    count += 1
                    break
        revans.append(count)
for i in range(Q):
    print(revans[-(i+1)])
