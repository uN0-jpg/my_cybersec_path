page = 0
money = 0
ch = ''

while page == 0:
    print("-" * 10)
    print("")
    print("[ m o n e y ]")
    print("")
    print("your money:", money, "$.  |   ", "What you wanna do?")
    print("1. Get 1$")
    print("2. Spend 1$")
    print("3. End the program")
    print("")
    print("")
    print("-" * 10)

    input(ch)

if ch == 1:
    money = money + 1
    page = 0

if ch == 2:
    money = money - 1
    page = 0
    
if ch == 3:
    exit
    page = 0

input()
