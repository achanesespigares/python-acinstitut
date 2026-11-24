// Sesión 6 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 6, tema: "Sesión 6 · Decidir: if, elif, else")

#portada([Decidir: #raw("if"), #raw("elif"), #raw("else")], subtitulo: [Elegir entre varios caminos y saber exactamente cuál se toma.], kicker: "Sesión 6 · Módulo 1", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 5.], [0:15], [Situación: un semáforo, y un cruce con dos semáforos seguidos.], [0:25], [#strong[Predice]. ¿Por qué no sale «Sobresaliente» con un 9,5? (Se cambia la nota y se vuelve a predecir.)], [0:45], [Construcción: #raw("if") encadenados frente a #raw("elif"), operadores lógicos, comparaciones encadenadas.], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen y tarea 6.],))

== Para empezar

#situacion[Un semáforo, y un cruce con dos semáforos seguidos. No es lo mismo dos preguntas que una pregunta con dos respuestas.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("nota = 7.5\nif nota >= 5:\n    print(\"Aprobado\")\nif nota >= 7:\n    print(\"Notable\")\nelif nota >= 9:\n    print(\"Sobresaliente\")\nelse:\n    print(\"Suficiente\")", talla: 17pt), uncover("2-", respuesta([#raw("Aprobado") · #raw("Notable")], [Son dos #raw("if") independientes. Con 9,5 tampoco sale Sobresaliente: el #raw("elif") nunca se alcanza porque 9,5 ≥ 7 ya es cierto.])))

== ¿Aprobado o suspenso?

#fuente[Condicionales · 1]

#codigo("nota = 6.5\nif nota >= 5:\n    resultado = \"aprobado\"\nelse:\n    resultado = \"suspenso\"\nprint(resultado)")

== La calificación: varias ramas

#fuente[Condicionales · 2]

#codigo("nota = 8.2\nif nota < 5:\n    calificacion = \"Insuficiente\"\nelif nota < 7:\n    calificacion = \"Aprobado\"\nelif nota < 9:\n    calificacion = \"Notable\"\nelse:\n    calificacion = \"Sobresaliente\"\nprint(calificacion)")

== Cuando el orden falla

#fuente[Condicionales · 3]

#codigo("nota = 9.5\ncalificacion = \"?\"\nif nota >= 5:\n    calificacion = \"Aprobado\"\nelif nota >= 9:\n    calificacion = \"Sobresaliente\"\nprint(calificacion)")

== ¿Es bisiesto?

#fuente[Condicionales · 4]

#codigo("año = 1900\nif año % 400 == 0:\n    bisiesto = True\nelif año % 100 == 0:\n    bisiesto = False\nelif año % 4 == 0:\n    bisiesto = True\nelse:\n    bisiesto = False\nprint(año, \"bisiesto:\", bisiesto)")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-06.ipynb", ([¿Qué imprime? con x = 7:], [Par o impar. Escribe un programa que, dado n, imprima \"par\" o \"impar\".], [Corrige el orden],))

== Tarea 6 · Calificación con validación

#tarea-casa(([Pide una nota con decimales.], [Si no está entre 0 y 10, escribe #raw("Nota no válida") y no sigas.], [Si es válida, escribe la calificación: Suspenso (\< 5), Suficiente (\< 6), Bien (\< 7), Notable (\< 9) o Sobresaliente.], [Ordena las condiciones para que cada una solo tenga que comprobar un límite.], [Prueba los bordes: 4,99, 5, 9, 10 y 10,5.],), [Un 6,5 es Bien y un 9 es Sobresaliente.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/condicionales/#preguntas-tipo-examen", siguiente: [Sesión 7 · Repetir: #raw("while"), #raw("for") y #raw("range")])
