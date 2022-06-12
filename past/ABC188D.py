N, C= map(int, input().split())

days = []
money = 0
daily = 0

for i in range(N):
    a,b,c = map(int, input().split())
    b+=1
    days.append([a,c])
    days.append([b,-c])

days.sort()

for i in range(len(days)-1):
    daily += days[i][1]
    money += (days[i+1][0] - days[i][0]) * min(daily, C)
print(money)
# すぬけ1日C円　1日の始め及び終わりに加入脱退
# サービスN個利用、i個めはai日めの初めからbi日目の終わりまで
# すぬけでない場合i個目のサービス1日ci円