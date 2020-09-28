###### Bienvenid@! Puedes encontrame en: 
[![Twitter](https://user-images.githubusercontent.com/282759/84680160-40c90c80-af00-11ea-8390-bb86858c5fa5.png)](https://twitter.com/AbdielGuerrer20) [![LinkedIn](https://user-images.githubusercontent.com/282759/84680162-4161a300-af00-11ea-912c-8f32e5cc1676.png)](https://www.linkedin.com/in/abdiel-guerrero-360a39195/)

[![Twitter: AbdielGuerrero](https://img.shields.io/twitter/follow/AbdielGuerrer20?style=social)](https://twitter.com/AbdielGuerrer20)[![Linkedin:Abdiel Guerrero](https://img.shields.io/badge/-AbdielGuerrero-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/abdiel-guerrero-360a39195/)](https://www.linkedin.com/in/abdiel-guerrero-360a39195/)[![GitHub abdielgv162](https://img.shields.io/github/followers/abdielgv162?label=follow&style=social)](https://github.com/abdielgv162)[![Instagram: AbdielGuerrero](https://img.shields.io/badge/-abdielgv162-blue?style=flat-square&logo=Instagram&logoColor=white&link=https://www.instagram.com/abdielgv162/)](https://www.instagram.com/abdielgv162/)

---

<div align="Center"><h2>Estadística computacional con Python </h2></div>
<div align="center">
    <img src="https://i.pinimg.com/originals/30/d9/1e/30d91e04235f12b644fcdf15081d164b.gif" width="400" height="250" >
</div>
<div align="Center">
    <br><i>Documento basado en el curso de Estadística Computacional de Platzi.</i></br>
    <i>Impartido por David Aroesti.</i>

</div>

---

  - [Objetivos](#objetivos)
  - [Programacion dinámica](#programacion-dinámica)
    - [Introduccion a la Programación Dinámica](#introduccion-a-la-programación-dinámica)
    - [Optimizacion de Fibonacci](#Optimizacion-de-Fibonacci)
      - [Explicacion Fibonacci recursivo vs Fibonacci Dinámico](#explicación-fibonacci-recursivo-vs-fibonacci-dinámico)
        - [Porque usar diccionarios y no listas?](#por-que-usar-diccionario-y-no-listas)
  - [Caminos aleatorios](#caminos-aleatorios)
    - [Qué son los caminos aleatorios?](#qué-son-los-caminos-aleatorios)
      -[Quantum cloud sculpture](#quantum-cloud-sculpture) 

---

## Objetivos

* Aprender cuándo utilizar Programación Dinámica y sus beneficios.
* Entender la diferencia entre programas deterministas y estocásticos.
* Aprender a utilizar Programacion Estocástica.
* Aprender a crear simulaciones computacionales válidas.
* Aprender a simplificar la notacion big O(n) de ciertos algoritmos de optimización.

---

## Programacion dinámica

### Introduccion a la Programación Dinámica

<i>La programación dinámica es es un método para reducir el tiempo de ejecución de un algoritmo mediante la utilización de subproblemas superpuestos y subestructuras óptimas.</i>

El matemático Richard Bellman inventó la programación dinámica en 1953 que se utiliza para optimizar problemas complejos que pueden ser discretizados y secuencializados.
<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Richard_Ernest_Bellman.jpg/220px-Richard_Ernest_Bellman.jpg" width="300" height="300" >
    <h5>Richard Bellman</h5>
</div>

Fun fact :
El nombre de Programación Dinámica lo escogió Bellman para esconder a los patrocinadores gubernamentales que financiaban su investigacion, el hecho que en realidad estaba haciendo matemáticas. Lo usó para que ningún congresista pudiera oponerse a ese nombre tan atractivo.

La programación dinámica permite optimizar ciertos problemas que cuentan con.

- <strong>Subestructura Óptima:</strong>
    <i>Una solución global óptima se puede encontrar al combinar soluciones óptimas de subproblemas locales.</i>
    En otras palabras, los subproblemas se resuelven a su vez dividiéndolos en subproblemas más pequeños hasta que se alcance el caso fácil, donde la solución al problema es trivial. 

- <strong>Problemas empalmados:</strong>
    <i>Una solución óptima que involucra resolver el mismo problema en varias ocasiones (cómo en el caso de la recursiviadad).</i>
    Es decir, que se usa un mismo subproblema para resolver diferentes problemas mayores. Por ejemplo, en la sucesión de Fibonacci <i>(F3 = F1 + F2 y F4 = F2 + F3)</i>.

La optimizacion para que el programa se ejecute mucho más rápido se logra a través de la <strong>memorización:</strong>
- <i>La memorización es una técnica para guardar cómputos previos y evitar realizarlos nuevamente.</i>
- <i>Normalmente se utiliza un diccionario { } , donde las consultas se pueden hacer en O(1) .</i>
- <i>Intercambia: Tiempo vs Espacio en memoria.</i>
  
La <strong>memorización</strong> nos ayuda a evitar computos adicionales, guardando el resultado de computaciones previas en alguna estructura de datos que podemos consultar rápidamente.

---

### Optimizacion de Fibonacci

Recordemos los numeros de Fibonacci.

<div align="center">
    <img src="https://lh3.googleusercontent.com/proxy/UFpKF4tnWm_gO3UI34Cn5BBVV4px66heCV_AaFDD3R5Zgjq_-tff97XyTTdXDT9wg57J3O4-agOLLtzqp437uGVGfYzb6r-ofp4W-abPDCfQOLx1DROL2aV3g8yBjHmUta5iBrhYvNKVlFOqdb3iHDI" >
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/PascalTriangleFibanacci.svg/360px-PascalTriangleFibanacci.svg.png" width="350" height="250" >
</div>

La forma recursiva de Fibonacci <i>f(n) = f<sub>n-1</sub> + f<sub>n-2 </sub></i> es muy fácil de implementar en código, pero es poco eficiente ya que repetimos el mismo computo muchas veces, aumentando innecesariamente la cantidad de iteraciones.

Para optimizar esta función haremos uso de la memorización anteriormente mencionada.
Aqui tenemos una implementación de <i>Fibonacci Recursivo vs Fibonacci Dinámico: </i>
```py
import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_dinamico(n, memoria={}):
    if n == 0 or n == 1 :
        return 1
    try:
        return memoria[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1, memoria) + fibonacci_dinamico(n-2, memoria)
        memoria[n] = resultado
        return resultado

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    n = int(input("Escoge un numero: "))
    # resultado = fibonacci_recursivo(n)
    resultado = fibonacci_dinamico(n)
    print(resultado)
```
---

#### Explicación Fibonacci Recursivo vs Fibonacci Dinámico

```py
def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
```

En esta parte tenemos la función de <i>fibonacci_recursivo()</i>.

Definimos la función con un parámetro <i>n</i> de entrada, ahora en el primer <i>if</i> cómo sabemos que el caso base de Fibonacci para 0 y 1 es igual a 1 solo retornamos 1. 

De no ser así, retornaremos una llamada recursiva de Fibonacci para el numero anterior (n-1) más el numero anterior a ese (n-2).

Recordemos que la recursividad es la forma en la cual se especifica un proceso basado en su propia definición, que en este caso es una función que se llama a sí misma.

```py
def fibonacci_dinamico(n, memoria={}):
    if n == 0 or n == 1 :
        return 1
    try:
        return memoria[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1, memoria) + fibonacci_dinamico(n-2, memoria)
        memoria[n] = resultado
        return resultado
```

Aqui tenemos la version <i>dinámica</i>.

Primero definimos la función <i>fibonacci_dinamico()</i>, donde a diferencia de la primera tenemos un parametro extra llamado <i>memoria{}</i> , que es un diccionario que en este caso será nuestra estructura de datos para efectuar la <i>memorización</i>

Ahora tenemos algo nuevo llamado <i>try/except</i>, este es un buen mecanismo para el control del flujo del programa ya que nos permite manejar la excepciones que puedan surgir y tomar acciones de recuperación para evitar la interrupción del programa o, al menos, para realizar algunas acciones adicionales antes de interrumpirlo.

```py
    try:
        return memoria[n]
```
Dentro del bloque try se ubica todo el código que pueda llegar a levantar una excepción, se utiliza el término levantar para referirse a la acción de <i>generar una excepción</i>.

Si tenemos como llave [n] en el diccionario, regresemos n.

```py
    except KeyError:
        resultado = fibonacci_dinamico(n-1, memoria) + fibonacci_dinamico(n-2, memoria)
        memoria[n] = resultado
        return resultado
```
El bloque except se encarga de capturar la excepción y nos da la oportunidad de procesarla.

Si no tenemos como llave [n] en el diccionario, anticiparemos el KeyError que nos saldría al intentar acceder a una llave que no existe.

Nos anticiparemos llamando a la funcion <i>fibonacci_dinamico()</i> para <i>(n-1) y (n-2)</i>, pero en este caso tendremos como parametro extra el diccionario <i>memoria{}</i>. Después guardaremos en <i>memoria{}</i> el resultado anterior y retornaremos este para la siguiente iteración.

Esta es la parte diferenciadora entre la versión recursiva simple y la versión dinámica, ya que al tener los resultados de iteraciones anteriores dentro del diccionario nos ahorraremos el tiempo del calcular todos los resultados anteriores de <i>n</i> para solo tener que buscar ese resultado anterior dentro del diccionario y sumarlo, lo cual hace MUCHO más eficiente el algoritmo.

Tan solo calcular n=50 con <i>fibonacci_recursivo()</i> toma muchísimo más tiempo que calcular n=500 con <i>fibonacci_dinamico()</i>.

```py
import sys
    .
    .
    .
    sys.setrecursionlimit(10000)
```

Estas lineas nos ayudan a incrementar el límite de recursividad limitado por python, importando la librería <i>sys</i> para seleccionar el limite de recursión.

---

#### Por que usar diccionario y no listas?

El algoritmo que usa Python internamente para buscar un elemento en un diccionario es muy distinto que el que utiliza para buscar en listas.

<i>Para buscar en las listas, se utiliza un algoritmos de comparación que tarda cada vez más a medida que la lista se hace más larga. En cambio, para buscar en diccionarios se utiliza un algoritmo llamado hash, que se basa en realizar un cálculo numérico sobre la clave del elemento, y tiene una propiedad muy interesante: sin importar cuántos elementos tenga el diccionario, el tiempo de búsqueda es siempre aproximadamente igual (O(1)).

Este algoritmo de hash es también la razón por la cual las claves de los diccionarios deben ser inmutables, ya que la operación hecha sobre las claves debe dar siempre el mismo resultado, y si se utilizara una variable mutable esto no sería posible.</i>

---

## Caminos aleatorios

### Qué son los caminos aleatorios?

* Es un tipo de simulación que elige aleatoriamente una decisión dentro de un conjunto de decisiones válidas.

* Se utilizan en muchos campos del conocimiento cuando los sistemas <i>no son deterministas</i> e incluyen elementos de aleatoriedad.

* Nos permiten realizar simulaciones de eventos de carácter probabilístico o no determinista para entender su comportamiento desde otra perspectiva de análisis.


<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/Brownian_motion_large.gif" width="300" height="300" ><img src="https://bardofmars.files.wordpress.com/2017/08/tumblr_n8zcbhqz8f1qio57co1_1280.gif" width="300" height="300" >
    <h6>Movimiento browniano y simulación de una fusión de dos galaxias a través de millones de años, respectivamente</h6>
</div>

---

#### Quantum cloud sculpture

La nube cuantica es una escultura diseñada por Antony Gormley , situada junto a la Cúpula del Milenio en Londres. Está construido a partir de una colección de unidades tetraédricas hechas de secciones de acero de 1,5 m de largo.

<i>Las secciones de acero se organizaron utilizando un modelo de computadora con un algoritmo de caminata aleatoria a partir de puntos en la superficie de una figura ampliada basada en el cuerpo de Gormley que forma un contorno residual en el centro de la escultura.</i>

Al diseñar Quantum Cloud , Antony Gormley fue influenciado por Basil Hiley , físico cuántico (y antiguo colega de David Bohm ). La idea de la nube cuántica vino de los pensamientos de Hiley en pre-espacio como una estructura matemática que subyace en el espacio-tiempo y la materia, y su comentario de que “el álgebra es la relación de las relaciones.” El comentario se hizo durante una conversación entre Gormley, Hiley y el escritor David Peat en una reunión de artistas y científicos en Londres en 1999, organizada por Peat.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Antony_Gormley_Quantum_Cloud_2000.jpg" width="300" height="400" ><img src="https://www.lusas.com/case/civil/images/ani_qc_wind.gif" width="300" height="400" >
    <h6>Quantum cloud sculpture</h6>
</div>

---

