// Sesión 13 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 13, tema: "Sesión 13 · Funciones")

#portada([Funciones], subtitulo: [Dar nombre a un trozo de programa, pasarle datos y recibir un resultado, y entender qué ve cada función.], kicker: "Sesión 13 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 12 y repaso del hito 1.], [0:15], [Situación: una receta que se usa en muchos platos; «haz la bechamel» resume seis pasos.], [0:25], [#strong[Predice] y visualizador: cada llamada abre su propio marco.], [0:40], [Construcción: parámetros, #raw("return"), valores por defecto, argumentos con nombre, #raw("*args"), ámbito, #raw("global"),…], [1:20], [Ejercicios de los dos capítulos.], [1:45], [Preguntas tipo examen y tarea 13.],))

== Para empezar

#situacion[Una receta que se usa en muchos platos; «haz la bechamel» resume seis pasos.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("def doble(x):\n    x = x * 2\n    return x\n\nn = 5\nprint(doble(n), n)\n\ndef saluda(nombre, saludo=\"Hola\"):\n    print(saludo, nombre)\n\nsaluda(\"Ana\")\nsaluda(\"Luis\", saludo=\"Buenas\")", talla: 16pt), uncover("2-", respuesta([#raw("10 5") · #raw("Hola Ana") · #raw("Buenas Luis")], [La #raw("x") de la función es otra variable: #raw("n") sigue valiendo 5.])))

== El área del rectángulo

#fuente[Funciones · 1]

#codigo("def area_rectangulo(base, altura):\n    area = base * altura\n    return area\n\na = area_rectangulo(3, 4)\nb = area_rectangulo(2, 5)\nprint(a + b)")

== #raw("print") no es #raw("return")

#fuente[Funciones · 2]

#codigo("def suma_mal(a, b):\n    print(a + b)\n\nr = suma_mal(2, 3)\nprint(r)")

== Funciones que usan funciones

#fuente[Funciones · 3]

#codigo("def cuadrado(x):\n    return x * x\n\ndef hipotenusa(a, b):\n    suma = cuadrado(a) + cuadrado(b)\n    return suma ** 0.5\n\nh = hipotenusa(3, 4)\nprint(h)")

== Valores por defecto y argumentos por nombre

#fuente[Funciones a fondo · 1]

#codigo("for llamada in [\"precio_final()\", \"precio_final(100, 10, 5, 3)\", \"precio_final(100, precio=50)\"]:\n    try:\n        eval(llamada)\n    except TypeError as e:\n        print(llamada, \"→\", e)", talla: 13pt)

== Cualquier número de argumentos: #raw("*args")

#fuente[Funciones a fondo · 2]

#codigo("def media(*notas):\n    total = 0\n    for n in notas:\n        total += n\n    return total / len(notas)\n\nprint(media(6, 8, 10))\nprint(media(5))")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-13.ipynb", ([Escribe una función celsius\_a\_fahrenheit(c) que devuelva c \* 9 \/ 5 +…], [¿Qué imprime?], [Corrige suma\_mal para que r valga 5.], [¿Válido o no? a) def f(a, b=1, c):; b) f(1, c=3) para def f(a, b=1,…], [¿Qué imprime?], [Suma flexible. Escribe suma\_todo(\*numeros) que devuelva la suma de…],))

== Tarea 13 · Refactorizar en funciones

#tarea-casa(([#raw("segundos_a_hms(total)") devuelve una tupla #raw("(h, m, s)") (tarea 5).], [#raw("calificacion(nota)") devuelve el texto de la calificación (tarea 6).], [#raw("media_de(*numeros)") acepta cualquier cantidad de números y devuelve su media, o #raw("None") si no recibe ninguno.], [Debajo, prueba cada función con los casos de las tareas originales.],), [#raw("segundos_a_hms(4000)") devuelve #raw("(1, 6, 40)") y #raw("media_de()") devuelve #raw("None").])

== El proyecto

#con-qr("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-1.ipynb", [Cuaderno del proyecto], situacion[#strong[Hito 2 del proyecto.] Las funciones del gestor de notas, probadas con datos escritos a mano.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/funciones-a-fondo/#preguntas-tipo-examen", siguiente: [Sesión 14 · Errores, ficheros, CSV y módulos])
