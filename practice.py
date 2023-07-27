
#4
# Даны два числа не равные нулю. Если оба числа положительные, то выдать их сумму, если оба числа отрицательные,
# то выдать их произведение, если числа положительное и отрицательное,
# то выдать квадрат положительного числа (number**2).

# number = float(input("Tell me number: "))
# number_1 = float(input("Tell me the second number: "))
# if number > 0 and number_1 > 0:
#     print(number + number_1)
# elif number < 0 and number_1 < 0:
#     print(number - number_1)
# elif number > 0:
#     print(number ** 2)
# else:
#     print(number_1 ** 2)

# Даны два различных числа (числа вводим с клавиатуры). Вычесть из большего числа меньшее и выдать разницу чисел.
# number1 = float(input("Tell me number: "))
# number2 = float(input("Tell me the second number: "))
# if number1 > number2:
#     print(number1 - number2)
# else:
#     print(number2 - number1)
#
# print(number1 - number2 if number1 > number2 else number2 - number1)
#
# print(abs(number1 - number2))



# Дано расстояние s в сантиметрах. Найти количество полных метров в нем (1 метр = 100 см).
# s = int(input("Tell me your destination: "))
# print(s // 100, "m.")


# Дано двузначное число. Вывести вначале его левую цифру (десятки), а затем — его правую цифру (единицы).
# value = float(input("Write here a two digit number: "))
# print(value // 10, value % 10)

# value = input("Write here a two digit number: ")
# print(value[0], value[1])
#
# a, b = input("Write here a two digit number: ")
# # print(a, b)
#
# # Дана сторона квадрата a. Найти его периметр P = 4*a. Найти его площадь S = a**2.
# a = float(input("Given the side of square "))
# print("P =", 4 * a)
# print("S =", a ** 2)



# Даны три числа: 2 положительных и одно отрицательное. Выдать произведение положительных чисел.
# number1 = float(input("Tell me number: "))
# number2 = float(input("Tell me the second number: "))
# number3 = float(input("Tell me the third number: "))
# if number3 < 0:
#     print(number1 * number2)
# elif number1 < 0:
#     print(number2 * number3)
# else:
#     print(number3 * number1)


# Дано трёхзначное число. Вывести произведение его цифр. 257 -> 70
# a, b, c = input("Write here a tree digit number: ")
# print(int(a) * int(b) * int(c))

# abc = int(input("Write here a tree digit number: "))
# c = abc % 10
# value = abc // 10
# b = value % 10
# a = value // 10
# print(a * b * c)

# Дано двузначное число вида ab. Если первая цифра чётная, то вывести сумму его цифр, если нечётное, то произведение
# c, d = input("Write here a two digit number: ")
# a = int(c)
# b = int(d)
# print(a + b if a % 2 == 0 else a * b)
# print(a * b if a % 2 else a + b)


# Дано четырёхзначное число. Если сумма первых двух цифр больше суммы третьей и четвёртой цифры,
# то вывести произведение крайних цифр числа, иначе вывести сумму второй и третьей цифры.
# a, b, c, d = input("Write here a four digit number: ")
# f = int(a)
# g = int(b)
# e = int(c)
# k = int(d)
# print(f * k if f + g > e + k else g + e)

# if f + g > e + k:
#     print(f * k)
# else:
#     print(g + e)

# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число,
# операцию и второе число, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число")
# и выводит результат на экран. Поддерживаемые операции: +, -, /, *.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0 невозможно!".
#
# number_1 = float(input("Your first number is: "))
# sign = input("Your sign is: ")
# number_2 = float(input("Tour second number is: "))
#
# if sign == "+":
#     print(number_1 + number_2)
# elif sign == "-":
#     print(number_1 - number_2)
# elif sign == "*":
#     print(number_1 * number_2)
# elif number_2:
#     print(number_1 / number_2)
# else:
#     print("Деление на 0 невозможно!")

# ДЗ, со строками.
# garden = 'В нашем саду растут 20 яблонь и 15 слив.'
# 1. Заменить 20 на 35.
# print(garden.replace("20", "35"))

# Поменять местами "яблонь" и "груш" используя replace.
# print(garden.replace("груш", "яблонь").replace("яблонь", "груш", 1))

# В переменную мы получаем наше предложение garden.
# Нужно вывести  суммарное количество деревьев в саду.
# Цифры могут быть многозначными.
# my_str = garden.split()
# print(int(my_str[4]) + int(my_str[7]))

# Поменять местами названия деревьев (могут быть любые), используя split и join.
# my_str = garden.split()
# my_str[5], my_str[8] = my_str[8].replace(".", ""), my_str[5] + "."
# print(" ".join(my_str))

# 0. Дано число a в диапазоне 1-9999.
# Вывести к нему описание чётное/нечётное.
# Вывести к нему описание 1-значное/2-значное/3-значное/4-значное.

# number = int(input("Your number from 1 to 9999 is: "))
# print("нечётное" if number % 2 else "чётное")
#
# if number < 10:
#     print("1-значное")
# elif number < 100:
#     print("2-значное")
# elif number < 1000:
#     print("3-значное")
# else:
#     print("4-значное")
#
# print(str(len(str(number))) + "-значное")

