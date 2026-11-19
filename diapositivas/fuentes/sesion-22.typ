// Sesión 22 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 22, tema: "Sesión 22 · Comprensiones y el else de los bucles")

#portada([Comprensiones y el #raw("else") de los bucles], subtitulo: [Construir listas, diccionarios y conjuntos en una línea, y saber cuándo un bucle terminó sin #raw("break").], kicker: "Sesión 22 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 21.], [0:15], [Situación: «de los de la lista, los mayores de edad, en mayúsculas»: una frase que hace tres cosas.], [0:25], [#strong[Predice] y visualizador.], [0:45], [Construcción: comprensiones con filtro, expresión condicional, de diccionario y de conjunto, anidadas, \`for ……], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen y tarea 22.],))

== Para empezar

#situacion[«de los de la lista, los mayores de edad, en mayúsculas»: una frase que hace tres cosas.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("print([x * x for x in range(6) if x % 2])\nprint({c: len(c) for c in [\"sol\", \"luna\"]})\nfor n in [3, 5, 7]:\n    if n % 2 == 0:\n        break\nelse:\n    print(\"ningún par\")")

#pause

#respuesta([#raw("[1, 9, 25]") · #raw("{'sol': 3, 'luna': 4}") · #raw("ningún par")], [El #raw("else") del #raw("for") se ejecuta porque no hubo #raw("break").])

== Filtrar y transformar a la vez

#fuente[Comprensiones, for…else y match · 1]

#codigo("palabras = [\"sol\", \"camino\", \"luz\", \"montaña\"]\nlargas = [p.upper() for p in palabras if len(p) > 3]\nprint(largas)")

== La expresión condicional

#fuente[Comprensiones, for…else y match · 2]

#codigo("notas = [4, 7, 5, 9]\netiquetas = [\"aprobado\" if n >= 5 else \"suspenso\" for n in notas]\nprint(etiquetas)", talla: 15pt)

== Diccionarios y conjuntos por comprensión

#fuente[Comprensiones, for…else y match · 3]

#codigo("palabras = [\"sol\", \"camino\", \"luz\", \"montaña\"]\nlongitudes = {p: len(p) for p in palabras}\niniciales = {p[0] for p in palabras}\nprint(longitudes)\nprint(sorted(iniciales))")

== Comprensiones anidadas

#fuente[Comprensiones, for…else y match · 4]

#codigo("casillas = [(fila, col) for fila in range(2) for col in range(3)]\nprint(casillas)", talla: 15pt)

== #raw("for … else"): el bucle que sabe si encontró algo

#fuente[Comprensiones, for…else y match · 5]

#codigo("intentos = 3\nwhile intentos > 0:\n    intentos = intentos - 1\nelse:\n    print(\"Se acabaron los intentos\")")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-22.ipynb", ([Del bucle a la comprensión], [Solo los pares], [Sin negativos. A partir de temperaturas = \[3, -2, 5, -7\], crea una…], [¿Qué imprime?], [Comandos. Con match, escribe un programa que, para orden = \"n\",…],))

== Tarea 22 · Del bucle a la comprensión

#tarea-casa(([Los números positivos.], [Los cuadrados de todos los números.], [La lista con #raw("\"par\"") o #raw("\"impar\"") para cada número (expresión condicional).], [Un diccionario de cada palabra con su longitud.], [El conjunto de las iniciales de las palabras.], [Ampliación: la traspuesta de #raw("[[1, 2, 3], [4, 5, 6]]") con una comprensión anidada.],), [El conjunto de iniciales tiene 3 elementos y la traspuesta es #raw("[[1, 4], [2, 5], [3, 6]]").])

== Antes de irte
#cierre(qr: "https://achanesespigares.github.io/python-acinstitut/capitulos/comprensiones/#preguntas-tipo-examen", siguiente: [Sesión 23 · #raw("match") y lambdas])
