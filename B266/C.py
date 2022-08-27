A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
flag = True
square = [A,B,C,D]
for i in range(4):
    if square[i][0]-square[(i+1)%4][0] == 0:
        line = float('inf')
    else:   
        line = (square[i][1]-square[(i+1)%4][1])/(square[i][0]-square[(i+1)%4][0])
    temp1 = line*(square[(i+2)%4][0]-square[(i+1)%4][0]) > square[(i+2)%4][1]-square[(i+1)%4][1]
    temp2 = line*(square[(i+3)%4][0]-square[(i+1)%4][0]) > square[(i+3)%4][1]-square[(i+1)%4][1]
    if temp1 ^ temp2:
        flag = False
if flag:
    print("Yes")
else:
    print("No")