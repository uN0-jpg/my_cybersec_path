from math import ceil

n = int(input())
num = 0
j = 0
length = 1
flag = False

for s in range(1, n + 1):
    if s == 1:
        print("1")
        length += 2
        continue
    mid = ceil(length / 2)
    while num < mid:
        num += 1
        print(num, end="")
    else:
        flag = True
    if flag == True:
        for f in range(mid, length):
            num -= 1
            print(num, end="")
        flag = False

    length += 2
    num = 0
    print()
