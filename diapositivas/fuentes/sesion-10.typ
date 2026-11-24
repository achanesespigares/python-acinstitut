// Sesión 10 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 10, tema: "Sesión 10 · Tablas, tuplas y conjuntos")

#portada([Tablas, tuplas y conjuntos], subtitulo: [Representar una tabla con una lista de listas y elegir entre lista, tupla y conjunto según lo que haga falta.], kicker: "Sesión 10 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 9.], [0:15], [Situación: el plano de una sala de cine; una entrada dice fila y asiento.], [0:25], [#strong[Predice]. Se compara #raw("[[0] * 3 for _ in range(2)]") con #raw("[[0] * 3] * 2"): el visualizador enseña por qué la…], [0:45], [Construcción: tablas, tuplas y desempaquetado, conjuntos y sus operaciones.], [1:20], [Ejercicios de los dos capítulos.], [1:45], [Preguntas tipo examen y tarea 10.],))

== Para empezar

#situacion[El plano de una sala de cine; una entrada dice fila y asiento.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("t = (1, 2) + (3,)\ns = {3, 1, 3, 2}\nprint(t, len(s), 2 in s)\nm = [[0] * 3 for _ in range(2)]\nm[1][2] = 5\nprint(m)")

#pause

#respuesta([#raw("(1, 2, 3) 3 True") · #raw("[[0, 0, 0], [0, 0, 5]]")], [#raw("(3,)") es una tupla de un elemento; el conjunto no repite.])

== Tablas: listas de listas

#fuente[Listas a fondo · 5]

#codigo("notas = [[7, 5, 9], [6, 8, 4]]\nmedias = []\nfor i in range(len(notas)):\n    suma = 0\n    for j in range(len(notas[i])):\n        suma = suma + notas[i][j]\n    medias.append(suma / len(notas[i]))\nprint(medias)")

== Tuplas: crearlas y leerlas

#fuente[Tuplas y conjuntos · 1]

#codigo("vacia = ()\nuno = (5,)               # la coma es la que hace la tupla\nno_es_tupla = (5)        # esto es solo el número 5 entre paréntesis\nfecha = (18, 11, 2026)\npunto = 3, 7             # los paréntesis se pueden omitir\nprint(type(uno).__name__, type(no_es_tupla).__name__, len(fecha))\nprint(fecha[0], fecha[-1], fecha[1:])\nprint(fecha.count(18), fecha.index(2026), 2026 in fecha)", talla: 15pt)

== Inmutables

#fuente[Tuplas y conjuntos · 2]

#codigo("alumno = (\"Ana\", [7, 9])\nalumno[1].append(8)       # la lista de dentro sí cambia\nprint(alumno, alumno[1][0])", talla: 17pt)

== Empaquetar y desempaquetar

#fuente[Tuplas y conjuntos · 3]

#codigo("a, b = 1, 2\na, b = b, a\nprint(a, b)\nfor nombre, nota in [(\"Ana\", 7), (\"Biel\", 9)]:\n    print(nombre, \"ha sacado un\", nota)")

== Conjuntos: sin repetidos y sin orden

#fuente[Tuplas y conjuntos · 4]

#codigo("mates = {\"Ana\", \"Biel\", \"Carla\"}\nfisica = {\"Biel\", \"Dani\"}\nprint(sorted(mates | fisica), sorted(mates & fisica), sorted(mates - fisica))\nprint(len(set([3, 1, 3, 2, 1])))\ntry:\n    mates[0]\nexcept TypeError as e:\n    print(\"Error:\", e)", talla: 13pt)

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-10.ipynb", ([Índices negativos], [¿Qué imprime?], [Quitar todos. Escribe un programa que quite todos los 0 de datos =…], [El total de la tabla], [La diagonal. Para la tabla m = \[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\],…], [¿Qué tipo es? a) (3); b) (3,); c) 3, 4; d) {}; e) set().],))

== Tarea 10 · Asientos de cine

#tarea-casa(([Crea una sala de 5 filas y 8 asientos con una lista de listas: #raw("0") es libre y #raw("1") ocupado.], [Ocupa la primera fila entera y los dos primeros asientos de la segunda.], [Escribe una función #raw("primera_libre(sala)") que devuelva la tupla #raw("(fila, asiento)") del primer asiento libre, recorriendo…], [Escribe una función #raw("libres(sala)") que cuente los asientos libres.], [Reserva el asiento que te dé #raw("primera_libre"), desempaquetando la tupla, y dibuja la sala con #raw("X") y #raw("·").],), [Antes de reservar, el primer libre es #raw("(1, 2)") y hay 30 libres.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/tuplas-y-conjuntos/#preguntas-tipo-examen", siguiente: [Sesión 11 · Cadenas y formato])
