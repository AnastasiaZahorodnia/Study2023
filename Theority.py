# a = 12  # int целые числа
# b = 3.141592  # float дробные числа
# c = 'text 22'  # str строки
# d = [2, 2, 2, 6.7, 'text', [6, 7]]  # list список changeable
# d[5][1] = 8
# print(d)
# k = d[5][1]
# print(k)
# e = (2, 6.7, 'text')  # tuple кортеж  # not changeable, less weight, speed
# print(e[0])
# f1 = True  # bool логический
# f2 = False
# m = {4, 5.6, 'cat', 4, 'cat'}  # set множества # random and changeable
# print(hash('cat'))
# s = {'key': 'value', 'Alex': [5, 4, 3, 5]}  # dict словарь
# print(s['Alex'])
#
# # import math
# # print(math.cos(math.pi))
#
# # + - * /
# print(4 ** 2)  # возведение в степень
# print(125 ** (1/3))  # кубический корень
# print(-16 ** (1/2))
# print(pow(5, 2))  # возведение в степень
# print(pow(4, 2))
# print(pow(-16, 0.5))
# 4 * 4 = 16 ** (1/2) = 4
# 2 * 2 * 2 = 8 ** (1/3) = 2
# print(7 // 3)  # целая часть от деления # how many times we put 3 in 7
# print(7 % 3)  # остаток от деления
# print(divmod(7, 3))  # (//, %)
# print(divmod(28, 10))
# print(abs(-7))  # модуль числа


# if условие1:      если
#     блок кода 1
# elif условие2:    иначе если
#     блок кода 2
# else:             иначе при всех остальных условиях
#     блок кода 3


# number = int(input('Введите число: '))
# if number > 0:
#     print("Number is positive")
# elif number < 0:
#     print("Number is negative")
# else:
#     print("Zero")


# ctrl + c, v, x, z, a, /

# > больше
# < меньше
# == равно
# != не равно
# >= больше или равно
# <= меньше или равно

# Логические операции
# a and b логическое И, True если оба True
# a or b логичесое ИЛИ, True если хотя бы один равен True
# not a  логическое НЕ   not True = False    not False = True

# a, b = (0,), 7
# # a, b = b, a
# if a and b > 0:
#     print('cat')

# False: False, None, 0, [], (), '', {}
# True: True, number != 0, len(iterable) > 0

# day_value = input("Whats the day today ")
# print("Today is a weekend" if day_value == "Sunday" or day_value == "Saturday" else "Today is a working day")

# # Строки str
# a = 'White cat black cat'
# # b = 'dog'
# # c = 7
# # print(a + b + str(c))  # конкатенация
# # print(a, b, c)
# # print(b * 4)
# # print('-' * 70)
# # print('cat' in a)  # вхождение подстроки в строку
# # print(len(b))  # длина строки
# # print(a.count('cat'))  # считает количество подстрок в строке
# # print(a.index('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет - ошибка
# # print(a.rindex('cat')) # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет - ошибка
# # print(a.find('catee')) # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет -1
# # print(a.rfind('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет -1
# # print(a.replace('cat', 'cow').replace('black', 'red'))  # замена текста
# # print(a.replace('cat', 'cow', 1))  # замена текста
# # print(a.replace('t', '')) # удаляем t
# # print('BMW'.lower())      # Перевести в нижний регистр
# # print('apple'.upper())    # перевести в верхний регистр
# # print('Apple'.swapcase()) # изменить регистр букв
# # print(a.title())  # меняет первую букву каждого слова на заглавную, а остальные на строчные
# # print(a.capitalize())  # меняет первую букву строки на заглавную, а остальные на строчные
# #
# # s = 'white     cat    black         cat dog'
# # print(s.split(" "))  # разбивает строку по разделителю на список текстовых элементов, without an element in the text
# # # cANNOT BE BROKEN
# # print(s.split())  # по умолчанию делится по множественному пробелу (любое количество любых пробельных символов), one separator
# # print('*'.join(['white', 'cat', 'black', 'cat']))  # склеивает в строку iterable текстовых элементов
# #
#
# a = 'x y z a b'
# # print(a.split(maxsplit=2))  # можем указать количество разбиений
# # print(a.rsplit(maxsplit=2))  # разбиение с конца строки
# #
# # print('white cat\nblack cat')
# # print("white cat" + "\n" + "black cat")
# # print(a.splitlines())  # разбиваем по строкам (/n)
# # print(a.splitlines(keepends=True))  # сохраняем символ переноса строки
# # #
# # s = 'Discworld'
# # # print(s.endswith('cat'))  # False
# # # print(s.endswith('world'))  # True
# # # print(s.endswith(('cat', 'world')))  # True / or
# # print(s.endswith('sc'))  # True
# # print(s.endswith('sc', 0, 4))  # True
# # print(s.startswith('Disc'))  # True
#
# # a = 'apple'
# # b = '12'
# # c = 'apple 12'
# # print(a.isalpha())  # состоит ли только из букв
# # print(a.isdigit())  # состоит ли только из цифр
# # print(a.isalnum())  # состоит ли только из букв или цифр
# # print(a.isspace())  # состоит ли только из пробельных символов (пробел, перевод строки \n, табуляция \t...)
# # print(a.islower())  # состоит ли строка из символов нижнего регистра
# # print(a.isupper())  # состоит ли строка из символов верхнего регистра
# # print(a.istitle())  # начинаются ли слова в строке с заглавных букв
#
# # fio = input('Введите ваши ФИО: ')
# # if fio.istitle():
# #     print(fio)
# # else:
# #     print(fio.title())
# #
# # print(fio if fio.istitle() else fio.title())
#
# # print(isinstance(a, (int, float, complex)))  # проверяет принадлежит ли переменная к тому или иному типу
# # print(type(a))  # показывает тип переменной
# # print('****apple**'.strip('*'))  # удаляет с начала и конца строки указанные символы
# # print('****apple**'.rstrip('*'))  # удаляет с конца строки указанные символы
# # print('****apple**'.lstrip('*'))  # удаляет с начала строки указанные символы
# # print('   apple         '.strip())  # по умолчанию удаляет пробельные символы
# # print('+-*/-+apple+++---///*'.strip('+-*/'))
# # print(ord(','))  # показывает код символа
# # print(chr(44))  # показывает символ по коду
# # print(chr(129519), chr(43458))
#
# # for i in range(1, 55296):
# #     print(chr(i), end=' ')
# #     if i % 60 == 0:
# #         print('\n', i, ': ', end='')

