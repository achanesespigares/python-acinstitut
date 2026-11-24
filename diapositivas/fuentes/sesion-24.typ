// Sesión 24 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 24, tema: "Sesión 24 · Cierres y generadores")

#portada([Cierres y generadores], subtitulo: [Fabricar funciones que recuerdan un dato, y producir valores uno a uno sin guardarlos todos.], kicker: "Sesión 24 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 23.], [0:15], [Situación: un sello de goma con la fecha ya puesta; cada sello recuerda su fecha.], [0:25], [#strong[Predice] y visualizador: el marco de #raw("multiplicador") sigue vivo después de terminar.], [0:45], [Construcción: funciones dentro de funciones, cierres, #raw("yield"), #raw("next").], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen y tarea 24.],))

== Para empezar

#situacion[Un sello de goma con la fecha ya puesta; cada sello recuerda su fecha.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("def multiplicador(k):\n    def f(x):\n        return k * x\n    return f\n\ndoble = multiplicador(2)\ntriple = multiplicador(3)\nprint(doble(5), triple(doble(1)))\n\ndef cuenta(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nprint(list(cuenta(3)), sum(cuenta(4)))", talla: 15pt), uncover("2-", respuesta([#raw("10 6") · #raw("[3, 2, 1] 10")], [#raw("triple(doble(1))") es 3 · 2; 4 + 3 + 2 + 1 = 10.])))

== Funciones que fabrican funciones: los cierres

#fuente[Funciones como valores · 3]

#codigo("def multiplicador(n):\n    def por(x):\n        return x * n\n    return por\n\ndoble = multiplicador(2)\ntriple = multiplicador(3)\nprint(doble(5), triple(5))")

== Ampliación · generadores

#fuente[Funciones como valores · 4]

#codigo("def cuenta_atras(n):\n    while n > 0:\n        yield n\n        n = n - 1\n\nfor v in cuenta_atras(3):\n    print(v)")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-24.ipynb", ([La más larga. Usa max con key para encontrar la palabra más larga de…], [Ordenar al revés], [De map a comprensión], [¿Qué imprime?], [Un generador de pares],))

== Tarea 24 · Descuentos y Fibonacci

#tarea-casa(([Escribe #raw("descuento(pct)"), que devuelve una función #raw("aplica(precio)") con el precio rebajado y redondeado a céntimos.], [Crea #raw("rebajas = descuento(20)") y #raw("black_friday = descuento(35)") y aplícalas a 50 €.], [Escribe el generador #raw("fibonacci(limite)"), que produce los términos de la sucesión (0, 1, 1, 2, 3…) mientras no pasen…], [Convierte en lista los de hasta 100, y saca los tres primeros de otro generador con #raw("next").],), [Las rebajas dejan 50 € en 40 €; el último término hasta 100 es 89.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/funciones-valores/#preguntas-tipo-examen", siguiente: [Sesión 25 · Ficheros, bytes y rutas])
