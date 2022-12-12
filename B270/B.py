X,Y,Z = map(int, input().split())

if (X<Y and Y<0) or (X>Y and Y>0):
    if (Z<Y and Y<0) or (Z>Y and Y>0):
        dist = -1
    else:
        dist = abs(Z) + abs(Z-X)
else:
    dist = abs(X)
print(dist)

