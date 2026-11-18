---
title: Simulacro del examen PCEP
subtitle: 35 preguntas, 50 minutos, como el de verdad
---

## Cómo es el examen

El **PCEP** (*Certified Entry-Level Python Programmer*) es la certificación de entrada del Python Institute. En su versión vigente, la PCEP-30-03, tiene **35 preguntas** y **50 minutos**, y se aprueba con un **70 %**. Las preguntas se reparten así entre las cinco secciones del temario:

| Sección | Qué entra | Peso | Preguntas | Dónde está en el libro |
|---|---|---|---|---|
| 1 | Fundamentos: intérprete, literales, variables, operadores, `input` y `print` | 17 % | 6 | Bloque 1 y [Cómo funciona Python](21-como-funciona-python.md) |
| 2 | Control de flujo: `if`, `while`, `for`, `range`, `break`, `continue` | 23 % | 8 | Bloque 2 y [Bucles a fondo](25-bucles-a-fondo.md) |
| 3 | Colecciones: listas, tuplas, conjuntos, diccionarios y cadenas | 26 % | 9 | Bloque 3 y bloque 3+ |
| 4 | Funciones y excepciones | 20 % | 7 | [Funciones](09-funciones.md), [Funciones a fondo](24-funciones-a-fondo.md) y [Excepciones](13-excepciones.md) |
| 5 | Ficheros y módulos: ficheros de texto, CSV, `math` y `random` | 14 % | 5 | [CSV, math y random](27-csv-math-random.md), [Módulos](12-modulos.md) y [Ficheros](17-ficheros.md) |

Los datos del examen son los del temario oficial publicado por el Python Institute (PCEP-30-03, revisado el 2 de noviembre de 2026). Consulta siempre la página oficial antes de presentarte: el formato puede cambiar.

## El simulacro

Cada vez que empiezas, el simulacro elige 35 preguntas al azar del banco, respetando el reparto por secciones, y baraja el orden de las opciones. Puedes moverte entre preguntas, marcarlas para revisarlas y entregar cuando quieras; si se acaba el tiempo, se entrega solo.

Al final verás la nota, los aciertos de cada sección y la explicación de cada fallo, con la ejecución paso a paso de las preguntas de código. Todas las preguntas son originales: están escritas para este libro y comprobadas ejecutando el código.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","modo":"simulacro","titulo":"Simulacro PCEP","etiqueta":"PCEP-30-03","n":35,"minutos":50,"aprobado":70,"idea":"Haz el simulacro en las mismas condiciones que el examen: sin apuntes, sin ejecutar código y de una sentada."}}
```

:::{tip} Cómo sacarle partido
- Haz el primer simulacro **antes** de repasar: te dirá qué secciones flojean.
- Repasa esas secciones con las preguntas de final de capítulo, que se corrigen una a una.
- Repite el simulacro: cada vez salen preguntas distintas. Cuando pases del 80 % con holgura, estás listo.
:::
