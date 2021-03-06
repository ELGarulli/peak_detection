import numpy as np
import matplotlib.pyplot as plt
from utils import median_distance, get_left_right_bound
from scipy.signal import find_peaks

y = np.genfromtxt('example_data/data_r.csv', delimiter=',')
y = y[1:]
max_x, _ = find_peaks(y, prominence=1)
y_g = np.gradient(y, 1)
avg_distance = abs(int(median_distance(max_x) / 2))
x = np.arange(0, len(y_g), 1, dtype=float)
lb = []
rb = []

for p in max_x:
    l = p - avg_distance if p - avg_distance > 0 else 0
    r = p + avg_distance if p + avg_distance < len(y_g) else len(y_g)
    bounds = get_left_right_bound(y=y_g[l:r], px=p, left_crop=l)
    lb.append(bounds[0])
    rb.append(bounds[1])

plt.plot(y, color="black")
plt.vlines(max_x, ymin=-1, ymax=2, color="blue", linestyle=":",  linewidth=0.75)
plt.vlines(lb, ymin=-1, ymax=2, color="green",  linewidth=0.75)
plt.vlines(rb, ymin=-1, ymax=2, color="red",  linewidth=0.75)
plt.show()
