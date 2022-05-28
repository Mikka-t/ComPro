# 002-Encyclopedia
import re


N = int(input())

ans=[]
if int(N%2) == 0:
    for i in range(pow(2,N)):
        count = 0
        for j in range(N):
            if (i>>j) & 1:
                count-=1
            else:
                count+=1
            if(count>0):
                break
        if count == 0:
            ans.append(i)
    if len(ans)!=0:
        for i in list(sorted(ans)):
            a=""
            for j in reversed(range(N)):
                if (i>>j) & 1:
                    a+=")"
                else:
                    a+="("
            print(a)
