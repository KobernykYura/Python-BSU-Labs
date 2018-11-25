import numpy as np
import skimage
import matplotlib.pyplot as plt
from skimage import io
from skimage import data

# Печать информации о библиотеке skimage
# help(skimage)
# help(skimage.io)
# help(skimage.data)

check = np.zeros((9,9))

check[::2, 1::2] = 1
check[1::2, ::2] = 1

plt.imshow(check, cmap='gray', interpolation='nearest')
plt.show()
