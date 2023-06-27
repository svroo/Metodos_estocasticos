# Transformacion de datos
# Created by: Rodrigo Salazar

# ------------- Librerias a utilizar -------------
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Obtenemos los datos de una distribución uniforme
datos = np.random.uniform(low=0, high=2, size=1000000)

# Creamos una lista donde se almacenan los datos
g = np.zeros_like(datos)

# Comenzamos a recorrer los datos
for i, dato in enumerate(datos):
    if 0 <= dato <= 2:
        g[i] = np.sqrt(2 * dato)
    else:
        g[i] = 0

# Graficamos los datos transformados y los originales
fig, (ax, ax2) = plt.subplots(ncols=2, figsize=(16, 7))
sns.histplot(datos, ax=ax)
ax.set_title("Datos originales")
ax.set_xlabel("Valores de x")
ax.set_ylabel("Conteo de valores")

# Grafico de la transformación
sns.histplot(g, ax=ax2)
ax2.set_title("transformacion")
ax2.set_xlabel("Valores de x")
ax2.set_ylabel("Conteo de valores")
plt.show()
