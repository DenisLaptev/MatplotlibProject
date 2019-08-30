import matplotlib.pyplot as plt
import numpy as np

# pie chart - круговая диаграмма - показывает как распределены 24 часа в дне, для пяти дней.
# Для каждого дня сумма времён, отводимых на занятия(sleeping, eating, working, playing)=24.

# x-coordinates
days = [1, 2, 3, 4, 5]

# y-coordinates
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['m', 'c', 'r', 'b']

# plt.xlabel('x')
# plt.ylabel('y')

plt.title('My title: pie chart')

# обход секторов против чс, начиная с startangle
plt.pie(slices,
        labels=activities,
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

# plt.legend()
plt.show()
