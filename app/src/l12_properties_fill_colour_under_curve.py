import matplotlib.pyplot as plt
import numpy as np

x_coords = [1, 2, 3]
y_coords = [5, 6, 7]

plt.xlabel('time,ps')
plt.ylabel('Epot,eV')

plt.title('Pd13 cluster')

ax1 = plt.subplot2grid((1, 1), (0, 0))

ax1.grid(True)

ax1.plot(x_coords, y_coords)
#ax1.fill_between(x_coords, y_coords, 0, alpha=0.3)
ax1.fill_between(x_coords, y_coords, y_coords[0], alpha=0.3)

ax1.set_xticks([1.0, 1.5, 2.0, 2.5, 3.0])
ax1.set_yticks([5, 6, 7])
ax1.grid(False)

plt.show()
