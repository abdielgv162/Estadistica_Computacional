from individuo import Aleatorio_Tradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, tipo_de_tendencia, pasos):
    inicio = campo.obtener_coordenada(tipo_de_tendencia)
    for _ in range(pasos):
        campo.mover_persona(tipo_de_tendencia)
    return inicio.distancia(campo.obtener_coordenada(tipo_de_tendencia))

def simular_caminata(pasos, numero_de_intentos, tipo_de_tendencia):
    origen = Coordenada(0,0)
    distancias = []
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_persona(tipo_de_tendencia, origen)
        simulacion_caminata = caminata(campo, tipo_de_tendencia, pasos)
        distancias.append(round(simulacion_caminata, 1))
    return distancias

def graficar(x,y):
    grafica = figure(title = 'Caminata aleatoria', x_axis_label = 'pasos', y_axis_label = 'distancias')
    grafica.line(x, y, legend_label = 'Distancia media')
    show(grafica)

def ejecutar_caminata (campo, tipo_de_tendencia, distancias_de_caminata):
    arreglo_x = []
    arreglo_y = []
    arreglo_x.append(campo.obtener_coordenada(tipo_de_tendencia).x)
    arreglo_y.append(campo.obtener_coordenada(tipo_de_tendencia).y)
    for _ in range(distancias_de_caminata):
        campo.mover_persona(tipo_de_tendencia) #se actualiza las coordenadas del borracho
        arreglo_x.append(campo.obtener_coordenada(tipo_de_tendencia).x)
        arreglo_y.append(campo.obtener_coordenada(tipo_de_tendencia).y)
    graficar(arreglo_x, arreglo_y)

def main(distancia, inicio, tipo_de_tendencia,numero_de_intentos,distancias_de_caminata):
    campo = Campo()
    campo.anadir_persona(tipo_de_tendencia, inicio)
    ejecutar_caminata(campo, tipo_de_tendencia, distancia)
    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_tendencia)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Distancia maxima = {distancia_maxima}')
        print(f'Distancia minima = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)

if __name__ == '__main__':
    distancias_de_caminata = [10,100,1000,10000]
    numero_de_intentos = 100
    distancia = 100000
    inicio = Coordenada(0,0)
    tipo_de_tendencia = Aleatorio_Tradicional('Abdiel')
    main(distancia, inicio, tipo_de_tendencia, numero_de_intentos, distancias_de_caminata)