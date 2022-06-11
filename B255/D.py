import bisect


N,Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ARR = [0]*(N+1)
ARR[0] = 0
for i in range(N):
    ARR[i+1] = ARR[i] + A[i]



for i in range(Q):
    count = 0
    X = int(input())
    index = bisect.bisect_left(A, X)
    count+= abs(ARR[index] - index*X)
    count+= abs(ARR[N]-ARR[index] - (N-index)*X)
    print(count)


"""
import bisect
def bitree_index(list, x):
    return bisect.bisect_left(list,x)
# (list, x, 0, n) to search for index(0-n)
# this list is sorted
list.insert(bitree_index(list,x))
"""

"""
for i in range(Q):
    count = 0
    X = int(input())
    for j in range(N):
        count += abs(A[j]-X)
    print(count)
"""
# 数列AのどれかAiに+=1 か -=1する
# i番目の質問:answer回使ってAの要素を全てXiにする