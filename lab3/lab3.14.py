import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='hot')
ax.set_zlim(-2, 2)


ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
plt.show()
