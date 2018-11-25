import numpy as np

# Задание 1. Используя приведенный пример, создайте матрицу a, найдите ее размерность, тип
# данных, размер элемента в матрице, размер матрицы, количество элементов. Создайте массив b,
# содержащий одну строку [6, 7, 8].

a = np.arange(15).reshape(3, 5)
b = np.array([6, 7, 8])

# Размерности матриц (кол-во осей)
print('Length of \"a\" as number of axis:\t', str(a.ndim))
print('Length of \"b\" as number of axis:\t', str(b.ndim), '\n')

# Размерности матриц (по осям)
print('Length of \"a\" as tuple:\t', str(a.shape))
print('Length of \"b\" as tuple:\t', str(b.shape), '\n')

# Кол-во элементов в массиве
print('Length of \"a\" as size:\t', str(a.size))
print('Length of \"b\" as size:\t', str(b.size), '\n')

# Типы данных матриц
print('Type of elements in \"a\":\t', str(a.dtype))
print('Type of elements in \"b\":\t', str(b.dtype), '\n')

# Типы данных матриц после явного задания типа
a = np.array([2.01, 3, 5, 7], np.int64)
b = np.array([2.01, 3, 5, 7], complex)

print('Type of elements in \"a\":\t', str(a.dtype))
print('Type of elements in \"b\":\t', str(b.dtype), '\n')

# Размер элемента в матрице
print('Size of each item in \'a\' of \'{0}\':\t{1}'.format(
    a.dtype, str(a.itemsize)))
print('Size of each item in \'b\' of \'{0}\':\t{1}\n'.format(
    b.dtype, str(b.itemsize)))

# Создание массива нулей
print(np.zeros((2, 4), dtype=np.int64), '\n')

# Создание массива единиц
print(np.ones((3, 6), dtype=np.int16), '\n')

# Создание массива из значений (arange)
print(np.arange(0, stop=10, step=2, dtype=np.int32), '\n')

# Создание массива из значений (arange)
z = np.linspace(0, stop=40, num=12, dtype=np.int32)
print('Array:\n{0}\nSize:\t{1}'.format(z, z.size), '\n')
