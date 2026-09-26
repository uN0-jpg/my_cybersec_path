#Ход коня
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x2 - x1 == 1 or x1 - x2 == 1:
    if y2 - y1 == 2 or y1 - y2 == 2:
        print('YES')
    else:
        print('NO')

elif x2 - x1 == 2 or x1 - x2 == 2:
    if y2 - y1 == 1 or y1 - y2 == 1:
        print('YES')
    else:
        print('NO')

else:
    print('NO')