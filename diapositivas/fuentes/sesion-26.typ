// Sesión 26 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 26, tema: "Sesión 26 · Cadenas a fondo")

#portada([Cadenas a fondo], subtitulo: [Trabajar con códigos de caracteres, comparar cadenas y usar los métodos de comprobación y troceado.], kicker: "Sesión 26 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 25.], [0:15], [Situación: un diccionario de papel: «Zeta» va antes que «alfa» si las mayúsculas cuentan primero.], [0:25], [#strong[Predice].], [0:40], [Construcción: Unicode, #raw("ord"), #raw("chr"), comparación, métodos #raw("is…"), #raw("split"), #raw("join"), #raw("find"), #raw("index").], [1:10], [Ejercicios del capítulo.], [1:30], [Presentación del proyecto 2: enunciado, hitos y rúbrica.], [1:50], [Tarea 26 y hito 1.],))

== Para empezar

#situacion[Un diccionario de papel: «Zeta» va antes que «alfa» si las mayúsculas cuentan primero.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("print(ord(\"A\"), chr(98), \"abc\" < \"abd\", \"Zeta\" < \"alfa\")\nprint(\"a,b,,c\".split(\",\"), \"-\".join(\"xyz\"))\nprint(\"3\".isdigit(), \"3.5\".isdigit(), \" hola \".strip().title())")

#pause

#respuesta([#raw("65 b True True") · #raw("['a', 'b', '', 'c'] x-y-z") · #raw("True False Hola")], [Las mayúsculas tienen códigos menores que las minúsculas.])

== Desplazar letras: el cifrado César

#fuente[Cadenas a fondo · 1]

#codigo("mensaje = \"hola\"\ncifrado = \"\"\nfor letra in mensaje:\n    codigo = ord(letra) + 3\n    cifrado = cifrado + chr(codigo)\nprint(cifrado)")

== Comparar cadenas

#fuente[Cadenas a fondo · 2]

#codigo("a = \"casa\"\nb = \"cama\"\ni = 0\nwhile a[i] == b[i]:\n    i = i + 1\nprint(a[i], b[i], ord(a[i]), ord(b[i]))\nprint(a < b)")

== Validar, buscar y contar

#fuente[Cadenas a fondo · 3]

#codigo("frase = \"la casa de la playa\"\nprint(frase.find(\"la\"), frase.rfind(\"la\"), frase.find(\"zz\"))\nprint(frase.index(\"casa\"), frase.rindex(\"la\"), frase.count(\"a\"), \"casa\" in frase)\nprint(frase.find(\"a\", 5), frase.find(\"a\", 5, 9), frase.count(\"a\", 10))\nprint(frase.startswith(\"la\"), frase.endswith(\"ya\"))\nprint(frase.split(), \"-\".join([\"a\", \"b\", \"c\"]))", talla: 13pt)

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-26.ipynb", ([Descifrar. Escribe el programa que deshace el cifrado César del…], [¿Qué imprime? print(sorted(\[\"pera\", \"Uva\", \"manzana\"\])).], [Solo dígitos. Escribe una función es\_codigo\_postal(s) que devuelva…], [Contar palabras],))

== Tarea 26 · El cifrado César

#tarea-casa(([Escribe #raw("cesar(texto, k)"), que desplaza cada letra #raw("k") posiciones en el alfabeto inglés, dando la vuelta al llegar a la…], [Las mayúsculas siguen siendo mayúsculas y las minúsculas, minúsculas.], [Usa #raw("ord"), #raw("chr") y el resto #raw("%") 26.], [Comprueba que #raw("cesar(cesar(t, k), -k)") devuelve #raw("t").],), [#raw("cesar(\"Hola, Mundo!\", 3)") es #raw("Krod, Pxqgr!").])

== El proyecto

#con-qr("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-2.ipynb", [Cuaderno del proyecto], situacion[#strong[Hito 1 del proyecto.] El diseño de las clases de la biblioteca (ver Proyecto 2).])

== Antes de irte
#cierre(qr: "https://achanesespigares.github.io/python-acinstitut/capitulos/cadenas-a-fondo/#preguntas-tipo-examen", siguiente: [Sesión 27 · Probar y depurar])