# Тернарный оператор
# if expression:
#     on_true
# else:
#     on_false
#
# on_true if expression else on_false

# Интервалы, слайсы, slices, срезы
# a = 'white cat black cat'
# print(a[3])  # t
# print(a[-1])  # t
# print(a[6:9])  # с 6 по 8 символы, последний не включительно
# print(a[:5])  # с начала строки по 4 символы
# print(a[16:])  # с 16 до конца строки
# print(a[:-3])  # cat
# print(a[6:16:2])  # c 6 по 15 с шагом 2
# print(a[::-1])  # развернуть строку
# print(a[::-3])
#
# t = 'шалашf'
# print("polidrom" if t[::-1] == t else "not polidrom")

# Списки list
# a = [1, 2, 3, 2, 2]
# b = [5, 6, 7]
# s = ['cat', 'dog', 'cow', '5apple']
#
# print(a + b)
# print(b * 4)
# print(a[1:4])
# print(5 in b)  # проверяем вхождение 1 элемента в список
# print(len(a))  # длина списка
# print(max(b))  # максимальное в списке b
# print(max(s, key=len))  # с помощью key можем изменить критерий сортировки
# print(min(s))  # минимальное в списке b
# print(a.count(2))  # считает количество указанных элементов
# print(a.index(2))  # возвращает индекс вхождения ПЕРВОГО найденного элемента, от start до end
# print(sum(b))  # возвращает сумму элементов
# m2 = [1, 2, 3, 2, 2]
# m = [['cat', 'dog'], ['cows', 'apple']]
# print(sum(m, []))  # из двумерного списка делаем одномерный
# print([] + ['cat', 'dog'] + ['cows', 'apple'])
# print(sum(m2, 100))
# exit()
# # print(sorted(m, key=len, reverse=True))  # возвращает отсортированный итерируемый объект
# print(m)
# m.sort(key=len, reverse=True)  # сортирует исходный список # reverse - backwards
# print(m)
# m.reverse()  # разворачивает список [::-1]
# print(m)
# m.append(7)  # добавляет элемент в конец списка
# print(m)
# m.extend(m2)  # добавляет элементы m2 в конец списка m
# m.extend('cat')
# print(m)
# m.insert(1, 8)  # добавить 8 по индексу 1
# print(m)
# m[0] = [1, 2]   # change object in list by index
# print(m)
# m[2:4] = [7, 8, 9]
# print(m)
# m[2:2] = [10, 20, 30]
# print(m)
# m.remove(2)  # удаляет первый найденый элемент
# print(m)
# d = m.pop(2)  # удаляет элемент по индексу и возвращает его
# print(m, d)
# d = m.pop()  # по умолчанию - последний элемент
# print(m, d)
# del m[1]  # удаляет по индексу
# print(m)
# m2 = m.copy()  # поверхностная копия списка
# m2.clear()  # очистка списка
# print(m2)
#
# from copy import deepcopy
# m = [1, 2, 3, [7, [8, 9]]]
# z = m.copy()
# m2 = deepcopy(m)  # глубокое копирование, each id changeable
# m[3][1][0] = 9
# print(m, m2)
# print(id(m[3]), id(m2[3]))
#
# x = [1, 2, 3]
# # x2 = x[:]
# # x2 = x * 1
# x2 = x + []
# x[0] = 5
# print(x, x2)

