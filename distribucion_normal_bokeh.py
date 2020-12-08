from bokeh.plotting import figure, show
import random
import math

def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)


def desviacion_estandar(X):
    return math.sqrt(varianza(X))

def distribucion_normal(X,mu,sigma):
    valores_y = []
    for x in X:
        y = (1/(sigma*math.sqrt(2*math.pi)))*math.exp(-1/2*((x-mu)/(sigma))**2)
        valores_y.append(y)
    return valores_y

def graficar(X,valores_y,media,sigma):
    
    grafica = figure(title=f'Distribución normal', x_axis_label='x', y_axis_label='y')
    
    grafica.line(X, valores_y, legend=f'Distribución normal',line_color='blue')

    media_y = [min(valores_y),max(valores_y)]
    media_x = [media,media]

    grafica.line(media_x, media_y, legend=f'Media',line_color='red')

    desviacion_estandar_1_y = [min(valores_y),max(valores_y)]
    desviacion_estandar_1_x = [media+sigma,media+sigma]

    grafica.line(desviacion_estandar_1_x, desviacion_estandar_1_y, legend=f'Desviación estándar',line_color='green')

    desviacion_estandar_2_y = [min(valores_y),max(valores_y)]
    desviacion_estandar_2_x = [media-sigma,media-sigma]

    grafica.line(desviacion_estandar_2_x, desviacion_estandar_2_y,line_color='green')

    show(grafica)

if __name__ == '__main__':

    X = sorted([random.randint(0, 100) for i in range(100)])
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    valores_y = distribucion_normal(X,mu,sigma)
    graficar(X,valores_y,mu,sigma)

    print(f'Arreglo X: {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviacion estandar = {sigma}')