# 1. Даны три числа. Найти сумму двух наибольших из них.
# a = float(input("First number is: "))
# b = float(input("The second number is: "))
# c = float(input("The third number is: "))
# if a > b > c:
#     print(a + b)
# elif b > a and c > a:
#     print(b + c)
# else:
#     print(a + c)

# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# print(b + c)

# 2. Дано число 0 < n < 10. Вывести верно фразу "На лугу пасётся ", n "корова/коровы/коров".
# n = int(input("На лугу пасётся: "))
# tail = ""
# if n == 1:
#     tail = "a"
# elif 1 < n < 5:
#     tail = "ы"
# # else:
# #     tail = ""
#
# print("На лугу пасётся", n, "коров" + tail)



# 3. Квадратное уравнение имеет вид ax2 + bx + c = 0 на вход в переменную stroka мы получаем от пользователя уравнение,
# # выдать значение коэффициентов a, b, c. Учитываем, что они могут быть многозначными. Например:
# stroka = '6x2 - 12x + 10 = 0'  -> a = 6  b = -12  c = 10
# stroka = input("The equation: ")
# stroka = '6x2 + 12x + 10 = 0'
# my_str = stroka.replace("x2", "").replace("x", "")
# s = my_str.split()
# print("a =", s[0], "b =", s[1].replace("+", "") + s[2], "c =", s[3].replace("+", "") + s[4])
# # print(int(s[1] + s[2]))
# # print(int('+12'))

# print("b =", s[1] + s[2] if s[1] == "-" else s[2])
# if s[1] == "-":
#     print("b =", s[1] + s[2])
# else:
#     print("b =", s[2])
#
# if s[3] == "-":
#     print("c =", s[3] + s[4])
# else:
#     print("c =", s[4])



# 1. Решить уравнение ax+b=0. Мы получает от пользователя уравнение. Решите его и выведите целое значение x.
# Вывод должен быть именно в формате: "х=значение".
# Примеры:
# # text = '2x+6=0'  ->  x=-3
# text = '-12x+24=0'  -> x=2
# text = '4x-100=0' -> x=25

# equation = '4x-100=0'.split("x")
# a = equation[1].replace("=0", "")
# x = int(a) // -int(equation[0])
# print("x=" + str(x))

# 0. Пользователь вводит: "Фамилия Имя Отчество" - преобразовать в Фамилия инициалы:
# Иванов петр игоревич -> Иванов П.И.
# name = input("Tell me your full name: ").title().split()
# print(name[0], name[1][0] + "." + name[2][0] + ".")

# 1. Дано целое число. Посчитать количество нулей в числе.
# 1002 -> 2
# 50 -> 1
# 0020 -> 1
# 0 -> 1

# int_number = int(input("Tell me number: "))
# print(str(int_number).count("0"))

# 2. Дано целое число. Посчитать количество нулей в начале числа.
# 107 -> 0
# 000200001 -> 3
# 0 -> 1
# string_1 = input("Tell me number: ")
# print(len(string_1) - len(string_1.lstrip("0")))


# 3. Дано целое число. Посчитать количество нулей в конце числа.
# 401 -> 0
# 800007000 -> 3
# 0 -> 1
# string = input("Tell me number: ")
# print(len(string) - len(string.rstrip("0")))

# 4. Пользователь вводит слово. Поменять местами первую и последнюю буквы.
# слава -> алавс
# a -> a
# '' -> ''
#
# word = input("Tell me one word: ")
# print(word if len(word) == 1 else word[-1:] + word[1:-1] + word[:1])


# spisok = [15, 6, 17, 480, 9]
# 1. Посчитать сумму крайних элементов в списке.
# print(spisok[0] + spisok[-1])

# 2. Посчитать разницу между максимальным и минимальным элементом списка.
# print(max(spisok) - min(spisok))

# 3. Посчитать количество знаков в максимальном элементе.
# print(len(str(max(spisok))))

# 4. Посчитать сумму элементов чётных позиций списка.
# print(sum(spisok[1::2]))

# 5. Посчитать квадрат центрального элемента в списке.
# print(spisok[len(spisok) // 2] ** 2)

# spisok = [15, 6, 171, 48, 9, 7, 12, 90]

# 1. Вывести общую сумму двух первых и двух последних элементов списка.
# print(sum(spisok[-2:]) + sum(spisok[:2]))
# print(sum(spisok[-2:] + spisok[:2]))

# 2. Если сумма элементов на чётных позициях больше, вывести "Чётные победили",
# если на нечётных - "Нечётные победили".


# print("Чётные победили" if sum(spisok[1::2]) > sum(spisok[::2]) else "Нечётные победили")

# 3. Переставить последний элемент списка на первое место и вывести новый список.
# Использовать только функции работы со списком без слайсов.

# spisok.insert(0, spisok.pop())
# print(spisok)


# 4. C клавиатуры вводим через пробел 3 целых числа.
# Напишите программу, которая выводит в три строки: сначала максимальное,
# потом минимальное, после чего оставшееся число.

# t = input("Tell me: ").split()
# t[0], t[1], t[2] = int(t[0]), int(t[1]), int(t[2])
# # t = [int(t[0]), int(t[1]), int(t[2])]
# t.sort()
# print(t[-1])
# print(t[0])
# print(t[1])


