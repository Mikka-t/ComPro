import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
 
def prime_decomposition(n):
    i = 2
    table = defaultdict(int)
    while i * i <= n:
        while n % i == 0:
            n //= i
            table[i] += 1
        i += 1
    if n > 1:
        table[n] += 1
    return table
 
 
n = int(readline())
prime_list = prime_decomposition(n)
ans = 1
memo = 1
for k, v in prime_list.items():
    for i in range(1, v + 1):
        memo = k * i
        while memo % k == 0:
            v -= 1
            memo //= k
        if v <= 0:
            if ans < k * i:
                ans = k * i
            break
print(ans)