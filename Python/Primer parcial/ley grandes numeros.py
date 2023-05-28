import math

def is_prime(n):
    """Función que devuelve True si n es primo, False en caso contrario"""
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True

def primes_up_to(n):
    """Función que devuelve una lista con los números primos menores o iguales a n"""
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def weak_and_strong_law_of_large_numbers(n):
    """Función que ilustra la ley débil y fuerte de los números"""
    primes = primes_up_to(n)
    print("Número de primos menores o iguales a", n, ":", len(primes))
    print("Densidad de los números primos menores o iguales a", n, ":", len(primes)/n)
    print("Densidad de los números primos en el conjunto de todos los números naturales:", 1/math.log(n))
    print()

# Ejemplo de uso de la función para n = 100, 1000 y 10000
weak_and_strong_law_of_large_numbers(100)
weak_and_strong_law_of_large_numbers(1000)
weak_and_strong_law_of_large_numbers(10000)