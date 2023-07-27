# a = 'Hello, Evgeniy'
# b = 'Deutsch'
# print(a + b)
# print(b + a)
# print(a * 5)
# print(len(a))
# print(a[3])
# print(a[3:15])
# print(a[3:-3])
# print(a[:8])
# print(a[7:])
# print(a[7::2])
# print(b[7::-2])
# print(a[7::-2])
# print(a[2])
# print(a[-2])
# print(a[:5])
# print(a[:-2])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[::-2])
# print(len(a))

# b = ' White cAt, Black Cat '
# print(b.upper())
# print(b.lower())
# print(b.capitalize())
# print(b.title())
# print(b.strip())
# print(b.rstrip())
# print(b.lstrip())
# print(b.replace('a', 'A', 1).upper())
# print(b.count('a', 0, 40))
# print(b.find('a', 0, 45))
# print(b.rfind('a', 8))
# print('+-*/-+apple+++---///*'.strip('+-*/'))
# print(b.swapcase())

##
# st = input('Tell smsh: ')
#
# if stroka.count('f') == 1:
#     print(stroka.find('f'))
# elif stroka.count('f') >= 2:
#     print(stroka.find('f'), stroka.rfind('f'))
# else:
#     pass

# print(stroka.count(' ') + 1)

# a = stroka.find('ra')
#
# for i in range(stroka.count('ra')):
#     print(stroka.find('ra'))
#     stroka.replace('ra', '  ')

# З рядка "abrakadabra" видаліть усі сполучення "ab".

# print(stroka.replace('ab', ' '))

# if stroka == stroka[::-1]:
#     print('Yes')
# else:
#     print('No')

# print(st[:st.find('h')] + st[st.rfind('h') + 1:])
# l = len(st) // 2
# print(st[l:] + st[:l])
# print(st.replace('1', 'one'))

# Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.

# st1 = 'Hey - you'.split()
# print(st1[2], st1[1], st1[0])
#
# st11 = 'Hey - you'
# print(st11[st11.find('-') + 1:], '-', st11[:st11.find('-')])

# Дана строка. Удалите из этой строки все символы @.

# str2 = '@ hey, @ user @'
# print(str2.replace('@', ''))

# Дана строка. Найдите в этой строке послднее вхождение буквы f, и выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз, выведите число -1, а если не встречается ни разу,
# выведите число -2.

# str3 = input('Tell me smth: ')
# print(str3.rfind('f'))
#
# if str3.count('f') == 1:
#     print(-1)
# elif str3.count('f') == 0:
#     print(-2)

# У рядку "abrakadabra" знайдіть усі індекси підрядка "ra" і виведіть їх (індекси) в консоль.

# abra = 'abrakadabra'
# print(abra.find('ra'))


#
# number = input('Number is: ')
#
# if len(number) == 12 and number[1] == '(' and number[5] == ')'\
#     and number.replace('(', '').replace(')', '').isdigit():
#     print('correct number', number)
# else:
#     print('uncorrect number')

#
# text = 'finished'
#
# print(text[1::2])

#
# t = 'whatever'
# t1 = 'with'
# print(t, t1)
#
# t = 'python'
# print(f'The text is: {t}. The len is: {len(t)}.')

#
# cities = 'Kyiv Kharkiv Lviv'
#
# print(cities.replace(' ', ', '))

#
# text = input('Tell me: ')
# c = 0
#
# for i in text:
#     if i.islower():
#         c += 1
#
# print(c)

# #
# name = 'Anastasia'.lower()
# k = ''
#
# for i in name:
#     if i == 'a':
#         k += i + name
#
# print(k)

#
# st = 'yellow'
# s = ''
# for i in st:
#     if i == 'y':
#         s += 'a'
#     else:
#         s += i
#
# print(s)

# #
# text = 'American English ua'.split()
#
# c = 0
# for i in text:
#     if len(i) <= 4:
#         print(len(i))

# for i in text:
#     if len(i) <= 4:
#         c += 1
#
# print(c)

#

# text = 'Whatever'
# print(text[-3:])

#
# Знайти кількість слів у рядку, які починаються з літери "П".
# Вивести на екран довжину найкоротшого і найдовшого слова в рядку.
# text1 = 'Погода в Германии, прогноз погоды в'.lower().split()
# c = 0
#
# for i in text1:
#     if i.startswith('п'):
#         c += 1
#
# print(c, min(text1, key=len), max(text1, key=len))
#
#
# # Замінити всі цифри "5" в рядку на цифри "9".
#
# number = '380505564375'.replace('5', '9')
# print(number)
#
# # Порахувати кількість великих літер у рядку
#
# text = 'ResulTs that Speak'
# c = 0
#
# for i in text:
#     if i.isupper():
#         c += 1
#
# print(c)