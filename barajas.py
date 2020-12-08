import random
import collections

#Usamos mayúsculas para referirnos a constantes.
PALOS = ['espada','corazon', 'rombo', 'trebol'] 
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja():
    barajas = []
    for i in PALOS:
        for j in VALORES:
            barajas.append((i,j))

    return barajas

def obtener_mano(barajas, tamano_de_mano):
    mano = random.sample(barajas,tamano_de_mano)#Obtén una muestra sin regresar las cartas.
    return mano

def main(tamano_de_mano,intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(int(intentos)):
        mano = obtener_mano(barajas, tamano_de_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))#Cuenta cuantas veces aparece un valor
        print(counter)
        for val in counter.values():
            print(val)
            if val == 2:
                pares += 1
                break

    probabilidad_par = pares / intentos
    print(f'la probabilidad de obtener un par en una mano de {tamano_de_mano} barajas es {probabilidad_par}' )


if __name__ == '__main__':
    tamano_de_mano = int(input('De cuantas barajas será la mano?'))
    intentos = int(input('Cuantos intentos seran?'))

    main(tamano_de_mano, intentos)

