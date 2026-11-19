---
title: Laboratorio
subtitle: Escribe tu propio programa y míralo pensar, paso a paso
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

## Ideas para practicar

- Copia un ejercicio de cualquier capítulo, **predice** qué hará y compruébalo aquí.
- Mete un error a propósito (un índice que no existe, una división entre cero) y mira en qué paso salta.
- Cambia un `for` por un `while` que haga lo mismo y compara las dos tablas de traza.
