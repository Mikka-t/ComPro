N = int(input())

def ans(lis):
    answer = []
    for i in range(len(lis)+1):
        if i == 0:
            answer.append(1)
        elif i == len(lis):
            answer.append(1)
        else:
            answer.append(lis[i]+lis[i-1])
    return answer

for i in range(N):
    if i == 0:
        temp = [1]
    else:
        temp = ans(temp)
    print(" ".join([str(strings) for strings in temp]))