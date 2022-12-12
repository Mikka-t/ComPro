N = int(input())
A = list(map(bin,map(int, input().split())))

eve = []
odd = []

for a in A:
    if a[-1]=="0":
        eve.append(a)
    else:
        odd.append(a)
if len(eve)<2 and len(odd)<2:
    print(-1)
else:
    if len(eve)>=2:
        eves = eve
        for i in range(len(eve)):
            eves[i] = int(eve[i],2)

        evemax1 = max(eves)
        eves.remove(evemax1)
        evemax2 = max(eves)
    else:
        evemax1 = -1
        evemax2 = 0

    if len(odd)>=2:
        odds = odd
        for i in range(len(odd)):
            odds[i] = int(odd[i],2)

        oddmax1 = max(odds)
        odds.remove(oddmax1)
        oddmax2 = max(odds)
    else:
        oddmax1 = -1
        oddmax2 = 0

    print(max(evemax1+evemax2, oddmax1+oddmax2))
