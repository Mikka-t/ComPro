a,b,d = map(int, input().split())
from math import *
r = sqrt(pow(a,2) + pow(b,2))
deg = degrees(atan2(b,a))
deg += d
deg = radians(deg)
ans = [r*cos(deg), r*sin(deg)]
s = str(ans[0]) + " " + str(ans[1])
print(s)