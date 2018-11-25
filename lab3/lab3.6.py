import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n) # Массив 12 элементов
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.axes([0.025, 0.025, 0.95, 0.95])
# Разукрашивание осей
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# Картежный перебор синего массива  
for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va= 'bottom')

# Картежный перебор красного массива 
for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va= 'top')

# Сдвиг осей на интервалы
plt.axis([-0.5,12,-1.25,1.25])
plt.show()