import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la secuencia congruencial periódica
a = 1103515245
c = 12345
m = 2**31

# Semilla inicial
x = 0

# Generar 50000 números aleatorios
numeros_aleatorios = []
for i in range(50000):
    x = (a*x + c) % m
    numeros_aleatorios.append(x/m)

# Generar histograma
plt.hist(numeros_aleatorios, bins=20)
plt.title('Histograma de números aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()