# # ДЗ, квест-алгоритм (каждое решение в одну строку) со списком [2, 4, 6, 1]:
# s = [2, 4, 6, 1]
# # 1. Добавить 7 в середину списка.
# print(s)
# # s[2:2] = [7]
# s.insert(2, 7)
# print(s)
# # 2. Удалить 6.
# s.remove(6)
# print(s)
# # 3. Вставить в начало списка сумму первого и последнего элементов.
# s.insert(0, s[0] + s[-1])
# print(s)
# # 4. Увеличить первый элемент списка на величину последнего элемента списка, удалив последний элемент.
# s.insert(0, s[0] + s.pop())
# print(s)
# # 5. Продублировать элементы списка 2 раза.
# s *= 2
# print(s)
# # 6. Вывести общую сумму первых трёх и последних трёх элементов списка s.
# print(sum(s[:3] + s[-3:]))
#
# # 7. Создать список s2 из первого и последнего элемента s.
# s2 = [s[0], s[-1]]
# print(s2)
# # 8. В третий и четвёртый элементы s2 поместить сумму и произведение элементов s2 соответственно.
# s2.extend([sum(s2), s2[0] * s2[1]])
# print(s2)
# # 9. К списку s прибавить элементы списка s2.
# s += s2
# print(s)
#
# # 10. К списку s прибавить буквы слова cat.
# s[0:0] = "cat"
# print(s)
#
# # 11. Создать список s3 в котором будут только цифры s.
# s3 = s[3:]
# print(s3)
#
# # 12. Отсортировать список s3 по убыванию.
# s3.sort(reverse=True)
# print(s3)
#
# # 13. Отзеркалить (развернуть) список s3.
# s3 = s3[::-1]
# print(s3)

# # 14. Вставить элементы списка s2 между первым и вторым элементом списка s3.
# s3[1:1] = s2
# print(s3)
#
# # 15. Удалить все элементы s3 на нечётных позициях.
# # del s3[::2]
# s3 = s3[1::2]
# print(s3)

# # 16. Заменить последнее число в списке s3 на его цифры.
# s3.extend(divmod(s3.pop(), 10))
# print(s3)

# Повторяем строки:
# В переменной chess мы получаем какой-то любой фрагмент шахматной партии.
# Например:
# chess = '1. d2 e6 2. e4 d5 3. Кc3 c5 4. Кf3 a4 5. e:d5 e:d5 6. Сe2 Кf6 7. O-O e5 8. Сg5 O-O 9. d:c5 Сe6 10. Кd4 С:c5 11. Кb3 Сe7 12. Сf3 Кe5 13. Лe1 К:f3+ 14. Ф:f3 Лc8 15. h3 h6'
# # 0. Распечатать первый ход партии: 1. d2 e6   Найти как можно больше решений.
# print(' '.join(chess.split()[:3]))
# print(' '.join(chess.split(' 2.', maxsplit=2)[:1]))
# print(chess.split(' 2.')[0])
# print(chess[:chess.index(" 2.")])
# # 1. Подсчитать сколько раз в партии ходили слонами.
# print(chess.count('С'))
# # 2. Если в партии было больше ходов слонами, чем ладьями - напечатать "Слоны были активнее", если ладьями, то напечатать "Ладьи были активнее".
# print("Слоны были активнее" if chess.count('С') > chess.count('Л') else "Ладьи были активнее")
# # 3. Распечатать на каком ходу у белых была короткая рокировка: O-O.
# print(chess[:chess.index('. O-O')].split()[-1])
# print(chess.split()[1::3].index('O-O') + 1)
#
# # 4. Распечатать на каком ходу у чёрных была короткая рокировка: O-O.
# c = chess.replace('. O-O', '. f4')
# print(c[:c.index('O-O')].split()[-2].rstrip('.'))
# print(chess.split()[2::3].index('O-O') + 1)
# # print(c[:c.index('O-O')].split()[-2].replace(".", " "))

# ДЗ, квест-алгоритм str
# a = 'It is delicious - borscht'
# b = 9
#
# # 1. Add a and b + text
# value = a + str(b) + '. Just add - an onion.'
# print(value)
#
# # 2. Move 9 to end
# v = value.replace("9", "").replace('onion.', 'onion 9.')
# print(v)
#
# # 3. Remove before the last element use slices
# v1 = v[:-3] + '.'
# print(v1)
#
# # 4. Напиши программу которая примет ответ пользователя и независимо от регистра выводит реакцию на ответ
# # answer = input('What color is the beet? ')
# # print('You are right' if answer.lower() == 'red' else 'That isnt correct color.')
#
# # 5. Сделай программу которая подсчитает длину ответа пользователя и если ответ не правильный выведет подсказку
# # print('Yes. Correct len is 3' if len(answer) == 3 else 'Correct len is 3')
#
# # 6. Add '.' in answer
# # if not answer.endswith('.'):
# #     answer += '.'
# #     print(answer)
#
# # 7. The user will write a mail and you have to print the Login and Domain
# # mail = input('Tell me your mail: ').split('@')
# # print(f'Login is {mail[0]}' + '\n' + f'Your Domain is {mail[1]}')
#
# # 8. Remove 'i' between the first and last use in the text
# print(v1[:v1.index('i') + 1] + v1[v1.index('i'):v1.rindex('i')].replace('i', '') + v1[v1.rindex('i'):])
#
#
# # 9. Swap sentences in v1
# # print(v1)
# # v11 = v1.split('. ')
# # print(v11[1], v11[0] + '.')
# v1 = ' '.join(v1.split('. ')[::-1]) + '.'
# print(v1)
#
# # 10. Count number of words in v1
# n2 = len(v1.replace('-', '').split())
# print(n2)


