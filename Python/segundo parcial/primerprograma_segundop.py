# Transformacion de datos
# Created by: Rodrigo Salazar

# ------------- Librerias a utilizar -------------
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Obtenemos los datos de una distribución uniforme
    datos = np.random.uniform(size=1000000)

    # Creamos una lista donde se almacenan los datos
    f = list()
    g = np.zeros_like(datos)

    # Comenzamos a recorrer los datos
    for i, dato in enumerate(datos):
        # print(dato)
        if 0 <= dato <= 0.5:
            # f.append(np.sqrt(2 * dato))
            g[i] = np.sqrt(2 * dato)
        elif 0.5 < dato <= 1:
            # f.append(2 - np.sqrt(2 * (1 - dato)))
            g[i] = 2 - np.sqrt(2 * (1 - dato))

    # Graficamos los datos transformados
    plt.figure(figsize=(8, 6))
    # _ = sns.histplot(f)
    _ = sns.histplot(g)
    _ = plt.title("transformacion")
    plt.show()
