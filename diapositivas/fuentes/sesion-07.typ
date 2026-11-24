// Sesión 7 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 7, tema: "Sesión 7 · Repetir: while, for y range")

#portada([Repetir: #raw("while"), #raw("for") y #raw("range")], subtitulo: [Repetir un bloque un número fijo de veces o mientras se cumpla una condición, y saber cuál de los dos usar.], kicker: "Sesión 7 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 6.], [0:15], [Situación: dar 10 vueltas a la pista frente a correr hasta cansarse.], [0:25], [#strong[Predice] y visualizador.], [0:40], [Construcción: #raw("while"), #raw("for"), #raw("range") con uno, dos y tres argumentos, acumuladores.], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen y tarea 7.],))

== Para empezar

#situacion[Dar 10 vueltas a la pista frente a correr hasta cansarse.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("for i in range(1, 10, 3):\n    print(i, end=\" \")\nprint()\nn = 0\nwhile n < 3:\n    n += 1\nprint(n)")

#pause

#respuesta([#raw("1 4 7") · #raw("3")], [#raw("range(1, 10, 3)") se para antes de 10.])

== La cuenta atrás con #raw("while")

#fuente[Bucles while y for · 1]

#codigo("n = 5\nwhile n > 0:\n    print(n)\n    n = n - 1\nprint(\"¡Despegue!\")")

== Sumar de 1 a 5 con #raw("for")

#fuente[Bucles while y for · 2]

#codigo("suma = 0\nfor k in range(1, 6):\n    suma = suma + k\nprint(suma)")

== Duplicar hasta pasarse de 100

#fuente[Bucles while y for · 3]

#codigo("x = 1\npasos = 0\nwhile x <= 100:\n    x = x * 2\n    pasos = pasos + 1\nprint(pasos, x)")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-07.ipynb", ([Traza a mano este bucle. ¿Qué imprime?], [Escribe con for], [El bucle roto. ¿Por qué este programa no termina nunca? Arréglalo.],))

== Tarea 7 · La tabla de multiplicar

#tarea-casa(([Pide un número #raw("n").], [Escribe su tabla del 1 al 10 con un #raw("for") y #raw("range"), con este formato: #raw("7 x 3 = 21").], [Escríbela otra vez con un #raw("while"). ¿Qué tienes que hacer a mano que el #raw("for") hacía solo?], [Ampliación: escribe solo las líneas cuyo resultado sea par.],), [La última línea de la tabla del 7 es #raw("7 x 10 = 70").])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/bucles/#preguntas-tipo-examen", siguiente: [Sesión 8 · #raw("break"), #raw("continue"), centinelas y bucles anidados])
