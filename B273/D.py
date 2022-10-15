H,W,rs,cs = map(int, input().split())
N = int(input())
rc = []
dl = []
for _ in range(N):
    rc.append(list(map(int, input().split())))
Q = int(input())
for _ in range(Q):
    temp = list(input().split())
    dl.append([temp[0], int(temp[1])])

wall_H = [[]]*H
wall_W = [[]]*W
# print(rc)
for i in range(N):
    wall_H[rc[i][0]-1] = wall_H[rc[i][0]-1]+ [rc[i][1]]
    wall_W[rc[i][1]-1] = wall_W[rc[i][1]-1]+ [rc[i][0]]
print(wall_H)
print(wall_W)

now = [rs,cs]
for i in range(Q):
    if dl[i][0] == "L":
        direct = [0,-1]
        temp = max(0,now[1]-dl[i][1]-1)
        for j in wall_H[now[0]-1]:
            if now[1]-dl[i][1] < j and j < now[1]:
                if temp < j:
                    temp = j
        print(now, dl[i], temp, "temp")
        now = [now[0], temp+1]
    elif dl[i][0] == "R":
        direct = [0,1]
        temp = min(W+1,now[1]+dl[i][1]+1)
        for j in wall_H[now[0]-1]:
            if now[1]+dl[i][1] > j and j > now[1]:
                if temp > j:
                    temp = j
        print(now, dl[i], temp, "temp")
        now = [now[0], temp-1]
    elif dl[i][0] == "U":
        direct = [-1,0]
        temp = max(now[0]-dl[i][1]-1,0)
        for j in wall_W[now[1]-1]:
            print(j)
            if now[0]-dl[i][1] < j and j < now[0]:
                if temp < j:
                    temp = j
        print(now, dl[i], temp, "temp")
        now = [temp+1, now[1]]
    elif dl[i][0] == "D":
        direct = [1,0]
        temp = min(now[0]+dl[i][1]+1,H+1)
        for j in wall_W[now[1]-1]:
            if now[0]+dl[i][1] > j and j > now[0]:
                if temp > j:
                    temp = j
        print(now, dl[i], temp, "temp")
        now = [temp-1, now[1]]
    print(f"{now[0]} {now[1]}")

