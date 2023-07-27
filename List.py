# l = [1, 2, 'cat', [1, 2]]
# print(l)
#
# for i in l:
#     print(i)

# a = input().split()
# print(a)

# l1 = []

# for i in range(10):
#     l1.append(int(input()))
#
# print(l1)

# i = int(input())
#
# while i != 0:
#     i = int(input())
#     l1.append(i)
#
# print(l1)

# new_l = input('Write: ').split()
#
# for i in new_l:
#     if int(i) < 5:
#         print(i)
#
# a = [i * 2 for i in range(15) if i % 2 == 0]
# print(a)
# # b = [i for i in input().split()]
#
# print(len(a))
# print(a + l)
# print(a * 4)
# print(a[1])
# print(l[3][1])
# print(l[-1])
# print(a[:7:2])
# print(a[::-1])
# print(a[3::3])
# print(a[1:-1])

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# l.append(11)
# print(l)
#
# l.extend([1, 2, 3])
# print(l)
#
# l.insert(4, 6)
# print(l)
#
#
# l.remove(7)
# print(l)
#
# print(l.pop(7))
# print(l)
#
# print(l.index(5, 1, 10))
#
# print(l.count(5))
#
# l.sort(reverse=True)
# print(l)
#
# text_l = ['text', 'a', 'A']
# text_l.sort()
#
# print(text_l)
#
# l.reverse()
# print(l)
#
# # l.clear()
# # print(l)
#
#
# print(sum(l, 100))
# l2 = [[4, 5], [6, 7]]
#
# print(sum(l2, []))
# for i in range(l.count(6)):
#     l.remove(6)
#
# print(l)



# 1)Створити список із семи цифр від 1 до 8
# l = [i for i in range(1, 9)]
# print(l)
# # 2)Видалити в ньому першу цифру 6
# l.remove(6)
# print(l)
# # 3)додати 6 нулів на початок списку
# for i in range(6):
#     l.insert(0, 0)
#
# print(l)
# # 4)додати число 100 в середину списку
# l1 = len(l) // 2
# l.insert(int(l1), 100)
# print(l)
#
# # 5)Додати 19 чисел 55 в кінець списку
# for i in range(19):
#     l.append(55)
#
# print(l)
# # 6)Видалити всі числа 55 зі списку
# for i in range(l.count(55)):
#     l.remove(55)
#
# print(l)

# listt = [-1, 0, 5, 3, 2]
# l2 = []
# for i in listt:
#     l2.append(i + 7.2)
#
# print(l2)

# l = int(input('Numbers: '))
# l2 = []
#
# while l != 0:
#     l2.append(l ** 2)
#     l = int(input('Numbers: '))
#
# print(l2)

# Написати програму видалення зі списку всіх номерів із кодом "+1" -
# ['+191734734', '+1915125456', '+6915213456', '+4915213456', '+1915634456']

# numbers = ['+191734734', '+1915125456', '+6915213456', '+4915213456', '+1915634456'] # todo
# n = []
# for i in numbers:
#     if not i.startswith('+1'):
#         n.append(i)
#
# print(n)

# l = [1, 2, 3, 4, 5, 6]
#
# print(l[1:] + l[0:1])
#
# l = input('Numbers: ').split()
#
# for i in l:
#     if 27 < int(i) < 93:
#         if int(i) % 2 == 0:
#             print(i)

# Написати аналогічну програму циклічного зсуву, але тепер вправо.

# l = [1, 2, 3, 4, 5, 6]
#
# print(l[-1:] + l[:-1])
#
# # Знайдіть суму всіх парних елементів списку.
#
#
# l1 = [int(i) for i in input('numbers: ').split() if int(i) % 2 == 0]
#
# print(sum(l1))
#
# # Виведіть усі елементи списку з парними індексами
#
# v = input('numbers: ').split()
#
# print(v[1::2])

# Користувач вводить з клавіатури числа, доти, доки не введе число 0.
# На основі введених даних потрібно сформувати список, що складається тільки з парних чисел.

# value = int(input('Numbers: '))
# new_l = []
#
# while value != 0:
#     if value % 2 == 0:
#         new_l.append(value)
#     value = int(input('Numbers: '))
#
# print(new_l)

#

# v = [int(i) for i in input('Numbers: ').split()]
# v1 = v.index(min(v))
# v2 = v.index(max(v))
#
# v[v1], v[v2] = v[v2], v[v1]
#
# print(v)
#

# n = [1, 2, 3, 1, 4, 1]
# n.sort()
# c = 0
# for i in range(len(n)):
#     if n[i] != n[i + 1]:
#         c += 1
#
# print(c)

# for i in range(len(n)):
#     if n[i] > n[i - 1]:
#         print(n[i])
#

# #
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# print(m[::2])

# Дано список чисел. Виведіть значення найбільшого елемента у списку, а потім індекс цього елемента у списку.
# Якщо найбільших елементів кілька, виведіть індекс першого з них (Не використовуючи min max)

# v = input('Numbers: ').split()
# n = []
#
# for i in range(len(v)):
#     if v[i] > v[i - 1]:
#         n.append(v[i])
#
# print(n[-1], v.index(n[-1]))
#
# Дано список чисел. Якщо в ньому є два сусідні елементи одного знака, виведіть ці числа.
# Якщо сусідніх елементів одного знака немає - не виводьте нічого. Якщо таких пар сусідів кілька - виведіть першу пару
#
#
# v = [int(i) for i in input('Numbers: ').split()]
#
# for i in range(len(v) - 1):
#     if v[i] > 0 and v[i + 1] > 0:
#         print(v[i], v[i + 1])
#     elif v[i] < 0 and v[i + 1] < 0:
#         print(v[i], v[i + 1])


#
# Вводяться цілі числа в один рядок через пробіл (не менше чотирьох).
# Необхідно знайти три найменших числа в цій послідовності чисел і вивести їх на екран у порядку
# зростання.
# #
# v = input('Numbers: ').split()
# v.sort()
# print(v[:3])

# Вводиться інформація по книзі (кожне значення з нового рядка): назва, автор, число
# сторінок (ціле число), ціна (дійсне число).На основі цих даних формується список book з елементами в порядку їхнього введення.
# Потім, з цього списку необхідно видалити 3-й елемент (число сторінок), як автора записати "Тарас Шевченко" і ціну збільшити в 2 рази.
#
# book_name = input()
# book_autor = input()
# book_page = input()
# book_price = input()
#
# book = [book_name, book_autor, book_page, book_price]
# book.remove(book_page)
# book.insert(book.index(book_autor), 'Тарас Шевченко')
# m = int(book[book.index(book_price)]) * 3
# book[book.index(book_price)] = m
# print(book)



