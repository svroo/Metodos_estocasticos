import numpy as np
import matplotlib.pyplot as plt

# Parámetros
num_steps = 1000  # Número de pasos en la caminata aleatoria
step_size = 0.5  # Longitud de cada paso

# Inicialización de la caminata aleatoria
x = np.zeros(num_steps)

# Iteración a través de los pasos y el cálculo de la nueva posición
for i in range(1, num_steps):
    x[i] = x[i-1] + np.random.normal(scale=step_size)

# Graficación de la caminata aleatoria
plt.plot(x)
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Caminata aleatoria')
plt.show()