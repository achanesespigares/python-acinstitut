// Sesión 23 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 23, tema: "Sesión 23 · match y lambdas")

#portada([#raw("match") y lambdas], subtitulo: [Elegir según la forma de un dato, y pasar funciones cortas como argumento para ordenar, transformar y filtrar.], kicker: "Sesión 23 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 22.], [0:15], [Situación: ordenar una clasificación por puntos y, si empatan, por orden alfabético.], [0:25], [#strong[Predice]. El #raw("-") delante de la nota invierte solo ese criterio.], [0:45], [Construcción: #raw("match") con patrones de secuencia, #raw("lambda"), #raw("key"), #raw("map"), #raw("filter").], [1:20], [Ejercicios de los dos capítulos.], [1:45], [Preguntas tipo examen y tarea 23.],))

== Para empezar

#situacion[Ordenar una clasificación por puntos y, si empatan, por orden alfabético.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("alumnos = [(\"Ana\", 7), (\"Luis\", 9), (\"Eva\", 7)]\nalumnos.sort(key=lambda a: (-a[1], a[0]))\nprint(alumnos)\nprint(list(map(lambda a: a[0][0], alumnos)))")

#pause

#respuesta([#raw("[('Luis', 9), ('Ana', 7), ('Eva', 7)]") · #raw("['L', 'A', 'E']")], [Primero por nota descendente; a igual nota, por nombre.])

== #raw("match"): elegir por la forma

#fuente[Comprensiones, for…else y match · 6]

#codigo("punto = (0, 3)\nmatch punto:\n    case (0, 0):\n        print(\"el origen\")\n    case (0, y):\n        print(\"en el eje vertical, a altura\", y)\n    case (x, 0):\n        print(\"en el eje horizontal, en\", x)\n    case _:\n        print(\"fuera de los ejes\")")

== Ordenar con un criterio

#fuente[Funciones como valores · 1]

#codigo("alumnos = [(\"Ana\", 7), (\"Biel\", 9), (\"Carla\", 5)]\npor_nota = sorted(alumnos, key=lambda a: a[1])\nprint(por_nota)")

== #raw("map") y #raw("filter")

#fuente[Funciones como valores · 2]

#codigo("datos = [3, 8, 11, 6]\ndobles = list(map(lambda x: x * 2, datos))\npares = list(filter(lambda x: x % 2 == 0, datos))\nprint(dobles, pares)")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-23.ipynb", ([Del bucle a la comprensión], [Solo los pares], [Sin negativos. A partir de temperaturas = \[3, -2, 5, -7\], crea una…], [¿Qué imprime?], [Comandos. Con match, escribe un programa que, para orden = \"n\",…], [La más larga. Usa max con key para encontrar la palabra más larga de…],))

== Tarea 23 · Calculadora y clasificación

#tarea-casa(([Escribe #raw("calcula(linea)"): parte la línea con #raw("split") y usa #raw("match") sobre la lista de partes.], [Para la división, devuelve un aviso si el divisor es 0.], [Con #raw("notas = [(\"Eva\", 7.5), (\"Ana\", 9), (\"Luis\", 7.5), (\"Bea\", 5)]"), ordena con #raw("sorted") y una #raw("lambda") de mayor a…], [Con #raw("filter") y una #raw("lambda"), quédate con los que tienen 7 o más.],), [#raw("calcula(\"10 / 4\")") da 2,5 y el orden empieza por Ana, Eva, Luis.])

== Antes de irte
#cierre(qr: "https://achanesespigares.github.io/python-acinstitut/capitulos/funciones-valores/#preguntas-tipo-examen", siguiente: [Sesión 24 · Cierres y generadores])
