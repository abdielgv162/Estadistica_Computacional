import random 
from bokeh.plotting import figure, show

def lanzamiento_dados(numero_de_dados, numero_de_lanzamientos):
    lista_de_sumas = []
    for _ in range(numero_de_lanzamientos):
        tiros = []
        for _ in range(numero_de_dados):
            valor= random.choice([1,2,3,4,5,6])
            tiros.append(valor)
        suma = sum(tiros,0)
        lista_de_sumas.append(suma)
    return lista_de_sumas

def graficar(x,y):
    grafica = figure(title = 'Lanzamiento de dados', x_axis_label = 'Numero de veces que se corrio la simulacion', y_axis_label = 'Probabilidad de obtener X numero')
    grafica.line(x, y)
    show(grafica)

def calcular_probabilidad(lista, n_simulaciones):
    sumar_n = 0
    for i in lista:
        if n in i:
            sumar_n += 1
    return sumar_n / n_simulaciones

def main(numero_de_dados, numero_de_lanzamientos, n_simulaciones):
    prob = []
    x_arreglo = []
    for i in range(n_simulaciones):
        lista = []
        for _ in range(i):
            lanzamientos = lanzamiento_dados(numero_de_dados,numero_de_lanzamientos)
            lista.append(lanzamientos)

        probabilidad_de_sumar_n = calcular_probabilidad(lista, n_simulaciones)
        prob.append(probabilidad_de_sumar_n)
        x_arreglo.append(i)

    graficar(x_arreglo, prob)
    print(f"Probabilidad de sumar n: {probabilidad_de_sumar_n}")

if __name__ == '__main__':
    print("Este programa calcula la probabilidad de que la suma de los dados dé n  UwU")
    numero_de_dados = int(input('Ingrese la cantidad de dados a lanzar: '))
    numero_de_lanzamientos = int(input('Cuantos lanzamientos se van a realizar?: '))
    n_simulaciones = int(input('Cuantas veces se va a correr la simulacion?: '))
    n = int(input("Elige n: "))
    
    main(numero_de_dados, numero_de_lanzamientos, n_simulaciones)