// Sesión 4 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 4, tema: "Sesión 4 · Variables, input y print")

#portada([Variables, #raw("input") y #raw("print")], subtitulo: [Guardar datos en variables, pedirlos al usuario y mostrarlos con el formato que se quiera.], kicker: "Sesión 4 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 3.], [0:15], [Situación: una etiqueta con nombre pegada a una caja.], [0:25], [#strong[Predice] y visualizador.], [0:40], [Construcción: asignación, #raw("input"), conversión con #raw("int") y #raw("float"), #raw("print") con #raw("sep") y #raw("end").], [1:20], [Ejercicios de los dos capítulos, en Colab (aquí #raw("input") sí funciona).], [1:45], [Preguntas tipo examen del capítulo 4 y tarea 4.],))

== Para empezar

#situacion[Una etiqueta con nombre pegada a una caja. Cambiar lo de dentro no cambia la etiqueta.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("x = 5\ny = x\nx = x + 2\nprint(x, y)")

#pause

#respuesta([#raw("7 5")], [#raw("y = x") copia el valor 5; cambiar #raw("x") después no toca #raw("y").])

== El marcador

#fuente[Variables y asignación · 1]

#codigo("local = 0\nvisitante = 0\nlocal = local + 1\nvisitante = visitante + 1\nlocal = local + 1\nprint(local, \"-\", visitante)")

== Intercambiar dos valores

#fuente[Variables y asignación · 2]

#codigo("a = 5\nb = 8\na, b = b, a\nprint(a, b)")

== Pedir datos, convertirlos y mostrarlos

#fuente[Cómo funciona Python · 1]

#codigo("print(1, 2, 3)\nprint(1, 2, 3, sep=\"-\")\nprint(\"sin salto\", end=\" \")\nprint(\"de línea\")")

== Palabras reservadas, sentencias y expresiones

#fuente[Cómo funciona Python · 2]

#codigo("import keyword\nprint(len(keyword.kwlist))\nprint(keyword.kwlist)")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-04.ipynb", ([Traza a mano. Haz la tabla de traza de este programa. ¿Qué imprime?], [¿Qué valor tiene n al final?], [Rotar tres valores], [¿Compilado o interpretado?], [Clasifica el error], [¿Qué imprime? a) print(3 + 2 \* 2  2); b) print(-3  2); c) print(7 \/\/…],))

== Tarea 4 · Tarjeta de presentación

#tarea-casa(([Pide con #raw("input") el nombre, el año de nacimiento y el año actual.], [Convierte los dos años a #raw("int") y calcula la edad que se cumple este año.], [Muestra la tarjeta en tres líneas: el nombre entre guiones, la edad y una despedida.], [Escribe la segunda línea con un solo #raw("print") y el parámetro #raw("sep").],), [Con «Ada», 2008 y 2026, la segunda línea debe decir que cumple 18 años.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/como-funciona-python/#preguntas-tipo-examen", siguiente: [Sesión 5 · Tipos, literales y operadores])
