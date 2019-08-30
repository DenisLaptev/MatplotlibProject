import matplotlib.pyplot as plt
import numpy as np
import csv

x_coords = []
y_coords = []

with open('../resources/csv_example.txt') as csvfile:
    points = csv.reader(csvfile, delimiter=',')
    for row in points:
        x_coords.append(int(row[0]))
        y_coords.append(int(row[1]))

plt.xlabel('x')
plt.ylabel('y')

plt.title('My title: data from file')

plt.plot(x_coords, y_coords, label='Loaded from file!')

plt.legend()
plt.show()