# # ДЗ, квест-алгоритм list
# list_quest = [1, 2, 3, 4, [5, 6]]
#
# # 1. Make one-dimencional list in list_quest. Create new  variable = one_list
# # list_quest = sum([list_quest[:-1]] + list_quest[-1:], [])
# one_list = list_quest[:-1] + list_quest[-1]
# # list_quest.extend(list_quest.pop())
# print(one_list)
#
# # 2. Add 700 in the second list in list
# list_quest[4].insert(1, 700)
# print(list_quest)
#
#
# # 3. Expand the second list in the list and list
# list_quest = [list_quest[-1][::-1]] + list_quest[:-1][::-1]
# print(list_quest)
#
# # 4. Find max of one_list and divide by the length of the one_list
# print(one_list)
# max_list = max(one_list) / len(one_list)
# print(max_list)
#
# # 5. Find 2 and replace with 205 in one_list
# one_list[one_list.index(2)] = 205
# print(one_list)
#
# # 6. Pull out every third elements in one_list
# print(one_list[2::3])
#
# # 7.Print result as Ivano-Frankivsk,by join and slices
# new_list = ['Ivano', '+', 'Frankivsk']
# # new_list = new_list[0] + '-' + new_list[-1]
# new_list = '-'.join(new_list[::2])
# print(new_list)
#
# # 8. Swap elements around
# print(one_list)
# one_list[::2], one_list[1::2] = one_list[1::2], one_list[::2]
# print(one_list)
#
# # 9. Add the last digit of the first number to the beginning of the list
# one_list.insert(0, one_list[0] % 100)
# print(one_list)
#
# # 10. Take the number in the middle and move it to the beginning
# one_list.insert(0, one_list.pop(len(one_list) // 2))
# print(one_list)

# # game idea
# seven_words = ['apple', 'melon', 'lemon', 'grape', 'orange', 'blueberry', 'kiwi']
# user_one = input('Tell me your word: ')
# user_two = input('Tell me index from 0 to 6: ')
#
# print('You won!' if user_one.index(user_one) == user_two else 'Try again!')

# Повторяем строки:
# В переменной ingredients мы получаем какой-то любой фрагмент ингредиентов рецепта.
# Например:
# recept = '1. 1 cups Sugar 2. 12 Eggs 3. 12 cup Flour 4. 4 cup Cocoa Powder 5. 1 pinch Salt 6. ½ cup Butter (melted) 7. 1 tablespoon Vanilla Extract 8. 1 tablespoon Butter 9. 1 tablespoon Cocoa Powder 10. add  Powdered Sugar 11. 1 cup Berry, Optional'
#
# # 0. Распечатать первый ингредиент. Найти как можно больше решений.
# print(recept[:recept.index(' 2.')])
#
# # 1. Вывести сколько яиц добавили.
# r = recept.split()
# print(r[r.index('Eggs') - 1])
#
# # 2. Если в рецепте было больше муки, чем какао порошка - напечатать "Муки больше чем какао порошка",
# # если какао порошка больше, то напечатать "Какао порошка больше чем муки".
#
# print("Муки больше чем какао порошка" if int(r[r.index('Flour') - 2]) > int(r[r.index('Cocoa') - 2]) else "Какао порошка больше чем муки")
#
# # 3. Распечатать каким по подсчету ингредиентом идет ванильный экстракт.
#
# print(r[r.index('Vanilla') - 3].rstrip('.'))
#
#
# # ДЗ на множества:
# # 1. Ребёнку нужно из кубиков с буквами сложить предложение "мама мыла раму". Какие кубики с буквами ему понадобятся? (кубика "пробел" не существует)
# str_mother = set("мама мыла раму")
# # str_mother.remove(' ')
# # str_mother -= {' '}
# print(*str_mother.difference(' '))
# # print(*str_mother)
#
# # # 2. В школе десятибальная система. У Егора за эту неделю были такие оценки [3, 4, 7, 5, 1, 5, 9, 2, 9, 10]. Напечатать каких оценок у него не было.
# scores = [3, 4, 7, 5, 1, 5, 9, 2, 9, 10]
# all_scores = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# all_scores = set(range(1, 101))
# print(all_scores - set(scores))
# print(all_scores.difference(scores))
#
# # # 3. Егор любит ходить в лес. В первую неделю он был в лесу в такие дни ['пн', 'ср', 'чт', 'вс'],
# # # во вторую неделю ['вт', 'ср', 'чт', 'сб'], а в третью ['вт', 'ср', 'пт', 'вс']. Найти любимый день недели Егора для похода в лес.
# first_week = ['пн', 'ср', 'чт', 'вс']
# second_week = ['вт', 'ср', 'чт', 'сб']
# third_week = ['вт', 'ср', 'пт', 'вс']
# print(set(first_week) & set(second_week) & set(third_week))
# print(set(first_week).intersection(second_week, third_week))

