import numpy as np

# Задание 2. Наберите код, приведенный в разделе «Создание массивов» в отдельном файле
# “myArray.py”. Выведите все массивы на экран, сравните вывод двухмерных и трехмерных массивов.
# Самостоятельно изучите работу функций array, zeros, zeros_like, ones, ones_like, empty, empty_like,
# arange, linspace, numpy.random.rand, numpy.random.randn, fromfunction, fromfile.

print('Работа функции array:\n', np.array(
    (2, 3, 4.11, 56, 7.3), dtype=np.float), '\n')

print('Работа функции zeros:\n', np.zeros((2, 3, 5), dtype=np.int32), '\n')
print('Работа функции zeros_like:\n',
      np.zeros_like([(4, 4, 2, 3), (5, 5, 5, 5)], dtype=np.int32), '\n')

print('Работа функции ones:\n', np.ones((2, 3), dtype=np.float), '\n')
print('Работа функции ones_like:\n', np.ones_like([(4, 4, 2, 3), (5, 5, 5, 5)]), '\n')

print('Работа функции empty:\n', np.empty((2, 3)), '\n')
print('Работа функции empty_like:\n', np.empty_like((2, 3, 4, 6, 3)), '\n')

print('Работа функции arange:\n', np.arange(
    start=6, stop=99, step=10, dtype=np.int32), '\n')
print('Работа функции linspace:\n', np.linspace(
    start=3, stop=33, num=5, dtype=int), '\n')

print('Работа функции numpy.random.rand:\n', np.random.rand(1, 4, 9), '\n')
print('Работа функции numpy.random.randn:\n', np.random.randn(4, 4), '\n')
