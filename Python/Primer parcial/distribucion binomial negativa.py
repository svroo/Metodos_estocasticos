import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

# Parámetros de la distribución binomial negativa
n = 10   # número de éxitos deseados
p = 0.5  # probabilidad de éxito en cada ensayo

# Generar datos de la distribución binomial negativa
rvs = nbinom.rvs(n, p, size=1000)

# Calcular los valores de probabilidad teóricos para los valores de k
k = np.arange(0, 40)
pmf = nbinom.pmf(k, n, p)

# Graficar la distribución binomial negativa
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(rvs, bins=20, density=True, alpha=0.5, label='Datos simulados')
ax.plot(k, pmf, 'ro-', label='Distribución teórica')
ax.legend(loc='best')
ax.set_xlabel('Número de ensayos hasta el {}-ésimo éxito'.format(n))
ax.set_ylabel('Probabilidad')
ax.set_title('Distribución binomial negativa o de Pascal')
plt.show()