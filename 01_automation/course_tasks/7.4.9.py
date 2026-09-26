n, total = int(input()), 0
for i in range(1, n + 1, 2):
    total += i
for i in range(0, n + 1, 2):
    total -= i
print(total)