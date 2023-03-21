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
