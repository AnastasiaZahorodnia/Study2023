# # Строки str
# a = "English is a West Germanic language of the Indo-European language family."
# b = 'French'
# c = 7
# print(a + b + " " + str(c) + ".")  # конкатенация
# print(a, b, c)
# print(a, (b + ' ') * 4)
# print("k" * 55, "5" * 55)
# print('cat' in a, "u" in b, "is" in a, "est" in a, "f" in b)  # вхождение подстроки в строку
# print(len(b))  # длина строки
#
# fact = "In 2006, the FIFA World Cup Final was held in Berlin. Cup, cup"
# print(len(fact))
# # print(a.count('cat'))  # считает количество подстрок в строке
# print(fact.count("In"), fact.count("Cup"))
# # print(a.index('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет - ошибка
# print(fact.index("Cup"))
# # print(a.rindex('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет - ошибка
# print(fact.rindex("Cup"))
# # print(a.find('catee'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет -1
# print(fact.find("Finals"), fact.find("In"))
# # print(a.rfind('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет -1
# print(fact.rfind("Cup"))
#
# climate = "Berlin has an oceanic climate. Berlin. "
# # print(a.replace('cat', 'cow').replace('black', 'red'))  # замена текста
# print(climate.replace("Berlin", "Lisbon"))
# print(climate.replace("Berlin", " ", 1)) # Delete Berlin
# # print(a.replace('cat', 'cow', 1))  # замена текста
# print(climate.replace("Berlin", "Lisbon", 1))
# print("Paris, London".replace("London", "Paris").replace("Paris", "London", 1))
# # print('BMW'.lower())  # Перевести в нижний регистр
# print("A reporter and a young".replace("a", " ").lower())
# # print('apple'.upper())  # перевести в верхний регистр
# print(climate.upper())
# # print('Apple'.swapcase())  # изменить регистр букв
# print(climate.swapcase())
# # print(a.title())  # меняет первую букву каждого слова на заглавную, а остальные на строчные
# print(climate.title())
# # print(a.capitalize())  # меняет первую букву строки на заглавную, а остальные на строчные
# print(climate.capitalize()) # TODO How to do big letter after "."
# #
# s = "you can use delete to remove a number"
# # print(s.split(" "))  # разбивает строку по разделителю на список текстовых элементов
# result = s.split()
# print(result)
# # print(s.split())  # по умолчанию делится по множественному пробелу
# print('*'.join(['white', 'cat', 'black', 'cat']))  # склеивает в строку iterable текстовых элементов
# print(".".join(result))
# print(s.split(maxsplit=2))  # можем указать количество разбиений
# print(s.rsplit(maxsplit=1))  # разбиение с конца строки
#
# ###########################################
# inf = "Bake for \n12–15 minutes."
# print(inf)
# # print(a.splitlines())  # разбиваем по строкам (/n)
# print(inf.splitlines())
# # print(a.splitlines(keepends=True))  # сохраняем символ переноса строки
# print(inf.splitlines(True))
# # s = 'Discworld'
# f = "Baking soda"
# # print(s.endswith('cat'))  # False
# print(f.endswith("ing"), f.endswith("da"), f.endswith((("ing", "g", "da"))))
# # print(s.endswith('world'))  # True
# # print(s.endswith(('cat', 'world')))  # True / or
# # print(s.endswith('sc', 0, 4))  # True
# print(f.endswith("ing", 0, 6))
# # print(s.startswith('Disc'))  # True
# print(f.startswith("Bak"))
# print(f.startswith("sod", 7))
# #
# # a = 'apple'
# # b = '12'
# # c = 'apple 12'
# inf1 = "Bake for \n12–15 minutes."
# # print(a.isalpha())  # состоит ли только из букв
# print(inf1.isalpha())
# # print(a.isdigit())  # состоит ли только из цифр
# print(inf1.isdigit())
# # print(a.isalnum())  # состоит ли только из букв или цифр
# print(inf1.isalnum())
# # print(a.isspace())  # состоит ли только из пробельных символов (пробел, перевод строки \n, табуляция \t...)
# print(inf1.isspace())
# # print(a.islower())  # состоит ли только строка из символов нижнего регистра
# print("an apple".islower())
# # print(a.isupper())  # состоит ли только строка из символов верхнего регистра
# print("THE APPLE".isupper())
# # # print(a.istitle())  # начинаются ли слова в строке с заглавных букв
# print("The Apple".istitle())
# # print(isinstance(a, (int, float, complex)))  # проверяет принадлежит ли переменная к тому или иному типу
# print(isinstance(8, (str, int)))
# # print(type(a))  # показывает тип переменной
# print(type(6))
# print('****apple**'.strip('*'))  # удаляет с начала и конца строки указанные символы
# print("-The apple 94 =2 - 2 * -".strip("-"))
# # print('****apple**'.rstrip('*'))  # удаляет с конца строки указанные символы
# print("-The apple 94 * =2 -2 * -".rstrip("-"))
# # print('****apple**'.lstrip('*'))  # удаляет с начала строки указанные символы
# print("- * The apple 94 * =2 -2 * -".lstrip("-*"))
# # print('   apple         '.strip())  # по умолчанию удаляет пробельные символы
# print("     apple  ".strip())
# print('+-*/-+apple+++---///*'.strip('+-*/')) #TODO why in 94 line only in the begining
#
# # print(ord(','))  # показывает код символа
# # print(ord("="))
# # print(chr(44))  # показывает символ по коду
# # print(chr(61))
# # print(chr(129519), chr(43458))

a = 'white cat black cat'
# print(a[3])  # t
a_1 = "Business and legal english"
# print(a_1[-1:-3])  #todo ?
# print(a_1[-3:-1])
# print(a_1[-1])
# print(a[-1])  # t
# print(a[6:9])  # с 6 по 8 символы, последний не включительно
# print(a_1[5:10])  # not include 10
# print(a[:5])  # с начала строки по 4 символы
# print(a_1[:5])
# print(a[16:])  # с 16 до конца строки
# print(a_1[10:])
# print(a[:-3])  # minus last cat
# print(a_1[:-3])
# print(a[6:16:2])  # c 6 по 15 с шагом 2
# print("Process finished"[:7:10])
# print(a[::-1])  # развернуть строку
# print(a_1[::-3])

# LIST
# a = [1, 2, 3, 4]
# b = ["fbb", "ab", "b", "c"]
# c = [8, "g"]

# print(a + b)
# print(c * 4)
# print(b[1:3])
# print(4 in a)
# print(len(c))
# print(max(a))
# print(min(a))
#
# # print(max(b, key=len))
# print(a.count(2))
# print(a.index(2))
# print(sum(a))
# d = [a]
# print(sum(d, []))
# f = [1, 2, [3, 4]]
# print(sorted(b, key=len, reverse=True))
# g = ["fg", "gh", "ji", "hjg", [3, 4]]
# g.sort(key=len)
# print(g)
# g.reverse()
# print(g)
# g.append(3)
# print(g)
# g.extend(b)
# print(g)
# g.insert(1, 8)
# print(g)
# g[0:1] = 1, 2
# print(g)
# g[1:3] = [5, 7, 8]
# print(g)
# g[2:2] = [6, 7, 8]
# print(g)
# g.remove(8)
# print(g)
# g[4].pop(0)
# print(g)
# g.pop()
# print(g)
# del g[-1]
# print(g)
# h = [6, 9, 0, -1]
# h2 = h.copy()
# h.clear()
# print(h2)
# h2.clear()
# print(h2)
#
# from copy import deepcopy
# m = [1, 2, [9, 8, [3]]]
# j = m.copy()
# m2 = deepcopy(m)
# m[2][2][0] = 8
# print(m)
# print(id(j[2]))
#
# nm = [1, 2, 3]
# mn = nm[:]
# mn1 = nm * 1
# mn2 = nm + []
# nm[0] = 5
# print(nm, mn2)
#
# nm.append("cat")
# print(nm)
#
# nm.extend("cat")
# print(nm)

