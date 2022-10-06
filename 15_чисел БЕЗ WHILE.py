sum_count = 0        # счетчик суммы отриц. чисел
multiply_count = 0   # счетчик произведения положит. чисел
for i in range(15):
    x = int(input('Введите число: '))
    if x > 0:
        multiply_count = multiply_count + x
    elif x < 0:
        sum_count = sum_count + x
    else:
        print('error')


print('Сумма отрицательных чисел = ' + str(sum_count))
print('Суммаположительных чисел = ' + str(multiply_count))


