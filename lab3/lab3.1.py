import numpy as np
import matplotlib.pyplot as plt

# figsize - размер фигуры
# dpi - качество изображения
plt.figure(figsize=(8,5),dpi=80) 
plt.subplot(111)

# np.linspace - Возвращайте равномерно распределенные
#  числа за определенный интервал.
X = np.linspace(-np.pi,np.pi,256,endpoint=True)
C, S = np.cos(X), np.sin(X) # sin & cos

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

# Установка осей по центру графика
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom') # установка штрихов ниже линии X
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left') # установка штрихов левее от Y
ax.spines['left'].set_position(('data', 0))

# Устанновка границ рисунка
plt.xlim(X.min() * 1.1, X.max() * 1.1)
# ------ Задание значения штрихов по X
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])

plt.ylim(X.min() * 1.1, X.max() * 1.1)
# ------ Задание значения штрихов по Y
plt.yticks([-1,1],
           [r'$-1$',r'$+1$'])
plt.legend(loc='upper left')

# Значение точки
t = 2*np.pi/3 
# ------ Значение t на COS относительно оси X
plt.plot([t,t],[0,np.cos(t)],
         color='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color='blue')
plt.annotate(r'$cos(\frac{2\pi}{3})=\frac{\sqrt{1}}{2}$',
             xy=(t, np.cos(t)),xycoords='data',
             xytext=(-90,-50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# ------ Значение t на SIN относительно оси X
plt.plot([t,t],[0,np.sin(t)],
         color='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color='red')
plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)),xycoords='data',
             xytext=(10,30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.show()


