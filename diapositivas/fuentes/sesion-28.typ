// Sesión 28 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 28, tema: "Sesión 28 · Trabajar en equipo y con IA")

#portada([Trabajar en equipo y con IA], subtitulo: [Usar ramas, commits y revisiones, y validar código generado por una IA antes de darlo por bueno.], kicker: "Sesión 28 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 27.], [0:15], [Situación: escribir un trabajo en grupo con un único documento: cada cual en su copia, y alguien revisa antes…], [0:25], [#strong[Predice]. La sangría del #raw("return True") lo cambia todo; y con 2 no se entra en el bucle.], [0:40], [Construcción: repositorio, rama, commit, pull request, revisión; el ciclo pedir, leer, probar y corregir con…], [1:10], [Taller del proyecto: cada equipo abre su primera rama y su primera revisión.], [1:45], [Tarea 28 y hito 3.],))

== Para empezar

#situacion[Escribir un trabajo en grupo con un único documento: cada cual en su copia, y alguien revisa antes de juntar.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#codigo("def es_primo(n):\n    for d in range(2, n):\n        if n % d == 0:\n            return False\n        return True\n\nprint(es_primo(9), es_primo(7), es_primo(2))")

#pause

#respuesta([#raw("True True None")], [#raw("return True") está dentro del bucle: solo se mira el divisor 2. Con 2 el bucle no da ninguna vuelta y la función devuelve #raw("None").])

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-28.ipynb", ([Clasifica el error], [Lee el traceback], [Diseña los casos], [Una prueba con unittest], [Revisa a la IA],))

== Tarea 28 · Validar el código de la IA

#tarea-casa(([Escribe pruebas para #raw("es_primo") con estos casos: 0, 1, 2, 3, 9, 25 y 97.], [Ejecuta las pruebas sobre la versión de la IA y apunta qué casos fallan y por qué.], [Corrige la función. Ampliación: que solo pruebe divisores hasta la raíz cuadrada de #raw("n").], [Escribe en tres líneas cómo lo harías en un equipo: en qué rama, qué diría el commit y qué pediría la revisión.],), [La versión de la IA falla en 5 de los 7 casos.])

== El proyecto

#con-qr("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-2.ipynb", [Cuaderno del proyecto], situacion[#strong[Hito 3 del proyecto.] Ficheros, flujo de git y uso de la IA documentado.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/probar-y-depurar/#preguntas-tipo-examen", siguiente: [Sesión 29 · Taller del proyecto y simulacro PCAP])
