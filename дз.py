# минимальное из 3-х чисел или просто print(min(a, b, c))

a, b, c = int(input('Введите число а: ')), int(input('Введите число b: ')), int(input('Введите число c: '))
if b > a < c:
    print(a)
elif c > b < a:
    print(b)
else:
    print(c)



# количество цифр числа

num = int(input("Введите число: "))
count = 0
while num > 0:
    count = count + 1
    num = num // 10
print("Количество цифр равно:", count)



# сумма чисел от 1 до n

n = int(input('Введите граничное число: '))
result = 0
for i in range(1, n + 1):   # так как невключительно, поэтому n + 1
    result += i
print(result)



# факториал натурального числа

n = int(input('Введите число для факториала: '))
factorial = 1
for each_value in range(1, n + 1):
    factorial = factorial * each_value
print(factorial)




