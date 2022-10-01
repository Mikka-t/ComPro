N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
limit = 2*N
j=0
donthave = 0
doub = 0
for i in range(len(A)-1):
    if A[i] == A[i+1]:
        doub += 1
As = set(A)


for i in range(1,limit):
    if i in As:
        j+=1
    else:
        donthave += 1
    if j + donthave*2 == N:
        ans = j+donthave
        break
    elif j + donthave*2 > N:
        ans = j+donthave-1
        break
print(ans)



# 学び:　二次元配列にして、i枚目時点で合計jにできるよという配列をboolでつくる
# するとN枚目時点で合計Sにできるかできないかという結果がでる
# できることが分かるなら、逆順に、N-aとN-bで存在する方を辿っていけばいい