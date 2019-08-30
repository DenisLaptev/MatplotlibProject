import matplotlib.pyplot as plt
import numpy as np

# stack plot - показывает как распределены 24 часа в дне, для пяти дней.
# Для каждого дня сумма времён, отводимых на занятия(sleeping, eating, working, playing)=24.

# x-coordinates
days = [1, 2, 3, 4, 5]

# y-coordinates
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.xlabel('x')
plt.ylabel('y')

plt.title('My title: stack plot')

plt.plot([], [], color='m', label='sleeping', linewidth=5)
plt.plot([], [], color='c', label='eating', linewidth=5)
plt.plot([], [], color='r', label='working', linewidth=5)
plt.plot([], [], color='k', label='playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

plt.legend()
plt.show()
