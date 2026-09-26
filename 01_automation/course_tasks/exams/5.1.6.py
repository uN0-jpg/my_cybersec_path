x1, y1, x2, y2 = int(input()), int(input()), int(input()),int(input())
# По диагонали есть обязательное условие: ОБЕ координаты меняются
if (x2 - x1 != 0) and (y2 - y1 != 0): # Разница x и разница y должна быть одинаковой.
    if (x2 - x1) == (y2 - y1) or (x1 - x2) == (y1 - y2) or (x1 - x2) == (y2 - y1):
        print('YES')
    else:
        print('NO')

else:
    print('NO')