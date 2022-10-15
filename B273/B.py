X,K = map(int, input().split())
ans = X
def my_round(val, digit):
    p = str(val)
    if p[-digit] in ["0","1","2","3","4"]:
        if len(p)==digit:
            p = "0"+"0"*digit
        else:
            if digit != 1:
                p = p[:-digit] + "0" +p[-digit+1:]
            else:
                p = p[:-1] + "0"
    else:
        if len(p)==digit:
            p = "1"+"0"*digit
        else:
            if digit != 1:
                p = p[:-digit] + "0" +p[-digit+1:]
            else:
                p = p[:-1] + "0"
            p = str(int(p)+pow(10,digit))
    return p

for i in range(K):
    ans = my_round(ans, i+1)

    # print(ans)
print(int(ans))