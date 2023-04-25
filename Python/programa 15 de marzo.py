# Programa que va a calcular el estado del clima usando una cadena de markov
#


# Librerias
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Inicializamos la semilla
np.random.seed(3)

# almacenamos los dos estados posibles
statesData = ["Sunny", "Rainny"]

# Almacenamos los estados de transicion
transitionStates = [["SuSu", "SuRa"], ["RaRa", "RaSu"]]

# Matriz de probabilidades
transitionMatrix = [[0.80, 0.20], [0.25, 0.75]]

# lista varia
weatheForecasting = list()

# Declaramos los dias
numDays = 365

# Inicializamos una variable
todayPrediction = statesData[0]

if __name__ == "__main__":
    for i in range(1, numDays):
        if todayPrediction == "Sunny":
            Transcondition = np.random.choice(
                transitionStates[0], replace=True, p=transitionMatrix[0]
            )
            if Transcondition == "Susu":
                pass
            else:
                todayPrediction = "Rainny"

        elif todayPrediction == "Rainny":
            Transcondition = np.random.choice(
                transitionStates[1], replace=True, p=transitionMatrix[1]
            )
            if Transcondition == "RaRa":
                pass
            else:
                todayPrediction = "Sunny"

        weatheForecasting.append(todayPrediction)

    # Mostramos los resultados que se almacenaron en la lista
    print(Counter(weatheForecasting))

    # Graficamos
    fig, (ax, ax1) = plt.subplots(ncols=2)
    fig.suptitle("Graficas")

    # plot sensillo
    ax.plot(weatheForecasting)
    ax.set_title("Grafico de weatherForecastin")
    ax.set_xlabel("Conteo")
    ax.set_ylabel("Estados posibles")

    # Histograma
    ax1.hist(weatheForecasting)
    ax1.set_title("Histograma de weatherForecastin")
    ax1.set_ylabel("Conteo")
    ax1.set_xlabel("Estados posibles")

    # Ajustamos el tamaño
    fig.set_size_inches(15.0, 7.0)

    plt.show()
