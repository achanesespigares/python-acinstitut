---
title: El curso en 30 sesiones
subtitle: De cero al PCEP, y del PCEP al PCAP, en sesiones de dos horas
---

## Para quién es esta guía

Este libro se puede leer por libre, pero también está pensado para un curso presencial: **30 sesiones de 2 horas**, una por semana, repartidas en dos módulos de 30 horas.

- **Módulo 1 · De cero al PCEP** (sesiones 1 a 15): para alumnado que no ha programado nunca. Cubre el temario entero del PCEP.
- **Módulo 2 · Del PCEP al PCAP** (sesiones 16 a 30): orientación a objetos, construcciones avanzadas, ficheros y pruebas. Cubre el temario del PCAP.

Cada módulo termina con un **proyecto práctico** que el alumnado construye en las últimas semanas y expone en la última sesión. Las sesiones no llevan fechas: sirven para cualquier calendario.

## El mapa del curso

| Sesión | Tema | En el libro | Al salir de clase |
|---|---|---|---|
| **1** | Especificar un problema | [Cómo leer](00-como-leer.md) · [Especificación](01-especificacion.md) | tarea 1 |
| **2** | Diseñar el algoritmo | [Algoritmo](02-algoritmo.md) | tarea 2 |
| **3** | Seguir un programa con una traza | [Trazas](03-trazas.md) | tarea 3 |
| **4** | Variables, `input` y `print` | [Variables](04-variables-asignacion.md) · [Cómo funciona Python](21-como-funciona-python.md) §1–2 | tarea 4 |
| **5** | Tipos, literales y operadores | [Tipos de datos](05-tipos-de-datos.md) · [Cómo funciona Python](21-como-funciona-python.md) §3–5 | tarea 5 |
| **6** | Decidir: `if`, `elif`, `else` | [Condicionales](06-condicionales.md) | tarea 6 |
| **7** | Repetir: `while`, `for`, `range` | [Bucles](07-bucles.md) | tarea 7 |
| **8** | `break`, `continue`, centinelas y bucles anidados | [Bucles a fondo](25-bucles-a-fondo.md) | tarea 8 |
| **9** | Recorrer y modificar listas | [Recorrer listas](08-recorrer-listas.md) · [Listas a fondo](22-listas-a-fondo.md) §1–4 | tarea 9 |
| **10** | Tablas, tuplas y conjuntos | [Listas a fondo](22-listas-a-fondo.md) §5 · [Tuplas y conjuntos](23-tuplas-y-conjuntos.md) | tarea 10 |
| **11** | Cadenas y formato | [Cadenas](10-cadenas.md) · [Cadenas y formato](26-cadenas-y-formato.md) | tarea 11 |
| **12** | Diccionarios | [Diccionarios](11-diccionarios.md) | tarea 12 · arranca el proyecto 1 |
| **13** | Funciones | [Funciones](09-funciones.md) · [Funciones a fondo](24-funciones-a-fondo.md) | tarea 13 · hito 2 |
| **14** | Errores, ficheros, CSV y módulos | [Excepciones](13-excepciones.md) §1–2 · [CSV, math y random](27-csv-math-random.md) | hito 3 |
| **15** | **Proyecto 1** y simulacro PCEP | [Proyecto 1](curso-proyecto-1.md) · [Simulacro PCEP](simulacro-pcep.md) | exposición |
| **16** | Módulos y paquetes | [Módulos](12-modulos.md) | tarea 16 |
| **17** | Excepciones a fondo | [Excepciones](13-excepciones.md) §3–6 | tarea 17 |
| **18** | Clases y objetos | [Clases y objetos](14-clases.md) §1–2 | tarea 18 |
| **19** | Atributos de clase, `__str__` y herencia | [Clases y objetos](14-clases.md) §3–4 | tarea 19 |
| **20** | Nombres ocultos y polimorfismo | [Clases a fondo](18-clases-a-fondo.md) §1–3 | tarea 20 |
| **21** | Herencia múltiple, MRO e introspección | [Clases a fondo](18-clases-a-fondo.md) §4–8 | tarea 21 |
| **22** | Comprensiones y `else` de los bucles | [Comprensiones](15-comprensiones.md) §1–5 | tarea 22 |
| **23** | `match` y lambdas | [Comprensiones](15-comprensiones.md) §6 · [Funciones como valores](16-funciones-valores.md) §1–2 | tarea 23 |
| **24** | Cierres y generadores | [Funciones como valores](16-funciones-valores.md) §3–4 | tarea 24 |
| **25** | Ficheros, bytes y rutas | [Ficheros y flujos](17-ficheros.md) | tarea 25 |
| **26** | Cadenas a fondo | [Cadenas a fondo](19-cadenas-a-fondo.md) | tarea 26 · arranca el proyecto 2 |
| **27** | Probar y depurar | [Probar y depurar](20-probar-y-depurar.md) §1–4 | tarea 27 · hito 2 |
| **28** | Trabajar en equipo y con IA | [Probar y depurar](20-probar-y-depurar.md) §5–6 | tarea 28 · hito 3 |
| **29** | Taller del proyecto y simulacro PCAP | [Proyecto 2](curso-proyecto-2.md) · [Simulacro PCAP](simulacro-pcap.md) | hito 4 |
| **30** | **Proyecto 2**: exposiciones | [Proyecto 2](curso-proyecto-2.md) | exposición |

