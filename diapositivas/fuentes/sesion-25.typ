// Sesión 25 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 25, tema: "Sesión 25 · Ficheros, bytes y rutas")

#portada([Ficheros, bytes y rutas], subtitulo: [Leer y escribir ficheros de texto y binarios con #raw("with"), y moverse por carpetas con #raw("pathlib").], kicker: "Sesión 25 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 24.], [0:15], [Situación: un cuaderno: se puede empezar de cero, añadir al final o solo leer.], [0:25], [#strong[Predice] y visualizador: se ve el disco cambiar.], [0:45], [Construcción: modos #raw("r"), #raw("w"), #raw("a"), #raw("b"), #raw("with"), #raw("read"), #raw("readline"), #raw("readlines"), #raw("bytes"), #raw("bytearray"),…], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen y tarea 25.],))

== Para empezar

#situacion[Un cuaderno: se puede empezar de cero, añadir al final o solo leer.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("with open(\"prueba.txt\", \"w\") as f:\n    f.write(\"uno\\ndos\\n\")\nwith open(\"prueba.txt\", \"a\") as f:\n    print(\"tres\", file=f)\nwith open(\"prueba.txt\") as f:\n    lineas = f.readlines()\nprint(len(lineas), lineas[-1].strip())\nb = bytearray(b\"abc\")\nb[0] = 65\nprint(b)", talla: 17pt), uncover("2-", respuesta([#raw("3 tres") · #raw("bytearray(b'Abc')")], [65 es el código de #raw("A").])))

== Escribir y volver a leer

#fuente[Ficheros y flujos · 1]

#codigo("with open(\"notas.txt\", \"w\") as f:\n    f.write(\"7\\n\")\n    f.write(\"9\\n\")\ntotal = 0\nwith open(\"notas.txt\") as f:\n    for linea in f:\n        total = total + int(linea)\nprint(total)")

== Las formas de leer

#fuente[Ficheros y flujos · 2]

#codigo("with open(\"lista.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"pan\\nleche\\nhuevos\\n\")\n\nwith open(\"lista.txt\", encoding=\"utf-8\") as f:\n    print(repr(f.read()))          # todo el texto de golpe\n\nwith open(\"lista.txt\", encoding=\"utf-8\") as f:\n    print(repr(f.readline()))      # una línea\n    print(f.readlines())           # las que quedan, en una lista\n\nwith open(\"lista.txt\", encoding=\"utf-8\") as f:\n    print([l.strip() for l in f])  # recorriendo: lo más habitual", talla: 15pt)

== Cuando abrir falla

#fuente[Ficheros y flujos · 3]

#codigo("import errno\n\ntry:\n    with open(\"no_existe.txt\") as f:\n        print(f.read())\nexcept FileNotFoundError as e:\n    print(\"No está:\", e.filename)\n    print(e.errno == errno.ENOENT, e.strerror)")

== Flujos binarios y #raw("bytearray")

#fuente[Ficheros y flujos · 4]

#codigo("datos = bytearray(4)\nfor i in range(len(datos)):\n    datos[i] = 65 + i\nwith open(\"datos.bin\", \"wb\") as f:\n    f.write(datos)\nprint(datos)")

== #raw("pathlib"): las rutas como objetos

#fuente[Ficheros y flujos · 5]

#codigo("print(Path(\"saludo.txt\").is_absolute(), Path(\"saludo.txt\").resolve().is_absolute())\nprint(sorted(f.name for f in Path(\".\").iterdir() if f.suffix in (\".txt\", \".bin\")))", talla: 13pt)

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-25.ipynb", ([El diario. Escribe un programa que añada la línea \"hoy he aprendido…], [Contar líneas. Escribe un programa que cuente cuántas líneas no…], [¿Qué hay en el fichero?], [A prueba de errores],))

== Tarea 25 · Un diario y una copia

#tarea-casa(([Con #raw("pathlib"), crea la carpeta #raw("diario") si no existe.], [Escribe #raw("escribe(fecha, texto)"), que añade el texto al fichero #raw("diario/<fecha>.txt").], [Escribe #raw("entradas()"), que devuelve las fechas con entrada, ordenadas (usa #raw("glob") y #raw("stem")).], [Escribe #raw("lee(fecha)"), que devuelve el texto o #raw("None") si ese día no hay fichero.], [Escribe #raw("copia(origen, destino)"), que copia un fichero binario en bloques de 1024 bytes y devuelve cuántos bytes copió.],), [Dos llamadas a #raw("escribe") con la misma fecha dejan dos líneas en el mismo fichero.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/ficheros/#preguntas-tipo-examen", siguiente: [Sesión 26 · Cadenas a fondo])
