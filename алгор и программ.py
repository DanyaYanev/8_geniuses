tasklist = int(input("Введите номер задания: "))
match tasklist:
    case 1:
        # Задание 1, 2
        # импорт модуля рандом для генерации чисел в списках
        from random import randint
        # создание первого списка
        print('первый список')
        mas1 = []
        for i in range(10):
            mas1.append(randint(-10, 100))
        print(sorted(mas1))                     # функция sorted - сортирует по возрастанию
        # создание 2 списка
        print('второй список')
        mas2 = []
        for i in range(10):
            mas2.append(randint(-10, 100))
        print(sorted(mas2))
        # odd - список, из нечетных элементов первого списка
        odd = [x for x in mas1 if x % 2]          # нечетные
        even = [x for x in mas2 if not x % 2]     # четные
        print('нечетые из первого')
        print(odd)
        print('четные из второго')
        print(even)
        print('результат')
        mas_total = [*odd, *even]
        print(mas_total)
        mas_reverse = []
        for i in reversed(mas_total):           # возвращает значения с конца в столбик
            mas_reverse.append(i)               # добавляет элемент в конец списка
        print(mas_reverse)
    case 3:
        # Задание 3
        a, b = int(input('Введите нижнюю границу: ')),  int(input('Введите верхнюю границу: '))
        mas = []
        for i in range(a, b+1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                mas.append(i)
        print('Простые числа:', mas)
    case 4:
        # Задание 4
        print('привет Ромка')
    case 5:
        # Задание 5 (которых нет во втором)
        mas1 = list(map(int, input('Введите первый список: ').split()))
        mas2 = list(map(int, input('Введите второй список: ').split()))
        print(mas1, mas2, sep='\n')
        result = list(set(mas1) - set(mas2))
        print('Разность списков:', result)
    case 6:
        # Задание 6 (уникальное число)
        mas = list(map(int, input().split(',')))
        # list - создает список, map - полезен, когда вам нужно применить функцию преобразования к
        # каждому элементу в коллекции или в массиве и преобразовать их в новый массив
        # т.е. map - применяет функцию к КАЖДОМУ ЭЛЕМЕНТУ в объекте
        # split() позволяет легко разделить начальную строку на отдельные кусочки.
        # Для этого в кавычках указывается разделитель.
        print(mas)
        # для того, чтобы проверить уникальность элеметнов, нужно использовать множества, которые не могут содержать
        # одинаковых элементов
        if len(set(mas)) == len(mas):      # set - создает множество
            print('Все числа уникальны')
        else:
            print('Есть одинаковые')
    case 7:
        # Задание 7 (четное нечетное число)
        num = int(input('Введите число: '))
        if num % 2 == 0:
            print('число четное')
        else:
            print('число нечетное')
    case 8:
        # Задание 8 (футы и дюймы)
        foot = int(input('Введите количество футов: '))
        inch = int(input('Введите количество дюймов: '))
        cm = foot * 30.48 + inch * 2.54
        print('Ваш рост составляет', cm, 'сантиметров')
    case 9:
        # Задание 9 (секунды, минуты, дни)
        print('s - секунды\nm - минуты\nd - дни')
        what = input('Введите нужную вам букву букву: ')
        if what == 's':
            sec = int(input('Введите количество секунд: '))
            minute = sec / 60
            days = minute / 1440
            print('В', sec, 'секундах:', minute, 'минут,', days, 'дней')
        elif what == 'm':
            minute = int(input('Введите количество минут: '))
            sec = minute * 60
            days = minute / 1440
            print('В', minute, 'минутах:', sec, 'секунд,', days, 'дней')
        elif what == 'd':
            days = int(input('Введите количество дней: '))
            minute = days * 1440
            sec = minute * 60
            print('В', days, 'дней:', sec, 'секунд,', minute, 'минут')
    case _:
        print('такой операции нет')
