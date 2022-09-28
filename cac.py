import math
print("Введите D чтобы решить квадратное уравнение или любую клавишу чтобы произвести математические операции ")
calc = input()
if calc == 'D':
    print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0): ")
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    D = (b ** 2) - 4 * a * c
    print("Дискриминант D = %.2f" % D)
    if D > 0:
        import math
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif D == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Нет корней")
else:
    print("Существующие операции: +, -, *, /, **.")
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
input()