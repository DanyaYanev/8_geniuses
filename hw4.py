#факториал натурального числа 
def factorial():
    n = 1
    num = int(input('Введите число'))
    for i in range(1, num + 1):
        n = n * i    
    print(n)
factorial()

#минимум среди 3 чисел
def min():
    a = int(input('Введите первое число '))
    b = int(input('Введите второе число '))
    c = int(input('Введите третье число '))
    if a > b and b > c:
        print('минимум:', c)
    elif a > c and c > b:
        print('минимум', b)
    else:
        b > c and c > a
        print('минимум:', a)
min()

#кол-во цифр в числе 
num = int(input('Введите число '))
n = 0
while num > 0:
    n = n + 1
    num = num // 10
print('Количество цифр:', n)

#сумма всех чисел 
def sum():
    sum = 0 
    n = int(input('Введите количество чисел '))
    for i in range(n):
        number = int(input('Введите число '))
        sum = number + sum
    print(sum) 
sum()


