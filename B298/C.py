N = int(input())
Q = int(input())

query = []
for _ in range(Q):
    query.append(list(map(int, input().split())))

from collections import defaultdict

boxes = defaultdict(lambda: [])
cards = defaultdict(lambda: [])

import bisect

for qu in query:
    if qu[0] == 1:
        if qu[2] not in cards[qu[1]]:
            bisect.insort(cards[qu[1]], qu[2])
        bisect.insort(boxes[qu[2]], qu[1])
    elif qu[0] == 2:
        print(" ".join([str(x) for x in boxes[qu[1]]]))
    elif qu[0] == 3:
        print(" ".join([str(x) for x in cards[qu[1]]]))
    


