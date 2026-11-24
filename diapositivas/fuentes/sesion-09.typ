// Sesión 9 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 9, tema: "Sesión 9 · Recorrer y modificar listas")

#portada([Recorrer y modificar listas], subtitulo: [Guardar muchos datos en una lista, recorrerla, cambiarla y no confundir una copia con un alias.], kicker: "Sesión 9 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 8.], [0:15], [Situación: una lista de la compra compartida en el móvil frente a una foto de esa lista.], [0:25], [#strong[Predice] y visualizador: el alias se ve con dos flechas hacia la misma caja.], [0:45], [Construcción: índices, rebanadas, #raw("append"), #raw("insert"), #raw("pop"), #raw("del"), #raw("sort") y #raw("sorted").], [1:20], [Ejercicios de los dos capítulos.], [1:45], [Preguntas tipo examen y tarea 9.],))

== Para empezar

#situacion[Una lista de la compra compartida en el móvil frente a una foto de esa lista.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("a = [3, 1, 2]\nb = a\nb.append(4)\nc = a[:]\nc[0] = 99\nprint(a, b, c)")

#pause

#respuesta([#raw("[3, 1, 2, 4] [3, 1, 2, 4] [99, 1, 2, 4]")], [#raw("b") es la misma lista que #raw("a"); #raw("c") es una copia.])

== Recorrer y sumar

#fuente[Recorrer listas · 1]

#codigo("notas = [7, 4, 9, 6, 8]\ntotal = 0\nfor nota in notas:\n    total = total + nota\nprint(\"Suma:\", total)")

== Recorrer por posición

#fuente[Recorrer listas · 2]

#codigo("notas = [7, 4, 9, 6, 8]\ntotal = 0\nfor i in range(len(notas)):\n    total = total + notas[i]\nprint(\"Media:\", total / len(notas))")

== El campeón provisional

#fuente[Recorrer listas · 3]

#codigo("notas = [7, 4, 9, 6, 8]\nmaximo = notas[0]\nfor i in range(1, len(notas)):\n    if notas[i] > maximo:\n        maximo = notas[i]\nprint(\"Máximo:\", maximo)")

== Buscar un valor

#fuente[Recorrer listas · 4]

#codigo("notas = [7, 4, 9, 6, 8]\nbuscada = 6\ni = 0\nwhile i < len(notas) and notas[i] != buscada:\n    i = i + 1\nif i < len(notas):\n    print(\"Está en la posición\", i)\nelse:\n    print(\"No está\")")

== Índices negativos y rebanadas

#fuente[Listas a fondo · 1]

#codigo("letras = [\"a\", \"b\", \"c\", \"d\", \"e\"]\nprint(letras[-1], letras[-2])\nprint(letras[1:4], letras[:2], letras[3:])\nprint(letras[::2], letras[::-1])\nprint(letras[-3:])")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-09.ipynb", ([Traza a mano. Haz la tabla de traza de este programa con notas = \[7,…], [¿Qué imprime? Con la misma lista:], [Buscar lo que no está], [Índices negativos], [¿Qué imprime?], [Quitar todos. Escribe un programa que quite todos los 0 de datos =…],))

== Tarea 9 · Estadística sin atajos

#tarea-casa(([Recorre la lista una vez y calcula a la vez el máximo, el mínimo y la suma.], [Calcula la media.], [Recorre la lista otra vez y cuenta cuántos datos están por encima de la media.], [Comprueba tus tres primeros resultados con #raw("max"), #raw("min") y #raw("sum").],), [La media es 18 y hay 2 datos por encima.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/listas-a-fondo/#preguntas-tipo-examen", siguiente: [Sesión 10 · Tablas, tuplas y conjuntos])
