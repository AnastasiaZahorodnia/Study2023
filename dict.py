# d = {'key': 'value', 2: 3.6, 3: [4, 5]}
#
# d1 = {}
#
# for i in range(3):
#     a = input()
#     b = input()
#     d1[a] = b
#
# print(d1)
#
# del d1['key']
#
# print(d1)

# new_d = dict(key = 4, key2 = 'value', g = 5.6)
#
# l_d = [i for i in 'hello']
# n_d = {i: i * 2 for i in 'hello'}
# print(n_d)
#
# c = [('a', 'b'), ('c', 'd')]
#
# for i, k in c:
#     print(i)
#     print(k)


dict_n = {'k': 'v', 1: 2, 1.3: 4.5}
for i in dict_n.keys():
    print(i)

for i, j in dict_n.items():
    print(i, j)

for i in dict_n.values():
    print(i)

print(list(dict_n.values()))

dict_n.update({'a': 3})

print(dict_n)

print(dict_n.pop('h', 7), dict_n)

print(dict_n.popitem(), dict_n)

print(dict_n.setdefault('p', 6), dict_n)

print(dict_n.get('k'))

print(list(dict_n.keys())[:1])

print(dict_n['k'])

d1 = {1: 1.0, 1.0: 0.1, True: 0.1, 0.1: True}
print(d1)

d2 = {0: 'cat', 0.0: 'dog', False: 'm'}
print(d2)

print(hash(0), hash(0.0), hash(False))

f = {}.fromkeys([8, 9, 6], 'get')

print(f)

h = {**f, **d1}

print(h)

a = f | d1

print(a)

f.update({'gr': 3})

print(f)

print(sorted({4: 6, 8: 7}, reverse=True))

from collections import *

l = [1, 2, 1, 4, 5, 2]
count = Counter(l)
print(count)

print(count.most_common())

d = deque([8, 9, 6])
d.popleft()
print(d)

d.appendleft(4)
print(d)

g = defaultdict(str)

for i in range(10):
    if i % 2 == 0:
        g['even'] = ''.join(str(i))
    else:
        g['odd'] = str(i)

print(g)