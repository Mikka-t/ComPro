h1,h2,h3,w1,w2,w3 = map(int, input().split())
h1 -= 3
h2 -= 3
h3 -= 3
w1 -= 3
w2 -= 3
w3 -= 3
count = 0
#1 3 a
#2 4 b
#c d e
for hoge1 in range(31):
    for hoge2 in range(31):
        for hoge3 in range(31):
            for hoge4 in range(31):
                a = h1-hoge1-hoge3
                b = h2-hoge2-hoge4
                c = w1-hoge1-hoge2
                d = w2-hoge3-hoge4
                e1 = h3-c-d
                e2 = w3-a-b
                e = e1
                if e1 == e2 and hoge1+hoge3<=h1 and hoge2+hoge4<= h2:
                    if hoge1+hoge2<=w1 and hoge3+hoge4<=w2:
                        if a>=0 and b>=0 and c>=0 and d>=0 and e>=0:
                            count += 1

print(count)




#h1 -= 3
#h2 -= 3
#h3 -= 3
#w1 -= 3
#w2 -= 3
#w3 -= 3
#
#def sum(k):
#    return (k*(k+1))//2
#
#n11 = min(h1,w1)
## if n11 is Constant?
#for i in range(n11):
#    n12 = min(h1-n11, w2)