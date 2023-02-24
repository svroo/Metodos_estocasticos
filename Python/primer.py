# Obtencion del valor esperado y desviación estandar
# Simulación del lanzamiento de dos dados para obtener la probabilidad
# de obtener un numero sumado a partir de ambas caras.
# Create by: Rodrigo Salazar Vega

# Librerias a utilizar
import numpy as np


def get_combinations(started = 2, ends = 12, faces = list())-> dict:
    """
    Funcion que retorna un diccionario donde la clave es un numero que inicializa
    en el 2 y se va incrementando de uno en uno hasta el 12, el valor de cada llave es la combinacion
    de caras de dos dados que sumados dan dicho numero.

    started : Numero donde inicia la busqueda de los dos numeros, por defecto 2
    ends : Numero hasta donde se detiene la busqueda, por defecto 12
    faces : lista que contiene numeros del 1 al 6 simulando las caras de un dado

    retorna un diccionario
    """

    # Declaramos el diccionario que vamos a regresar
    res = dict()

    # Inicializamos el ciclo donde se van a buscar esos dos numeros que sumados den el started
    while started not in res.keys() and started <= ends:

        # Inicializamos una lista para almacenar la pareja de numeros que sumados sean igual al started
        aux = list()

        for num_one in faces:
            for num_two in faces:
                if num_one + num_two == started:
                    aux.append((num_one, num_two))

        res[started] = aux

        started += 1

    return res

def get_all_items(items = dict()) -> int:
    """
    Funcion que retorna el total de elementos generados en la funcion get_combinations

    items : diccionario donde la clave es el numero que los valores sumados dan

    retorna un entero
    """
    # Variable auxiliar donde se almacenara el total de las combianciones de numeros que sumados dan la llave
    # del diccionario
    total = 0

    for num in items.keys():
        total += len(items[num])

    return total

def value_of_randomVariable(items = dict(), total = int()) -> dict:
    """
    Funcion que calcula el valor de la variable aleatoria, el cual es el total de elementos 
    por cada llave del diccionario entre el total de todas las combinaciones.

    items : diccionario donde los valores, sumados dan la clave
    total : entero que es total de items que estan en los valores del diccionario

    retorna un diccionario donde la llave es el numero y el valor es su valor de variable aleatoria
    """
    aux = dict()

    for num in items.keys():
        aux[num] = len(items[num]) / total

    return aux

def get_mean(items = dict())-> float:
    """
    Función que calcula la media de los valores de la variable aleatoria para cada numero
    del 2 al 12.

    items : Diccionario que contiene como llave los numeros del 2 al 12 y como valor
    el valor que adquiere la variable aleatoria en dicho caso

    retorna un numero florante
    """
    # Variable auxiliar que ira sumando todos lo valores de
    # la variable aleatoria
    suma = 0

    for num in items.keys():
        suma += (items[num] * num)

    print(suma)

    return suma

def desviacion_estandar(items = dict(), media = float()) -> float:
    """
    Funcion que calcula la diferencia de cada valor, respecto a la media 
    y luego lo multiplica por su probabilidad.
    
    items : diccionario que contiene los valores de cada numero 
    del 2 al 12 de su valor como variable aleatoria
    
    media : media de los valores que vienen en el diccionario de items
    
    retorna un diccionario.
    """

    # Variable auxiliar que almacena la resta de cada valor con la media
    sum = 0

    for num in items.keys():
        sum += ((items[num] - media) ** 2) * items[num]

    # print('valor menos media: \n',finall)

    return sum


if __name__ == '__main__':

    # Simulacion de las caras del dado
    dado = [1, 2, 3, 4, 5, 6]

    res = get_combinations(faces= dado)

    prob = get_all_items(res)

    final = value_of_randomVariable(items= res, total= prob)

    mean = get_mean(final)

    final = desviacion_estandar(final, mean)

    print(final)


    