# ДЗ, квест-алгоритм (каждое решение в одну строку)
# first = {1, 2, 3, 4, 5}
# second = {9, 8, 7, 6, 5, 4, 3}
# third = {'mouse', 'cat', 'rabbit'}
#
# # 1. Вывести на экран «Есть общие цифры», если в первом и втором множестве есть общие цифры, и если нет вывести «Нет общих цифр»
# print('Нет общих цифр' if first.isdisjoint(second) else 'Есть общие цифры')
#
# # 2. Объединить first и third множество в одно. Создать новую переменную value_union.
# # value_union = first.union(third)
# value_union = first | third
# print(value_union)
#
#
# # 3. Print elements by which second and value_union sets differ.
# print(second, value_union)
# print(*second.symmetric_difference(value_union))
# print(*second ^ value_union)
#
# # 4. Вывести элементы, которые есть в first и в value_union.
# print(*first & value_union)
# print(*first.intersection(value_union))
#
# # 5. Проверить есть ли ‘о’ в value_union.
# print('o' in value_union)
#
# # 6. Add elements of list in first.
# first.update([6, 7])
# print(first)
#
# # 7. Удалить самое большое число из множества second.
# second.remove(max(second))
# print(second)
#
# # 8. Найти минимальное число из множеств first и second.
# print(min(first.union(second)))

# ДЗ, работа со словарём:
#
# 1) Единицы массы пронумерованы следующим образом: 1 — грамм, 2 — килограмм, 3 — центнер, 4 — тонна.
# Дан номер единицы массы n (целое число в диапазоне 1–4) и масса тела m в этих единицах (натуральное число).
# Найти массу тела в килограммах.
# n=3 m=12 -> Масса равна 1200.0 кг
# n=1 m=100 -> Масса равна 0.1 кг
# n = int(input('Tell me your number in range 1-4: '))
# m = float(input('Tell me number: '))
# mass_units = {1: 0.001, 2: 1, 3: 100, 4: 1000}
# print(f'Масса равна {mass_units.get(n) * m} кг')

# 2) Данны данные по средним температурам в неделю трёх месяцев лета.
# summer = {
#     'Июнь': [20, 22, 24, 28],
#     'Июль': [24, 25, 29, 32],
#     'Август': [25, 28, 31, 29]}
# # 1. Вывести температуру первой недели лета.
# print(summer['Июнь'][0])
# # 2. Вывести максимальную температуру в июне.
# print(max(summer['Июнь']))
# # 3. Вывести минимальную температуру в июле.
# print(min(summer['Июль']))
# 4. Вывести максимальную температуру лета.
# if max(summer['Июнь']) > max(summer['Июль']) > max(summer['Август']):
#     print(max(summer['Июнь']))
# elif max(summer['Июль']) > max(summer['Август']) > max(summer['Июнь']):
#     print(max(summer['Июль']))
# else:
#     print(max(summer['Август']))
#
# print(max(max(summer['Июнь']), max(summer['Июль']), max(summer['Август'])))
# print(max(summer['Июнь'] + summer['Июль'] + summer['Август']))
#
# print(max(sum(summer.values(), [])))
# print(max(max(summer.values(), key=max)))

# 5. Сравнить какой месяц был самый жаркий и вывести его название(суммировать температуры каждого месяца).
# if sum(summer['Июнь']) > sum(summer['Июль']) > sum(summer['Август']):
#     print('Июнь')
# elif sum(summer['Июль']) > sum(summer['Август']) > sum(summer['Июнь']):
#     print('Июль')
# else:
#     print('Август')

# summer = {'Июнь': sum(summer['Июнь']), 'Июль': sum(summer['Июль']), 'Август': sum(summer['Август'])}
# print(max(summer, key=summer.get))

# print(max(summer, key=lambda x: sum(summer[x])))
# print(max(summer.items(), key=lambda x: sum(x[1]))[0])
#
# ДЗ, цикл for:
# 1. Сколько чисел в интервале от 100 до 200, которые делятся на 17 без остатка?
# count_i = []
# for i in range(100, 201):
#     if i % 17 == 0:
#         count_i.append(i)
# print(len(count_i))
#
# print(len([i for i in range(100, 201) if i % 17 == 0]))
# print([i for i in range(100, 201) if i % 17 == 0])
# print(len([i for i in range(102, 201, 17)]))
# print(len(range(102, 201, 17)))
#

# 2. Мы получаем список от пользователя вида spisok = [5, 0, -1, 3, -2, 10, -12, -20, 30, 7].
# # Вывести все положительные числа кратные 5 через запятую.
# spisok = [5, 0, -1, 3, -2, 10, -12, -20, 30, 7]
# new = []
# for i in spisok:
#     if i > 0 and i % 5 == 0:
#         new.append(i)
# print(*new, sep=',')

# print(*[i for i in spisok if i > 0 and i % 5 == 0], sep=',')

