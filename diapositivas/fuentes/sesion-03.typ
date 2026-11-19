// Sesión 3 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 3, tema: "Sesión 3 · Seguir un programa con una traza")

#portada([Seguir un programa con una traza], subtitulo: [Ejecutar un programa a mano, línea a línea, apuntando el valor de cada variable.], kicker: "Sesión 3 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 2.], [0:15], [Situación: el marcador de un partido; quien lo apunta en la pizarra siempre sabe cuánto va.], [0:25], [Predice: el programa de arriba, con una tabla de traza en papel.], [0:45], [Construcción: la tabla de traza, con el capítulo.], [1:20], [Ejercicios del capítulo.], [1:45], [Cierre y tarea 3.],))

== Para empezar

#situacion[El marcador de un partido; quien lo apunta en la pizarra siempre sabe cuánto va.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("a = 1\nb = 0\nwhile a < 20:\n    b = b + a\n    a = a * 3\nprint(a, b)")

#pause

#respuesta([#raw("27 13")], [Tres vueltas: (b, a) pasa por (1, 3), (4, 9) y (13, 27).])

== El programa misterioso

#fuente[Trazas a mano · 1]

#codigo("a = 7\nb = 3\na = a + b\nb = a - b\na = a - b\nprint(a, b)")

== ¿Qué calcula este bucle?

#fuente[Trazas a mano · 2]

#codigo("n = 472\nsuma = 0\nwhile n > 0:\n    suma = suma + n % 10\n    n = n // 10\nprint(suma)")

== Una traza para encontrar un error

#fuente[Trazas a mano · 3]

#codigo("total = 0\ntotal = total + 4\ntotal = total + 8\nmedia = total / 3\ntotal = total + 6\nprint(media)")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-03.ipynb", ([Traza este programa y di qué imprime:], [¿Qué calcula? Haz la traza con n = 5:], [Encuentra el error],))

== Tarea 3 · Una traza completa

#tarea-casa(([Dibuja una tabla con una columna para #raw("x"), otra para #raw("y") y otra para la condición #raw("x > y").], [Rellénala fila a fila, una por vuelta del bucle.], [Escribe lo que imprime el programa.], [Comprueba en Colab. Si no coincide, busca la primera fila en la que te equivocaste.],), [El bucle da exactamente dos vueltas.])

== Antes de irte
#cierre(qr: "https://achanesespigares.github.io/python-acinstitut/capitulos/trazas/#preguntas-tipo-examen", siguiente: [Sesión 4 · Variables, #raw("input") y #raw("print")])
