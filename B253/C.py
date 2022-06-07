
Q = int(input())
num_num = {}

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if query[1] not in num_num:
            num_num[query[1]] = 1
        else:
            num_num[query[1]]+=1
    elif query[0] == 2:
        if query[1] in num_num:
            if num_num[query[1]] > query[2]:
                num_num[query[1]] -= query[2]
            else:
                del num_num[query[1]]
    elif query[0] == 3:
        print(int(max(num_num)-min(num_num)))