import matplotlib.pyplot as plt
import numpy as np

path_to_file = '../resources/csv_example.txt'

x_coords, y_coords = np.loadtxt(path_to_file, delimiter=',', unpack=True)

plt.xlabel('x')
plt.ylabel('y')

plt.title('My title: data from file using numpy')

plt.plot(x_coords, y_coords, label='Loaded from file!')

plt.legend()
plt.show()
