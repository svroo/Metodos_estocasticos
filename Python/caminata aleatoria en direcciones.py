import random

def caminata_aleatoria(probabilidades, pasos):
    """Función para realizar una caminata aleatoria con diferentes probabilidades de moverse en diferentes direcciones.
    
    Args:
    probabilidades (list): Lista de probabilidades para moverse en diferentes direcciones. Las probabilidades deben sumar 1.
    pasos (int): Número de pasos a dar en la caminata.
    
    Returns:
    int: La posición final después de dar los pasos especificados.
    """
    
    posicion = 0
    
    for _ in range(pasos):
        direccion = random.choices([-1, 1], weights=probabilidades)[0]
        posicion += direccion
    
    return posicion

import matplotlib.pyplot as plt

# Definimos las probabilidades y el número de pasos
probabilidades = [0.4, 0.6]
pasos = 100

# Generamos la caminata aleatoria
posiciones = [caminata_aleatoria(probabilidades, pasos) for _ in range(100)]

# Graficamos la caminata
plt.plot(posiciones)
plt.xlabel('Pasos')
plt.ylabel('Posición')
plt.title('Caminata Aleatoria')
plt.show()