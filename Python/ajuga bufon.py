import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Función para calcular el valor de pi utilizando el problema de las agujas de Buffon
def buffon(n):
    # Definimos la longitud de la aguja y la separación entre rayas
    L = 1.0  # longitud de la aguja
    t = 2.0  # separación entre rayas

    # Generamos n lanzamientos aleatorios de la aguja
    n = 10000
    x = np.random.uniform(0, t/2, n)  # posición horizontal aleatoria de la aguja
    theta = np.random.uniform(0, np.pi/2, n)  # ángulo aleatorio de la aguja

    # Calculamos la probabilidad estimada de que la aguja cruce una línea
    hits = np.sum(L/2 * np.sin(theta) > x)
    p = hits / n

    # Calculamos el valor estimado de pi
    pi = 2 * L / (t * p)
    return (pi)

# Función para calcular el valor de pi utilizando el problema de los dardos
def darts(n):
    hits = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            hits += 1
    return (4 * (hits / n))

# Rango de iteraciones a probar
n_values = range(10, 10000, 100)

# Listas para almacenar los valores de pi estimados
buffon_pi = []
darts_pi = []

# Calcular los valores de pi estimados para cada número de iteraciones
for n in n_values:
    buffon_pi.append(buffon(n))
    darts_pi.append(darts(n))

# Calcular el valor real de pi
real_pi = math.pi

# Gráfica de los valores estimados de pi versus el número de iteraciones
plt.plot(n_values, buffon_pi, label='Agujas de Buffon')
plt.plot(n_values, darts_pi, label='Dardos')
plt.axhline(y=real_pi, color='red', linestyle='--', label='Valor real de pi')
plt.xlabel('Número de iteraciones')
plt.ylabel('Valor estimado de pi')
plt.legend()
plt.show()