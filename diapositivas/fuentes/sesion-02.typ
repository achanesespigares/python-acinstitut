// Sesión 2 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 2, tema: "Sesión 2 · Diseñar el algoritmo")

#portada([Diseñar el algoritmo], subtitulo: [Escribir los pasos de una solución en lenguaje natural, numerados, y probarlos a mano.], kicker: "Sesión 2 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 1: cada alumno lee su caso límite.], [0:15], [Situación: buscar la carta más alta de un mazo boca abajo, mirando de una en una.], [0:25], [Predice: el algoritmo de arriba, a mano.], [0:40], [Construcción: secuencia, decisión y repetición, con el capítulo.], [1:20], [Ejercicios del capítulo.], [1:45], [Cierre y tarea 2.],))

== Para empezar

#situacion[Buscar la carta más alta de un mazo boca abajo, mirando de una en una.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#cita[\1. Apunta el primer número en un papel. \
\2. Para cada número siguiente: si es mayor que el del papel, tacha el del papel y apunta este. \
\3. Di el número del papel.]

#pause

#respuesta([9], [El papel siempre guarda el mayor visto hasta ahora.])

== El mayor de tres números

#fuente[Diseñar el algoritmo · 1]

#codigo("a = 4\nb = 9\nc = 7\nmayor = a\nif b > mayor:\n    mayor = b\nif c > mayor:\n    mayor = c\nprint(mayor)")

== El algoritmo de Euclides

#fuente[Diseñar el algoritmo · 2]

#codigo("a = 48\nb = 18\nwhile b != 0:\n    r = a % b\n    a = b\n    b = r\nprint(a)")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-02.ipynb", ([Pseudocódigo. Escribe el algoritmo para decidir si un alumno aprueba:…], [Euclides a mano], [Tres piezas. En el algoritmo «cuenta cuántos números pares hay entre…],))

== Tarea 2 · El menor de una lista

#tarea-casa(([Escribe en lenguaje natural, con pasos numerados, un algoritmo que encuentre #strong[el menor] de una lista de números.], [Pruébalo a mano con la lista 7, 3, 9, 3, 5.], [¿Qué hace tu algoritmo si la lista tiene un solo número?],), [Con 7, 3, 9, 3, 5 debe salir 3.])

== Antes de irte
#cierre(qr: "https://achanesespigares.github.io/python-acinstitut/capitulos/algoritmo/#preguntas-tipo-examen", siguiente: [Sesión 3 · Seguir un programa con una traza])
