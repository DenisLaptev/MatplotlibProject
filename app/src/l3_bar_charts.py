import matplotlib.pyplot as plt
import numpy as np

x1_coords = [2, 4, 6, 8, 10]
y1_coords = [6, 7, 8, 2, 4]

x2_coords = [1, 3, 5, 7, 9]
y2_coords = [7, 8, 2, 4, 2]

plt.xlabel('x')
plt.ylabel('y')

plt.title('My title')

plt.bar(x1_coords, y1_coords, label='bars1', color='r')
plt.bar(x2_coords, y2_coords, label='bars2', color='c')

plt.legend()

plt.show()
