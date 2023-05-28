import numpy as np
import matplotlib.pyplot as plt

# Creamos las vatiables
u = np.random.rand(1000)
# print(u > 0)
x = -np.log(u)
x_menos = -np.log(1 - u)

# Graficamos
fig, (ax, ax1, ax2) = plt.subplots(ncols=3)
ax.hist(x, "auto")
ax.set_title("Grafica de x")

ax1.hist(u, "auto")
ax1.set_title("Grafica u")

ax2.hist(x_menos, "auto")
ax2.set_title("Grafica de log(1-u)")

plt.show()