# 3. Мы получаем список от пользователя вида spisok = [5, 0, -1, 3, -2]. Вывести наименьшее положительное число в списке.
# spisok = [5, 0, -1, 3, -2]
# decision = []
# for i in spisok:
#     if i > 0:
#         decision.append(i)
# print(min(decision))
#
# print(min([i for i in spisok if i > 0]))

# 4. Написать программу, которая находит в списке spisok = [5, 4, -1, 0, -2, 0, 5, 4, 4, 7] число,
# которое встречается наибольшее количество раз.
# spisok = [5, 4, -1, 0, -2, 0, 5, 4, 4, 7]
# print(max(spisok, key=spisok.count))

# value = []
# for i in spisok:
#     value.append(spisok.count(i))
# print(value)
# max_value = max(value)
# print(max_value)
# index_max = value.index(max_value)
# print(index_max)
# print(spisok[index_max])

# winner = winner_count = 0
# for i in spisok:
#     x = spisok.count(i)
#     if x > winner_count:
#         winner = i
#         winner_count = x
# print(winner)


# 5. Написать программу которая подсчитывает количество цифр в строке, например "Олимпиада в Сочи была в 2014 году" и их сумму.
# Вывод должен быть "В строке цифр: X, сумма этих цифр: Y"
# stroka = "Олимпиада в Сочи была в 2014 году"
# y = 0
# x = ''
# for i in stroka:
#     if i.isdigit():
#         y += int(i)
#         x += i
# print(f"В строке цифр: {len(x)}, сумма этих цифр: {y}")

# value = [int(i) for i in stroka if i.isdigit()]
# print(f"В строке цифр: {len(value)}, сумма этих цифр: {sum(value)}")

# print(f"В строке цифр: {len(value := [int(i) for i in stroka if i.isdigit()])}, сумма этих цифр: {sum(value)}")

# Необходимо написать функцию, которая вернёт сумму всех элементов списка до n умноженных на свой индекс.
# Для пустого списка возвращаем 0.
# Пример:
# n = 5, index_multiplier([1, 2, 3, 4, 5]) ➞ 40
# n = 3, index_multiplier([2, 4, 6, 40, 50]) ➞ 16
# n = 6, index_multiplier([]) ➞ 0

# n = 3
# s = [2, 4, 6, 40, 50]
# c = 0
# for a, b in enumerate(s[:n]):
#     c += a * b
# print(c)


# 1: Как жизнь?
# 2: Всё, Ок, растут 2 сына дошкольника.
# 1: Сколько им лет?
# 2: Произведение их лет равно количеству уток.
# 1: Мне недостаточно информации.
# 2: Старший сын похож на мать.
# 1: Тогда понятно.
# Сколько лет детям?


# ДЗ:
# 1. Даны два целых числа A и B (A < B). Найти сумму квадратов всех чисел от A до B включительно.
#
# a = int(input('Tell me number A: '))
# b = int(input('Tell me number B: '))
# value = []
# for i in range(a, b + 1):
#         value.append(i ** 2)
# print(sum(value))
#
# print(sum(i ** 2 for i in range(a, b + 1)))


# 2. Даны целые положительные числа A и B (A < B). Вывести все целые числа от A до B включительно;
# при этом каждое число должно выводиться с новой строки столько раз, каково его значение.
# Например:
# a = 2
# b = 4
# 22
# 333
# 4444
# a = int(input('Tell me number A: '))
# b = int(input('Tell me number B: '))
# print(f"a = {a} \nb = {b}")
# for i in range(a, b + 1):
#     print(str(i) * i)
#
# print(*(str(i) * i for i in range(a, b + 1)), sep='\n')

# 3. Пользователь через пробел вводит целые числа в диапазоне [-20;20]. Найти произведение тех чисел, которые находятся в диапазоне [2;10],
# если таких чисел нет - вывести "-1".
# Пример:
# 13 -1 0 1   -> -1
# 3 4 14 -1   -> 12
# 1 2 3       -> 6

# value = input('Numbers: ').split()
# value2 = 1
# for i in value:
#     i = int(i)
#     if 1 < i < 11:
#         value2 *= i
# print(-1 if value2 == 1 else value2)

# A1 A2 A3 A4 A5 A6 A7 A8
# B1 B2 B3 B4 B5 B6 B7 B8
# C1 C2 C3 C4 C5 C6 C7 C8
# D1 D2 D3 D4 D5 D6 D7 D8
# E1 E2 E3 E4 E5 E6 E7 E8
# F1 F2 F3 F4 F5 F6 F7 F8
# G1 G2 G3 G4 G5 G6 G7 G8
# H1 H2 H3 H4 H5 H6 H7 H8


# for i in 'ABCDEFGH':
#     for j in '12345678':
#         print(i + j, end=' ')
#     print()

#  1  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31 32
# 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48
# 49 50 51 52 53 54 55 56
# 57 58 59 60 61 62 63 64
#
# for j in range(8):  # 0 1 2 3 ... 7
#     for i in range(1, 9):
#         print(f"{j * 8 + i:>2}", end=' ')
#     print()

#

# for i in range(4):
#     print('cat')
#     print('dog')

