import numpy as np
import matplotlib.pyplot as plt
a = 1
b = 2
x = np.array([1, 2, 3, 4])
y = a * x + b
plt.title("Linear Equation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x, y)
plt.grid()
plt.show()


x = np.array([10, 15, 20, 25])
y = np.array([1, 2, 3, 4])
plt.plot(x, y, linestyle="dotted")
plt.show()