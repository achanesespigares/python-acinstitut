// Sesión 1 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 1, tema: "Sesión 1 · Especificar un problema")

#portada([Especificar un problema], subtitulo: [Decir con precisión qué entra, qué sale y qué se supone antes de escribir una sola línea.], kicker: "Sesión 1 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Presentación del curso, del libro y de Colab.], [0:15], [Situación: pedir a alguien que nos compre «pan» por teléfono.], [0:30], [Predice: las tres líneas de arriba. Se ejecutan en Colab. La diferencia entre #raw("2 + 3") y #raw("\"2 + 3\"") es la…], [0:45], [Construcción: entradas, salida, precondición y ejemplos de prueba, con el capítulo.], [1:20], [Ejercicios del capítulo, por parejas: cada pareja especifica y la de al lado busca un caso que la rompa.], [1:45], [Cierre y presentación de la tarea 1.],))

== Para empezar

#situacion[Pedir a alguien que nos compre «pan» por teléfono. ¿Qué puede salir mal? Cuántas barras, de qué tipo, qué hacer si no hay.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("print(\"Hola\")\nprint(2 + 3)\nprint(\"2 + 3\")")

#pause

#respuesta([#raw("Hola") · #raw("5") · #raw("2 + 3")], [Entre comillas es texto: Python no lo calcula.])

== De los ejemplos a las pruebas

#fuente[Especificar el problema · 2]

#codigo("def media(notas):\n    return sum(notas) / len(notas)\n\nprint(media([5, 7]) == 6.0)\nprint(media([10]) == 10.0)\nprint(abs(media([4, 5, 5]) - 4.6667) < 0.001)")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-01.ipynb", ([Especifica este encargo: «Di si un número es par».], [Encuentra el hueco], [Casos límite. Para el encargo «Calcula la nota media quitando la peor…],))

== Tarea 1 · El precio con descuento

#tarea-casa(([Escribe las #strong[entradas]: qué datos necesita el programa y de qué tipo son.], [Escribe la #strong[salida]: qué devuelve y en qué unidad.], [Escribe las #strong[precondiciones]: qué valores no tienen sentido (¿un descuento del 150 %?).], [Escribe #strong[tres ejemplos de prueba] con su resultado, calculado a mano.], [Busca la #strong[grieta]: un caso en el que la especificación no dice qué hacer.],), [Con precio 100 € y descuento 20 %, tu especificación debe dar 80 €.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/especificacion/#preguntas-tipo-examen", siguiente: [Sesión 2 · Diseñar el algoritmo])
