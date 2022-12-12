S = input()
T = input()
if len(S)> len(T):
    print("No")
else:
    flag = False
    sl = ""
    prev = ""
    preprev = ""
    j = 0
    for i in range(len(S)):
        if S[i] == T[j]:
            j += 1
            preprev = prev
            prev = S[i]
        elif preprev == prev and T[j] == prev:
            while T[j] == prev:
                j += 1
            if S[i] == T[j]:
                j += 1
                preprev = prev
                prev = S[i]
            else:
                flag = True
        else:
            flag = True

    prev = ""
    preprev = ""
    if S[-1] != T[-1]:
        flag = True
    elif len(S)>1 and len(T)>1:
        if S[-2] != T[-2]:
            flag = True


    if flag:
        print("No")
    else:
        print("Yes")

# 同じ文字にれんぞく＝同じ文字ひとつ挿入
# S==T?