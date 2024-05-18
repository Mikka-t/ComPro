S = input()

length = len(S)
for i in range(length//2):
    S = S[:2*i]+S[2*i+1]+S[2*i]+S[2*i+2:]

print(S)