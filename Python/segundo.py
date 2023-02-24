# Programa que genera una distribución uniforme 
# Create by: Rodrigo Salazar Vega

# Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt

######## CODIGO ########
# def generate_dist():
#     return np.random.exponential(1.0, 10000)

if __name__ == '__main__':
    exponential = np.random.exponential(5.0, 10000)

    count, bins, ignored = plt.hist(exponential, density=True)
    plt.show()

    # Generar 1000 números aleatorios con distribución exponencial de parámetro lambda = 0.5
    samples = np.random.exponential(scale=1/0.5, size=1000)

    # Calcular el valor de la PDF en x = 1 para la distribución exponencial de parámetro lambda = 0.5
    pdf_value = 0.5 * np.exp(-0.5 * 1)

    # Calcular el valor de la CDF en x = 2 para la distribución exponencial de parámetro lambda = 0.5
    cdf_value = 1 - np.exp(-0.5 * 2)
