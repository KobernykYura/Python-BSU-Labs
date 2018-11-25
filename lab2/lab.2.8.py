from skimage import data 

from skimage import morphology
from skimage import measure
import numpy as np
from skimage import data
from skimage import filters
from matplotlib import pyplot as plt

# Метод Оцу (threshold_otsu()) – один из самых распространенных
# методов для пороговой сегментации изображений
coins = data.coins()
val = filters.threshold_otsu(coins)
mask = coins < val

plt.figure(1)
plt.subplot(221), plt.axis('off')
plt.imshow(coins, cmap='gray')  # До сегментации
plt.subplot(222), plt.axis('off')
plt.imshow(mask, cmap='gray')  # После сегментации


# Адаптивная пороговая сегментация
block_size = 35
fig = filters.threshold_adaptive(coins, block_size, offset=10)

plt.subplot(223), plt.axis('off')
plt.imshow(coins, cmap='gray')  # До сегментации
plt.subplot(224), plt.axis('off')
plt.imshow(fig, cmap='gray')  # После сегментации

plt.show()