Cuando se cita «§ 3» de un capítulo, se refiere al movimiento 3 de su construcción: una sesión puede cubrir solo una parte de un capítulo largo.

El detalle de cada sesión está en [Módulo 1](curso-modulo-1.md) y [Módulo 2](curso-modulo-2.md). Los proyectos, con sus hitos, su rúbrica y una solución de referencia, en [Proyecto 1](curso-proyecto-1.md) y [Proyecto 2](curso-proyecto-2.md).

## Cómo es una sesión

Todas las sesiones siguen el mismo esquema, el del método de este libro: primero una situación cotidiana con respuesta obvia, después la pregunta que la generaliza, y solo entonces el código.

| Tiempo | Momento | Qué se hace |
|---|---|---|
| 0:00 – 0:15 | **Punto de partida** | Se corrige en voz alta la tarea anterior y se plantea la situación cotidiana del día. |
| 0:15 – 0:40 | **Predice y mira** | Cada alumno escribe en papel qué hará el programa del día; después se proyecta el visualizador y se comprueba paso a paso. |
| 0:40 – 1:20 | **Construcción** | Se escribe el código en Colab entre todos, a partir de la idea del capítulo. |
| 1:20 – 1:45 | **Práctica** | Ejercicios del capítulo, por parejas. |
| 1:45 – 2:00 | **Cierre** | Preguntas tipo examen del capítulo, en directo, y presentación de la tarea semiguiada. |

:::{tip} Predecir antes de ejecutar
La regla de oro del curso: **nunca se ejecuta un programa sin haber predicho antes qué hará**. Si la predicción falla, el error está en el modelo mental, y eso es justo lo que el visualizador ayuda a corregir. Equivocarse al predecir no resta: es la mejor información de la clase.
:::

## Las herramientas

- **El libro**, abierto en el navegador: cada capítulo tiene sus visualizadores, sus ejercicios con solucionario y sus preguntas tipo examen.
- **Google Colab** (o Jupyter) para escribir y ejecutar el código propio. Se copia el código de las celdas del libro en un cuaderno nuevo. El libro también puede ejecutar sus celdas en el navegador, excepto `input()`; para los programas que piden datos, Colab.
- **Un cuaderno de clase** por alumno, en Colab, con una sección por sesión: lo que se predijo, lo que pasó y las tareas.

## Las tareas semiguiadas

Cada sesión termina con una **tarea semiguiada**: un problema pequeño, del tamaño de lo visto en clase, partido en pasos y con una comprobación final («con estos datos, tiene que salir esto»). La idea es que el alumno nunca se quede bloqueado delante de la pantalla en blanco, pero que el código lo escriba él.

Las soluciones están al final de cada módulo. Se corrigen al principio de la sesión siguiente, en el punto de partida.

## Evaluación

Una propuesta, para adaptar:

| Qué | Peso |
|---|---|
| Tareas semiguiadas, entregadas a tiempo y funcionando | 25 % |
| Proyecto del módulo (código, documentación y exposición) | 45 % |
| Simulacro de examen al final del módulo | 30 % |

El simulacro es el del libro: se puede hacer en clase, en las mismas condiciones que el examen oficial, y la nota sale al momento.
