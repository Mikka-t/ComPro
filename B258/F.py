T = int(input())

for i in range(T):
    B,K,Sx,Sy,Gx,Gy = map(int, input().split())
    if (Sx <= B and B <= Gx) or (Gx <= B and B <= Sx):
        if (Sy <= B and B <= Gy) or (Gy <= B and B <= Sy):
            time_pat = []
            time = abs(Sy-B)*K + abs(Sx-B) + abs(Gy-B) + abs(Gx-B)*K
            time_pat.append(time)
            time = abs(Sx-B)*K + abs(Sy-B) + abs(Gx-B) + abs(Gy-B)*K
            time_pat.append(time)
            time = abs(Sx-B)*K + abs(Sy-B) + abs(Gy-B) + abs(Gx-B)*K
            time_pat.append(time)
            time = abs(Sy-B)*K + abs(Sx-B) + abs(Gx-B) + abs(Gy-B)*K
            time_pat.append(time)
            print(min(time_pat))
        else:
            time = abs(Sx-Gx)*K + abs(Sy-Gy)
            print(time)
    else:
        if (Sy <= B and B <= Gy) or (Gy <= B and B <= Sy):
            time = abs(Sx-Gx) + abs(Sy-Gy)*K
            print(time)
        else:
            time_pat = []
            time = (abs(Sx-Gx) + abs(Sy-Gy))*K
            time_pat.append(time)
            time = abs(Sx-Gx) + (abs(Sy-B) + abs(Gy-B))*K
            time_pat.append(time)
            time = abs(Sy-Gy) + (abs(Sx-B) + abs(Gx-B))*K
            time_pat.append(time)
            print(min(time_pat))
