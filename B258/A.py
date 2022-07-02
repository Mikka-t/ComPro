#N,X = map(int, input().split())
K = int(input())

de = 21
de += K//60
de = de % 24
minu = K%60
ans = ""
ans += str(de) + ":"
ans += "{0:02d}".format(minu)
print(ans)
