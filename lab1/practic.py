import numpy as np
import matplotlib.pyplot as plt

a = np.random.rand(10,10)

print(a, '\n')

print(a.flat, '\n')

plt.hist(a.flat)
plt.show()
