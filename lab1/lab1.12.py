import matplotlib.pyplot as plt
import numpy as np

# Задание 12. Реализуйте код, приведенный в примерах

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10*np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

# Динамически закрепляем на графике переменные из объекта 
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

# Отдельное окно для графиков
plt.figure(1, figsize=(9, 3))

# Диаграмма (столбцы)
plt.subplot(131)
plt.bar(names, values)

# Точечный график
plt.subplot(132)
plt.scatter(names, values)

# Линейный график
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()
