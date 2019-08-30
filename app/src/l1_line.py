import matplotlib.pyplot as plt
import numpy as np

x_coords = [1, 2, 3]
y_coords = [5, 6, 7]

plt.xlabel('time,ps')
plt.ylabel('Epot,eV')

plt.title('Pd13 cluster')

plt.plot(x_coords, y_coords)

plt.show()
