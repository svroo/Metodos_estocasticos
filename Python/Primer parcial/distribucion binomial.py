import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.5

x = range(n+1)
y = binom.pmf(x, n, p)

plt.plot(x, y, 'bo', ms=10)
plt.vlines(x, 0, y, colors='b', lw=5, alpha=0.5)

plt.xlabel('Número de éxitos')
plt.ylabel('Probabilidad')
plt.title('Distribución binomial con n=10, p=0.5')

plt.show()