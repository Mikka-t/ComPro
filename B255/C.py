X,A,D,N = map(int, input().split())
num_max = A+D*(N-1)
if D>0:
    if A<=X and X<=num_max:
        X-=A
        temp = abs(X)%abs(D)
        print(min(abs(temp), abs(D-temp)))
    elif A < X:
        print(abs(num_max-X))
    else:
        print(abs(A-X))
elif D<0:
    if A>=X and X>=num_max:
        X-=A
        temp = abs(X)%abs(D)
        print(min(abs(temp), abs(abs(D)-temp)))
    elif A < X:
        print(abs(A-X))
    else:
        print(abs(num_max-X))
else:
    print(abs(X-A))

# X+=1 か X-=1 をanswer回繰り返し
# Xが　初項A 交差D 項数Nの等差数列Sに含まれるようにする

# Xと等差数列Sに含まれる任意の数の最小距離answer
# Sの最大値A+D(N-1)