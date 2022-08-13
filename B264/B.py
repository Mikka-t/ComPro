R,C = map(int, input().split())

if R >= C:
    if R <= 15-C+1:
        if C%2==1:
            print("black")
        else:
            print("white")
    else:
        if R%2==1:
            print("black")
        else:
            print("white")
else:
    if R <= 15-C+1:
        if R%2==1:
            print("black")
        else:
            print("white")
    else:
        if C%2==1:
            print("black")
        else:
            print("white")
    
