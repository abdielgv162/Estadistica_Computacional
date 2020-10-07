import random 

def tirar_dado(numero_de_intentos):
    secuencia_de_tiros = []
    for _ in range(numero_de_tiros):
        tiro = random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []  #En este arreglo guardaremos los datos de los tiros.
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)    
        tiros.append(secuencia_de_tiros)
    
    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1
    
    probabilidad_de_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(f'Probabilidad de obtener POR LO MENOS un 1 en {numero_de_tiros} tiros = {probabilidad_de_tiros_con_1}')

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas veces se va a tirar el dado?: '))
    numero_de_intentos = int(input('Cuantas veces se va a correr la simulación?: '))
    main(numero_de_tiros, numero_de_intentos)