N = int(input())
sx,sy,tx,ty = map(int, input().split())

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

C = UnionFind(N)
circle = []
for i in range(N):
    circle.append(list(map(int, input().split())))
for i in range(len(circle)):
    for j in range(i+1, len(circle)):
        dist = pow(circle[i][0]-circle[j][0],2)+pow(circle[i][1]-circle[j][1],2)
        if dist <= pow(circle[i][2]+circle[j][2],2) and dist >= pow(abs(circle[i][2]-circle[j][2]),2):
            C.unite(i,j)

for i in range(len(circle)):
    dist = pow(circle[i][0]-sx,2)+pow(circle[i][1]-sy,2)
    if round(dist, 6) == pow(circle[i][2],2):
        s_cir = i
    dist = pow(circle[i][0]-tx,2)+pow(circle[i][1]-ty,2)
    if round(dist, 6) == pow(circle[i][2],2):
        t_cir = i

if C.same(s_cir, t_cir):
    print("Yes")
else:
    print("No")
