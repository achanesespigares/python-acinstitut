// Sesión 27 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 27, tema: "Sesión 27 · Probar y depurar")

#portada([Probar y depurar], subtitulo: [Leer un traceback de abajo arriba, escribir pruebas unitarias y buscar el porqué de un error con método.], kicker: "Sesión 27 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 26.], [0:15], [Situación: una avería en cadena: el coche no arranca porque la batería no carga porque la correa está rota.], [0:25], [#strong[Predice] y visualizador: el traceback enseña la pila de llamadas al revés.], [0:45], [Construcción: #raw("assert"), tracebacks, #raw("unittest"), depuración por hipótesis.], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen, tarea 27 y hito 2.],))

== Para empezar

#situacion[Una avería en cadena: el coche no arranca porque la batería no carga porque la correa está rota.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("def media(lista):\n    return sum(lista) / len(lista)\n\ndef informe(datos):\n    return f\"Media: {media(datos):.1f}\"\n\nprint(informe([4, 6]))\nprint(informe([]))", talla: 17pt), uncover("2-", respuesta([#raw("Media: 5.0") y después #raw("ZeroDivisionError")], [El traceback acaba en la línea de #raw("media"), la división; la causa está en quien la llamó con una lista vacía.])))

== #raw("assert"): una comprobación en una línea

#fuente[Probar, depurar y trabajar en equipo · 1]

#codigo("def media(notas):\n    assert len(notas) > 0, \"la lista está vacía\"\n    return sum(notas) / len(notas)\n\nprint(media([6, 8]))\nprint(media([]))")

== Pruebas unitarias con #raw("unittest")

#fuente[Probar, depurar y trabajar en equipo · 3]

#codigo("import unittest\n\ndef media(notas):\n    if len(notas) == 0:\n        raise ValueError(\"la lista está vacía\")\n    return sum(notas) / len(notas)\n\nclass PruebasMedia(unittest.TestCase):\n    def test_caso_tipico(self):\n        self.assertEqual(media([6, 8]), 7)\n\n    def test_un_solo_valor(self):            # caso límite\n        self.assertEqual(media([5]), 5)\n…", talla: 17pt)

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-27.ipynb", ([Clasifica el error], [Lee el traceback], [Diseña los casos], [Una prueba con unittest], [Revisa a la IA],))

== Tarea 27 · Pruebas para la calificación

#tarea-casa(([Toma #raw("calificacion(nota)") de la tarea 13 y cámbiala para que #strong[lance] #raw("ValueError") si la nota no está entre 0 y 10, en…], [Escribe una clase #raw("PruebaCalificacion(unittest.TestCase)") con tres pruebas: los bordes (5, 9, 10), justo por debajo…], [En Colab, ejecútalas con #raw("unittest.main(argv=[\"ignorado\"], exit=False)").], [Rompe a propósito la función (cambia un #raw("<") por #raw("<=")) y mira qué prueba falla.],), [Las tres pruebas pasan con la función correcta; con #raw("nota <= 5") falla la de los bordes.])

== El proyecto

#con-qr("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-2.ipynb", [Cuaderno del proyecto], situacion[#strong[Hito 2 del proyecto.] Clases, excepciones y pruebas del proyecto.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/probar-y-depurar/#preguntas-tipo-examen", siguiente: [Sesión 28 · Trabajar en equipo y con IA])
