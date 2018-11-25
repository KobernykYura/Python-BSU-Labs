import matplotlib.pyplot as plt
import numpy as np

n = 8
X, Y = np.mgrid[0:n, 0:n]
#plt.quiver(X, Y)
T = np.arctan2(Y - n / 2., X - n/2.)
R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
U = R * np.cos(T)
V = R * np.sin(T)
plt.quiver(X, Y, U, V, R, alpha=.5)
plt.quiver(X, Y, U, V, edgecolor='black', facecolor='None', linewidth=.5)

plt.xticks(())
plt.yticks(())
plt.show()