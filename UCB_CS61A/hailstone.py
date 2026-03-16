def hailstone(x):
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x / 2
        else:
            x = x * 3 + 1
    print(1)
while True:
    hailstone(int(input('input your number:')))
