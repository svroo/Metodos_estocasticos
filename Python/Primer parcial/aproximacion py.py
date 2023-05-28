# Metodo de montecarlo
# Aproximación del valor de pi por lanzamiento de agujas

# Bibliotecas
import numpy as np
import random

# Codigo
if __name__ == '__main__':
    # Definimos la longitud de la aguja y la separación entre rayas
    l = 1.0 # Longitud de la aguja
    t = 2.0 # Separacion entre rayas

    # Generamos n lanzamientos aleatorios de la aguja
    n = 10000
    x = np.random.uniform(0, t/2, n) # posicion horizontal aleatoria de la aguja
    theta = np.random.uniform(0, np.pi/2, n) # Posicion aleatorio de la aguja

    # Calculamos la probabilidad estimada de que la aguja cruce una linea
    hits = np.sum(l/2 * np.sin(theta) > x)
    p = hits / n
    
    # Calculamos el valor estimado de pi
    pi = 2 * l / (t*p)

    # Mostramos el valor
    print('El valor estimado de pi por lanzamiento de aguja es: ', pi)

    # Aproximación del valor de pi por lanzamiento de dardos
    
    # Definimos el número de dardos que se lanzarán
    n = 10000

    # Contador para el número de dardos que caen dentro del círculo
    hits = 0

    # Lanzamos n dardos al azar dentro del cuadrado [-1,1]x[-1,1]
    for i in range(n):
        # Generamos coordenadas x e y aleatorias
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Verificamos si el dardo cae dentro del círculo de radio 1
        if x**2 + y**2 <= 1:
            hits += 1

    # Calculamos el valor estimado de pi
    pi = 4 * hits / n

    # Imprimimos el valor estimado de pi
    print("El valor estimado de pi mediante lanzamiento de dados, es:", pi)

    # Va