# Создать двухмерный список нулей 9 на 9. Распечатать список.
# ls = [[0] * 9 for i in range(9)]
# print(*ls, sep='\n')
# #
# for x in range(9):
#     for y in range(9):
#         print(ls[x][y], end=' ')
#     print()

# 1. Провести по главным диагоналям линии из 1. Распечатать список.
# for j in range(9):  # 0 1 2 3 ... 8
#     for i in range(9):
#         print(f"{int(i==j) or int(i + j == 8)}", end=' ')  # if one of them is true then print 1 if not print 0
#     print()

# for x in range(9):
#     ls[x][0 + x] = ls[x][8 - x] = 1
#     for y in range(9):
#         print(ls[x][y], end=' ')
#     print()

# # 2. Сделать рамочку из 1.  Распечатать список.
# for i in range(9):
#     for j in range(9):
#         print(f'{int(i == 0 or i == 9 - 1) or int(j == 0 or j == 9 - 1)}', end=' ')
#     print()

# for x in range(9):
#     ls[8][x] = 1
#     ls[x][0] = 1
#     ls[x][8] = 1
#     for y in range(9):
#         ls[0][y] = 1
#         print(ls[x][y], end=' ')
#     print()
# print(*ls, sep='\n')

# 3. Сделать букву z из 1.  Распечатать список.

# for i in range(9):
#     for j in range(9):
#         print(f'{int(i == 0 or i == 9 - 1) or int(i + j == 8)}', end=' ')
#     print()

# for x in range(9):
#     for y in range(9):
#         ls[0][y] = 1
#         ls[8][y] = 1
#         ls[x][8 - x] = 1
#         print(ls[x][y], end=' ')
#     print()


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

# *
# **
# ***
# ****

# for j in range(1, 5):
#     print('*' * j)

# Напишите программу, в которой задается  целое число n [1:9] и выводится лестница из n ступенек,
# i-я ступенька должна состоять из чисел от 1 до i без пробелов.
# Пример вывода:
# 1
# 12
# 123
# 1234
# 12345

# n2 = 4
# j = ''
# for i in range(1, n2 + 1):
#     j += str(i)
#     print(j)

# Напишите программу, в которой задается целое число n [1:9] и выводится пирамида из n ступенек,
# i-я ступень должна состоять из чисел от 1 до i и обратно без пробелов.
# Пример вывода:
#     1
#    121
#   12321
#  1234321
# 123454321

# n1, n2 = 1, 6  #input

# n1 = int(input('Tell me first number from 1 to 9: '))
# n2 = int(input('Tell me second number from 1 to 9: '))
# j = ''
# n2 = 6
# for i in range(1, n2 + 1):
#     j += str(i)
#     print(' ' * (n2 - i), j + j[:-1][::-1], sep='')

    # Напишите программу, в которой задается целое число n [1:9] и выводится ромб из n*2-1 ступенек,
# i-я ступень должна состоять из чисел от 1 до i и обратно без пробелов.
# Пример вывода:
#    1
#   121
#  12321
# 1234321
#  12321
#   121
#    1

# n1, n2 = 1, 4
# n1 = int(input('Tell me first number from 1 to 9: '))
# n2 = int(input('Tell me second number from 1 to 9: '))
j = ''
#
# for i in range(1, n2):
#     j += str(i)
#     k = j + j[-2::-1]
#     print(f"{k:^15}")
# #
# for i2 in range(int(len(k) / 2)):
#     print(f"{k[:int(len(k) / 2) - i2] + k[int(len(k) / 2) + 2 + i2:]:^15} ")
# n1, n2 = 1, 5
# for i in range(1, n2 + 1):
#     j += str(i)
#     print(' ' * (n2 - i), j + j[:-1][::-1], sep='')
#
# for i in range(1, n2):
#     # k = j[:-1]
#     print(j[:n2 - i] + j[::-1][n2  - i:])
#     exit()

# for i in range(1, n2 + 1):  # 1, 2, 3, 4
#     j = j[:-1]
#     print(' ' * i, j + j[:-1][::-1], sep='')  # 1, 2, 3, 4


# n2 = 4
# for i in range(1, n2 + 1):  # 1, 2, 3, 4
#     print(*range(1, i + 1), sep='')

# n2 = 4
# for i in range(1, n2 + 1):  # 1, 2, 3, 4
#     print(' ' * (n2 - i), *range(1, i + 1), *range(i - 1, 0, -1), sep='')

# n2 = 4
# for i in range(1, n2 + 1):  # 1, 2, 3, 4
#     print(' ' * (n2 - i), *range(1, i + 1), *range(i - 1, 0, -1), sep='')
# for i in range(n2 - 1, 0, -1):  # (3, 0, 1)
#     print(' ' * (n2 - i), *range(1, i + 1), *range(i - 1, 0, -1), sep='')
#
# print(*range(2, 8, 2))
# print(*range(8, 2, -2))
#
# for i in range(4):
#     print(i, 'cat')

