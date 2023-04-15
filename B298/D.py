Q = int(input())
queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))

S = 1
MOD =  998244353
MODLEN = len(str(MOD))
ROOF = 1000000000
MODMOD=1000000000%MOD
#print(MODMOD,"modmod")
lenS = 0
cnt = 0

for query in queries:
    #print(S+cnt*MOD)
    if query[0] == 1:
        S = 10*S + query[1]
        lenS += 1
        if S >= ROOF:
            S %= MOD
            cnt += 1
        #print(S, 1)

    elif query[0] == 2:
        #S = S%(pow(10,(len(str(S))-1)))

        if lenS < MODLEN:
            S = int(str(S)[1:])
        else:
            S -= MODMOD
            lenS -= 1
        #print(S, 2)
        
    elif query[0] == 3:
        print(S%MOD)
