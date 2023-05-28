import numpy as np
import matplotlib.pyplot as plt

# Función de densidad triangular
def f(x):
    if 0 <= x <= 1:
        return 2*x
    elif 1 < x <= 2:
        return 2*(2-x)
    else:
        return 0

# Función de distribución acumulada triangular
def F(x):
    if 0 <= x <= 1:
        return x**2
    elif 1 < x <= 2:
        return 2*x - 0.5*x**2 - 1
    else:
        return 0

# Tamaño de la muestra
n = 10000

# Generar muestra de x
u = np.random.uniform(size=n)
x = np.zeros_like(u)
for i in range(n):
    x[i] = np.interp(u[i], [F(0), F(2)], [0, 2])

# Definir los límites del histograma
x_bins = np.linspace(0, 2, 100)

# Calcular f_max
f_max = max([f(x) for x in x_bins])

# Crear histograma triangular
y_vals = np.where(x_bins <= 1, f_max * x_bins, f_max * (2 - x_bins))
y_interp = np.interp(x, x_bins, y_vals)
plt.hist(x, bins=x_bins, weights=y_interp, density=True, edgecolor='black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()