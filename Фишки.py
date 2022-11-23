# dir - возвращает список атрибутов

# АТРИБУТЫ ОЧЕНЬ ПОЛЕЗНЫ !!!
'''
print('\ndir() with no argument\n')
print(dir())
'''

'''
def test():
    print("work")

print(dir(test))

test.__call__()  # __call__() - вызывает функцию.   Выполняет сам класс как функцию
# work
'''

'''
def test(name: str) -> int: print("work")
print(dir(test))

print(test.__annotations__)

['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', 
'__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', 
'__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', 
'__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__']

{'name': <class 'str'>, 'return': <class 'int'>}
'''

'''
def test():
    """ Привет """
    return 1

print(test())  # возвращает значение ф-ии, т.е. 1

print(test.__doc__) #
print(test.__name__)  # возвращает название ф-ии
'''

#################################################


'''
# Прикольный код
text = 'PYTHON'
for index in range(len(text)):
    print("".join(list(text)[:index + 1]))
'''

'''
# Копирование списка напрямую в список
mas1 = [1, 2, 3, 4]
mas2  = [5, 6, 7, 8]
mas1.append(mas2.copy())
print(mas1)
# [1, 2, 3, 4, [5, 6, 7, 8]]
'''

#################################################
# СОЗДАНИЕ ДИНАМИЧЕСКОГО КЛАССА

'''
# Type — это встроенная функция, которая помогает определить тип переменной, передаваемой на вход.
a = type('Hello', (object,), {"value": "world"})
print(a.value)
# world


# ЭТО РАВНО ТАКОМУ КОДУ:
class Hello(object):
    value = "world"

#a = Hello()
#print(a.value)

print(Hello.value)  # так правильнее, нежели верхние 2 строчки
'''


#################################################

'''
# TYPE
a = 5
b = []
c = {}
d = ()
print(type(a), type(b), type(c), type(d), sep='\n')

# Такой же код, только проще

mas = [5, [], {}, ()]
for i in mas:
    print(type(i))
'''