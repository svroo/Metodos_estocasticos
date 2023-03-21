# Generación de números aleatorios uniformemente distribuidos (mediante una secuancia congruencial periodica)

# x_{0}=semilla
# x_{n+1}=ax_{u}+b~mod~w

import numpy as np
from matplotlib import pyplot as plt


def seed(ini):
	global ran
	ran = ini

def randcon(n):
	global ran
	a = 16887 # 7^5
	m = 2147483647 #2^3 -1
	num = []
	for k in range(n):
		ran = a * ran % m
		num = num + [ran]
	return np.array(num)

if __name__ =='__main__':
	plt.hist(randcon(50000),binds='auto')
	plt.show()