import numpy as np
import matplotlib.pyplot as plt

def simular_juego(p, pasos, simulaciones):
    resultados = np.zeros(simulaciones)
    for i in range(simulaciones):
        puntos = 0
        for _ in range(pasos):
            puntos += np.random.choice([1, -1], p=[p, 1-p])
        resultados[i] = puntos
    unicos, conteos = np.unique(resultados, return_counts=True)
    probabilidades = conteos / simulaciones
    return unicos, probabilidades

pasos = 100
simulaciones = 10000
p = 0.5

resultados, probabilidades = simular_juego(p, pasos, simulaciones)

plt.stem(resultados, probabilidades)
plt.xlabel('Puntos')
plt.ylabel('Probabilidad')
plt.title('Probabilidades de resultados después de {} pasos'.format(pasos))
plt.show()