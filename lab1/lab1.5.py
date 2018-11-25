import numpy as np

# Задание 5. Реализуйте код, приведенный в примере. Изучите работу функции ndarray.shape,
# reshape, resize, ravel.


# Реализуйте код приведенный в примерах (START)
a = np.floor(10*np.random.random((3, 4)))
print('a=\n', a, '\n')
print('a.shape =\n', a.shape, '\n')

print('a.ravel =\n', a.ravel(), '\n')  # В строку
print('a.reshape(6, 2)', a.reshape(6, 2), '\n')  # По заданной форме shape(6,2)
print(a.T, '\n')
print(a.T.shape, '\n')
print(a.shape, '\n')

a = np.floor(10*np.random.random((3, 4)))
print(a, '\n')
a.resize((2, 6))
print('a.resize((2, 6))\n', a, '\n')
a.reshape(3, -1)
print(a, '\n')
b = a.reshape(3, -1)
print('a.reshape(3, -1)\n', b, '\n')
# Реализуйте код приведенный в примерах (END)