# print(divmod(28))
# print(divmod(7, 3))  # (//, %)
# print(divmod(28, 10))
# Основные способы форматирования строк:
# name = 'Alice'
# age = 20
# number_of_date = 48.9
# surname = "Ivanov"
# # 1. Конктенация.
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет.')
# print("My second name is " + surname + ". I'm " + str(number_of_date) + " y.o. ")
# # 2. %-форматирование
# print('Меня зовут %s. Мне %d лет.' % (name, age))
# print("My second name is %s. Im %d yo. " % (surname, number_of_date))
# print('Меня зовут %(x)s. Мне %(y)d лет.' % ({'y': age, 'x': name}))
# print("My name is %(x)s. Im %(y)d, %(x)s ." % ({'y': age, 'x': number_of_date}))
# # 3. Метод format()
# print('Меня зовут {}. Мне {} лет.'.format(name, age))
# print("My second name is {}. Im {}. ".format(surname, number_of_date))
# print('Меня зовут {x}. Мне {y} лет.'.format(x=name, y=age))
# print("My name {x}. Im {y} yo.".format(x=surname, y=number_of_date))
# # 4. f-строка
# print(f'Меня зовут {name}. Мне {age} лет.')
# print(f"My second name is {surname}.Im {number_of_date} yo.")
# pi = 3.1415926
# print(f'pi = {pi:.2f}')
# print(f"pi = {pi}")
# h, m = 2, 5
# hour, min = 3, 7
# print(f'Время на часах: {h:02d}:{m:02d}')
# print(f"Time is: {hour:02d}:{min:02d}")
# print(f'{1234567890:,}')  # 1,234,567,890
# print(f"{27821:,}")
# print(f'pi * age = {pi * age}')
# print(f"pi * number = {pi * number_of_date}")
# planets = ['Юпитер', 'Сатурн', 'Венера']
# names = ["Dima", "Sasha", "Kolya"]
# print(f'Субботу назвали в честь планеты {planets[1]}')
# print(f"His name is {names[1]}")
# print(f'Субботу назвали в честь планеты {planets[1].upper()}')
# print(f"His name is {names[2].upper()}")
# print(f'Округление 3.5 = {round(3.5)}, округление 4.5 = {round(4.5)}')  # to the nearset even number
# print(f"Rounding 5.67 = {round(5.67)}, {round(5.5)}, {round(5.3)}")
# print('{0:*^20}'.format('Выравнивание'))  # center
# print('{0:*^20}'.format("Name"))
# print('{0:*>20}'.format('Выравнивание'))
# print("{0:*>20}".format(54))  #todo "{0:*>20}" ?
# print('{0:*<20}'.format('Выравнивание'))
# print("{0:*<20}".format("Frog"))
# print('{1:*<20}'.format('Выравнивание', 'cat', 'dog'))
# print('{0:*<10}'.format("Leo", "snake")) #todo how to do it with both of words
# print(f'{"Выравнвиание":*^20}')  # center
# print(f'{"Center":=^20}')  #todo whats ^
# print(f'{"Выравнвиание":*>20}')   # on right
# print(f"{'on right':*>20}")
# print(f'{"Выравнвиание":*<20}')
# print(f"{'on left':*<20}")
#
# print('apple'.center(20, '*'))  # возвращает отцентрированную строку
# print("Dove".center(10, "*"))
# a, b, c = 5, 7, 9
# print(a, b, c, end='+++')  # end опеределяет, чем заканчивается вывод строки
# # print(a, b, c, end="*")
# # print(a, b, c, sep='---')  # sep определяет, что стоит между переменными
# print(a, b, c, sep="--")
# # Экранирование
# print(r'C:\new\table')  # "сырая" строка
# print('C:\\new\\table')  # с помощью \ #todo ?

#
# a = 12  # int целые числа
# a1 = 2
# b = 3.141592  # float дробные числа
# b1 = 5.76
# c = 'text 22'  # str строки
# c1 = 'text 31'
# d = [2, 2, 2, 6.7, 'text', [6, 7]]  # list список changeable
# d1 = [3, 5, 'text', [5, 7]]
# d1[3][0] = 6
# print(d1)
# d[5][1] = 8
# print(d)
# k1 = d1[3][0]
# print(k1)
# k = d[5][1]
# print(k)
# e = (2, 6.7, 'text')  # tuple кортеж  # not changeable, less weight, speed
# e1 = (2, 5.6, 'test')
# print(e1[0])
# print(e[0])
# f1 = True  # bool логический
# f11 = True
# f2 = False
# f22 = False
# m = {4, 5.6, 'cat', 4, 'cat'}  # set множества # random and changeable
# m1 = {5, 7.8, 'dog'}
# print(hash('dog'))
# print(hash('cat'))
# s = {'key': 'value', 'Alex': [5, 4, 3, 5]}  # dict словарь
# s1 = {'key1': 'float', 'Katerina': [3, 5, 6]}
# print(s1['key1'])
# print(s['Alex'])

# + - * /
# print(4 ** 2)  # возведение в степень
# print(5 ** 2)
# print(125 ** (1/3))  # кубический корень
# print(125 ** (1/3))
# print(-16 ** (1/2))
# print(-16 ** (1/2))
# print(pow(5, 2))  # возведение в степень
# print(pow(5, 2))
# print(pow(-16, 0.5))
# print(pow(-16, 0.5))
# # 4 * 4 = 16 ** (1/2) = 4
# # 2 * 2 * 2 = 8 ** (1/3) = 2
# print(7 // 3)  # целая часть от деления # how many times we put 3 in 7
# print(7 % 3)  # остаток от деления
# print(divmod(7, 3))  # (//, %)
# print(abs(-7))  # модуль числа

# a, b = (0,), 7
# # a, b = b, a
# if a and b > 0:
#     print('cat')

# False: False, None, 0, [], (), '', {}
# True: True, number != 0, len(iterable) > 0

# Строки str
# a = 'White cat black cat C'
# b = 'dog'
# c = 7
# # print(a + b + str(c))  # конкатенация
# print( a + b + str(c))
# # print(a, b, c)
# print(a, b, c)
# # print(b * 4)
# print(str(c) * 4)
# # print('-' * 70)
# print('=' * 5)
# # print('cat' in a)  # вхождение подстроки в строку
# print('white' in a)
# # print(len(b))  # длина строки
# print(len(str(c)))
# # print(a.count('cat'))  # считает количество подстрок в строке
# print(a.count('c'))
# # print(a.index('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет - ошибка
# print(a.index('cat'))
# # print(a.rindex('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет - ошибка
# print(a.rindex('cat'))
# # print(a.find('catee'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет -1
# print(a.find('caT'))
# # print(a.rfind('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет -1
# print(a.rfind('cat'))
# # print(a.replace('cat', 'cow').replace('black', 'red'))  # замена текста
# print(a.replace('cat', 'dog'))
# # print(a.replace('cat', 'cow', 1))  # замена текста
# print(a.replace('cat', 'dog', 1))
# # print(a.replace('t', ''))  # удаляем t
# print(a.replace('c', '', 1))
# # print('BMW'.lower())  # Перевести в нижний регистр
# print('BMW'.lower())
# # print('apple'.upper())  # перевести в верхний регистр
# print('bmw'.upper())
# # print('Apple'.swapcase())  # изменить регистр букв
# print('Bmw'.swapcase())
# # print(a.title())  # меняет первую букву каждого слова на заглавную, а остальные на строчные
# print(a.title())
# # print(a.capitalize())  # меняет первую букву строки на заглавную, а остальные на строчные
# print('White cat. Black cat'.capitalize())
# #
# s = 'white     cat    black         cat dog'
# # print(s.split(" "))  # разбивает строку по разделителю на список текстовых элементов, without an element in the text
# s1 = s.split('cat')
# print(s1)
# print(s.split('cat'))
# # # cANNOT BE BROKEN
# # print(s.split())  # по умолчанию делится по множественному пробелу, one separator
# print(s.split())
# # print('*'.join(['white', 'cat', 'black', 'cat']))  # склеивает в строку iterable текстовых элементов
# print(''.join(s1))
# #
#
# a = 'x y z a b'
# # print(a.split(maxsplit=2))  # можем указать количество разбиений
# print(a.split("x", maxsplit=2))
# # print(a.rsplit(maxsplit=2))  # разбиение с конца строки
# #
# # print('white cat\nblack cat')
# print('white cat\nblack cat')
# # print("white cat" + "\n" + "black cat")
# print('white cat' + '\n' + 'black cat')
# # print(a.splitlines())  # разбиваем по строкам (/n)
# print('white cat\nblack cat'.splitlines())
# # print(a.splitlines(keepends=True))  # сохраняем символ переноса строки
# print('White cat\nblack cat'.splitlines(keepends=True))
# #
# s = 'Discworld'
# # print(s.endswith('cat'))  # False
# print(s.endswith('cat'))
# # print(s.endswith('world'))  # True
# print(s.endswith('rld'))
# # print(s.endswith(('cat', 'world')))  # True / or
# print(s.endswith(('cat', 'world', 'fun')))
# # print(s.endswith('sc', 0, 4))  # True
# print(s.startswith('is', 0))
# # print(s.startswith('Disc'))  # True
# print(s.startswith('Disc'))
#
# a = 'apple'
# b = '12'
# c = 'apple 12'
# # print(a.isalpha())  # состоит ли только из букв
# print(a.isalpha())
# # print(a.isdigit())  # состоит ли только из цифр
# print(a.isdigit())
# # print(a.isalnum())  # состоит ли только из букв или цифр
# print(a.isalnum())
# # print(a.isspace())  # состоит ли только из пробельных символов (пробел, перевод строки \n, табуляция \t...)
# print('\n'.isspace())
# # print(a.islower())  # состоит ли строка из символов нижнего регистра
# print('acdjh'.islower())
# # print(a.isupper())  # состоит ли строка из символов верхнего регистра
# print('GHD'.isupper())
# # print(a.istitle())  # начинаются ли слова в строке с заглавных букв
# print('Gbjk'.istitle())

# fio = input('Введите ваши ФИО: ')
# if fio.istitle():
#     print(fio)
# else:
#     print(fio.title())
#
# print(fio if fio.istitle() else fio.title())

