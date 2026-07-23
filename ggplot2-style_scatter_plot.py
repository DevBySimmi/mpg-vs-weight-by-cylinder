import matplotlib.pyplot as plt
import numpy as np

# Data
weight_4 = [1.5, 1.8, 2.0, 2.1, 2.2, 2.4, 2.5, 2.6, 2.8, 3.1]
mpg_4 = [30.5, 34, 27.3, 26, 32.5, 22.8, 21.5, 21.5, 21.5, 24.5]

weight_6 = [2.6, 2.8, 3.0, 3.2, 3.3, 3.4]
mpg_6 = [21, 19.8, 21, 24.4, 19.2, 18.7]

weight_8 = [3.2, 3.4, 3.5, 3.6, 3.7, 3.8, 4.0, 4.1, 5.2, 5.4]
mpg_8 = [16, 15.2, 15, 14.3, 15.2, 19.2, 16.5, 13.3, 10.4, 10.4]

# Scatter points
plt.scatter(weight_4, mpg_4, label="4", s=70)
plt.scatter(weight_6, mpg_6, label="6", s=70)
plt.scatter(weight_8, mpg_8, label="8", s=70)

# Regression lines
for x, y in [
    (weight_4, mpg_4),
    (weight_6, mpg_6),
    (weight_8, mpg_8)
]:
    slope, intercept = np.polyfit(x, y, 1)

    line_x = np.linspace(min(x), max(x), 100)
    line_y = slope * line_x + intercept

    plt.plot(line_x, line_y, linewidth=2)

# Labels and title
plt.title("MPG vs Weight by Cylinder")
plt.xlabel("Weight")
plt.ylabel("MPG")

plt.legend(title="Cylinders")
plt.grid(True, alpha=0.3)

# Show graph
plt.show()