// Sesión 12 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 12, tema: "Sesión 12 · Diccionarios")

#portada([Diccionarios], subtitulo: [Guardar datos por nombre en vez de por posición, y contar con un diccionario.], kicker: "Sesión 12 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 11.], [0:15], [Situación: una agenda de teléfonos: se busca por nombre, no por número de página.], [0:25], [#strong[Predice] y visualizador.], [0:40], [Construcción: claves y valores, #raw("get"), #raw("items"), recorrer, contar.], [1:10], [Ejercicios del capítulo.], [1:35], [Presentación del proyecto 1: el enunciado, los hitos y la rúbrica.], [1:50], [Tarea 12 y primer hito.],))

== Para empezar

#situacion[Una agenda de teléfonos: se busca por nombre, no por número de página.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("stock = {\"pan\": 3, \"leche\": 0}\nstock[\"huevos\"] = 12\nstock[\"pan\"] -= 1\nprint(stock.get(\"queso\", \"no hay\"), len(stock))\nfor k, v in stock.items():\n    if v == 0:\n        print(k)")

#pause

#respuesta([#raw("no hay 3") · #raw("leche")], [#raw("get") no falla si la clave no existe.])

== Contar cada letra

#fuente[Diccionarios · 1]

#codigo("texto = \"abracadabra\"\ncuenta = {}\nfor letra in texto:\n    if letra in cuenta:\n        cuenta[letra] = cuenta[letra] + 1\n    else:\n        cuenta[letra] = 1\nprint(cuenta)")

== Las notas de la clase

#fuente[Diccionarios · 2]

#codigo("notas = {\"Ana\": 7, \"Biel\": 4, \"Carla\": 9}\nnotas[\"Biel\"] = 5\nnotas[\"Dani\"] = 6\naprobados = 0\nfor nombre in notas:\n    if notas[nombre] >= 5:\n        aprobados = aprobados + 1\nprint(aprobados)")

== Métodos útiles

#fuente[Diccionarios · 3]

#codigo("notas = {\"Ana\": 7, \"Biel\": 5, \"Carla\": 9}\nprint(notas.keys())              # las claves\nprint(notas.values())            # los valores\nprint(notas.get(\"Zoe\", \"sin nota\"))   # get no da error si la clave no está\nfor nombre, nota in notas.items():    # claves y valores a la vez\n    print(nombre, \"→\", nota)", talla: 13pt)

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-12.ipynb", ([¿Qué imprime?], [Contar palabras], [La mejor nota. Con notas = {\"Ana\": 7, \"Biel\": 5, \"Carla\": 9}, escribe…],))

== Tarea 12 · Frecuencia de palabras

#tarea-casa(([Guarda un texto en una variable. Usa este: #raw("El perro come. ¿El gato come? El perro duerme, y el gato también come.")], [Pásalo a minúsculas y quita los signos #raw(".,;:!?¿¡") con #raw("replace") dentro de un bucle.], [Parte el texto en palabras con #raw("split").], [Cuenta cada palabra con un diccionario y #raw("get(palabra, 0)").], [Recorre el diccionario para encontrar la palabra más repetida.],), [La más repetida es «el», 4 veces; «come» aparece 3.])

== El proyecto

#con-qr("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-1.ipynb", [Cuaderno del proyecto], situacion[#strong[Hito 1 del proyecto.] La especificación y el algoritmo del gestor de notas (ver Proyecto 1).])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/diccionarios/#preguntas-tipo-examen", siguiente: [Sesión 13 · Funciones])
