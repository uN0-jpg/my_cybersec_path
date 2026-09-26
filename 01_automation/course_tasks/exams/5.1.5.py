n = int(input())
if n % 2 != 0:
    print('YES')

else:
    if 2 <= n <= 5:
        print('NO')
    if 6 <= n <= 20:
        print('YES')
    if n > 20:
        print('NO')