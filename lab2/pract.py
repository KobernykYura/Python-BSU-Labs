from skimage import data 
from skimage import filters
from matplotlib import pyplot as plt

astronaut = data.astronaut()

camera_sobel = filters.sobel(astronaut[...,2]) # Фильт границ предметов изображения
plt.imshow(astronaut, cmap='gray')  # До сегментации

# После фильтра
plt.imshow(camera_sobel, cmap='gray', interpolation='nearest')
plt.show()
