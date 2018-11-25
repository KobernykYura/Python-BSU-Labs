# Задание 1. Загрузите библиотеку skimage, отобразите список модулей,
# составляющих ее. Загрузите изображение camera из модуля data, узнайте его размеры.
# Загрузите изображение I согласно Вашему варианту. Найдите минимальное и максимальное значение по каждому каналу в изображении I.
# Установите на изображении I в ноль интенсивности тех пикселей, значение яркости в которых по синему каналу меньше медианы.

import numpy as np
import skimage
from skimage import color
from skimage import io

# Отображение списка модулей библиотеки
# help(skimage)

from skimage import data
from skimage import measure

# Загрузка камеры и расчет длинны
camdata = data.camera()
print('Shape camera() ndarray: ', camdata.shape, '\n')
print('Shape dtype ndarray: ', camdata.dtype, '\n')
print('Shape max() ndarray: ', camdata.max(), '\n')

# Загрузка изображения
vcamdata = data.imread('D:/Visual Studio Projects/Python/local_logo.png')
print(vcamdata, '\n')

print('BGR \n')
print('Minimum value onchanel 0: ', vcamdata[..., 0].min(), '\n')
print('Minimum value onchanel 1: ', vcamdata[..., 1].min(), '\n')
print('Minimum value onchanel 2: ', vcamdata[..., 2].min(), '\n')

print('Maximum value onchanel 0: ', vcamdata[..., 0].max(), '\n')
print('Maximum value onchanel 1: ', vcamdata[..., 1].max(), '\n')
print('Maximum value onchanel 2: ', vcamdata[..., 2].max(), '\n')

# Меньшие, чем медиана на оси 0
print('vcamdata = \n', vcamdata, '\n')

cmean = vcamdata[..., 0].mean()
print('cmean = \n', cmean, '\n')

vcarray = vcamdata < cmean
vcamdata[vcarray] = 0

io.imshow(vcamdata)
io.show()

vcamdata = data.camera()
# Меньшие, чем медиана по всей таблице
print('vcamdata = \n', vcamdata, '\n')

cmean = vcamdata.mean()
vcarray = vcamdata < cmean
vcamdata[vcarray] = 0

print('vcamdata = \n', vcamdata, '\n')
io.imshow(vcamdata)
io.show()

# Задание 1 (END).

import scipy
from skimage import img_as_ubyte

face = img_as_ubyte(scipy.misc.face())
print(face.shape)
io.imshow(face)
io.show()
io.imsave('aminal_face.png', face)


face = io.imread('D:/Visual Studio Projects/Python/aminal_face.png')
cmean = face.mean()
vcarray = face < cmean
face[vcarray] = 0

io.imshow(face)
io.show()
