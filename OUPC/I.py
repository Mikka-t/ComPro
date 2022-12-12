def exEuclid(a,b):
    A = [a,b] # a0, a1
    X = [1,0] # x0, x1
    Y = [0,1] # y0, y1
    while A[1]:
        q = A[0]//A[1]
        A[0], A[1] = A[1], A[0]%A[1]
        X[0], X[1] = X[1], X[0]-q*X[1]
        Y[0], Y[1] = Y[1], Y[0]-q*Y[1]
    return [A[0], X[0], Y[0]]

def inv(a,n):
    return exEuclid(a,n)[1] % n

N,K = map(int, input().split())

mod = pow(10,9)+7
N2 = pow(N,2)
e = 1
# debug = 1
for i in range(N):
    invtemp = inv((N2-i), mod)
    e = (e * ((K-i) * invtemp) % mod) % mod
    # debug *= (K-i)/(N2-i)

# print((2*N+2)*debug)
print(((2*N+2)*e)%mod)




# Y = XZ mod M
# Y/X = Z mod M

# Nの配列を2個用意すればいい？ 毎回全体に1/Nが加算
# m回目に配列のi番目がビンゴる確率は m-1回目までにN-1になる確率×m回目にそこに来る確率
# ((N-b-1)/(N-b))^(m-1-(N-1)) * (1/(N-b))^(N-1) * m-1CN-1  *1/N
# ビンゴ数b　　　むり！逐次的にしないとビンゴするたびにbかわる
# いやいける？


# N^2このうちKこの数字が読み上げられた
# 2N+2本の列は独立？
# 