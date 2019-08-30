import matplotlib.pyplot as plt
import numpy as np

plt.xlabel('time,ps')
plt.ylabel('Epot,eV')

plt.title('Pd13 cluster')

ax1 = plt.subplot2grid((1, 1), (0, 0))

ax1.set_xticks([1.0, 1.5, 2.0, 2.5, 3.0])
ax1.set_yticks([5, 6, 7])

ax1.grid(False)

ax1.axhline(5.2, color='k', linewidth=5)

plt.show()
