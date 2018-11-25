import matplotlib.pyplot as plt
import numpy as np

# Задание 10. Реализуйте код, приведенный в примерах.

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

a = np.arange(4)**2

plt.plot([1, 2, 3, 4], a)
plt.xlabel('square numbers')
plt.show()
