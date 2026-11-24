---
title: Simulacro del examen PCAP
subtitle: 42 preguntas, 65 minutos, como el de verdad
description: "Simulacro del examen PCAP: 42 preguntas, 65 minutos, como el de verdad. Python paso a paso, con visualizadores y diagrama de flujo."
---

## Cómo es el examen

El **PCAP** (*Certified Associate Python Programmer*) es la certificación de nivel asociado del Python Institute, el paso siguiente al PCEP. En su versión vigente, la PCAP-31-04, tiene **42 preguntas** y **65 minutos**, y se aprueba con un **72 %**. Las preguntas se reparten así entre las seis secciones del temario:

| Sección | Qué entra | Peso | Preguntas | Dónde está en el libro |
|---|---|---|---|---|
| 1 | Módulos y paquetes: importar, `sys.path`, paquetes, `pip` | 12 % | 5 | [Módulos y paquetes](12-modulos.md) |
| 2 | Excepciones: jerarquía, `else` y `finally`, propagar, excepciones propias | 12 % | 5 | [Excepciones](13-excepciones.md) |
| 3 | Cadenas: Unicode y UTF-8, comparar, validar, buscar y contar | 9,5 % | 4 | [Cadenas a fondo](19-cadenas-a-fondo.md) |
| 4 | Programación orientada a objetos: atributos, nombres ocultos, herencia, MRO | 28,5 % | 12 | [Clases y objetos](14-clases.md) y [Clases a fondo](18-clases-a-fondo.md) |
| 5 | Construcciones avanzadas y E/S: comprensiones, `match`, lambdas, cierres, ficheros | 24 % | 10 | [Comprensiones](15-comprensiones.md), [Funciones como valores](16-funciones-valores.md) y [Ficheros](17-ficheros.md) |
| 6 | Pruebas, depuración, trabajo en equipo y uso de la IA | 14 % | 6 | [Probar, depurar y trabajar en equipo](20-probar-y-depurar.md) |

Los datos del examen son los del temario oficial publicado por el Python Institute (PCAP-31-04, revisado el 2 de noviembre de 2026). Consulta siempre la página oficial antes de presentarte: el formato puede cambiar.

## El simulacro

Cada vez que empiezas, el simulacro elige 42 preguntas al azar del banco, respetando el reparto por secciones, y baraja el orden de las opciones. Algunas preguntas piden **varias** respuestas, como en el examen real: lo indica el enunciado. Puedes moverte entre preguntas, marcarlas para revisarlas y entregar cuando quieras; si se acaba el tiempo, se entrega solo.

Al final verás la nota, los aciertos de cada sección y la explicación de cada fallo, con la ejecución paso a paso de las preguntas de código. Todas las preguntas son originales: están escritas para este libro y comprobadas ejecutando el código.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcap","modo":"simulacro","titulo":"Simulacro PCAP","etiqueta":"PCAP-31-04","n":42,"minutos":65,"aprobado":72,"idea":"Haz el simulacro en las mismas condiciones que el examen: sin apuntes, sin ejecutar código y de una sentada."}}
```

:::{tip} Cómo sacarle partido
- La sección 4, orientación a objetos, vale casi un tercio del examen: si flojea, empieza por ahí.
- Repasa con las preguntas de final de capítulo, que se corrigen una a una, y repite el simulacro: cada vez salen preguntas distintas.
- Cuando pases del 80 % con holgura, estás listo.
:::
