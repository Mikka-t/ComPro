N,Q,X = map(int, input().split())
W = list(map(int, input().split()))

#繰り越される数
weigh = 0
for i in range(N):
    weigh += W[i]
    if weigh >= X:
        weigh = 0
# weighははじめのN個詰めて余ったおもさ　


# 10^100個
# N個ごとに同じ重さ
# N個目で総和X以上になったら繰り返せる
# ならなかったら何個が入っている？何kgが繰り越された？
# 箱に入ってる個数の数列欲しい