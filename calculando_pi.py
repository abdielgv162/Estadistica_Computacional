import random 
import math
from funciones_estadisticas import desviacion_estandar, media
#De nuestro programa anterior importamos estas funciones que son de utilidad.


def lanzar_puntitos(total_de_puntitos):
    adentro_circulo = 0 #Inicialmente no hay ninguno

    for _ in range(total_de_puntitos):
        x = random.random() * random.choice([-1,1])
        y= random.random() *  random.choice([-1,1])
        #Originalmente arroja un valor entre 0 y 1
        #Por ello lo multiplicamos por -1 o 1 aleatoriamente para tener 
        #el rango de puntos dentro del cuadrado.
        pitagorazo = math.sqrt(x**2 + y**2)

        if pitagorazo <= 1: 
                adentro_circulo += 1

    return (4 * adentro_circulo) / (total_de_puntitos)
        #Recordemos que el 4 representa el area de nuestro cuadrado de 2x2


def estimacion(total_de_puntitos, intentos):
    estimados = []

    for _ in range (intentos):
        estimacion_pi = lanzar_puntitos(total_de_puntitos)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Estimado = {round(media_estimados , 5)}, desviación estándar = {round(sigma , 5)} de un total de {total_de_puntitos} lanzamientos.')
    return (media_estimados, sigma)

def estimar_pi(precision, numero_de_intentos):
    numero_de_puntitos = 10000
    sigma = precision

    while sigma >= precision / 1.96:
    #95% de confiabilidad
        media, sigma = estimacion(numero_de_puntitos, numero_de_intentos)
        numero_de_puntitos *= 2
    
    return media 


if __name__ == '__main__':
    estimar_pi(0.01, 100)
