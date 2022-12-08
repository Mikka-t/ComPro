K = int(input())
import math
pf={}
temp = K
for i in range(2,int(math.sqrt(temp))+1):
    while temp%i==0:
        pf[i]=pf.get(i,0)+1
        temp//=i
if temp>1:
    pf[temp]=1
ansmax = 1
temp_arr = []
for i in pf:
    if i <= pf[i]:
        ans = i
        count = 1
        while count < pf[i]:
            ans += 1
            temp = ans
            n = temp//i
            count += n
            print(count, n)

    else:
        ans = i+(pf[i]-1)

    if ansmax < ans:
        ansmax = ans
        ind = i
    temp_arr.append([i,ans])
ans = ansmax

temp = 1
temp1 = K//pow(ind,pf[ind])
print(temp1)
for i in range(len(temp_arr)):
    while temp1 < pow(temp_arr[i][0],temp_arr[i][1]) :
        ans += temp_arr[i][0]
        temp*=temp_arr[i][0]
        temp1 = K//(temp*pow(ind,pf[ind]))
    

print(pf)

print(ans)
"""
count = 0
for i in range(100):
    if i %3 == 0:
        print(i, count)
        count += 1
"""