import random
import math


def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)

    contador = 0
    for x in X:
        contador += (x - mu)**2

    return contador / len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))

if __name__ == '__main__':
    X = [random.randint(1,2) for i in range(20)]
    mu = media(X)
    var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'\nValores random:\n{X}\n')
    print(f'Media: {mu}\n')
    print(f'Varianza: {round(var,3)}\n')
    print(f'Desviación estándar: {round(sigma,3)}\n')