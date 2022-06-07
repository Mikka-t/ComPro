N = int(input())
import numpy as np

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

for i in range(N):
    i_arr = np.array(factorization(i))
    if all(i_arr[x][1] % 2 == 0 for x in range(i_arr.shape[0])):


        


