import random
import collections


def crear_baraja():
    NEGRAS = ['Picas','Treboles']
    ROJAS = ['Corazones','Diamantes']
    NUMEROS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    baraja = []

    for i in NEGRAS:
        for j in NUMEROS:
            baraja.append((i,j))
    for i in ROJAS:
        for j in NUMEROS:
            baraja.append((i,j))
    return baraja
    #print(baraja)


def tomar_una_mano(tamano_de_mano):
    baraja = crear_baraja()
    mano = random.sample(baraja, tamano_de_mano)
    return mano

def main(tamano, intentos):
    baraja = crear_baraja()#Llamamos a la creación de las cartas

    manos = []
    for _ in range (int(intentos)):#Por cada intento tomaremos n cartas
        mano = tomar_una_mano(tamano)
        #print(f'\n {mano}')
        manos.append(mano)

    #print(f'\n {manos}\n')

    corrida = 0
    for i in manos:
        valores = []
        for j in i:
            valores.append(j[0])
        #print(valores)
        contador = dict(collections.Counter(valores))#Cuenta cuantas veces aparece un valor por cada ejecución
        #print(contador)

        
        for i in contador.values():
            if i == 5:
                corrida += 1
    
    probabilidad_corrida = corrida / intentos

    print(f'La probabilidad de una corrida es de: {probabilidad_corrida}')


if __name__ == '__main__':
    tamano = int(input('Ingrese el tamaño de la mano: '))
    intentos_simulacion = int(input('Cuantas veces se ejecutará la simulación?:'))
    main(tamano, intentos_simulacion)