import matplotlib.pyplot as plt
import numpy as np

x1_coords = [1, 2, 3]
y1_coords = [5, 6, 7]

x2_coords = [1, 2, 3]
y2_coords = [10, 6, 12]

plt.xlabel('time,ps')
plt.ylabel('Epot,eV')

plt.title('Pd13 cluster')

plt.plot(x1_coords, y1_coords, label='First graph')
plt.plot(x2_coords, y2_coords, label='Second graph')

plt.legend()

plt.show()
