A,B,C = map(int, input().split())
A = A % 10

if A == 5 or A == 6 or A == 0 or A == 1:
    print(A)
elif A == 4 or A == 9:
    if B % 2 == 0:
        print(pow(A,2,10))
    else:
        print(A)
else:
    # I want B^C % 4
    B = B % 4
    if B == 0:
        n = 4
    if B == 1:
        n = 1
    elif B == 2:
        if C == 1:
            n = 2
        else:
            n = 4
    elif B == 3:
        if C % 2 == 0:
            n = 1
        else:
            n = 3

    print(pow(A,n,10))

# B^C mod 4
"""
0
1
2 0
3 1 3
"""
# A^n mod 10
"""
1
2 4 8 6 2
3 9 7 1 3
4 6 4
5
6
7 9 3 1 7
8 4 2 6 8
9 1 9
0
"""