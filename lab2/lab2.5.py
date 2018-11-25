# Сегментация изображений

from skimage import measure
import numpy as np
from skimage import data
from skimage import filters
from matplotlib import pyplot as plt

# Метод Оцу (threshold_otsu()) – один из самых распространенных
# методов для пороговой сегментации изображений
camera = data.camera()
val = filters.threshold_otsu(camera)
mask = camera < val

plt.figure(1)
plt.subplot(121), plt.axis('off')
plt.imshow(camera, cmap='gray')  # До сегментации
plt.subplot(122), plt.axis('off')
plt.imshow(mask, cmap='gray')  # После сегментации
plt.show()

# После того, как объекты были сегментированы, необходимо их отделить 
# (выделить) друг от друга. Для этих целей можно использовать маркирование.

n = 20
l = 256
im = np.zeros((l, l))
points = l * np.random.random((2, n ** 2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1

# Многомерный гауссовский фильтр.
im = filters.gaussian(im, sigma=l / (4. * n))
blobs = im > im.mean()

all_lables = measure.label(blobs)
blobs_labels = measure.label(blobs, background=0)

plt.figure(2)
plt.subplot(121), plt.axis('off')
plt.imshow(all_lables, cmap='gray')  # Серый
plt.subplot(122), plt.axis('off')
plt.imshow(blobs_labels, cmap='pink')  # Розовый
plt.show()