import matplotlib.pyplot as plt
import numpy as np

# гистограмма позволяет рисовать распределение, например число людей определённого возраста.
# barchart: x,y = person_id, person_age
# histogram: x,y = person_age_interval, number_of_persons


y_coords = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44,
            43, 42, 48]
x_coords = [x for x in range(len(y_coords))]

# на рисунке будут только столбцы с этими х-координатами
x_coords_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.xlabel('x')
plt.ylabel('y')

plt.title('My title: bar plot')
plt.bar(x_coords, y_coords)
plt.show()

plt.title('My title: histogram plot')
plt.hist(y_coords, x_coords_bins, histtype='bar', rwidth=0.8)
plt.show()
