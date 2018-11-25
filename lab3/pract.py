import numpy as np
import matplotlib.pyplot as plt

# figsize - размер фигуры
# dpi - качество изображения
plt.figure(figsize=(8, 5), dpi=80)
plt.subplot(111)

# np.linspace - Возвращайте равномерно распределенные
#  числа за определенный интервал.
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)  # sin & cos


# axes() - азмещение рисунка поверх другого по особым координатам
plt.axes([.1, .1, .8, .8])
plt.xticks(())
plt.yticks(())
plt.text(.6, .6, '',
         ha='center', va='center', size=20, alpha=.5)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")


# Установка осей по центру графика
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # установка штрихов ниже линии X
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')  # установка штрихов левее от Y
ax.spines['left'].set_position(('data', 0))


plt.axes([.2, .2, .3, .3])
plt.xticks(())
plt.yticks(())
plt.text(.5, .5, '',
         ha='center', va='center', size=10, alpha=.5)

plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

# Установка осей по центру графика
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # установка штрихов ниже линии X
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')  # установка штрихов левее от Y
ax.spines['left'].set_position(('data', 0))


plt.show()
