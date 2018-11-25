import matplotlib.pyplot as plt
import numpy as np

# Задание 14. Реализуйте код, приведенный в примерах


def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# Отдельное окно для графиков 1
plt.figure(1)

# График размером:211
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# График размером:212
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# Отдельное окно для графиков 2
plt.figure(2)
plt.plot([4, 5, 6])

# Отдельное окно для графиков 2
plt.figure(3)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# График размером:212
plt.figure(1)
plt.subplot(211)
plt.title('Easy 1, 2, 3')
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
