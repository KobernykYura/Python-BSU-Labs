import matplotlib.pyplot as plt
import numpy as np

# Задание 13. Реализуйте код, приведенный в примерах

# 1) Именованные аргументы
x = np.arange(0., 5., 0.2)
y = x**2

plt.plot(x, y, linewidth=2.0)
plt.show()

# 2) Сеттер 2D
line, = plt.plot(x, y, '-')
line.set_antialiased(False)

# 3) Использование комманды setp()
x1 = np.arange(0., 5., 0.2)
y1 = x1**(0.5)
x2 = np.arange(1., 5., 0.1)
y2 = x2**2
lines = plt.plot(x1, y1, x2, y2)

plt.setp(lines, color='g', linewidth=2.0)
plt.show()
