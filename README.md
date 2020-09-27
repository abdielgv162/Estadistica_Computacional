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

## Tabla de contenido:
- [Tabla de contenido:](#tabla-de-contenido)
- [Objetivos](#objetivos)
- [Introduccion a la Programación Dinámica](#introduccion-a-la-programación-dinámica)

---

## Objetivos

* Aprender cuándo utilizar Programación Dinámica y sus beneficios.
* Entender la diferencia entre programas deterministas y estocásticos.
* Aprender a utilizar Programacion Estocástica.
* Aprender a crear simulaciones computacionales válidas.
* Aprender a simplificar la notacion big O(n) de ciertos algoritmos de optimización.

---

## Introduccion a la Programación Dinámica

<i>La programación dinámica es es un método para reducir el tiempo de ejecución de un algoritmo mediante la utilización de subproblemas superpuestos y subestructuras óptimas.</i>

El matemático Richard Bellman inventó la programación dinámica en 1953 que se utiliza para optimizar problemas complejos que pueden ser discretizados y secuencializados.
<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Richard_Ernest_Bellman.jpg/220px-Richard_Ernest_Bellman.jpg" width="300" height="300" >
    <h5>Richard Bellman</h5>
</div>

Funfact :
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
