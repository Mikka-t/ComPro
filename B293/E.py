A,X,M = map(int, input().split())

def euclid(a, b):
    while b:
            a, b = b, a % b
    return a

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

def mod_binary(g, k, n):
    y = 1
    k_b = format(k,'b')
    for i in k_b:
        if i == '1':
            y = ((pow(y,2) % n) * g) % n
        else:
            y = pow(y,2) % n
    return y

def inv(a,n):
    return exEuclid(a,n)[1] % n

def lcm(a,b):
    return (a*b)//euclid(a,b)

r = A%M
temp1 = 1
amari = []
i = 0
while True:
    i+=1
    temp2 = mod_binary(r,i,M)
    amari.append(temp2)
    print(temp2)
    if temp2 == temp1:
        break
print(amari)
sum = 0
for i in amari:
    sum += mod_binary(r,i,M)
sum *= X//len(amari)

for i in range(X%len(amari)):
    sum += mod_binary(r,i,M)
print(sum%M)