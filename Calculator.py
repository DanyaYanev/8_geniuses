import math
print("Существующие операции: +, -, *, /, **.")
next = 'y'
while next == 'y':
    num1 = float(input("Введите первое число: "))
    op = input("Введите операцию: ")
    num2 = float(input("Введите второе число: "))
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '**':
        print(math.sqrt(num1))
    else:
        print("ERROR")
    next = input("Введите 'y' чтобы продолжить или любую клавишу чтобы завершить: ")