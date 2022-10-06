sum_pos = 0        # счетчик суммы отриц. чисел
sum_neg = 0   # счетчик произведения положит. чисел
for i in range(15):
    x = int(input('Введите число: '))
    if x > 0:
        sum_neg = sum_neg + x
    elif x < 0:
        sum_pos = sum_pos + x
    else:
        print('error')


print('Сумма отрицательных чисел = ' + str(sum_pos))
print('Сумма положительных чисел = ' + str(sum_neg))


