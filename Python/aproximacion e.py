# Aproximacion de la función e por limite y factorial

import math

def e_limit(n : int):
    return math.pow(1 + 1/n, n)

def e_factoria(n : int):
    e = 0
    for i in range(n):
        e += 1 / math.factorial(i)
    return e

if __name__ == '__main__':
    print('e_limit(10)', e_limit(10))
    print('e_factorial (10): ', e_factoria(10))