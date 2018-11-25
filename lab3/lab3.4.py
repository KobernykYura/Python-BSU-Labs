import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.plot(X,Y+1, color='blue', alpha=1.00)
# Красим все промежутки в синий цвет поднимая график вверх на 1 
plt.fill_between(X, Y+1, y2=1, where=None, interpolate=False, step=None, data=None,color='cornflowerblue')

plt.plot(X,Y-1, color='blue', alpha=1.00)
# Красим верхние промежутки в синий цвет,
# нижние в красный, опуская график вниз на 1 
plt.fill_between(X, Y-1, y2=-1, where=Y>0, interpolate=False, step=None, data=None,color='cornflowerblue')
plt.fill_between(X, Y-1, y2=-1, where=Y<0, interpolate=False, step=None, data=None,color='pink')
plt.show()