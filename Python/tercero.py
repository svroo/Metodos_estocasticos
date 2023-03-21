# Programa que genera y emula los lanzamientos de una aguja
# a un panel de lineas paralelas


#### librerias a utilizar ####
import numpy as np
from numpy import pi, sin, random


#### codigo #####
def rand_array(n)-> np.array:

    lista =[0] * n

    for i in range(n):
        lista[i] = random.random()
    
    return np.array(lista)

def bufon (throws):

    x = rand_array(throws)
    theta = rand_array(throws)
    
    # los convertimos a angulos
    theta = 0.5 * pi *theta

    # creamos los ensayos del lanzamiento
    hits = x <= 0.5*sin(theta)

    return throws / sum(hits)

if __name__ == '__main__':
    print(bufon(1000000))