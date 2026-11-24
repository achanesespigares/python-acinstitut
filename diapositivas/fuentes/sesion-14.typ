// Sesión 14 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 14, tema: "Sesión 14 · Errores, ficheros, CSV y módulos")

#portada([Errores, ficheros, CSV y módulos], subtitulo: [Que un programa no se rompa con datos inesperados, leer y escribir ficheros CSV, y usar #raw("math") y #raw("random").], kicker: "Sesión 14 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 13.], [0:15], [Situación: un cajero que, si la tarjeta falla, avisa y devuelve la tarjeta en vez de apagarse.], [0:25], [#strong[Predice] y visualizador.], [0:40], [Construcción: #raw("try")\/#raw("except"), el bucle que pide hasta que el dato es válido, leer y escribir un CSV, #raw("math") y…], [1:10], [Ejercicios de los dos capítulos.], [1:30], [Taller del proyecto: el profesor pasa por las parejas.], [1:50], [Hito 3.],))

== Para empezar

#situacion[Un cajero que, si la tarjeta falla, avisa y devuelve la tarjeta en vez de apagarse.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("try:\n    n = int(\"12a\")\n    print(\"convertido\")\nexcept ValueError:\n    print(\"no es un número\")\nfinally:\n    print(\"fin\")")

#pause

#respuesta([#raw("no es un número") · #raw("fin")], [#raw("finally") se ejecuta siempre.])

== El texto que no es un número

#fuente[Excepciones · 1]

#codigo("texto = \"doce\"\ntry:\n    numero = int(texto)\n    doble = numero * 2\nexcept ValueError:\n    doble = 0\n    print(\"No es un número\")\nprint(doble)")

== Seguir adelante dentro de un bucle

#fuente[Excepciones · 2]

#codigo("datos = [10, 0, 5]\nresultados = []\nfor d in datos:\n    try:\n        resultados.append(100 // d)\n    except ZeroDivisionError:\n        resultados.append(None)\nprint(resultados)")

== Un fichero de texto en dos minutos

#fuente[CSV, math y random · 1]

#codigo("with open(\"diario.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"lunes: álgebra\\n\")\nwith open(\"diario.txt\", \"a\", encoding=\"utf-8\") as f:\n    f.write(\"martes: funciones\\n\")\nwith open(\"diario.txt\", encoding=\"utf-8\") as f:\n    for linea in f:\n        print(linea.strip())\ntry:\n    open(\"no_existe.txt\")\nexcept FileNotFoundError as e:\n    print(\"Error:\", e)")

== Escribir y leer un CSV

#fuente[CSV, math y random · 2]

#codigo("import csv\nwith open(\"notas.csv\", \"w\", newline=\"\") as f:\n    w = csv.writer(f)\n    w.writerow([\"nombre\", \"nota\"])\n    w.writerow([\"Ana\", 7])\n    w.writerow([\"Biel\", 9])\nwith open(\"notas.csv\", newline=\"\") as f:\n    filas = list(csv.reader(f))\nprint(filas)\ntotal = 0\nfor fila in filas[1:]:\n    total += int(fila[1])\nprint(total)")

== El módulo #raw("math"): redondear de cuatro maneras

#fuente[CSV, math y random · 3]

#codigo("import math\nfor x in [2.5, -2.5, 2.7]:\n    print(x, math.ceil(x), math.floor(x), math.trunc(x), round(x))\nprint(math.sqrt(16), math.pi, math.factorial(5), math.hypot(3, 4))", talla: 15pt)

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-14.ipynb", ([¿Qué imprime?], [Pedir un número], [El orden. ¿Qué imprime este programa? ¿Cómo lo arreglarías?], [Nota media. Escribe un programa que lea notas.csv (el del apartado 1)…], [Añadir una fila], [¿Qué imprime? print(math.ceil(4.01), math.floor(-0.5),…],))

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/csv-math-random/#preguntas-tipo-examen", siguiente: [Sesión 15 · Proyecto 1 y simulacro PCEP])