# # print(isinstance(a, (int, float, complex)))  # проверяет принадлежит ли переменная к тому или иному типу
# print(isinstance(a, (str)))
# # print(type(a))  # показывает тип переменной
# print(type(a))
# # print('****apple**'.strip('*'))  # удаляет с начала и конца строки указанные символы
# print('_** *cat***'.strip('*_')) #TODO doesnt work
# # print('****apple**'.rstrip('*'))  # удаляет с конца строки указанные символы
# print('**orange** *'.rstrip('*'))
# # print('****apple**'.lstrip('*'))  # удаляет с начала строки указанные символы
# print('* *orange-*'.lstrip('*'))
# # print('   apple         '.strip())  # по умолчанию удаляет пробельные символы
# print(' pie  '.strip())
# # print('+-*/-+apple+++---///*'.strip('+-*/'))
# print('*+-./pie.,.'.strip('*+-./,'))
# # print(ord(','))  # показывает код символа
# # print(chr(44))  # показывает символ по коду
# # print(chr(129519), chr(43458))
#
#
# # Интервалы, слайсы, slices, срезы
# a = 'white cat black cat'
# # print(a[3])  # t
# print(a[3])
# # print(a[-1])  # t
# print(a[-2])
# # print(a[6:9])  # с 6 по 8 символы, последний не включительно
# print(a[4:5])
# # print(a[:5])  # с начала строки по 4 символы
# print(a[:5])
# # print(a[16:])  # с 16 до конца строки
# print(a[16:])
# # print(a[:-3])  # cat
# print(a[:-10])
# # print(a[6:16:2])  # c 6 по 15 с шагом 2
# print(a[::2])
# # print(a[::-1])  # развернуть строку
# print(a[::-2])
# #
# t = 'шалашf'
# print("polidrom" if t[::-1] == t else "not polidrom")

# Списки list
# a = [1, 2, 3, 2, 2]
# b = [5, 6, 7]
# s = ['cat', 'dog', 'cow', '5apple']
# #
# # print(a + b)
# print(a + b)
# # print(b * 4)
# print(s[1] * 4)
# # print(a[1:4])
# print(s[1:3])
# # print(5 in b)  # проверяем вхождение 1 элемента в список
# print(1 in b)
# # print(len(a))  # длина списка
# print(len(s))
# # print(max(b))  # максимальное в списке b
# print(max(b))
# # print(max(s, key=len))  # с помощью key можем изменить критерий сортировки
# print(max(s, key=len))
# # print(min(s))  # минимальное в списке b
# print(min(s, key=len))
# # print(a.count(2))  # считает количество указанных элементов
# print(a.count(2))
# # print(a.index(2))  # возвращает индекс вхождения ПЕРВОГО найденного элемента, от start до end
# print(a.index(2))
# # print(sum(b))  # возвращает сумму элементов
# print(sum(b))
# m2 = [1, 2, 3, 2, 2]
# m = ['cat', 'dog', 'cows', 'apple']
# print(sum([m], []))  # из двумерного списка делаем одномерный
# # print(sorted(m, key=len, reverse=True))  # возвращает отсортированный итерируемый объект
# print(sorted(m, key=len, reverse=True))
# # print(m)
# # m.sort(key=len, reverse=True)  # сортирует исходный список # reverse - backwards
# m.sort(key=len, reverse=True)
# print(m)
# # m.reverse()  # разворачивает список [::-1]
# m.reverse()
# print(m)
# # m.append(7)  # добавляет элемент в конец списка
# m.append(8)
# print(m)
# # print(m)
# m.extend(m2)
# print(m)
# # m.extend(m2)  # добавляет элементы m2 в конец списка m
# # m.extend('cat')
# print(m)
# # m.insert(1, 8)  # добавить 8 по индексу 1
# m.insert(1, [6, 8])
# print(m)
# # print(m)
# # m[0] = [1, 2]   # change object in list by index
# m[1] = 9
# print(m)
# # m[2:4] = [7, 8, 9]
# m[3:3] = [5, 7, 8]
# print(m)
# # m[2:2] = [10, 20, 30]
# # print(m)
# # m.remove(2)  # удаляет первый найденый элемент
# m.remove(2)
# print(m)
# # d = m.pop(2)  # удаляет элемент по индексу и возвращает его
# # d = m.pop(2)
# # print(d, m)
# # print(m, d)
# # d = m.pop()  # по умолчанию - последний элемент
# d1 = m.pop()
# print(m, d1)
# # del m[1]  # удаляет по индексу
# del m[1]
# print(m)
# # m2 = m.copy()  # поверхностная копия списка
# m2 = m.copy()
# print(m2)
# # m2.clear()  # очистка списка
# m2.clear()
# print(m2)
# # print(m2)

#
# from copy import deepcopy
# m = [1, 2, 3, [7, [8, 9]]]
# z = m.copy()
# print(z)
# m2 = deepcopy(m)
# print(m, m2)
# # z = m.copy()
# # m2 = deepcopy(m)  # глубокое копирование, each id changeable
# m[3][1][0] = 9
# # print(m, m2)
# print(id(m2[3]), id(z[3]), id(m[3]))
# # print(id(m[3]), id(m2[3]))
# #
# x = [1, 2, 3]
# # # x2 = x[:]
# x2 = x[:]
# # # x2 = x * 1
# x2 *= 1
# print(x2)
# # x2 = x + []
# x2 = x + []
# print(x2)
# # x[0] = 5
# x[0] = 5
# print(x)
# print(x, x2)

# # Множества set
# s = [1, 'cat', 'dog', 'cat', 5, 5, 'dog']
# # m = set(s)
# m1 = set(s)
# print(m1)
# # print(m)
# # print(set('apple'))
# print(set('apple'))
# print(len(m1))
# print(1 in m1)
# # print(len(m))
# # print(2 in m)
# #
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = {5, 6}
#
# # print(b.isdisjoint(c))  # True, если НЕ имеются общие элементы
# print(b.isdisjoint({3}))
# # print(c.issubset(b))  # c <= b
# print(b.issubset({3, 4, 5}))
# # print(c <= b)
# # print(b.issuperset(c))  # b >= c
# print(b.issuperset({3, 8, 7}))
# # print(b >= c)
# #
# football = {'A', 'B', 'C'}
# chess = {'B', 'C', 'D'}
# #
# # print(football.union(chess))  # объединение
# # print(football | chess)
# print(football.union(chess))
# print(football | chess)
# # print(football.intersection(chess))  # пересечение
# # print(football & chess)
# print(football.intersection(chess))
# print(football & chess)
# # print(football.difference(chess))  # разница
# # print(football - chess)
# print(football.difference(chess))
# print(football - chess)
# # print(football.symmetric_difference(chess))  # симетричная разница (объединяем множества и удаляем пересечение)
# # print(football ^ chess)
# print(football.symmetric_difference(chess))
# print(football ^ chess)
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# #
# # a.intersection_update(b)  # a = a & b    a &= b
# # print(a)
# a.intersection_update(b)
# print(a)
# # b.difference_update(a)  # b = b - a    b -= a
# # print(b)
# b.difference_update(a)
# print(b)
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# #
# # a.symmetric_difference_update(b)  # a = a ^ b, a ^= b
# # print(a)
# a.symmetric_difference_update(b)
# print(a)
# # a.add('apple')  # добавляет элемент в множество (неизменяемого типа)
# a.add('cat')
# a = a | {9}
# print(a)
# # a |= {9}
# # print(a)
# #
# # a.update({3, 4})  # объедияет элементы итерируемого объекта с множеством
# a.update({3, 4})
# a.update('cow')
# a.update([9, 7])
# print(a)
# # a.update('cat and grape')
# # print(a)
# #
# # a.remove(2)  # удаляет элемент множества, если элемента нет - ошибка
# # print(a)
# a.remove(2)
# print(a)
# # a.discard(50)  # удаляет элемент множества, если элемента нет - pass
# # print(a)
# a.discard(50)
# print(a)
# # d = a.pop()  # удаляет и возвращает случайный элемент множества ("первый" элемент)
# # print(d, a)
# a.pop()
# print(a)
# # a2 = a.copy()  # копия множества
# # a2.clear()  # очистка множества
# a2 = a.copy()
# a2.clear() # todo why outoot None if a.clear(
# print(a2)
# a = {'d', 'p', 'c', 'e', 't', 'n', 'apple', 'a', 'g', 'r'}
# # print(sorted(a))
# print(sorted(a))
# #
# x = [1, 2, 3, 4]
# y = [3, 4, 5, 6]
# # x = list(set(x) - set(y))
# # print(x)
# x = list(set(x) - set(y))
# print(x)
# animals = ['cat', 'dog', 'cow', 'rabbit', 'elefant', 'dog']
# # animals = set(animals).pop()
# animals = set(animals).pop()
# print(animals)
# animals = list(set(animals))
# print(animals)
# animals = list(set(animals))
# print(animals)
#
# # a, b, *c = animals
# a, b, *c = ['ab', 'cd', 'fg', 'gh']
# # a, b, *c = range(3)
# a, b, *c = range(6)
# # a, b, *c = {'cat', 'dog', 'cow', 'rabbit'}
# print(a, b, c)

