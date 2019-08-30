import matplotlib.pyplot as plt
import numpy as np

# scatter plot - это точки на координатной плоскости/пространстве

x_coords = [1, 2, 3, 4, 5, 6, 7, 8]
y_coords = [5, 2, 4, 2, 1, 4, 5, 2]

plt.xlabel('x')
plt.ylabel('y')

plt.title('My title: scatter plot')

plt.scatter(x_coords, y_coords, label='my_label', color='k', marker='*', s=100)

plt.legend()
plt.show()