# Основные способы форматирования строк:
# name = 'Alice'
# age = 20
# # 1. Конктенация.
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет.')
# # 2. %-форматирование
# print('Меня зовут %s. Мне %d лет.' % (name, age))
# print('Меня зовут %(x)s. Мне %(y)d лет.' % ({'y': age, 'x': name}))
# # 3. Метод format()
# print('Меня зовут {}. Мне {} лет.'.format(name, age))
# print('Меня зовут {x}. Мне {y} лет.'.format(x=name, y=age))
# # 4. f-строка
# print(f'Меня зовут {name}. Мне {age} лет.')
# pi = 3.1415926
# print(f'pi = {pi:.2f}')
# h, m = 2, 5
# print(f'Время на часах: {h:02d}:{m:02d}')
# print(f'{1234567890:,}')  # 1,234,567,890
# print(f'pi * age = {pi * age}')
# planets = ['Юпитер', 'Сатурн', 'Венера']
# print(f'Субботу назвали в честь планеты {planets[1]}')
# print(f'Субботу назвали в честь планеты {planets[1].upper()}')
# print(f'Округление 3.5 = {round(3.5)}, округление 4.5 = {round(4.5)}')  # to the nearset even number
#
# print('{0:*^20}'.format('Выравнивание'))  # center
# print('{0:*>20}'.format('Выравнивание'))
# print('{0:*<20}'.format('Выравнивание'))
# print('{1:*<20}'.format('Выравнивание', 'cat', 'dog'))
# print()
# print(f'{"Выравнвиание":*^20}')  # center
# print(f'{"Выравнвиание":*>20}')   # right
# print(f'{"Выравнвиание":*<20}')
#
# # print('apple'.center(20, '*'))  # возвращает отцентрированную строку
# a, b, c = 5, 7, 9
# print(a, b, c, end='+++')  # end опеределяет, чем заканчивается вывод строки
# print(a, b, c, sep='---')  # sep определяет, что стоит между переменными

# # Экранирование
# print(r'C:\new\table')  # "сырая" строка
# print('C:\\new\\table')  # с помощью \
# print('C:\new\table')


# Множества set
# s = [1, 'cat', 'dog', 'cat', 5, 5, 'dog']
# m = set(s)
# print(m)
# print(set('apple'))
# print(len(m))
# print(2 in m)
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = {5, 6}
# #
# # print(b.isdisjoint(c))  # True, если НЕ имеются общие элементы
# print(c.issubset(b))  # c <= b TRUE if all item the same
# # print(c <= b)
# print(b.issuperset(c))  # b >= c
# print(b >= c)
#
# football = {'A', 'B', 'C'}
# chess = {'B', 'C', 'D'}
#
# print(football.union(chess))  # объединение
# print(football | chess)
#
# print(football.intersection(chess))  # пересечение
# print(football & chess)
#
# print(football.difference(chess))  # разница
# print(football - chess)
#
# print(football.symmetric_difference(chess))  # симетричная разница (объединяем множества и удаляем пересечение)
# print(football ^ chess)
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
#
# a.intersection_update(b)  # a = a & b    a &= b
# print(a)
#
# b.difference_update(a)  # b = b - a    b -= a
# print(b)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
#
# a.symmetric_difference_update(b)  # a = a ^ b, a ^= b
# a = a ^ b
# print(a)
#
# a.add('apple')  # добавляет элемент в множество (неизменяемого типа)
# a |= {9}
# print(a)
#
# a.update({3, 4})  # объедияет элементы итерируемого объекта с множеством
# a.update('cat and grape')
# print(a)
#
# a.remove(2)  # удаляет элемент множества, если элемента нет - ошибка
# print(a)
#
# a.discard(50)  # удаляет элемент множества, если элемента нет - pass
# print(a)
#
# d = a.pop()  # удаляет и возвращает случайный элемент множества ("первый" элемент)
# print(d, a)
#
# a2 = a.copy()  # копия множества
# a2.clear()  # очистка множества
#
# a = {'d', 'p', 'c', 'e', 't', 'n', 'apple', 'a', 'g', 'r'}
# print(sorted(a))
#
#
# x = [1, 2, 3, 4]
# y = [3, 4, 5, 6]
# x = list(set(x) - set(y))
# print(x)
#
# animals = ['cat', 'dog', 'cow', 'rabbit', 'elefant']
# animals = set(animals).pop()
# animals = list(set(animals).pop())
# print(animals)

