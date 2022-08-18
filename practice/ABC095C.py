A,B,C,X,Y = map(int, input().split())

money = min(X,Y)*min(A+B, 2*C)
if X>Y:
    money += min(A*(X-Y), 2*C*(X-Y))
else:
    money += min(B*(Y-X), 2*C*(Y-X))
print(money)