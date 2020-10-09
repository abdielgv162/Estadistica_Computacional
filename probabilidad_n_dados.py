import random 

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


def main(numero_de_dados, numero_de_lanzamientos, n_simulaciones, n):
    lista = []
    for _ in range(n_simulaciones):
        lanzamientos = lanzamiento_dados(numero_de_dados,numero_de_lanzamientos)
        lista.append(lanzamientos)

    suma_n = 0
    for i in lista:
        if n in i:
            suma_n += 1
    
    probabilidad_de_sumar_n = suma_n / n_simulaciones
    print(f"Probabilidad de sumar n: {probabilidad_de_sumar_n}")

if __name__ == '__main__':
    print("Este programa calcula la probabilidad de que la suma de los dados dé n  UwU")
    numero_de_dados = int(input('Ingrese la cantidad de dados a lanzar: '))
    numero_de_lanzamientos = int(input('Cuantos lanzamientos se van a realizar?: '))
    n_simulaciones = int(input('Cuantas veces se va a correr la simulacion?: '))
    n = int(input("Elige n: "))
    
    main(numero_de_dados, numero_de_lanzamientos, n_simulaciones, n)