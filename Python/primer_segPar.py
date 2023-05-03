# Librerias a utilizar
import numpy as np
from matplotlib import pyplot as plt


# Funcion
def simNorm(n=100000):
    u1 = np.random.rand(n)
    u2 = np.random.rand(n)
    w1 = np.sqrt(-2 * np.log(u1))
    w2 = 2 * np.pi * u2
    z1 = w1 * np.cos(w2)
    z2 = w2 * np.sin(w2)
    return (z1, z2, u1, w2)


if __name__ == "__main__":
    z1, z2, u1, u2 = simNorm()

    # Creacion de histogramas
    pl, (axs, axs1) = plt.subplots(ncols=2)
    axs.hist(u1, "auto")
    axs1.hist(z1, "auto")
    plt.show()
