'''
num = int(input("Введите число: "))
for i in range(3):
    new_num = int(input("Введите число для сравнения: "))
    if num == new_num:
        print("равно")
    else:
        print("не равно")
'''

num = float(input('Введите число для сравнения: '))
for i in range(3):
    new_num = float(input('Введите число: '))
    if num != new_num:
        print('НЕ РАВНО')
        exit()
    elif num == new_num:
        print('Равно')