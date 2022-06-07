import math
N, A, B = map(int, input().split())

def f(N):
    return (N*(N+1))//2

sum = f(N)
sum -= A*f(N//A)
sum -= B*f(N//B)

def gcd(a, b):
    while b:
        temp = a
        a = b
        b = temp % a
    return a

def lcm(a, b):
    return (a * b) // gcd (a, b)

LCMAB= lcm(A,B)

if N >= LCMAB:
    sum += LCMAB*f(N//LCMAB)


print(int(sum))
