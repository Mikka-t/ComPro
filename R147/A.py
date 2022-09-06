import heapq
N = int(input())
A = list(map(lambda x:int(x)*(-1), input().split()))

heapq.heapify(A)

ans = 0
count = len(A)
Amin = max(A)

while count != 1:
    temp = -((-heapq.heappop(A)) % (-Amin))
    ans += 1
    if temp == 0:
        count -= 1
    elif temp > Amin:
        Amin = temp
        heapq.heappush(A, temp)
    else:
        heapq.heappush(A, temp)

print(ans)