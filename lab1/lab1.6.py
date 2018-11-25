import numpy as np
from numpy import newaxis

# Задание 6. Реализуйте код, приведенный в примере. Изучите работу функций: hstack, vstack,
# column_stack, concatenate, c_, r_.

a = np.floor(10*np.random.random((2, 2)))
b = np.floor(10*np.random.random((2, 2)))

v = np.vstack((a, b))
h = np.hstack((a, b))
print('np.vstack = \n', v, '\n')
print('np.hstack = \n', h, '\n')

d = np.column_stack((a, b))
print('np.column_stack = \n', d, '\n')
a = np.array([4., 2.])
b = np.array([3., 8.])

# Для двумерных
d = np.column_stack((a, b))
print('np.column_stack(([4., 2.],[3., 8.])) = \n', d, '\n')

# Объединение вдоль второй размерности
d = np.hstack((a, b))
print('np.hstack = \n', d, '\n')

print(a[:, newaxis], '\n')
print(np.column_stack((a[:, newaxis], b[:, newaxis])), '\n')
print(np.hstack((a[:, newaxis], b[:, newaxis])), '\n')

z = np.floor(10*np.random.random((2, 12)))
d1 = np.hsplit(z, 3)
print('np.hsplit(z, 3) = \n', d1, '\n')
d2 = np.hsplit(a, (3, 4))
print('np.hsplit(z, (3, 4)) = \n', d2, '\n')

print('d1.r_ = ', np.r_, '\n')  # Класс RClass
print('d2.r_ = ', np.c_, '\n')  # Класс CClass

print('concatination of d1 element = \n', np.concatenate(d1), '\n')
