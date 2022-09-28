# Калькулятор для 2-х чисел

import math
print("Доступные операции: +, -, *, /, D")
op = input("Выберите операцию: ")
if op != 'D':
    num1 = int(input('Введите 1 число: '))
    num2 = int(input('Введите 2 число: '))
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    a = int(input('Введите коэффициент a: '))
    b = int(input('Введите коэффициент b: '))
    c = int(input('Введите коэффициент c: '))
    D = b**2-4*a*c
    if D > 0:
        x1 = (-b - (math.sqrt(D))) / (2 * a)
        x2 = (-b + (math.sqrt(D))) / (2 * a)
        print(x1, x2)
    elif D == 0:
        x = -b / 2*a
        print(x)
    else:
        print('Корней нет')