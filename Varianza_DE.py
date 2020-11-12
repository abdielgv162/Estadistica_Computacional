import random

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X: 
        acumulador += (x - mu)**2
    return acumulador / len(X)

if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)

    print(X)
    print(mu)