def largest_factor(a):
    for i in range(2,a):
        if a % i == 0:
            print(a / i)
            break
        elif a % i != 0 and i == a-1:
            print(None)

while True:
    largest_factor(int(input('input the number:')))