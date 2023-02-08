N,M = map(int, input().split())
AB = []
for _ in range(M):
    AB.append(list(map(int, input().split())))


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

Uni = UnionFind(N+1)
edges = []

for i in AB:
    if Uni.same(i[0],i[1]):
        edges.append(i)
    else:
        Uni.unite(i[0],i[1])
print(len(edges))