# Словарь dict
# # a = {'key': 'value', 1: 'one', 5.8: 'five', True: 'yes', (1, 9): 7.9}
# a = {'key': 'value', 1: 'one', 5.8: 'five', True: 'yes', (1, 9): 7.9}
# # b = dict([(7, 1), ('b', ' cat')])
# b = dict([(7, 1), ('b', 'cat')])
# # c = dict(key1='cat', key2='dog', key3=7)
# c = dict(five='cat', two='dog', key3=7)
# print(a, b, c)
# # print(b, c)
# # print(a)
# d = {1: 'cat', 1.0: 'dog', True: 'cow'}
# d = {0: 'cat', 0.0: 'dog', False: 'cow'}
# print(d)
# print(hash(True), hash(1), hash(1.0))
# week = {
#     'Выходной': 'Воскресенье',
#     1: 'Понедельник',
#     2: 'Вторник',
#     3: 'Среда',
#     4: 'Четверг'
# }
# # print(week['Выходной'])  # возвращает значение по ключу, используем, если уверены в наличие ключа
# print(week['Выходной'])
# # print(week.get(22, 'Такого ключа нет!'))  # возвращает значение по ключу, если ключа нет - None
# print(week.get(22, 'There is no version'))
# # print(week.setdefault(5, 'Пятница'))  # возвращает значение по ключу, если ключа нет - создаст такой ключ
# print(week.setdefault(5, 'Friday'))
# print(week)
# # print(week.keys())  # возвращает все ключи
# print(week.keys())
# # print(week.values())  # возвращает все значения
# print(week.values())
# # print(week.items())  # возвращает (ключ, значение)
# print(week.items())
# print(week)
# # week.update({6: 'Суббота'})  # добавляет элемент(ы) словаря
# week.update({6: 'Saturday'})
# # week[7] = 'Воскресенье'
# print(week)
# week[7] = 'Sunday'
# print(week)
# # del week[4]  # удаляет элемент словаря по ключу
# del week[4]
# print(week)
# # d = week.pop(50, 'Значение')  # удаляет элемент по ключу и возвращает его значение, если ключа нет - возратит Значение
# d = week.pop(50, 'Value')
# print(week, d)
# # week2 = week.copy()  # поверхностная копия словаря
# week2 = week.copy()
# week2.clear()
# print(week, week2)
# # week2.clear()  # очистить словарь
# #
# s = {'a': 1, 'b': 2, 'cat': 'animal'}
# # item = s.popitem()  # удаляет и возвращает последнюю пару (ключ, значение)  python >= 3.7
# item = s.popitem()
# print(s, item)
# # print(s, item)
# #
# # d = {}.fromkeys(['cat', 'dog', 'cow'], 0)  # создаёт слвоарь из iterable ключей с одним значением для всех ключей, по умолчанию - None
# d = {}.fromkeys(['cat', 'dog', 'cow'], [6])
# print(d)
# print(d)
#
# #
# # z = {i: [] for i in ['cat', 'dog', 'cow']}
# # z['cow'].append('grass')
# # print(z)
# #
# id_users = {
#     12: 'Alex',
#     22: 'Alice',
#     47: 'Tom'
# }
# user = 12
# print(f'Привет, {id_users.get(user, "Stranger")}')
# #
# x = {1: 'one', 2: 'two'}
# y = {2.0: 'cat', True: 'dog'}
# # z = {**x, **y}  # объединение словарей
# z = {**x, **y}
# print(z)
# #
# # z2 = y | x  # объединение словарей python >= 3.9
# x2 = y | x
# # print(z2)
# #
# # # Сортировка словаря по значениям
# store = {'apple': 40, 'oranges': 80, 'ananas': 70, 'banana': 10}
# # print(sorted(store, key=store.get))
# print(sorted(store, key=store.get))
# print(sorted(store.values()))
# print(sorted(store, key=len))
# #
# from collections import Counter
#
# items = ['apple', 'banana', 'apple', 'grape', 'banana', 'apple']
# cf = Counter(items)
# print(cf)
# print(cf.most_common())
# print()
# from collections import Counter
#
# items = ['apple', 'banana', 'apple', 'grape', 'banana', 'apple']
# cf = Counter(items)  # создаёт итератор подсчёта количества элементов
# print(cf)
# print(cf['apple'])
# print(cf.most_common())  # возвращает список кортежей подсчёта элементов

# Многомерные массивы
# x = [0] * 2
# x = [0] * 2
# # print(x)
# # # y = [0 for i in range(4)]
# y = [0 for i in range(4)]
# # # print(x)
# print(y)
# # #
# # # z = [[0] * 2 for i in range(4)]  # !!!
# z = [[0] * 2 for i in range(4)]
# print(z)
# # # t = [x for i in range(4)]
# t = [x for i in range(4)]
# print(t)
# z[0][1] = 1
# print(z)
# z[0][1] = 1
# print(z)
# # [[0, 0], [0, 0], [0, 0], [0, 0]]
#
# b = [[[0] * 2 for i in range(4)] for k in range(2)]
# b[0][0][1] = 1
# print(b)
# [[[0, 0], [0, 0], [0, 0], [0, 0]],  [[0, 0], [0, 0], [0, 0], [0, 0]]]
#
# # a = 12  # int целые числа
# a = 12
# # b = 3.141592  # float дробные числа
# b = 3.47
# print(b)
# # c = 'text 22'  # str строки
# c = 'text 22'
# print(c)
# # d = [2, 2, 2, 6.7, 'text', [6, 7]]  # list список changeable
# d = [2, 5, 6, 3, 'text', [5, 4]]
# print(d)
# d[5][0] = 1
# print(d[5])
# # d[5][1] = 8
# # print(d)
# # k = d[5][1]
# k = d[5][1]
# print(k)
# # print(k)
# # e = (2, 6.7, 'text')  # tuple кортеж  # not changeable, less weight, speed
# e = (2, 6.7, ' text 22')
# print(e[0])
# # print(e[0])
# # f1 = True  # bool логический
# f1 = True
# # f2 = False
# f2 = False
# # m = {4, 5.6, 'cat', 4, 'cat'}  # set множества # random and changeable
# m = {4, 5.6, 'cat'}
# print(m)
# print(hash('key'))
# # print(hash('cat'))
# # s = {'key': 'value', 'Alex': [5, 4, 3, 5]}  # dict словарь
# s = {'key': 'value', 'Alex': [5, 4, 5]}
# print(s['Alex'])
# # print(s['Alex'])
#
# # # import math
# # # print(math.cos(math.pi))
# #
# import math
# print(math.cos(math.pi))
# # # + - * /
# # print(4 ** 2)  # возведение в степень
# print(4 ** 2)
# # print(125 ** (1/3))  # кубический корень
# print(125 ** (1/3))
# # print(-16 ** (1/2))
# print(-16 ** (1/2))
# # print(pow(5, 2))  # возведение в степень
# print(pow(5, 2))
# # print(pow(4, 2))
# print(pow(4, 2))
# print(pow(-16, 0.5))
# # 4 * 4 = 16 ** (1/2) = 4
# # 2 * 2 * 2 = 8 ** (1/3) = 2
# # print(7 // 3)  # целая часть от деления # how many times we put 3 in 7
# print(7 // 3)
# # print(7 % 3)  # остаток от деления
# print(3 % 7)
# # print(divmod(7, 3))  # (//, %)
# print(divmod(7, 3))
# print(divmod(1000, 10))
# # print(divmod(28, 10))
# # print(abs(-7))  # модуль числа
# print(abs(7))



# a, b = (0,), 7
# a, b = (0,), 7
# if a and b > 0:
#     print('cat')
# # a, b = b, a
# if a and b > 0:
#     print('cat')

# False: False, None, 0, [], (), '', {}
# True: True, number != 0, len(iterable) > 0

# day_value = input("Whats the day today ")
# print("Today is a weekend" if day_value == "Sunday" or day_value == "Saturday" else "Today is a working day")

