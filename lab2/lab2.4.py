# Фильтер Собеля для детектирования горизонтальных линий
import numpy as np
from skimage import morphology
from skimage import exposure
from matplotlib import pyplot as plt
from skimage import data
from skimage import filters

text = data.text()
hsobel_text = filters.sobel_h(text)

plt.figure()
plt.imshow(text, cmap='gray')
plt.show()

plt.figure()
plt.imshow(hsobel_text, cmap='gray')
plt.show()

# Нелокальные фильтры используют все изображение или
# его часть для изменения интенсивности в одном пикселе.
# В примере показано изменение контрастности в областях.

camera = data.camera()
camera_equalized = exposure.equalize_hist(camera)  # выравнивание гистограммы
plt.figure()
plt.imshow(camera, cmap='gray')
plt.show()

plt.figure()
plt.imshow(camera_equalized, cmap='gray')
plt.show()

# Модификация изображения структурным элементом.
# Эрозия – значение пикселя заменяется на минимальное значение,
# которое охватывается в его окрестности структурным элементом.

a = np.zeros((7, 7), dtype=np.uint8)
a[1:6, 2:5] = 1
print(a)
b = morphology.binary_erosion(a, morphology.diamond(1)).astype(np.uint8)
print(b)

# Дилатация – значение пикселя заменяется на максимальное значение,
# которое охватывается в его окрестности структурным элементом.

a = np.zeros((5, 5), dtype=np.uint8)
a[2, 2] = 1
print(a) # diamond() - Generates a flat, diamond-shaped structuring element
b = morphology.binary_dilation(a, morphology.diamond(1)).astype(np.uint8)
print(b)

# Операция открытия – последовательное выполнение сначала эрозии,
# а затем дилатации. Эта операция позволяет 
# удалить мелкие объекты и сгладить углы

a = np.zeros((5, 5), dtype=np.uint8)
a[2, 2] = 1
print(a) # diamond() - Generates a flat, diamond-shaped structuring element
b = morphology.binary_opening(a, morphology.diamond(1)).astype(np.uint8)
print(b)

from skimage.morphology import disk
from skimage import data
from skimage import filters
import matplotlib.pyplot as plt

coins = data.coins()
coins_zoom = coins[10:80, 300:370] # выделение остова
median_coins = filters.median(coins_zoom, disk(1))

plt.figure()
plt.imshow(coins_zoom, cmap='gray')
plt.show()

plt.figure()
plt.imshow(median_coins, cmap='gray')
plt.show()

from skimage import restoration
tv_coins = restoration.denoise_tv_chambolle(coins_zoom, weight=0.1) # Убрать шум
gaussian_coins = filters.gaussian(coins_zoom, sigma=2)

plt.figure()
plt.imshow(tv_coins, cmap='gray')
plt.show()

plt.figure()
plt.imshow(gaussian_coins, cmap='gray')
plt.show()
