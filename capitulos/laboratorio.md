---
title: Laboratorio
subtitle: Escribe tu propio programa y míralo pensar, paso a paso
description: "Laboratorio: escribe tu propio programa y míralo pensar, paso a paso. Libro de Python con visualizadores y diagrama de flujo."
---

En el resto del libro los visualizadores enseñan programas que ya están escritos. Aquí el programa lo escribes tú: pulsa **Ejecutar y ver** y recórrelo paso a paso, igual que en los capítulos.

```{anywidget} ../widgets/traza.mjs
{"config": {"tipo": "laboratorio", "titulo": "Laboratorio", "etiqueta": "tu código, paso a paso"}}
```

## Qué vas a ver

- **Cada línea que se ejecuta**, con una frase que explica qué acaba de pasar.
- **La memoria**: las variables con su valor, y cada llamada a una función con sus variables propias.
- **Las listas como casillas**: si tu programa recorre una lista con un `for`, la lista se dibuja y se ve qué casilla se está mirando en cada vuelta.
- **Los objetos**, con sus atributos, y los ficheros que el programa crea, en una carpeta de mentira.
- **La pantalla**, con lo que escribe cada `print`, y los errores con su mensaje de Python.
- **La tabla de traza**, que se va rellenando sola.

## Para que funcione bien

:::{note} Antes de empezar
- **La primera vez tarda unos segundos**: el navegador descarga Python. Después, cada ejecución es casi instantánea.
- **Tu código no sale de tu ordenador.** Python se ejecuta dentro del navegador, y el programa se guarda en él para la próxima visita.
- **Si usas `input()`**, escribe las respuestas en el recuadro *Si tu programa usa input()*, una por línea.
- **En clase, «Proyectar»** pone el laboratorio a pantalla completa y con letra grande. Para salir, el mismo botón o la tecla Esc.
- **Si algo falla**, el laboratorio explica en castellano qué le pasa a la línea, y al final de la ejecución da una pista para el error.
- **Programas cortos**: el laboratorio se detiene a los 1000 pasos, para que un bucle que no termina no bloquee la página. Para programas largos, mejor Colab.
- Solo la biblioteca estándar de Python: `math`, `random`, `csv`… sí; paquetes externos, no.
:::

## El laboratorio completo

Este laboratorio tiene un hermano: [«Mirar y ver · cómo piensa tu código»](https://python.antonychanes.com/mirar-y-ver/). Está organizado en ocho áreas (Variables, Decisiones, Patrones, Funciones, Colecciones, Algoritmos, Física y código, y Tu código) y 22 puestos. Cada puesto trae varias versiones del mismo programa, una con una trampa típica, y un chequeo automático al final.

Los dos funcionan con el mismo Python, que el navegador descarga una sola vez, y se pasan los programas:

- **Abrir en Mirar y ver ↗**, junto a «Ejecutar y ver», lleva tu programa a Mirar y ver: allí lo ves en **cajas y flechas** (qué nombre apunta a qué objeto), puedes **predecir** cada paso antes de darlo o dibujar una **gráfica** con sus variables. Todos los visualizadores del libro tienen el mismo enlace, debajo.
- **Abrir en el laboratorio del libro ↗**, en «Tu código» de Mirar y ver, lo trae de vuelta aquí, donde se ven con más detalle las clases, los ficheros, los generadores y las excepciones con su `except`.

Todos los visualizadores, también el de este laboratorio, tienen el botón **Diagrama de flujo** (o la tecla D): dibuja el diagrama del programa debajo del código y, paso a paso, ilumina el bloque que se acaba de ejecutar, marca con un borde punteado el siguiente y cuenta cuántas veces ha salido cada condición por el Sí y por el No.

## Ideas para practicar

- Copia un ejercicio de cualquier capítulo, **predice** qué hará y compruébalo aquí.
- Mete un error a propósito (un índice que no existe, una división entre cero) y mira en qué paso salta.
- Cambia un `for` por un `while` que haga lo mismo y compara las dos tablas de traza.
