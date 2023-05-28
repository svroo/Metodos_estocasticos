# Programa que genera distribuciones de probabilidad
# Create by: Rodrigo Salazar Vega

# Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt

######## CODIGO ########
# def generate_dist():
#     return np.random.exponential(1.0, 10000)

if __name__ == '__main__':
    # Distribucion exponencial
    exponential = np.random.exponential(5.0, 10000)
    plt.figure()
    count, bins, ignored = plt.hist(exponential, density=True)
    plt.title('Distribución exponencial')
    plt.show()

    # Distribucion normal
    mu, sigma = 0, 0.01
    s = np.random.normal(mu, sigma, 1000)
    plt.figure()
    plt.hist(s, bins=100)
    plt.title('Distribución Normal')
    plt.show()

    # Distribución Uniforme
    s = np.random.uniform(0, 1, 1000)
    plt.hist(s, bins=100)
    plt.title('Distribución Uniforme')
    plt.show()

    # Distribución exponencial
    beta = 0.5
    s = np.random.exponential(beta, 1000)
    plt.figure()
    plt.hist(s, bins=100)
    plt.title('Distribución exponencial')
    plt.show()

    # Distribución Gamma
    k, theta = 2, 0.5
    s = np.random.gamma(k, theta, 1000)
    plt.figure()
    plt.hist(s, bins=100)
    plt.title('Distribución gamma')
    plt.show()

    # Distribución Poisson
    lam = 5
    s = np.random.poisson(lam, 1000)
    plt.figure()
    plt.hist(s, bins=30)
    plt.title('Distribución de Poisson')
    plt.show()