# # Строки str
# # a = 'White cat black cat'
# a = 'White cat black cat'
# b = 'dog'
# c = 7
# # b = 'dog'
# # c = 7
# # print(a + b + str(c))  # конкатенация
# print(a + b + str(c))
# print(a, b, c)
# # print(a, b, c)
# print(4 * b)
# # print(b * 4)
# print('/' * 70)
# # print('-' * 70)
# # print('cat' in a)  # вхождение подстроки в строку
# print('cat' in a)
# # print(len(b))  # длина строки
# print(len(b))
# # print(a.count('cat'))  # считает количество подстрок в строке
# print(a.count('cat'))
# # print(a.index('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет - ошибка
# print(a.index('cat'))
# # print(a.rindex('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет - ошибка
# print(a.rindex('cat'))
# # print(a.find('catee'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет -1
# print(a.find('cate'))
# # print(a.rfind('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет -1
# print(a.rfind('cate'))
# # print(a.replace('cat', 'cow').replace('black', 'red'))  # замена текста
# print(a.replace('cat', 'dog'))
# print(float(False))
# # print(a.replace('cat', 'cow', 1))  # замена текста
# # print(a.replace('t', ''))  # удаляем t
# print(a.replace('t', '', 1))
# # print('BMW'.lower())  # Перевести в нижний регистр
# print('BMW'.lower())
# # print('apple'.upper())  # перевести в верхний регистр
# print('apple'.upper())
# # print('Apple'.swapcase())  # изменить регистр букв
# print('aPple'.swapcase())
# # print(a.title())  # меняет первую букву каждого слова на заглавную, а остальные на строчные
# print(a.title())
# # print(a.capitalize())  # меняет первую букву строки на заглавную, а остальные на строчные
# print(a.capitalize())
# #
# # s = 'white     cat    black         cat dog'
# s = 'white   cat black   cat dog'
# print(s.split(' '))
# # print(s.split(" "))  # разбивает строку по разделителю на список текстовых элементов, without an element in the text
# # # cANNOT BE BROKEN
# # print(s.split())  # по умолчанию делится по множественному пробелу, one separator
# # print('*'.join(['white', 'cat', 'black', 'cat']))  # склеивает в строку iterable текстовых элементов
# print('*'.join(['white', 'cat']))
# #
#
# # a = 'x y z a b'
# a = 'x, y, r, e'
# print(a.split(maxsplit=2))
# # print(a.split(maxsplit=2))  # можем указать количество разбиений
# # print(a.rsplit(maxsplit=2))  # разбиение с конца строки
# #
# # print('white cat\nblack cat')
# print('white cat\nblack cat')
# print('white cat', 'white cat', sep='\n')
# print('white cat' + '\n' + 'black cat')
# # print("white cat" + "\n" + "black cat")
# # print(a.splitlines())  # разбиваем по строкам (/n)
# print(a.splitlines())
# print(a.split())
# # print(a.splitlines(keepends=True))  # сохраняем символ переноса строки
# print(a.splitlines(keepends=True))
# # s = 'Discworld'
# s = 'Discworld'
# # print(s.endswith('cat'))  # False
# print(s.endswith('cat'))
# # print(s.endswith('world'))  # True
# print(s.endswith('world'))
# # print(s.endswith(('cat', 'world')))  # True / or
# print(s.endswith(('cat', 'd')))
# # print(s.endswith('sc', 0, 4))  # True
# # print(s.endswith('sx', 0, 4, 'ld'))
# # print(s.startswith('Disc'))  # True
# print(s.startswith(('Disc', 'fg')))
# a = 'apple'
# b = '12'
# c = 'apple 12'
# # print(a.isalpha())  # состоит ли только из букв
# print(a.isalpha())
# # print(a.isdigit())  # состоит ли только из цифр
# print(a.isdigit())
# # print(a.isalnum())  # состоит ли только из букв или цифр
# print(a.isalnum())
# # print(a.isspace())  # состоит ли только из пробельных символов (пробел, перевод строки \n, табуляция \t...)
# print(' '.isspace())
# # print(a.islower())  # состоит ли строка из символов нижнего регистра
# print(a.islower())
# # print(a.isupper())  # состоит ли строка из символов верхнего регистра
# print('FROG'.isupper())
# # print(a.istitle())  # начинаются ли слова в строке с заглавных букв
# print('White Cat'.istitle())
# # fio = input('Введите ваши ФИО: ')
# # if fio.istitle():
# #     print(fio)
# # else:
# #     print(fio.title())
# #
# # print(fio if fio.istitle() else fio.title())
#
# # print(isinstance(a, (int, float, complex)))  # проверяет принадлежит ли переменная к тому или иному типу
# print(isinstance(a, (int, float, str)))
# # print(type(a))  # показывает тип переменной
# print(type(a))
# # print('****apple**'.strip('*'))  # удаляет с начала и конца строки указанные символы
# print('***apple***'.lstrip('* '))
# # print('****apple**'.rstrip('*'))  # удаляет с конца строки указанные символы
# # print('****apple**'.lstrip('*'))  # удаляет с начала строки указанные символы
# # print('   apple         '.strip())  # по умолчанию удаляет пробельные символы
# print('  apple          '.strip())
# print('+-*/-+apple+++---///*'.strip('+-*/'))
# # print(ord(','))  # показывает код символа
# print(ord(','))
# # print(chr(44))  # показывает символ по коду
# print(chr(44))
# print(chr(129519), chr(43458))
#
# for i in range(1, 55296):
#     print(chr(i), end=' ')
#     if i % 60 == 0:
#         print('\n', i, ': ', end='')

# Тернарный оператор
# if expression:
#     on_true
# else:
#     on_false
#
# on_true if expression else on_false
#
# Интервалы, слайсы, slices, срезы
# a = 'white cat black cat'
# # print(a[3])  # t
# print(a[3])
# # print(a[-1])  # t
# print(a[-2])
# # print(a[6:9])  # с 6 по 8 символы, последний не включительно
# print(a[6:8])
# # print(a[:5])  # с начала строки по 4 символы
# print(a[:6])
# # print(a[16:])  # с 16 до конца строки
# print(a[16:])
# # print(a[:-3])  # cat
# print(a[:-3])
# # print(a[6:16:2])  # c 6 по 15 с шагом 2
# print(a[6:16:2])
# # print(a[::-1])  # развернуть строку
# print(a[::-1])
# #
# t = 'шалашf'
# print("polidrom" if t[::-1] == t else "not polidrom")

# # Списки list
# a = [1, 2, 3, 2, 2]
# b = [5, 6, 7]
# s = ['cat', 'dog', 'cow', '5apple']
# #
# # print(a + b)
# print(a + b)
# # print(b * 4)
# print(b * 4)
# # print(a[1:4])
# print(a[1:6])
# # print(5 in b)  # проверяем вхождение 1 элемента в список
# print( 5 in b)
# # print(len(a))  # длина списка
# print(len(a))
# # print(max(b))  # максимальное в списке b
# print(max(b))
# # print(max(s, key=len))  # с помощью key можем изменить критерий сортировки
# print(max(s, key=len))
# # print(min(s))  # минимальное в списке b
# print(min(s, key=len))
# # print(a.count(2))  # считает количество указанных элементов
# print(s.count('cat'))
# # print(a.index(2))  # возвращает индекс вхождения ПЕРВОГО найденного элемента, от start до end
# print(a.index(2))
# # print(sum(b))  # возвращает сумму элементов
# print(sum(b))
# m2 = [1, 2, 3, 2, 2]
# m = [['cat', 'dog'], ['cows', 'apple']]
# # print(sum(m, []))  # из двумерного списка делаем одномерный
# print(sum(m, []))
# print(sum(m2, 100))
# # # print(sorted(m, key=len, reverse=True))  # возвращает отсортированный итерируемый объект
# print(sorted(m, key=len, reverse=True))
# print(m)
# # print(m)
# # m.sort(key=len, reverse=True)  # сортирует исходный список # reverse - backwards
# # print(m)
# m.sort(key=len, reverse=True)
# print(m)
# # m.reverse()  # разворачивает список [::-1]
# # print(m)
# m.reverse()
# print(m)
# # m.append(7)  # добавляет элемент в конец списка
# # print(m)
# m.append(7)
# print(m)
# # m.extend(m2)  # добавляет элементы m2 в конец списка m
# # m.extend('cat')
# # print(m)
# m.extend(m2)
# print(m)
# m.insert(1, 8)
# print(m)
# # m.insert(1, 8)  # добавить 8 по индексу 1
# # print(m)
# # m[0] = [1, 2]   # change object in list by index
# # print(m)
# m[0] = [1, 2]
# print(m)
# # m[2:4] = [7, 8, 9]
# # print(m)
# m[2:4] = [7, 8, 9]
# print(m)
# # m[2:2] = [10, 20, 30]
# # print(m)
# m[2:2] = [10, 30, 40]
# print(m)
# # m.remove(2)  # удаляет первый найденый элемент
# # print(m)
# m.remove(2)
# print(m)
# # d = m.pop(2)  # удаляет элемент по индексу и возвращает его
# # print(m, d)
# d = m.pop()
# print(d)
# # d = m.pop()  # по умолчанию - последний элемент
# # print(m, d)
# # del m[1]  # удаляет по индексу
# # print(m)
# del m[1]
# print(m)
# # m2 = m.copy()  # поверхностная копия списка
# m2 = m.copy()
# print(m2)
# m2.clear()
# print()
# # m2.clear()  # очистка списка
# # print(m2)
# #
# # from copy import deepcopy
# from copy import deepcopy
# m = [1, 2, 3, [7, [8, 9]]]
# z = m.copy()
# m2 = deepcopy(m)
# m[3][1][0] = 9
# print(m, m2)
# # z = m.copy()
# # m2 = deepcopy(m)  # глубокое копирование, each id changeable
# # m[3][1][0] = 9
# # print(m, m2)
# print(id(m[3]), id(m2[3]))
# #
# x = [1, 2, 3]
# # # x2 = x[:]
# x2 = x[:]
# x3 = x * 1
# print(x3)
# x4 = x + []
# print(x)
# # # x2 = x * 1
# # x2 = x + []
# # x[0] = 5
# x[0] = 5
# print(x, x2)
# # print(x, x2)

