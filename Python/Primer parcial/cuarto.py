# emular lanzamiento de dardos en un area de 4
# con un circulo de area pi

import numpy as np
from numpy import random

def pi_aprox(n):
	con = 0.0
	
	for i in range(n):
		x = 2 * random.random() - 1
		y = 2 * random.random() - 1
		if (x*x) + (y*y) < 1:
			con += 1.0
	return 4 * con / n

if __name__ == '__main__':
	print(pi_aprox(10000))
