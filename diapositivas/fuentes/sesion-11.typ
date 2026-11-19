// Sesión 11 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 11, tema: "Sesión 11 · Cadenas y formato")

#portada([Cadenas y formato], subtitulo: [Recorrer y trocear texto, usar sus métodos y presentar resultados con f-strings.], kicker: "Sesión 11 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 10.], [0:15], [Situación: una palabra escrita con letras de imán en la nevera; para cambiar una hay que componer otra…], [0:25], [#strong[Predice]. Las rebanadas se dibujan con los índices entre las letras.], [0:45], [Construcción: inmutabilidad, métodos, #raw("in"), f-strings con anchura y decimales.], [1:20], [Ejercicios de los dos capítulos.], [1:45], [Preguntas tipo examen y tarea 11.],))

== Para empezar

#situacion[Una palabra escrita con letras de imán en la nevera; para cambiar una hay que componer otra palabra.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("s = \"Programar\"\nprint(s[0], s[-1], s[2:5], s[::-1])\nprint(s.upper().count(\"R\"))\nprint(f\"{3.14159:.2f}|{42:>5}|\")")

#pause

#respuesta([#raw("P r ogr ramargorP") · #raw("3") · #raw("3.14|   42|")], [#raw("s[2:5]") va del índice 2 al 4.])

== Contar vocales

#fuente[Cadenas · 1]

#codigo("palabra = \"murciélago\"\nvocales = 0\nfor letra in palabra:\n    if letra in \"aeiouáéíóú\":\n        vocales = vocales + 1\nprint(vocales)")

== Darle la vuelta a una palabra

#fuente[Cadenas · 2]

#codigo("palabra = \"radar\"\nal_reves = \"\"\nfor letra in palabra:\n    al_reves = letra + al_reves\nprint(al_reves, al_reves == palabra)")

== Trozos de una cadena: las rebanadas

#fuente[Cadenas · 3]

#codigo("palabra = \"programar\"\nprint(palabra[0:3])    # pro\nprint(palabra[3:])     # gramar: desde la 3 hasta el final\nprint(palabra[-1])     # r: las posiciones negativas cuentan desde el final\nprint(palabra[::-1])   # ramargorp: toda la cadena, al revés", talla: 13pt)

== Métodos que ya vienen hechos

#fuente[Cadenas · 4]

#codigo("frase = \"Hola, mundo\"\nprint(frase.upper())             # HOLA, MUNDO\nprint(frase.count(\"o\"))          # 2\nprint(frase.replace(\"mundo\", \"clase\"))\nprint(frase.split(\", \"))         # ['Hola', 'mundo']\nprint(frase)                     # la original no ha cambiado", talla: 15pt)

== Comillas, escapes y varias líneas

#fuente[Cadenas y formato · 1]

#codigo("print('Dijo \"hola\" y se fue')        # comillas dobles dentro de simples\nprint(\"It's fine\")                   # un apóstrofo dentro de dobles\nprint('It\\'s fine')                  # o escapado\nprint(\"Columna1\\tColumna2\\nfila1\\tfila2\")\nprint(\"C:\\\\Users\\\\tony\")\npoema = \"\"\"Primera línea\nsegunda línea\ntercera línea\"\"\"\nprint(poema)\nprint(len(\"a\\nb\"))                   # \\n es UN carácter", talla: 13pt)

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-11.ipynb", ([Predice el resultado: \"python\"\[1:4\], \"python\"\[-2\] y len(\"hola mundo\").], [Mayúsculas a mano], [¿Palíndromo? ¿Es palíndromo \"Anita lava la tina\"? ¿Qué tendrías que…], [Escapes. Escribe con un solo print y una sola cadena:], [¿Qué imprime? a) \"python\".capitalize(); b) \"Hola Mundo\".swapcase();…], [Iniciales. Escribe una función que reciba \"ana garcía lópez\" y…],))

== Tarea 11 · Validador de contraseñas

#tarea-casa(([Pide una contraseña.], [Recorre sus caracteres una vez y anota con tres variables #raw("bool") si has visto mayúscula, minúscula y cifra.], [Guarda en una lista el texto de cada regla que no se cumple.], [Si la lista está vacía, escribe #raw("válida"); si no, escribe cada fallo en una línea.],), [#raw("Python2026") es válida; #raw("python 2026A") solo falla por el espacio.])

== Antes de irte
#cierre(qr: "https://achanesespigares.github.io/python-acinstitut/capitulos/cadenas-y-formato/#preguntas-tipo-examen", siguiente: [Sesión 12 · Diccionarios])
