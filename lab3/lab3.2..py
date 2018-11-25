import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure(figsize=(8,4)) # Размер окна
G = gridspec.GridSpec(3,3) # Сетка 3x3

axes_1 = plt.subplot(G[0,:]) # Площать с левого по правый край
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24,alpha=.1)

axes_2 = plt.subplot(G[1,:-1])  # Площать с 0 по 1 узел сетки
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24,alpha=.2)

axes_3 = plt.subplot(G[1:,-1]) # Площать с левого по правый край
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24,alpha=.3)

axes_4 = plt.subplot(G[-1,0]) # Площать
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24,alpha=.4)

axes_5 = plt.subplot(G[-1,-2]) # Площать
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24,alpha=.5)

plt.tight_layout()
plt.show()
