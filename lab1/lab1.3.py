import numpy as np

# Задание 3. Реализуйте код приведенный в примерах. Для матрицы b найдите максимальный
# элемент по всей матрице, по строкам, по столбцам.

# Реализуйте код приведенный в примерах (START)
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a-b
d = b**2
f = 10*np.sin(a)  # Поэлементное произведение
k = a < 35

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
D = A * B  # Поэлементное произведение
V = np.dot(A, B)  # Векторное произведение
print('Each element multiplication:\n{0}\n'.format(D))
print('Vector multiplication:\n{0}\n'.format(V))

b = np.arange(12).reshape(3, 4)
print('b=\n',b)

s1 = np.sum(b, axis=0)  # Сумма по столбцам
s2 = np.sum(b, axis=1)  # Сумма по строкам

print('Сумма по столбцам:\t{0}\n'.format(s1))
print('Сумма по строкам:\t{0}\n'.format(s2))
# Реализуйте код приведенный в примерах (END)


a1 = np.max(b, axis=0)  # Max по столбцам
a2 = np.max(b, axis=1)  # Max по строкам
a3 = np.max(b)  # Max по всей матрицы

print('Max по столбцам:\t{0}\n'.format(a1))
print('Max по строкам:\t{0}\n'.format(a2))
print('Max по всей матрицы:\t{0}\n'.format(a3))

a1 = np.min(b, axis=0)  # Min по столбцам
a2 = np.min(b, axis=1)  # Min по строкам
a3 = np.min(b)  # Min по всей матрицы

print('Min по столбцам:\t{0}\n'.format(a1))
print('Min по строкам:\t{0}\n'.format(a2))
print('Min по всей матрицы:\t{0}\n'.format(a3))

a1 = np.sin(b)  # Sin элементов матрицы
a2 = np.cos(b)  # Cos элементов матрицы
a3 = np.exp(b)  # Exp элементов матрицы

print('Sin элементов матрицы:\n{0}\n'.format(a1))
print('Cos элементов матрицы:\n{0}\n'.format(a2))
print('Exp элементов матрицы:\n{0}\n'.format(a3))
