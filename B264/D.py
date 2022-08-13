S = input()

a = S.find('a')
t = S.find('t')
c = S.find('c')
o = S.find('o')
d = S.find('d')
e = S.find('e')
r = S.find('r')
arr = [a,t,c,o,d,e,r]
count = 0
for letter in arr:
    count += letter
    for i in range(7):
        if arr[i] > letter:
            arr[i] -= 1
print(count)