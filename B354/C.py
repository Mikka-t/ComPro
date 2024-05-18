N = int(input())
chal = []
for i in range(N):
    chal.append(list(map(int, input().split())))
    chal[-1].append(str(i+1))

idx_memo_ans = set()


chal_tmp = sorted(chal, reverse=True)

while True:
    cnt = 0
    idx_memo = set([])
    chal_tmp = sorted(chal_tmp, reverse=True)
    cost_min = [float('inf')] * len(chal_tmp)
    cost_min[0] = chal_tmp[0][1]

    for i in range(1,len(chal_tmp)):
        if chal_tmp[i][1] <= cost_min[i-1]:
            cost_min[i] = chal_tmp[i][1]
        else:
            cost_min[i] = cost_min[i-1]
            cnt += 1
            idx_memo.add(chal_tmp[i][2])
    idx_memo_ans = idx_memo_ans.union(idx_memo)   
    #print(cost_min)
    #print(idx_memo)
    #print(chal_tmp)
    chal_tmp = [row for i, row in enumerate(chal_tmp) if chal_tmp[i][2] not in idx_memo]


    if cnt ==0:
        break

# print(idx_memo_ans,"ans")

# print(cost_min)
# print(idx_memo)
ans = sorted([chal[i][2] for i in range(N) if chal[i][2] not in idx_memo_ans])
print(len(ans))
print(" ".join(ans))
