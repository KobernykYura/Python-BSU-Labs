import numpy as np

'''
 Задание 7. Реализуйте код, написанный в примерах,
 закомментируйте строки без комментариев.

 Комментарий без комментария!!!
'''

a = np.arange(12)
b = a
print('b is a = ', b is a)
b.shape = 3, 4

# Изменены обе переменных
print('b.shape = a.shape = ', b.shape == a.shape)

# Передана не копия массива


def f(x):
    print(id(x))


# Проверяем id элементов
print(id(a))
f(b)

c = a.view()  # Наследование данных
print('c is a = ', c is a)
print('c.base is a = ', c.base is a)

print('c.flags.owndata = ', c.flags.owndata)
c.shape = 2, 6
print('a.shape == c.shape = ', a.shape == c.shape)
c[0, 4] = 1234
print('a = \n', a, '\n')
print('c = \n', c, '\n')

print('a[0, 4] == c[0, 4] = ', a[1, 0] == c[0, 4])

d = a.copy()  # Копирование

print('d = \n', d, '\n')
print('c = \n', c, '\n')

print('d is a = ', d is a)
print('d.base is a = ', d.base is a)
d[0, 0] = 9999
print('a[0, 0] == d[0, 0]   =  ', a[0, 0] == d[0, 0])
