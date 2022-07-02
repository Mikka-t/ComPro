N,X = map(int, input().split())
game=[]
for i in range(N):
    game.append(list(map(int, input().split())))

progress_time=0

min_time = float('inf')
for i in range(N):
    progress_time += game[i][0]+game[i][1]
    if X-i-1<0:
        break
    this_time = progress_time + game[i][1]*(X-i-1)
    if this_time < min_time:
        min_time = this_time
print(int(min_time))







# 1回目：a1+b1
# 2回目: a1+b1+b1 or a1+b1+a2+b2
# 3回目: a1+b1+b1+b1 or a1+b1+a2+b2+b2 or a1+b1+a2+b2+a3+b3