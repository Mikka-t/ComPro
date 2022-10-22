N,x,y = map(int, input().split())
A = list(map(int, input().split()))
arr1=[]
arr2=[]
for i in range(N):
    if i %2 == 0:
        arr1.append(A[i])
    else:
        arr2.append(A[i])
"""
arr1 = sorted(arr1)
arr2 = sorted(arr2)
sum1=[arr1[0]]
sum2=[arr2[0]]
for i in range(1,len(arr1)):
    sum1.append( arr1[i] + sum1[i-1])
for i in range(1,len(arr2)):
    sum2.append(arr2[i]+sum2[i-1])
num1 = sum1[-1]//2
num2 = sum2[-1]//2
"""
def equal_part(arr,su2):
    fl = False
    part = [False]*(su2+1)
    for i in range(len(arr)):

        if 0<=arr[i] and arr[i] <= su2:
            part[arr[i]] = True
        if arr[i] < 0 and arr[i] >= -su2:
            part[-arr[i]] = True
        if fl:
            break
        for j in range(len(part)):
            if part[j] and 0<=arr[i]+j and arr[i]+j<=su2:
                part[arr[i]+j] = True
            if part[j] and 0<=arr[i]-j and arr[i]-j<=su2:
                part[arr[i]-j] = True
            if part[su2]:
                fl=True
                break
    return fl

sum1 = sum(arr1[1:])
sum2 = sum(arr2)
flag = False
# arr1 is x dir
if (sum1+x)%2 == 0 and (sum2+y)%2 == 0:
    flag = equal_part(arr1[1:]+[abs(x-arr1[0])],(sum1+x-arr1[0])//2) and equal_part(arr2+[y],(sum2+y)//2)
    print(equal_part(arr1[1:]+[abs(x-arr1[0])],(sum1+x-arr1[0])//2))
    print(arr1[1:], arr2)
    print(equal_part(arr2+[y],(sum2+y)//2))
if flag:
    print("Yes")
else:
    print("No")







