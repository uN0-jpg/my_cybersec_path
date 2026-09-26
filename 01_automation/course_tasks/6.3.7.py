from math import *

a, b, c = float(input()), float(input()), float(input())
x1, x2 = float(), float()
D = b**2 - 4 * a * c
counter = 0

if D < 0 and a != 0:
    print("Нет корней")
elif D == 0 and a != 0:
    x1 = -1 * (b / (2 * a))
    print(x1)
elif D > 0 and a != 0:
    x1 = (-1 * b - sqrt(D)) / (2 * a)
    x2 = (-1 * b + sqrt(D)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))

else:
    print('Ошибка')