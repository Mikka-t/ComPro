from math import sqrt
# import numpy as np
# from numpy import linalg as LA
def add(arr1,arr2):
    arrA = [0]*3
    for i in range(3):
        arrA[i] = arr1[i] + arr2[i]
    return arrA

def subtract(arr1,arr2):
    arrA = [0]*3
    for i in range(3):
        arrA[i] = arr1[i] - arr2[i]
    return arrA

def norm(arr1):
    ret = 0
    for i in range(3):
        ret += pow(arr1[i],2)
    return sqrt(ret)

def cross(arr1,arr2):
    ret = [0]*3
    ret[0] = arr1[1]*arr2[2]-arr1[2]*arr2[1]
    ret[1] = -arr1[0]*arr2[2]+arr1[2]*arr2[0]
    ret[2] = arr1[0]*arr2[1]-arr1[1]*arr2[0]
    return ret

def div(arr1,num):
    ret = [0]*3
    for i in range(3):
        ret[i] = arr1[i]/num
    return ret

def prod(arr1,num):
    ret = [0]*3
    for i in range(3):
        ret[i] = arr1[i]*num
    return ret

A=  list(map(int, input().split()))
B=  list(map(int, input().split()))
C=  list(map(int, input().split()))
N = int(input())
v = list(map(int, input().split()))


# ref: http://ynomura.pgw.jp/archives/2009/08/20.html

BC =  subtract(C,B)

G = (1+sqrt(5))/2
edge =  norm( subtract(A,C))
AElen = G*edge/2
EDlen = AElen - edge/2
BC_e = div(BC,edge)

D =  div(add(B,C),2)
AD =  subtract(D,A)
ADlen =  norm(AD)
AD_e = div(AD,ADlen)
# AD:ED = ED:(AD_e houkou)HD
# HD = ED^2 / AD
HDlen = pow(EDlen,2) / ADlen
HD = prod(AD_e , HDlen)
HElen = EDlen*AElen/ADlen
# (cr_e houkou)HE:DE = EA:DA
# HE = DE*EA/DA 

AB =  subtract(B,A)
AC =  subtract(C,A)
cr =  prod(cross(AB,AC),(-1))
cr_e = div(cr, norm(cr)) # seikika tyokkou bekutoru

HE = prod(cr_e,HElen)

E =  add( add(D, prod(HD,(-1))), HE)
DE =  subtract(E,D)
DElen =  norm(DE)
DE_e = div(DE,DElen)
AE =  subtract(E,A)
AElen =  norm(AE)
AE_e = div(AE,AElen)

V2 =  add(A,prod(DE_e,edge))
V13mean =  add( add(A,prod(DE_e,(edge/2))), prod(AE_e,(DElen)))
V1 =  add(V13mean, prod(BC_e,AElen))
V3 =  add(V13mean, prod(BC_e,(-1)*AElen))
V4 =  add(A,prod(AE,2))
V5 =  add(V1,prod(AE_e,edge))
V8 =  add(V3,prod(AE_e,edge))
V6 =  add(C,prod(DE_e,(AElen*2)))
V9 =  add(V4,prod(DE_e,edge))
V7 =  add(V6,prod(BC,(-1)))

Vs =   [V1,V2,V3,V4,V5,V6,V7,V8,V9]
for i in range(N):
    ansV = Vs[v[i]-1]
    ans = ""
    for j in range(3):
        ans += str(ansV[j])
        if j != 2:
            ans += " "
    print(ans)
    

"""
import numpy as np
Vs = np.array([V1,V2,V3,V4,V5,V6,V7,V8,V9,A,B,C])
VT = Vs.T

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("x", size = 14)
ax.set_ylabel("y", size = 14)
ax.set_zlabel("z", size = 14)
ax.scatter(VT[0], VT[1], VT[2],s=40, color = "red")

plt.show()
"""