# Основные способы форматирования строк:
# name = 'Alice'
# age = 20
# test = 'text'
# # # 1. Конктенация.
# # print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет.')
# print('My name is ' + name + '. I am ' + str(age) + ' years old.')
# # # 2. %-форматирование
# # print('Меня зовут %s. Мне %d лет.' % (name, age))
# print('My name %s. I am %d years old.' % (name, age))
# # print('Меня зовут %(x)s. Мне %(y)d лет.' % ({'y': age, 'x': name}))
# print('My name %(x)s. I am %(y)d years old.' % ({'y': age, 'x': name}))
# # # 3. Метод format()
# # print('Меня зовут {}. Мне {} лет.'.format(name, age))
# print('My name {}. I am {} y.o.'.format(name, age))
# # print('Меня зовут {x}. Мне {y} лет.'.format(x=name, y=age))
# print('My name is {x}. I am {y} years old.'.format(x=name, y=age))
# # # 4. f-строка
# # print(f'Меня зовут {name}. Мне {age} лет.')
# print(f'My name is {name}. I am {age} y.o.')
# pi = 3.1415926
# # print(f'pi = {pi:.2f}')
# print(f'pi = {pi:.2f}')
# h, m = 2, 5
# print(f'Time is: {h:02d}:{m:02d}')
# # print(f'Время на часах: {h:02d}:{m:02d}')
# # print(f'{1234567890:,}')  # 1,234,567,890
# print(f'{123456789:,}')
# # print(f'pi * age = {pi * age}')
# print(f'pi * age = {pi * age}')
# planets = ['Юпитер', 'Сатурн', 'Венера']
# # print(f'Субботу назвали в честь планеты {planets[1]}')
# print(f'Saturday was named after the planet {planets[1]}')
# # print(f'Субботу назвали в честь планеты {planets[1].upper()}')
# print(f'Saturday was named after the planet {planets[1].upper()}')
# # print(f'Округление 3.5 = {round(3.5)}, округление 4.5 = {round(4.5)}')  # to the nearset even number
# print(f'3.5 = {round(3.5)}, 4.5 = {round(4.5)}')
# #
# # print('{0:*^20}'.format('Выравнивание'))  # center
# print('{0:*^10}'.format('Round'))
# # print('{0:*>20}'.format('Выравнивание'))
# # print('{0:*<20}'.format('Выравнивание'))
# # print('{1:*<20}'.format('Выравнивание', 'cat', 'dog'))
# # print()
# # print(f'{"Выравнвиание":*^20}')  # center
# # print(f'{"Выравнвиание":*>20}')   # right
# # print(f'{"Выравнвиание":*<20}')
# #
# # # print('apple'.center(20, '*'))  # возвращает отцентрированную строку
# print('apple'.center(20, '*'))
# a, b, c = 5, 7, 9
# # print(a, b, c, end='+++')  # end опеределяет, чем заканчивается вывод строки
# print(a, b, c, end='\n')
# # print(a, b, c, sep='---')  # sep определяет, что стоит между переменными
# print(a, b, c)
# #
# # # Экранирование
# # print(r'C:\new\table')  # "сырая" строка
# print(r'C:\new\table')
# # print('C:\\new\\table')  # с помощью \
# print('C:\\new\\table')
# # print('C:\new\table')

# Множества set
# s = [1, 'cat', 'dog', 'cat', 5, 5, 'dog']
# m = set(s)
# print(m)
# # print(m)
# # print(set('apple'))
# print(set('apple'))
# # print(len(m))
# print(len(m))
# # print(2 in m)
# print(1 in m)
# #
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = {5, 6}
# #
# # print(b.isdisjoint(c))  # True, если НЕ имеются общие элементы
# print(b.isdisjoint(c))
# # print(c.issubset(b))  # c <= b TRUE if all items are the same
# print(b.issubset(c))
# # print(c <= b)
# print(c >= b)
# # print(b.issuperset(c))  # b >= c
# print(b.issuperset(c))
# # print(b >= c)
# print(b >= c)
# #
# football = {'A', 'B', 'C'}
# chess = {'B', 'C', 'D'}
# #
# # print(football.union(chess))  # объединение
# print(football.union(chess))
# print(football | chess)
# # print(football | chess)
# #
# # print(football.intersection(chess))  # пересечение
# print(football.intersection(chess))
# print(football & chess)
# # print(football & chess)
# #
# # print(football.difference(chess))  # разница
# print(football.difference(chess))
# print(football - chess)
# print(chess - football)
# # print(football - chess)
# #
# # print(football.symmetric_difference(chess))  # симетричная разница (объединяем множества и удаляем пересечение)
# print(football.symmetric_difference(chess))
# print(football ^ chess)
# # print(football ^ chess)
# #
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# #
# # a.intersection_update(b)  # a = a & b    a &= b
# a.intersection_update(b)
# print(a)
# a = a & b
# print(a)
# # print(a)
# #
# # b.difference_update(a)  # b = b - a    b -= a
# b.difference_update(a)
# print(b)
#
# # print(b)
# #
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# #
# # a.symmetric_difference_update(b)  # a = a ^ b, a ^= b
# a.symmetric_difference_update(b)
# print(a)
# a = a ^ b
# print(a)
# # print(a)
# # exit()
# #
# # a.add('apple')  # добавляет элемент в множество (неизменяемого типа)
# a.add('apple')
# print(a)
# # a |= {9}
# # print(a)
# a = a | {9}
# print(a)
# #
# # a.update({3, 4})  # объедияет элементы итерируемого объекта с множеством
# a.update({3, 4})
# print(a)
# a.update('cat and grape')
# print(a)
# #
# a.remove(2)
# print(a)
# # a.remove(2)  # удаляет элемент множества, если элемента нет - ошибка
# # print(a)
# #
# # a.discard(50)  # удаляет элемент множества, если элемента нет - pass
# a.discard(50)
# print(a)
# # print(a)
# #
# # d = a.pop()  # удаляет и возвращает случайный элемент множества ("первый" элемент)
# d = a.pop()
# print(d)
# # print(d, a)
# #
# # a2 = a.copy()  # копия множества
# a2 = a.copy()
# print(a, a2)
# # a2.clear()  # очистка множества
# a2.clear()
# print(a2)
# #
# a = {'d', 'p', 'c', 'e', 't', 'n', 'apple', 'a', 'g', 'r'}
# # print(sorted(a))
# print(sorted(a))
# #
# #
# x = [1, 2, 3, 4]
# y = [3, 4, 5, 6]
# # x = list(set(x) - set(y))
# x = set(x) - set(y)
# print(x)
# # print(x)
# #
# animals = ['cat', 'dog', 'cow', 'rabbit', 'elefant']
# # # animals = set(animals).pop()
# animals = list(set(animals).pop())
# print(animals)
# # animals = list(set(animals))
# # print(animals)
# #
# # a, b, *c = animals
# a, b, *c = animals
# a, b, *c = range(3)
# a, b, *c = {'cat', 'dog', 'cow', 'rabbit'}
# print(a, b, c)

# # Словарь dict
# # a = {'key': 'value', 1: 'one', 5.8: 'five', True: 'yes', (1, 9): 7.9}
# a = {'key': 'value', 1: 'one', 5.8: 'five', True: 'yes', (1, 9): 7.9}
# b = dict([(7, 1), ('b', 'cat')])
# # b = dict([(7, 1), ('b', 'cat')])
# c = dict(key1='cat', key2='dog', key3=7)
# print(a)
# print(b, c)
# # c = dict(key1='cat', key2='dog', key3=7)
# #
# # # print(b, c)
# # print(a)
# # d = {1: 'cat', 1.0: 'dog', True: 'cow'}
# d = {1: 'cat', 1.0: 'dog', True: 'cow'}
# # d = {0: 'cat', 0.0: 'dog', False: 'cow'}
# d = {0: 'cat', 0.0: 'dog', False: 'cow'}
# print(d)
# print(hash(True), hash(1), hash(1.0))
# week = {
#     'Выходной': 'Воскресенье',
#     1: 'Понедельник',
#     2: 'Вторник',
#     3: 'Среда',
#     4: 'Четверг'
# }
# # print(week['Выходной'])  # возвращает значение по ключу, используем, если уверены в наличие ключа
# print(week[1])
# # print(week.get(22, 'Такого ключа нет!'))  # возвращает значение по ключу, если ключа нет - None
# print(week.get(2, 'There is no the key'))
# # print(week.setdefault(5, 'Пятница'))  # возвращает значение по ключу, если ключа нет - создаст такой ключ
# print(week.setdefault(5, 'Friday'))
# # print(week.keys())  # возвращает все ключи
# print(week.keys())
# # print(week.values())  # возвращает все значения
# print(week.values())
# # print(week.items())  # возвращает (ключ, значение)
# print(week.items())
# print(week)
# # week.update({6: 'Суббота'})  # добавляет элемент(ы) словаря
# week.update({6: 'Saturday'})
# print(week)
# week[7] = 'Sunday'
# print(week)
# # week[7] = 'Воскресенье'
# # print(week)
# # del week[4]  # удаляет элемент словаря по ключу
# del week[4]
# print(week)
# # print(week)
# d = week.pop(50, 'Value')
# print(d)
# # d = week.pop(50, 'Значение')  # удаляет элемент по ключу и возвращает его значение, если ключа нет - возратит Значение
# # print(week, d)
# week2 = week.copy()
# print(week2)
# # week2 = week.copy()  # поверхностная копия словаря
# # week2.clear()  # очистить словарь
# week2.clear()
# print(week2)
# #
# s = {'a': 1, 'b': 2, 'cat': 'animal'}
# # item = s.popitem()  # удаляет и возвращает последнюю пару (ключ, значение)  python >= 3.7
# item = s.popitem()
# print(item)
# # print(s, item)
# #
# # d = {}.fromkeys(['cat', 'dog', 'cow'], 0)  # создаёт слвоарь из iterable ключей с одним значением для всех ключей, по умолчанию - None
# d = {}.fromkeys(['cat', 'dog', 'cow'], 0)
# print(d)
# d['cow'] += 5
# print(d)
# # print(d)
# # d['cow'] += 5
# # print(d)
# #
# z = {i: [] for i in ['cat', 'dog', 'cow']}
# z['cow'].append('grass')
# print(z)
# #
# id_users = {
#     12: 'Alex',
#     22: 'Alice',
#     47: 'Tom'
# }
# user = 222
# # print(f'Привет, {id_users.get(user, "Stranger")}')
# #
# x = {1: 'one', 2: 'two'}
# print(x)
# y = {2.0: 'cat', True: 'dog'}
# print(y)
# # z = {**x, **y}  # объединение словарей
# z = {**x, **y}
# print(z)
# # print(z)
# #
# # z2 = y | x  # объединение словарей python >= 3.9
# z2 = y | x
# print(z2)
# # print(z2)
# #
# # # Сортировка словаря по значениям
# store = {'apple': 40, 'oranges': 80, 'ananas': 70, 'banana': 10}
# print(store)
# print(sorted(store, key=store.get))
# print(store.get('oranges'))
# # print(sorted(store, key=store.get))
# # print(sorted(store.values()))
# print(sorted(store.values()))
# # print(sorted(store, key=len))
# print(sorted(store, key=len))
# print(sorted(store))
# # from collections import Counter
# #
# from  collections import Counter
# # items = ['apple', 'banana', 'apple', 'grape', 'banana', 'apple']
# items = ['apple', 'banana', 'apple', 'grape']
# # cf = Counter(items)  # создаёт итератор подсчёта количества элементов
# # print(cf)
# cf = Counter(items)
# print(cf)
# # print(cf['apple'])
# print(cf['apple'])
# # print(cf.most_common())  # возвращает список кортежей подсчёта элементов
# print(cf.most_common())

