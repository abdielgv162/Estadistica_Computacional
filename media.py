import random

def media(X):
    return sum(X) / len(X)

if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    µ = media(X)
    print(X)
    print(µ)