import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3 ) * np.exp(-x ** 2 - y ** 2)

n = 10
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3.0 * n)
X, Y = np.meshgrid(x, y)
plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(f(X, Y), interpolation='nearest', cmap='bone', origin='lower')
# colorbar - добавление к рисунку цветовой столб-индикатор цветового пространства
# работает с изображениями
plt.colorbar(shrink=.92)
plt.xticks(()) # Убрать штрихи
plt.yticks(())

plt.show()