# Цикл for
# for переменная in iterable:
#     тело цикла
# else:
#     код выполняется, если цикл завершился нормально (без break)

# a = [1, 2, 7, 12, 14, 4, 34, 57]
# for i in a:
#     if i == 12:
#         continue  # досрочное завершение итерации
#     if i == 4:
#         break  # досрочное завершение цикла
#     print(i)
# else:
#     print('cat')
#
# for i in a:
#     if i == 12:
#         continue
#     if i == 4:
#         break
#     print(i, end=' ')
#
# # for i in range(2, 9, 2):  # 4 6 8
# #     print(i, 'cat')
#
# for i in range(2, 9, 2):
#     print(i, 'cat')
#
# # for i in enumerate(a):  # возвращает (индекс, элемент)
# #     print(i)
# for i in enumerate(a):
#     print(i)
#
# # for x, y in enumerate(a, 10):  # можем указать начало индексации
# #     print(x, y)
#
# for x, y in enumerate(a, 10):
#     print(x, y)
#
# # Списковые включения (list comprehension)
# # list_new = []
# new_list = []
# for i in range(1, 11):
#     new_list.append(i ** 2)
# print(new_list)
# # for i in range(1, 11):
# #     list_new.append(i ** 2)
# # print(list_new)
# #
# # print([i ** 2 for i in range(1, 11)])
# print([i ** 2 for i in range(1, 11)])
# #
# # print({i for i in range(1, 11)})
# # print({i: i ** 2 for i in range(1, 11)})
# print((i ** 2 for i in range(1, 11)))
# #
# # print([i ** 2 for i in range(1, 11) if i % 2 == 0])
#
# print({i for i in range(1, 11)})
# print({i: i ** 2 for i in range(1, 11)})
# print((i for i in range(1, 11)))
# print([i ** 2 for i in range(1, 11) if i % 2 == 0])
#
# # Вывести чётные числа в интервале [1, 20], если число меньше или равно 10, то - квадрат, а если больше 10 - куб.
# print([i ** 2 if i < 11 else i ** 3 for i in range(1, 21) if i % 2 == 0])
# # print([i ** 2 if i < 11 else i ** 3 for i in range(1, 21) if i % 2 == 0])
# # print([(i ** 3, i ** 2)[i < 11] for i in range(1, 21) if i % 2 == 0])
# print([(i ** 3, i ** 2)[i < 11] for i in range(1, 21) if i % 2 == 0])

#
# # Подсчитать количество и сумму цифр
# s = 'cat 217 dog781'
# # value = [int(i) for i in s if i.isdigit()]
# v = [int(i) for i in s if i.isdigit()]
# print(len(v))
# print(sum(v))
#
# # for x in range(10):
# #     for y in range(10):
# #         print(f'x = {x} y = {y} {x * 10 + y}')
# #
# # print([x * 10 + y for x in range(10) for y in range(10)])
#
# for x in range(10):
#     for y in range(10):
#         print(f'x = {x}, y = {y} {x * 10 + y}')
#
# # Сгенирировать список из букв имён, которые меньше 4 символов:
# s = ['Tom', 'Jerry', 'Bob', 'Vinny']
#
# # print([x for i in s if len(i) < 4 for x in i])
# for i in s:
#     for x in i:
#         if len(i) < 4:
#             print(x)
#
# print([x for i in s if len(i) < 4 for x in i])
# print([x for i in s for x in i if len(i) < 4])
#
# # print([x for i in s for x in i if len(i) < 4])
# for i in s:
#     for x in i:
#         if len(i) < 4:
#             print(x)

# Многомерные массивы
# x = [0] * 2
# y = [0 for i in range(4)]
# print(x)
# print(y)

# x = [0] * 2
# print(x)
# y = [0 for i in range(4)]
# # z = [[0] * 2 for i in range(4)]  # !!!
# z = [[0] * 2 for i in range(4)]
# print(z)
# t = [x for i in range(4)]
# print(t)
# # t = [x for i in range(4)]
# # z[0][1] = 1
# # print(z)
# t[0][1] = 1
# print(t)
#
#
# # # [[0, 0], [0, 0], [0, 0], [0, 0]]
# #
# # b = [[[0] * 2 for i in range(4)] for k in range(2)]
# b = [[[0] * 2 for i in range(4)] for k in range(2)]
# print(b)
# b[0][0][1] = 1
# print(b)
# # [[[0, 0], [0, 0], [0, 0], [0, 0]],  [[0, 0], [0, 0], [0, 0], [0, 0]]]
#
#
# # s = [i for i in range(1_000_000)]
# s = [i for i in range(1000000)]
# s2 = (i for i in range(1000000))
# print(s2)
# print(s.__sizeof__())
# print(s.__sizeof__())
# f = (2, 4)
# print(type(f))
# s2 = (i for i in range(1_000_000))
# print(s2)
# print(s.__sizeof__())
# print(s2.__sizeof__())

### My Questions

# print(hash(7.0))
# print(3 % 7)  # 3
# print(7 % 3)  # 1
# a = '''x, y, z, n
# 1 2 3 4
# 5 6 6 7'''
# print(a.splitlines())
# print(a.split())
#
# b = [4, 5, 6, 8]
# b.clear()
# print(b)
# pi = 3.1415926
# print(f'pi = {pi:.1f}')
# h, m, p = 12, 5, 1.512
# print(f"Time is: {h:05d}:{m:02d} {p:%} {p:.0%} {p:+.2f} {1234567890:,}")
#
# z = int(input('Сколько оставить знаков после запятой? '))
# print(f'{pi:.{z * 2}f}')
#
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

# i = 0
# while i < 5:
#     i += 1
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i, 'cat')

# while True:  # вечный цикл
#     x = input('Введите фрукт: ')
#     if x == 'exit':
#         break
#     print(x * 2)
# while True:
#     x = input('Gbu: ')
#     if x == 'exit':
#         break
#     print(x * 2)

# s = [i for i in range(1_000_000)]
# s = [i for i in range(1000000)]
# # s2 = (i for i in range(1_000_000))
# s2 = (i for i in range(1000000))
# print(s)
# print(s2)
# print(s2)
# print(s.__sizeof__())
# print(s2.__sizeof__())
# print(s.__sizeof__())
# print(s2.__sizeof__())

# У нас есть колода карт с мастями (♥♦♠♣) и карты от шестёрки до туза.
# Сформировать колоду вида: 6♥, 6♦, 6♠, 6♣ ... Т♣.
# Перемешать её и вывести первые случайные 6 карт.
# Можно ли решить задачу в одну строку?
# masti = '♥♦♠♣'
# number = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
# k = set()
#
# for i in number:
#     for j in masti:
#         k.add(i + j)
# print(*tuple(k)[:6])
# # k = set()
# # for i in number:
# #     for j in masti:
# #         k.add(i + j)
# # print(*tuple(k)[:6])
# #
# print(*tuple({i + j for i in number for j in masti}))
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
# while True:
#     x = input('Fruits: ')
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
#
# def degree(x, y):
#     x, y = abs(x), abs(y)
#     return x ** y
#
#
# print(degree(6, 8))

# # (4 ** 2) ** 8 + 10 ** 3
# # degree = lambda x, y: abs(x) ** abs(y)   # lambda parameters: return
# degree = lambda x, y: abs(x) ** abs(y)
# print(degree(5, 8))
# print(degree(degree(4, 2), 8) + degree(10, 3))
# # print(degree(-2, -4))
# # print(degree(degree(4, 2), 8) + degree(10, 3))
#
# # def mysum(*s):
# #     return sum(s)
# #
# def mysum(*s):
#     return sum(s)
#
#
# mysum = lambda *s: sum(s)
# print(mysum(1, 4, 6, 3))
#
# mysum = lambda *s: sum(s)
# print(mysum(1, 2, 3, 4))

# def func(x):
#     return x[1]