# a, b, *c = animals
# print(c)
# a, b, *c = range(3)
# print(c)
# a, b, *c = {'cat', 'dog', 'cow', 'rabbit'}
# print(c)
# print(a, b, c)

# Словарь dict
# a = {'key': 'value', 1: 'one', 5.8: 'five', True: 'yes', (1, 9): 7.9}
# b = dict([(7, 1), ('b', ' cat')])
# c = dict(key1='cat', key2='dog', key3=7)
# print(b, c)
# print(a)

# Коллизия хэширования
# d = {1: 'cat', 1.0: 'dog', True: 'cow'}
# d2 = {0: 'cat', 0.0: 'dog', False: 'cow'}
# print(d)
# print(d2)
# print(hash(True), hash(1), hash(1.0))

# week = {
#     'Выходной': 'Воскресенье',
#     1: 'Понедельник',
#     2: 'Вторник',
#     3: 'Среда',
#     4: 'Четверг'
# }
# print(week['Выходной'])  # возвращает значение по ключу, используем, если уверены в наличие ключа
# print(week.get(22, 'Такого ключа нет!'))  # возвращает значение по ключу, если ключа нет - None
# print(week.setdefault(5, 'Пятница'))  # возвращает значение по ключу, если ключа нет - создаст такой ключ
# print(week.keys())  # возвращает все ключи
# print(week.values())  # возвращает все значения
# print(week.items())  # возвращает (ключ, значение)
# print(week)
# week.update({6: 'Суббота'})  # добавляет элемент(ы) словаря
# week[7] = 'Воскресенье'
# print(week)
# del week[4]  # удаляет элемент словаря по ключу
# print(week)
# d = week.pop(50, 'Значение')  # удаляет элемент по ключу и возвращает его значение, если ключа нет - возратит Значение
# print(week, d)
# week2 = week.copy()  # поверхностная копия словаря
# week2.clear()  # очистить словарь
#
# s = {'a': 1, 'b': 2, 'cat': 'animal'}
# item = s.popitem()  # удаляет и возвращает последнюю пару (ключ, значение)  python >= 3.7
# print(s, item)
#
# d = {}.fromkeys(['cat', 'dog', 'cow'], 0)  # создаёт слвоарь из iterable ключей с одним значением для всех ключей, по умолчанию - None
# print(d)
# d['cow'] += 5
# print(d)
#
# z = {i: [] for i in ['cat', 'dog', 'cow']}
# z['cow'].append('grass')
# print(z)
#
# id_users = {
#     12: 'Alex',
#     22: 'Alice',
#     47: 'Tom'
# }
# user = 222
# print(f'Привет, {id_users.get(user, "Stranger")}')
#
# x = {1: 'one', 2: 'two'}
# y = {2.0: 'cat', True: 'dog'}
# z = {**x, **y}  # объединение словарей
# print(z)
#
# z2 = y | x  # объединение словарей python >= 3.9
# print(z2)
#
# # Сортировка словаря по значениям
# store = {'apple': 40, 'oranges': 80, 'ananas': 70, 'banana': 10}
# print(sorted(store))
# print(sorted(store, key=store.get))
# print(sorted(store.values()))
# print(sorted(store, key=len))
#
# from collections import Counter
#
# items = ['apple', 'banana', 'apple', 'grape', 'banana', 'apple']
# cf = Counter(items)  # создаёт итератор подсчёта количества элементов
# print(cf)
# print(cf['apple'])
# print(cf.most_common())  # возвращает список кортежей подсчёта элементов

# Цикл for
# for переменная in iterable:
#     тело цикла
# else:
#     код выполняется, если цикл завершился нормально (без break)

# a = [1, 2, 7, 12, 14, 34, 57]
# for i in a:
#     if i == 12:
#         continue  # досрочное завершение итерации
#     if i == 4:
#         break  # досрочное завершение цикла
#     print(i)
# else:
#     print('cat')

# for i in range(2, 9, 2):  # 2 4 6 8
#     print(i, 'cat')

# for i in enumerate(a):  # возвращает (индекс, элемент)
#     print(i)

