from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

from skimage import morphology
from skimage import segmentation
from skimage.feature import peak_local_max

# Шаг 1 - Построение изображения из двух пересекающихся областей
x, y = np.indices((80, 80))  # Возвращает массив, представляющий индексы сетки.
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20

mask_cicle1 = (x - x1) ** 2 + (y - y1) ** 2 < r1 ** 2
mask_cicle2 = (x - x2) ** 2 + (y - y2) ** 2 < r2 ** 2
image = np.logical_or(mask_cicle1, mask_cicle2)

# Шаг 2 - Теперь их необходимо разделить
# Посторим маркеры как локальные максимумы расстояния

# Точное эвклидовое дистанционное преобразование.
distance = ndimage.distance_transform_edt(image)
# Найти пики в изображении в виде списка координат или булевой маски.
local_maxi = peak_local_max(distance, indices=False,
                            footprint=np.ones((3, 3)), labels=image)
# Связать метки между областями целочисленного массива.
markers = morphology.label(local_maxi)

# ------- Алгоритм случайного блуждания --------
markers[~image] = -1
labels_rw = segmentation.random_walker(image, markers)


plt.figure(1)
plt.subplot(231), plt.axis('off')
plt.imshow(image, cmap='gray')  # Маска кругов
plt.subplot(232), plt.axis('off')
plt.imshow(local_maxi, cmap='gray')  # Локальные максимумы 
plt.subplot(233), plt.axis('off')
plt.imshow(distance)   # Размытые круги
plt.subplot(234), plt.axis('off')
plt.imshow(markers)   # Цветные максимумы (маркеры)
plt.subplot(235), plt.axis('off')
plt.imshow(labels_rw)   # 3-я картинка
plt.show()
