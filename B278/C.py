
N,Q = map(int, input().split())
TAB = []
for _ in range(Q):
    TAB.append(list(map(int, input().split())))

follow = {}

for tab in TAB:
    T = tab[0]
    A = str(tab[1]-1)
    B = str(tab[2]-1)
    if T==1:
        follow[A+"_"+B] = True
    elif T==2:
        follow[A+"_"+B] = False
    elif T==3:
        if follow.get(A+"_"+B, False) and follow.get(B+"_"+A, False):
            print("Yes")
        else:
            print("No")
