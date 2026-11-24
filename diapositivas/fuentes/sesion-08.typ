// Sesión 8 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 8, tema: "Sesión 8 · break, continue, centinelas y bucles anidados")

#portada([#raw("break"), #raw("continue"), centinelas y bucles anidados], subtitulo: [Salir de un bucle antes de tiempo, saltar una vuelta y repetir hasta que llegue un valor especial.], kicker: "Sesión 8 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 7.], [0:15], [Situación: pasar lista y saltarse a quien ya se ha ido; cerrar el cuaderno cuando suena el timbre.], [0:25], [#strong[Predice] y visualizador.], [0:40], [Construcción: #raw("break"), #raw("continue"), el valor centinela, #raw("while True"), bucles anidados.], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen y tarea 8.],))

== Para empezar

#situacion[Pasar lista y saltarse a quien ya se ha ido; cerrar el cuaderno cuando suena el timbre.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("for n in range(1, 10):\n    if n % 2 == 0:\n        continue\n    if n > 6:\n        break\n    print(n, end=\" \")")

#pause

#respuesta([#raw("1 3 5")], [Los pares se saltan; al llegar a 7 se sale.])

== #raw("continue"): saltar una vuelta

#fuente[Bucles a fondo · 1]

#codigo("datos = [4, -2, 7, -5, 3]\nsuma = 0\nfor d in datos:\n    if d < 0:\n        continue\n    suma += d\nprint(suma)")

== #raw("while") con centinela

#fuente[Bucles a fondo · 2]

#codigo("total = 0\ndato = int(input(\"Nota (-1 para acabar): \"))\nwhile dato != -1:\n    total += dato\n    dato = int(input(\"Nota (-1 para acabar): \"))\nprint(\"Total:\", total)")

== El operador morsa #raw(":=")

#fuente[Bucles a fondo · 3]

#codigo("datos = [3, 8, 1]\nif (n := len(datos)) > 2:\n    print(\"Hay\", n, \"datos\")\n\npila = [1, 2, 3]\nwhile (cima := pila.pop()) != 1:\n    print(\"saco\", cima)")

== #raw("range") con paso, también hacia atrás

#fuente[Bucles a fondo · 4]

#codigo("print(list(range(0, 10, 3)))\nprint(list(range(10, 0, -2)))\nprint(list(range(5, 0, -1)))\nprint(list(range(0, 5, -1)))      # vacío: con paso negativo, hacia 5 no se llega", talla: 13pt)

== Bucles anidados

#fuente[Bucles a fondo · 5]

#codigo("for fila in range(1, 4):\n    for col in range(1, 5):\n        print(fila * col, end=\"\\t\")\n    print()")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-08.ipynb", ([¿Qué imprime?], [Contar vueltas], [Adivina el número], [Hacia atrás. Escribe con range la lista \[20, 15, 10, 5, 0\].], [Tabla de multiplicar],))

== Tarea 8 · La media con centinela

#tarea-casa(([Pide notas una a una hasta que se escriba #raw("-1").], [Si una nota no está entre 0 y 10, avisa y sáltala con #raw("continue").], [Lleva dos acumuladores: la suma y cuántas notas válidas van.], [Al terminar, escribe la media con dos decimales, o #raw("No hay notas") si no se escribió ninguna válida.],), [Con 7, 12, 5, 8 y −1, el 12 se ignora y la media es 6,67.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/bucles-a-fondo/#preguntas-tipo-examen", siguiente: [Sesión 9 · Recorrer y modificar listas])
