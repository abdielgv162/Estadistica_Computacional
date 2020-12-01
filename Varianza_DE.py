import random
import math

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)

    contador = 0

    for x in range X:
        contador += (x - mu)**2
        return contador / len(X)

def dexviacion_estandar(X):
    return math.sqrt(varianza(X))

if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)

    print(X)
    print(mu)