# ДЗ, while:
# 1. Пользователь вводит по одному либо названия фруктов, либо целые числа. Стоп-слово - exit.
# Вывести в результате сумму чисел и список фруктов.
# i, list_fruit = 0, []
# while True:
#     fruit_number = input('Tell a fruit or a number: ')
#     if fruit_number.isdigit():
#         i += int(fruit_number)
#     elif fruit_number == 'exit':
#         break
#     else:
#         list_fruit.append(fruit_number)
# print(i, list_fruit)
# 2. Пользователь вводит по одному числа. Стоп-слово "exit". Найти какая сумма больше чётных чисел или нечётных.
# even_numbers = odd_numbers = 0
# while True:
#     value = input('Number: ')
#     if value == 'exit':
#         break
#     v = int(value)
#     if v % 2 == 0:
#         even_numbers += v
#     else:
#         odd_numbers += v
# print('The sum of odd numbers is greater' if odd_numbers > even_numbers else 'The sum of even numbers is greater')




# 3. В банк положили 1000 руб под процент 10% в год. Через сколько лет на счету будет 1 млн руб?
# count, r = 1000, 0
# while count < 1000000:
#     count *= 1.1
#     r += 1
# print(r, count)
# 1000 + 100 = 1100
# 1000 * x    = 1100
# x = 1.1

# 1 - 100
# 1.1 - 110
# 1.5 - 150
#
# 1 - 100
# x - 180
#
# x = 1 * 180 / 100 = 1.8


# Вывести на экран таблицу умножения (от 1 до 10)
# 1. Таблица Пифагора https://free4print.ru/wp-content/uploads/2015/09/tablica-umnozheniya-cherno-belaya-650x919.jpg
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i * j:>2}', end=' ')
#     print()
# 2. Столбики друг под другом, разделённые пустой строкой.
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i * j:>2}')
#     print()
# 3. https://mama.ru/wp-content/uploads/2017/09/tabl-1.jpg
#
# for x in range(2):
#     for i in range(1, 11):
#         for j in range(2, 6):
#             print(f'{j + 4 * x} * {i:>2} = {i * (j + 4 * x):>2}   ', end=' ')
#         print()
#     print()

#
# ДЗ:
# 1. Написать программу, которая находит в списке spisok = [5, 4, -1, 0, -2, 0, 5, 4, 4, 7] число,
# которое встречается наибольшее количество раз.
# spisok = [5, 4, -1, 0, -2, 0, 5, 4, 4, 7]
# print(max(spisok, key=spisok.count))

# 2. Дан список целых чисел. Вывести максимальное количество его одинаковых элементов и сам элемент.
# s = [0, 1, 1, 1, 2, 3, 3, 4] -> 'Элемент: 1, повторений: 3'
# s = [0, 1, 1, 1, 2, 3, 3, 4]
# m = max(s, key=s.count)
# print(f'Элемент: {m}, повторений: {s.count(m)}')

#
# Повторяем циклы:
# 1.  У нас есть участники соревнования с данными.
# Например: Иван - 10 баллов, Семён - 20 баллов, Игорь - 30, Алекс - 5 баллов.
# Вывести  тройку победителей каждого с новой строки с 1 по 3 места.
# Затем 15 баллов набирает Света. Вывести новую тройку победителей.
# 1 место: Игорь - 30

# grades = {'Ivan': 10,
#           'Alex': 5,
#           'Semen': 20,
#           'Igor': 30}
#
# # print(sorted(grades, key=grades.get, reverse=True)[:3])
# for x, y in enumerate(sorted(grades, key=grades.get, reverse=True)[:3], 1):
#     print(f'{x} место: {y} - {grades[y]}')


# w = []
# while len(w) < 3:
#     for i in sorted(grades, key=grades.get, reverse=True):
#         w.append(i)
#     print(w[:3])
#     # print(*sorted(grades, key=grades.get, reverse=True)[:3])
#     grades.update({'Sveta': 15})
#     print(grades[str(sorted(grades, key=grades.get, reverse=True))])


#
# 2. Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае.
# После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и
# просит вас помочь ей определить, какие числа мог задумать Август.
#
# Входные данные:
# Первая строка входных данных содержит число n — наибольшее число, которое мог загадать Август.
# Далее идут строки, содержащие вопросы Беатрисы. Каждая строка представляет собой набор чисел, разделенных пробелами.
# После каждой строки с вопросом идет ответ Августа: YES или NO.
#
# Наконец, последняя строка входных данных содержит одно слово HELP.
#
# Выходные данные:
# Вы должны вывести все числа, которые мог задумать Август через запятую.
#
# Пример 1:
# # входные данные:
# # До какого числа? 13
# # Введите числа: 2 4 6 7 8 9 12 13
# # Правильно? NO
# # Введите числа: HELP
# # 1, 3, 5, 10, 11
#
# Пример 2:
# До какого числа? 10
# Введите числа: 1 2 3 4 5
# Правильно? YES
# Введите числа: 2 4 6 8
# Правильно? NO
# Введите числа: HELP
# 1, 3, 5, 10
#
# Пример 3:
# До какого числа?:10
# Введите числа:2 4 6
# Правильно?:YES
# Введите числа:6 8 10
# Правильно?:YES
# Введите числа:HELP
# 6


# n = int(input('До какого числа?: '))
#
#
# for i in an:
#     if i.isalpha():
#         print(i)
#         print(*range(1, n + 1))


# while True:  # вечный цикл
#     an = input('Введите числа: ')
#     if an == 'HELP':
#         break
#     x = input('Правильно? ')

