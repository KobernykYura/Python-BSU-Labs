import matplotlib.pyplot as plt
import numpy as np

n = 2048
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

plt.scatter(X, Y,c=np.arctan2(Y,X), alpha=.5)
plt.axis([-1,1,-1,1])
plt.show()