# for x, y in enumerate(a, 10):  # можем указать начало индексации
#     print(x, y)

# Списковые включения (list comprehension)
# list_new = []
# for i in range(1, 11):
#     list_new.append(i ** 2)
# print(list_new)
#
# print([i ** 2 for i in range(1, 11)])
#
# print({i for i in range(1, 11)})
# print({i: i ** 2 for i in range(1, 11)})
# print((i ** 2 for i in range(1, 11)))
#
# print([i ** 2 for i in range(1, 11) if i % 2 == 0])

# Вывести чётные числа в интервале [1, 20], если число меньше или равно 10, то - квадрат, а если больше 10 - куб.
# print([i ** 2 if i < 11 else i ** 3 for i in range(1, 21) if i % 2 == 0])
# print([(i ** 3, i ** 2)[i < 11] for i in range(1, 21) if i % 2 == 0])

# Подсчитать количество и сумму цифр
# s = 'cat 217 dog781'
# value = [int(i) for i in s if i.isdigit()]
# print(len(value))
# print(sum(value))

# for x in range(9):
#     for y in range(9):
#         print(f'x = {x} y = {y} {x * 10 + y}')
#
# print([x * 10 + y for x in range(10) for y in range(10)])

# Сгенирировать список из букв имён, которые меньше 4 символов:
# s = ['Tom', 'Jerry', 'Bob', 'Vinny']

# print([x for i in s if len(i) < 4 for x in i])
# print([x for i in s for x in i if len(i) < 4])
# for i in s:
#     for x in i:
#         if len(i) < 4:
#             print(x)

# Многомерные массивы
# x = [0] * 2
# y = [0 for i in range(4)]
# print(x)
# print(y)
#
# z = [[0] * 2 for i in range(4)]  # !!!
# t = [x for i in range(4)]
# z[0][1] = 1
# print(z)
# # [[0, 0], [0, 0], [0, 0], [0, 0]]
#
# b = [[[0] * 2 for i in range(4)] for k in range(2)]
# b[0][0][1] = 1
# print(b)
# [[[0, 0], [0, 0], [0, 0], [0, 0]],  [[0, 0], [0, 0], [0, 0], [0, 0]]]


# s = [i for i in range(1_000_000)]
# s2 = (i for i in range(1_000_000))
# print(s2)
# print(s.__sizeof__())
# print(s2.__sizeof__())

# У нас есть колода карт с мастями (♥♦♠♣) и карты от шестёрки до туза.
# Сформировать колоду вида: 6♥, 6♦, 6♠, 6♣ ... Т♣.
# Перемешать её и вывести первые случайные 6 карт.
# Можно ли решить задачу в одну строку?
# masti = '♥♦♠♣'
# number = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
# k = set()
# for i in number:
#     for j in masti:
#         k.add(i + j)
# print(*tuple(k)[:6])
#
# print(*tuple({i + j for i in number for j in masti})[:6])

# Цикл while
# while условие:
#     тело цикла
# else:
#     код выполняется, если цикл завершился без break

# i = 0
# while i < 5:
#     i += 1
#     if i == 2:
#         continue
#     if i == 14:
#         break
#     print(i, 'cat')
# else:
#     print('dog')
#
# while True:  # вечный цикл
#     x = input('Введите фрукт: ')
#     if x == 'exit':
#         break
#     print(x * 2)

# Функции def
# def name(params):
#     body function
#     return result

# def degree(x, y):
#     x, y = abs(x), abs(y)
#     return x ** y


# (4 ** 2) ** 8 + 10 ** 3
# degree = lambda x, y: abs(x) ** abs(y)   # lambda parameters: return
# print(degree(-2, -4))
# print(degree(degree(4, 2), 8) + degree(10, 3))

# def mysum(*s):
#     return sum(s)
#
#
# mysum = lambda *s: sum(s)
# print(mysum(1, 2, 3, 4))

# def func(x):
#     return x[1]
#
#
# students = [
#     ('Alice', 8),
#     ('Alex', 17),
#     ('Ivan', 10)
# ]
# print(sorted(students, key=func))
# print(sorted(students, key=lambda x: x[1], reverse=True))
#
# print(sorted([16, 3, 8, 2, 1], reverse=True))
#
# grades = [{'name': 'Jennifer', 'final': 95},
#           {'name': 'David', 'final': 92},
#           {'name': 'Aaron', 'final': 98}]
#
# def fun_dict(y):
#     return y['final']
#
#
# print(sorted(grades, key=fun_dict))
# print(sorted(grades, key=lambda y: y['final']))
# print(sorted(grades, key=lambda j: j['name']))
