# Caminata aleatoria como proceso estocastico

#### Librerias a utilizar
import random
import matplotlib.pyplot as plt

def random_walk(x, time):
    TS = [0] ; X=[0]
    
    for ts in range(1, time + 1):
        TS.append(ts)
        rand = random.choice(x)
        step = X[ts-1] + rand
        X.append(step)
        
    plt.figure(figsize=(8, 6))
    plt.plot(TS, X, label='Random walk')
    plt.xlabel('time')
    plt.ylabel('walk')
    plt.show()
    

if __name__ == '__main__':
    random_walk([-1,1], 50)