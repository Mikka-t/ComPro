H = int(input())

plant = 0
i = 0
day = 0
while True:
    plant += pow(2, i)
    day += 1
    i += 1 
    if plant > H:
        print(day)
        break

