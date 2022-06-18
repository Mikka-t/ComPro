N = int(input())
A = list(map(int, input().split()))

temp=[]
for i in A:
    for j in range(len(temp)):
        temp[j] += i
    temp.append(i)

count = 0

for i in temp:
    if i >= 4:
        count+=1
print(count)




# 0, 1, 2, 3
# P=0
# 0にコマを1個おく
# 全てのコマを+Ai大きいマスにすすめる。
# x+Ai>=4ならPに+1する