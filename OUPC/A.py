A,B,N = map(int, input().split())

card_sum = B-A+1
nums = {}
min = 10000000
max = 0
answered = False
if card_sum >= N:
    for i in range(N):
        if (A+i)%N not in nums:
            nums[(A+i)%N] = 1
        else:
            nums[(A+i)%N] += 1
    for i in nums:
        nums[i] *= card_sum//N

for i in range(1,(card_sum)%N+1):
    if i not in nums:
        nums[i] = 1
    else:
        nums[i] += 1


for i in range(N):
    if not answered:
        if i not in nums:
            min = 0
            answered = True
        else:
            if nums[i] < min:
                min = nums[i]
    if i in nums:
        if nums[i]>max:
            max = nums[i]

print(min,max)
        