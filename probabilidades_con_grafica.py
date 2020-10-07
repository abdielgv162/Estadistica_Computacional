import random
from bokeh.plotting import figure, show


def tirar_dado(numero_de_intentos):
    secuencia_de_tiros = []
    for _ in range(numero_de_tiros):
        tiro = random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros

def graficar(x,y):
    grafica = figure(title = 'Lanzamiento de dados', x_axis_label = 'Numero de veces que se corrio la simulacion', y_axis_label = 'Probabilidad de obtener X numero')
    grafica.line(x, y)
    show(grafica)

def calcular_probabilidad(tiros, numero_intentos_simulacion):
    tiros_con_1 = 0

    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1
    return tiros_con_1 / numero_intentos_simulacion

def main(numero_de_tiros, numero_de_intentos):
    prob = []
    x_arreglo = []
    for n in range(1,numero_de_intentos):
        tiros = []
        for _ in range(n):
            secuencia_de_tiros = tirar_dado(numero_de_tiros)    
            tiros.append(secuencia_de_tiros)

        probabilidad_de_tiros_con_1 = calcular_probabilidad(tiros, n)
        prob.append(probabilidad_de_tiros_con_1)
        x_arreglo.append(n)

    graficar(x_arreglo, prob)
    print(f'Probabilidad de obtener POR LO MENOS un 1 en {numero_de_tiros} tiros = {probabilidad_de_tiros_con_1}')

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas veces se va a tirar el dado?: '))
    numero_de_intentos = int(input('Cuantas veces se va a correr la simulación?: '))
    main(numero_de_tiros, numero_de_intentos)