# def func(x):
#     return x[1]
# #
# #
# students = [
#     ('Alice', 8),
#     ('Alex', 17),
#     ('Ivan', 10)
# ]
# # print(sorted(students, key=func))
# print(sorted(students, key=func, reverse=True))
# # print(sorted(students, key=lambda x: x[1], reverse=True))
# #
# print(sorted(students, key=lambda x: x[1], reverse=True))
#
# # print(sorted([16, 3, 8, 2, 1], reverse=True))
# print(sorted([16, 3, 8, 2, 1]))
# #
# grades = [{'name': 'Jennifer', 'final': 95},
#           {'name': 'David', 'final': 92},
#           {'name': 'Aaron', 'final': 98}]
# #
# # def fun_dict(y):
# #     return y['final']
# #
# def func_dict(y):
#     return y['final']
# #
#
# # print(sorted(grades, key=fun_dict))
# print(sorted(grades, key=func_dict))
# # print(sorted(grades, key=lambda y: y['final']))
# print(sorted(grades, key=lambda y: y['final']))
# # print(sorted(grades, key=lambda j: j['name']))
# print(sorted(grades, key=lambda y: y['name']))
#
# value = int(input('Tell me a number: '))
# hour = value // 60
# min = value % 60
# print(f'{value} min - hour: {hour}, min: {min}')
# number = int(input('Tell me number: '))
# last_digit = number % 10
# # middle_digit = number % 100 // 10
# # first = number // 100
# # print(last_digit + middle_digit + first)
# # print(last_digit * middle_digit * first)
# digit2 = number % 1000 // 100
# digit3 = number % 100 // 10
# print(digit3)

# num = int(input())
# last = num % 10
# second = num % 100 // 10
# first = num // 100
# print(last, second, first, sep='')
# print(last, first, second, sep='')

# v, v1, v2, v3 = int(input()), int(input()), int(input()), int(input())
# print(v ** v1 + v2 ** v3)

# password = input()
# pas2 = input()
#
# if pas2 == password:
#     print('ok')
# else:
#     print('not ok')

# a = 12  # int целые числа
# a = 12
# # b = 3.141592  # float дробные числа
# b = 3.21
# c = 'text 43'
# # c = 'text 22'  # str строки
# # d = [2, 2, 2, 6.7, 'text', [6, 7]]  # list список changeable
# d = [2, 2, 4.8, ' text', [6, 8], 4]
# d[5] = 8
# print(d)
# k = d[4][1]
# print(k)
# # d[5][1] = 8
# # print(d)
# # k = d[5][1]
# # print(k)
# # e = (2, 6.7, 'text')  # tuple кортеж  # not changeable, less weight, speed
# e = (2, 6.7, 'text')
# print(e[0])
# # print(e[0])
# # f1 = True  # bool логический
# f1 = True
# # f2 = False
# f2 = False
# # m = {4, 5.6, 'cat', 4, 'cat'}  # set множества # random and changeable
# m = {4, 5.6, 'cat', 8, 'cat'}
# print(m)
# print(hash('cat'))
# # print(hash('cat'))
# # s = {'key': 'value', 'Alex': [5, 4, 3, 5]}  # dict словарь
# s = {'key': 'value', 'Alex': [5, 8, 9]}
# print(s['Alex'])
#
# # print(s['Alex'])
# #
#
#
# # import math
# import math
# # print(math.cos(math.pi))
# print(math.cos(math.pi))
# #
# # # + - * /
# # print(4 ** 2)  # возведение в степень
# print(4 ** 2)
# # print(125 ** (1/3))  # кубический корень
# print(125 ** (1/3))
# # print(-16 ** (1/2))
# print(-16 ** (1/2))
# # print(pow(5, 2))  # возведение в степень
# print(pow(5, 2))
# # print(pow(4, 2))
# # print(pow(-16, 0.5))
# print(pow(-16, 0.5))
# # 4 * 4 = 16 ** (1/2) = 4
# # 2 * 2 * 2 = 8 ** (1/3) = 2
# # print(7 // 3)  # целая часть от деления # how many times we put 3 in 7
# print((7 // 3))
# # print(7 % 3)  # остаток от деления
# print(7 % 3)
# # print(divmod(7, 3))  # (//, %)
# print(divmod(7, 3))
# # print(divmod(28, 10))
# print(divmod(28, 10))
# # print(abs(-7))  # модуль числа
# print(abs(-7))
#
# # if условие1:      если
# #     блок кода 1
# # elif условие2:    иначе если
# #     блок кода 2
# # else:             иначе при всех остальных условиях
# #     блок кода 3
#
#
# # number = int(input('Введите число: '))
# number = int(input('Number '))
# # if number > 0:
# if number > 0:
#     print('k')
# elif number < 0:
#     print('h')
# else:
#     print('Zero')
# else:
#     print("Zero")


# ctrl + c, v, x, z, a, /

# > больше
# < меньше
# == равно
# != не равно
# >= больше или равно
# <= меньше или равно

# a and b логическое И, True если оба True
# a or b логичесое ИЛИ, True если хотя бы один равен True
# not a  логическое НЕ   not True = False    not False = True

# # a, b = (0,), 7
# a, b = (0,), 7
# print(a, b)
# # # a, b = b, a
# # if a and b > 0:
# if a and b > 0:
#     print('cat')
# #     print('cat')
#
# # False: False, None, 0, [], (), '', {}
# # True: True, number != 0, len(iterable) > 0
#
# # day_value = input("Whats the day today ")
# day_value = input('Whats the day today')
# print('Today is a weekend' if day_value == 'Sunday' or day_value == 'Saturday' else 'Today is a working day')
# # print("Today is a weekend" if day_value == "Sunday" or day_value == "Saturday" else "Today is a working day")
#

a = 'White cat black cat'
b = 'dog'
c = 7
# # print(a + b + str(c))  # конкатенация
# print(a + b + str(c))
# print(a, b, c)
# # # print(a, b, c)
# # # print(b * 4)
# print(b * 4)
# # # print('-' * 70)
# print('-' * 70)
# # # print('cat' in a)  # вхождение подстроки в строку
# print('cat' in a)
# # # print(len(b))  # длина строки
# print(len(b))
# # # print(a.count('cat'))  # считает количество подстрок в строке
# print(a.count('cat'))
# # print(a.index('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет - ошибка
# print(a.index('cat'))
# # # print(a.rindex('cat')) # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет - ошибка
# print(a.rindex('cat'))
# # # print(a.find('catee')) # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет -1
# print(a.find('catee'))
# # # print(a.rfind('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет -1
# print(a.rfind('cat'))
# # # print(a.replace('cat', 'cow').replace('black', 'red'))  # замена текста
# print(a.replace('cat', 'cow').replace('black', 'red'))
# # # print(a.replace('cat', 'cow', 1))  # замена текста
# print(a.replace('cat', 'cow', 1))
# # # print(a.replace('t', '')) # удаляем t
# print(a.replace('t', ''))
# # # print('BMW'.lower())      # Перевести в нижний регистр
# print('BMW'.lower())
# # # print('apple'.upper())    # перевести в верхний регистр
# print('apple'.upper())
# # # print('Apple'.swapcase()) # изменить регистр букв
# print('Apple'.swapcase())
# # # print(a.title())  # меняет первую букву каждого слова на заглавную, а остальные на строчные
# print(a.title())
# # # print(a.capitalize())  # меняет первую букву строки на заглавную, а остальные на строчные
# print(a.capitalize())
# #
# s = 'white     cat  black         cat dog'
# # # print(s.split(" "))  # разбивает строку по разделителю на список текстовых элементов, without an element in the text
# print(s.split(' '))
# # # # cANNOT BE BROKEN
# # # print(s.split())  # по умолчанию делится по множественному пробелу (любое количество любых пробельных символов), one separator
# # # print('*'.join(['white', 'cat', 'black', 'cat']))  # склеивает в строку iterable текстовых элементов
# print('*'.join(['white', 'cat', 'black', 'cat']))
# # #
# #
# a = 'x y z a b'
# # # print(a.split(maxsplit=2))  # можем указать количество разбиений
# print(a.split(maxsplit=2))
# # # print(a.rsplit(maxsplit=2))  # разбиение с конца строки
# # #
# # # print('white cat\nblack cat')
# print('white cat\nblack cat')
# # # print("white cat" + "\n" + "black cat")
# print('white cat' + '\n' + 'black cat')
# # # print(a.splitlines())  # разбиваем по строкам (/n)
# print('white cat\nblack cat'.splitlines(keepends=True))
# # print(a.splitlines(keepends=True))  # сохраняем символ переноса строки
# # # #
# s = 'Discworld'
# # # # print(s.endswith('cat'))  # False
# print(s.endswith('cat'))
# # # print(s.endswith('world'))  # True
# print(s.endswith('world'))
# # # # print(s.endswith(('cat', 'world')))  # True / or
# print(s.endswith(('cat', 'world'))) #TODO why doeble (
# # # print(s.endswith('sc'))  # True
# print(s.endswith('sc'))
# # # print(s.endswith('sc', 0, 4))  # True
# print(s.endswith('sc', 0, 4))
# # # print(s.startswith('Disc'))  # True
# print(s.startswith('Disc'))
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
#
# name = input('Whats ur name ')
# print(name, 'Hallo')

# num1 = int(input('2 Numbers: '))
# num2 = int(input('2 Numbers: '))
#
# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

# num1 = int(input('Tell me a num: '))
#
# if num1 % 2 == 0:
#     print('G')

# word1 = input('Tell me smth ')
# word2 = input('Tell me smth: ')
#
# if word1 in word2:
#     print('Yes')
# else:
#     print('No')

# n = int(input('Text '))
#
# while n != 0:
#     n = int(input('Text '))

# n = [1, 2, 3, 'Text', 4.7, [5, 6]]
#
# for i in n:
#     print(i)

# input = {'autor': 'book'}
l = list(input(''))
print(l)
