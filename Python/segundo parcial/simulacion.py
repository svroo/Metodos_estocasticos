# Programa que estima el numero de tiros que necesitamos para obtenerdos caras seguidas, simulando tirar una moneda
# Created by: Rodrigo

# ---------- Librerias --------------------
import numpy as np
import matplotlib.pyplot as plt

# from numpy import random


def my(n):
    y = list()
    for k in range(n):
        nh = 0
        c = 0
        while True:
            c += 1
            r = int(np.random.random() + 0.5)
            if r == 1 and nh == 1:
                break
            if r == 1 and nh == 0:
                nh = 1
            if r == 0:
                nh = 0
        y.append(c)
    # return sum(y) / n, y
    return y


if __name__ == "__main__":
    j = 10000
    valores = [my(n) for n in range(10, j, 10)]

    # calculamos la media acumulada
    mean_values = np.cumsum(np.array(valores)) / np.arange(1, 1j + 1)

    # Graficamos
    fig, ax = plt.subplots(ncols=1)
    ax.plot(mean_values)
    ax.axhline(y=6, color="r", linestyle="0")
    plt.title("Media acumulada de lanzamientos para obtener dos caras consecutivas")
    plt.xlabel("Numero de simulación")
    plt.ylabel("Media de lanzamientos")
    plt.show()


# print("promedio", my(1000))
