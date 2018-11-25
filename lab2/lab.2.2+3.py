# Задание 2. Реализуйте код, приведенный в примерах.

from skimage import io
from skimage import color
from skimage import data_dir
import os

# Загрузка изображения из сети

filename = os.path.join(data_dir, 'camera.png')
camera = io.imread(filename)
logo = io.imread('D:/Visual Studio Projects/Python/local_logo.png')
# io.imsave('local_logo.png', logo)

import matplotlib.pyplot as plt

# Вывод скачанного изображения
plt.imshow(logo, cmap='gray', interpolation='nearest')
plt.show()


# Вывод максимальных значений
from skimage import img_as_float

camera_float = img_as_float(camera)
print(camera.max(), ' : ', camera_float.max())
# Входные данны отличаются от выходных

# До фильтра
plt.imshow(camera_float, cmap='gray', interpolation='nearest')
plt.show()

from skimage import filters
camera_sobel = filters.sobel(camera) # Фильт границ предметов изображения
print(camera_sobel.max())

# После фильтра
plt.imshow(camera_sobel, cmap='gray', interpolation='nearest')
plt.show()


import scipy
from skimage import img_as_ubyte

face = img_as_ubyte(scipy.misc.face())
print(face.shape)
io.imshow(face)
io.show()
