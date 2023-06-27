# Librerias
import random


# Inicio codigo
def promedio_lanzamientos(num_lanzamientos=10000) -> float:
    lanzamientos = 0
    num_experimentos = num_lanzamientos
    caras_seguidas = 0

    for _ in range(num_experimentos):
        while caras_seguidas < 3:
            lanzamiento = random.choice(["C", "S"])
            lanzamientos += 1
            if lanzamiento == "C":
                caras_seguidas += 1
            else:
                caras_seguidas = 0

        caras_seguidas = 0

    return lanzamientos / num_experimentos


print("El promedio de lanzamientos necesarios es:", promedio_lanzamientos())
