import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as cm

n = 10
Z = np.random.uniform(0,1,20)
Z = np.ones(20)
plt.pie(Z, explode=Z*.02, colors = cm.TABLEAU_COLORS)
plt.show()