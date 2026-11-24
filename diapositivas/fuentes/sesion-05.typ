// Sesión 5 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 5, tema: "Sesión 5 · Tipos, literales y operadores")

#portada([Tipos, literales y operadores], subtitulo: [Distinguir #raw("int"), #raw("float"), #raw("str") y #raw("bool"), y predecir el resultado de cualquier expresión con sus operadores y prioridades.], kicker: "Sesión 5 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 4.], [0:15], [Situación: repartir 7 caramelos entre 2: a cada uno le tocan 3 y sobra 1.], [0:25], [#strong[Predice]. Las dos últimas líneas suelen fallar casi a todos: es el momento de hablar de prioridades y de…], [0:45], [Construcción: tipos, literales (#raw("0b"), #raw("0o"), #raw("0x"), #raw("1e3")), operadores y su prioridad.], [1:20], [Ejercicios de los dos capítulos.], [1:45], [Preguntas tipo examen del capítulo 5 y tarea 5.],))

== Para empezar

#situacion[Repartir 7 caramelos entre 2: a cada uno le tocan 3 y sobra 1.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("print(7 / 2, 7 // 2, 7 % 2)\nprint(2 ** 3 ** 2)\nprint(\"3\" + \"4\", 3 + 4)\nprint(-7 // 2)")

#pause

#respuesta([#raw("3.5 3 1") · #raw("512") · #raw("34 7") · #raw("-4")], [#raw("**") se agrupa por la derecha (2⁹); #raw("//") redondea hacia abajo, también con negativos.])

== Cada valor con su tipo

#fuente[Tipos de datos · 1]

#codigo("edad = 17\naltura = 1.75\nnombre = \"Lucía\"\nmayor = edad >= 18\nprint(nombre, mayor)")

== Texto que parece número

#fuente[Tipos de datos · 2]

#codigo("a = \"5\"\nb = \"3\"\njunto = a + b\nsuma = int(a) + int(b)\nmedia = suma / 2\nprint(junto, suma, media)")

== Horas y minutos: división entera y resto

#fuente[Tipos de datos · 3]

#codigo("minutos = 135\nhoras = minutos // 60\nresto = minutos % 60\nprint(horas, \"h\", resto, \"min\")")

== Literales: escribir valores directamente

#fuente[Cómo funciona Python · 3]

#codigo("print(0.1 + 0.2, 0.1 + 0.2 == 0.3)\nprint(round(0.1 + 0.2, 2) == 0.3, abs((0.1 + 0.2) - 0.3) < 1e-9)", talla: 15pt)

== Operadores: quién va primero

#fuente[Cómo funciona Python · 4]

#codigo("print(2 ** 3 ** 2)      # 2 ** 9 = 512: la potencia se agrupa por la derecha\nprint(-2 ** 2)          # -(2 ** 2) = -4: la potencia va antes que el signo\nprint(10 - 4 - 3)       # (10 - 4) - 3 = 3: la resta, por la izquierda\nprint(True or False and False)   # and antes que or: True", talla: 13pt)

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-05.ipynb", ([Predice el tipo y el valor], [Encuentra el error], [Segundos a h:m:s], [¿Compilado o interpretado?], [Clasifica el error], [¿Qué imprime? a) print(3 + 2 \* 2  2); b) print(-3  2); c) print(7 \/\/…],))

== Tarea 5 · De segundos a horas, minutos y segundos

#tarea-casa(([Pide un número entero de segundos.], [Calcula las horas con #raw("//").], [Calcula lo que sobra con #raw("%"), y de ahí los minutos y los segundos.], [Muestra el resultado con un f-string: #raw("1 h 6 min 40 s").], [Prueba con 3600 y con 59 antes de dar la tarea por buena.],), [4000 segundos son 1 h 6 min 40 s.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/como-funciona-python/#preguntas-tipo-examen", siguiente: [Sesión 6 · Decidir: #raw("if"), #raw("elif"), #raw("else")])
