// Sesión 16 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 16, tema: "Sesión 16 · Módulos y paquetes")

#portada([Módulos y paquetes], subtitulo: [Usar módulos de la biblioteca estándar con cualquier forma de #raw("import"), y escribir un módulo propio que se pueda importar y también ejecutar.], kicker: "Sesión 16 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Comentario del simulacro PCEP de la sesión 15: qué secciones fallaron más.], [0:20], [Situación: una caja de herramientas; no se saca todo para apretar un tornillo.], [0:30], [#strong[Predice]. #raw("round(2.5)") da 2: redondeo al par, una pregunta clásica de examen.], [0:45], [Construcción: formas de #raw("import"), #raw("dir"), #raw("__name__"), #raw("sys.path"), paquetes y subpaquetes, #raw("pip") y PyPI, y qué…], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen PCAP y tarea 16.],))

== Para empezar

#situacion[Una caja de herramientas; no se saca todo para apretar un tornillo.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("import math\nfrom random import randint as r\nprint(math.floor(-2.5), math.ceil(-2.5), round(2.5))\nprint(type(r(1, 6)))")

#pause

#respuesta([#raw("-3 -2 2") · #raw("<class 'int'>")], [#raw("floor") baja, #raw("ceil") sube; #raw("round") redondea al par cuando está a mitad.])

== Usar #raw("math")

#fuente[Módulos y paquetes · 1]

#codigo("import math\nradio = 3\narea = math.pi * radio ** 2\nredondeada = round(area, 2)\nlado = math.sqrt(area)\nprint(redondeada, round(lado, 2))")

== Números al azar que se pueden repetir

#fuente[Módulos y paquetes · 2]

#codigo("import random\nrandom.seed(7)\ntiradas = []\nfor i in range(5):\n    tiradas.append(random.randint(1, 6))\nprint(tiradas)")

== Paquetes y dónde busca Python

#fuente[Módulos y paquetes · 4]

#codigo("import math\nimport sys\nprint([nombre for nombre in dir(math) if not nombre.startswith(\"_\")][:10])\nprint(sys.path[0])", talla: 13pt)

== Cuando importar sale mal

#fuente[Módulos y paquetes · 5]

#codigo("try:\n    import numpi\nexcept ModuleNotFoundError as e:\n    print(type(e).__name__, \"·\", e)\nprint(issubclass(ModuleNotFoundError, ImportError))")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-16.ipynb", ([Tres formas. Escribe de tres maneras distintas un programa que…], [¿Qué pasa? Este programa da un error. ¿Por qué?], [Media con statistics],))

== Tarea 16 · Tu primer módulo

#tarea-casa(([En una celda de Colab escribe #raw("%%writefile geometria.py") en la primera línea y debajo el módulo.], [Define una constante #raw("PI") tomada de #raw("math") y las funciones #raw("area_circulo(r)") y #raw("area_rectangulo(base, altura)").], [Añade un bloque #raw("if __name__ == \"__main__\":") con dos pruebas que impriman resultados.], [En otra celda, haz #raw("import geometria") y usa las dos funciones.], [Ejecuta el módulo como programa con #raw("!python geometria.py").],), [#raw("geometria.area_rectangulo(3, 4)") devuelve 12, y al importarlo no se imprime nada.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/modulos/#preguntas-tipo-examen", siguiente: [Sesión 17 · Excepciones a fondo])
