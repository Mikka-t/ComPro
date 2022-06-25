#N = int(input())
N,X = map(int, input().split())

list=[]
for i in range(26):
    for j in range(N):
        list.append(chr(i+65))
print(list[X-1])