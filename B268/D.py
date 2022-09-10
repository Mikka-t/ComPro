import itertools
N,M = map(int, input().split())
S = []
T = []
length = 0
for i in range(N):
    S.append(input())
    length += len(S[i])
for _ in range(M):
    T.append(input())
T = set(T)

flag = False
for perm in itertools.permutations(S):
    #print(perm)
    count = 0
    lenP = len(perm)
    letters = 16 - length
    for a in range(max(letters,1)):
        for b in range(max(letters-a-1,1)):
            for c in range(max(letters-a-b-2,1)):
                for d in range(max(letters-a-b-c-3,1)):
                    for e in range(max(letters-a-b-c-d-4,1)):
                        for f in range(max(letters-a-b-c-d-e-5,1)):
                            for g in range(max(letters-a-b-c-d-e-f-6,1)):
                                for h in range(max(letters-a-b-c-d-e-f-g-7,1)):
                                    if a+b+c+d+e+f+g+h <= letters:
                                        ans = ""
                                        ans += perm[0]
                                        bars=[a,b,c,d,e,f,g,h]
                                        for i in range(lenP-1):
                                            ans += "_" * (bars[i]+1)
                                            ans += perm[i+1]
                                        if (ans not in T) and len(ans)<=16 and len(ans)>=3:
                                            flag = True
                                            answer = ans
                                            break
                                if flag:
                                    break
                            if flag:
                                break
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break
if flag:
    print(answer)
else:
    print(-1)                
                                    

