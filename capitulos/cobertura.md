---
title: El temario oficial, objetivo a objetivo
subtitle: Dónde cubre este libro cada punto del PCEP y del PCAP
description: "El temario oficial, objetivo a objetivo: dónde cubre este libro cada punto del PCEP y del PCAP. Python paso a paso, con visualizadores y diagrama de flujo."
---

El Python Institute publica el temario de cada examen como una lista de **objetivos** numerados. Esta página los recorre todos, resumidos en castellano, y dice en qué capítulos del libro se trabaja cada uno.

Los temarios son los de la **versión 1.5**, revisada por el Python Institute el **2 de noviembre de 2026**. El texto oficial completo, en inglés, está en [el temario del PCEP](https://pythoninstitute.org/pcep-exam-syllabus) y [el temario del PCAP](https://pythoninstitute.org/pcap-exam-syllabus).

:::{note} Cómo se comprueba
La página la escribe el script `herramientas/cobertura.py`. Para cada objetivo, busca en los capítulos indicados los términos que ese objetivo exige: ✓ si están todos, ◐ si falta alguno (y dice cuál) y ✗ si no hay ninguno. Si un capítulo cambia, se vuelve a ejecutar y la página se pone al día sola.
:::

## De un vistazo

**PCEP-30-03** · 35 de 35 objetivos cubiertos

| Sección | Preguntas del examen | Peso | Objetivos cubiertos | Preguntas en el banco |
|---|---|---|---|---|
| 1 · Fundamentos de programación y de Python | 6 | 17 % | 6 de 6 | 18 |
| 2 · Control del flujo: condicionales y bucles | 8 | 23 % | 8 de 8 | 17 |
| 3 · Colecciones: listas, tuplas, conjuntos, diccionarios y cadenas | 9 | 26 % | 9 de 9 | 31 |
| 4 · Funciones y excepciones | 7 | 20 % | 7 de 7 | 16 |
| 5 · Ficheros e importación de módulos | 5 | 14 % | 5 de 5 | 14 |

**PCAP-31-04** · 42 de 42 objetivos cubiertos

| Sección | Preguntas del examen | Peso | Objetivos cubiertos | Preguntas en el banco |
|---|---|---|---|---|
| 1 · Módulos y paquetes | 5 | 12 % | 5 de 5 | 14 |
| 2 · Excepciones | 5 | 12 % | 5 de 5 | 13 |
| 3 · Cadenas | 4 | 9,5 % | 4 de 4 | 10 |
| 4 · Programación orientada a objetos | 12 | 28,5 % | 12 de 12 | 25 |
| 5 · Construcciones avanzadas y entrada y salida | 10 | 24 % | 10 de 10 | 24 |
| 6 · Pruebas, depuración, trabajo en equipo e IA | 6 | 14 % | 6 de 6 | 13 |

## PCEP-30-03

35 preguntas en 50 minutos; se aprueba con el 70 %. Puedes practicarlo entero en el [simulacro](simulacro-pcep.md).

### Sección 1 · Fundamentos de programación y de Python

6 preguntas del examen (17 %) · 18 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **1.1.1** | Cómo es un lenguaje y cómo se ejecuta: léxico, sintaxis, semántica, errores, intérprete y compilador | [Cómo funciona Python](21-como-funciona-python.md) | ✓ |
| **1.2.1** | Reglas de estructura: palabras reservadas, expresiones e instrucciones, sangría, comentarios | [Cómo funciona Python](21-como-funciona-python.md) · [Condicionales](06-condicionales.md) | ✓ |
| **1.3.1** | Literales `int`, `float`, `str` y `bool`, y los límites de la coma flotante | [Tipos de datos](05-tipos-de-datos.md) · [Cómo funciona Python](21-como-funciona-python.md) | ✓ |
| **1.3.2** | Variables e identificadores, con las reglas de nombres y la guía PEP 8 | [Variables y asignación](04-variables-asignacion.md) · [Cómo funciona Python](21-como-funciona-python.md) | ✓ |
| **1.4.1** | Operadores numéricos, de cadenas, de asignación, lógicos y de comparación, y su prioridad | [Tipos de datos](05-tipos-de-datos.md) · [Cómo funciona Python](21-como-funciona-python.md) | ✓ |
| **1.4.2** | Entrada y salida por consola con `print()` e `input()`, y conversión de tipos | [Variables y asignación](04-variables-asignacion.md) · [Tipos de datos](05-tipos-de-datos.md) · [Cómo funciona Python](21-como-funciona-python.md) | ✓ |

### Sección 2 · Control del flujo: condicionales y bucles

8 preguntas del examen (23 %) · 17 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **2.1.1** | `if` e `if-else` | [Condicionales](06-condicionales.md) | ✓ |
| **2.1.2** | Cadenas `if-elif-else` y el orden de las ramas | [Condicionales](06-condicionales.md) | ✓ |
| **2.1.3** | Condiciones compuestas y anidadas | [Condicionales](06-condicionales.md) | ✓ |
| **2.2.1** | `while`, valores centinela, bucles infinitos y el operador morsa | [Bucles while y for](07-bucles.md) · [Bucles a fondo](25-bucles-a-fondo.md) | ✓ |
| **2.2.2** | `for` y el recorrido de iterables con `in` | [Bucles while y for](07-bucles.md) · [Recorrer listas](08-recorrer-listas.md) | ✓ |
| **2.2.3** | `range()` con inicio, fin y paso | [Bucles while y for](07-bucles.md) | ✓ |
| **2.2.4** | Bucles anidados y estructuras combinadas | [Bucles a fondo](25-bucles-a-fondo.md) | ✓ |
| **2.2.5** | `break`, `continue` y `pass` | [Bucles a fondo](25-bucles-a-fondo.md) | ✓ |

### Sección 3 · Colecciones: listas, tuplas, conjuntos, diccionarios y cadenas

9 preguntas del examen (26 %) · 31 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **3.1.1** | Crear listas, índices positivos y negativos, rebanadas y copias | [Recorrer listas](08-recorrer-listas.md) · [Listas a fondo](22-listas-a-fondo.md) | ✓ |
| **3.1.2** | Modificar, buscar, ordenar y recorrer listas; `in` y `len()` | [Recorrer listas](08-recorrer-listas.md) · [Listas a fondo](22-listas-a-fondo.md) | ✓ |
| **3.1.3** | Listas multidimensionales | [Listas a fondo](22-listas-a-fondo.md) | ✓ |
| **3.2.1** | Tuplas: inmutabilidad, anidamiento y diferencias con las listas | [Tuplas y conjuntos](23-tuplas-y-conjuntos.md) | ✓ |
| **3.3.1** | Conjuntos: crear, añadir, quitar y pertenencia | [Tuplas y conjuntos](23-tuplas-y-conjuntos.md) | ✓ |
| **3.4.1** | Diccionarios: acceso, cambios, borrado y recorrido con `keys()`, `values()` e `items()` | [Diccionarios](11-diccionarios.md) | ✓ |
| **3.5.1** | Construir cadenas: comillas, escapes, multilínea, índices, rebanadas e inmutabilidad | [Cadenas](10-cadenas.md) · [Cadenas y formato](26-cadenas-y-formato.md) | ✓ |
| **3.5.2** | Transformar cadenas: mayúsculas, `find()`, `split()`, `join()`, `strip()`, `replace()` | [Cadenas](10-cadenas.md) · [Cadenas a fondo](19-cadenas-a-fondo.md) · [Cadenas y formato](26-cadenas-y-formato.md) | ✓ |
| **3.5.3** | Dar formato: f-strings, `format()` y el operador `%` | [Cadenas y formato](26-cadenas-y-formato.md) | ✓ |

### Sección 4 · Funciones y excepciones

7 preguntas del examen (20 %) · 16 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **4.1.1** | Definir y llamar funciones propias | [Funciones](09-funciones.md) | ✓ |
| **4.1.2** | Valores devueltos, `None` y devolver varios valores | [Funciones](09-funciones.md) · [Funciones a fondo](24-funciones-a-fondo.md) | ✓ |
| **4.1.3** | Parámetros, argumentos, valores por defecto y argumentos con nombre | [Funciones](09-funciones.md) · [Funciones a fondo](24-funciones-a-fondo.md) | ✓ |
| **4.1.4** | `*args` y `**kwargs` | [Funciones a fondo](24-funciones-a-fondo.md) | ✓ |
| **4.1.5** | Ámbito local y global, nombres que se tapan y la instrucción `global` | [Funciones](09-funciones.md) · [Funciones a fondo](24-funciones-a-fondo.md) | ✓ |
| **4.2.1** | Excepciones básicas de Python y cuándo saltan | [Excepciones](13-excepciones.md) | ✓ |
| **4.2.2** | Atender excepciones con `try` y `except` | [Excepciones](13-excepciones.md) | ✓ |

### Sección 5 · Ficheros e importación de módulos

5 preguntas del examen (14 %) · 14 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **5.1.1** | Ficheros de texto: modos `r`, `w` y `a`, y la instrucción `with` | [Ficheros y flujos](17-ficheros.md) · [CSV, math y random](27-csv-math-random.md) | ✓ |
| **5.1.2** | Ficheros CSV con el módulo `csv`: `reader()` y `writer()` | [CSV, math y random](27-csv-math-random.md) | ✓ |
| **5.2.1** | Importar y usar módulos | [Módulos y paquetes](12-modulos.md) · [CSV, math y random](27-csv-math-random.md) | ✓ |
| **5.2.2** | El módulo `math`: `ceil()`, `floor()`, `trunc()`, `sqrt()` | [CSV, math y random](27-csv-math-random.md) | ✓ |
| **5.2.3** | El módulo `random`: `random()`, `seed()`, `choice()`, `sample()` | [CSV, math y random](27-csv-math-random.md) | ✓ |

## PCAP-31-04

42 preguntas en 65 minutos; se aprueba con el 72 %. Puedes practicarlo entero en el [simulacro](simulacro-pcap.md).

### Sección 1 · Módulos y paquetes

5 preguntas del examen (12 %) · 14 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **1.1.1** | Formas de `import`, alias, `import *`, nombres cualificados y nombres que chocan | [Módulos y paquetes](12-modulos.md) | ✓ |
| **1.1.2** | `dir()`, la ruta de búsqueda `sys.path` y los fallos al importar | [Módulos y paquetes](12-modulos.md) | ✓ |
| **1.2.1** | Módulos propios, `if __name__ == "__main__"`, `__pycache__` e importaciones circulares | [Módulos y paquetes](12-modulos.md) | ✓ |
| **1.2.2** | Paquetes y subpaquetes, el papel de `__init__.py` y los errores al importarlos | [Módulos y paquetes](12-modulos.md) | ✓ |
| **1.3.1** | PyPI, `pip` y `requirements.txt` | [Módulos y paquetes](12-modulos.md) | ✓ |

### Sección 2 · Excepciones

5 preguntas del examen (12 %) · 13 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **2.1.1** | Orden de los `except`, varios tipos a la vez, el objeto excepción y qué rama atiende | [Excepciones](13-excepciones.md) | ✓ |
| **2.1.2** | `else` y `finally` con `try` y `except` | [Excepciones](13-excepciones.md) | ✓ |
| **2.1.3** | La jerarquía de excepciones, `BaseException` frente a `Exception`, y `args` | [Excepciones](13-excepciones.md) | ✓ |
| **2.1.4** | Lanzar excepciones, volver a lanzarlas y cómo se propagan entre funciones | [Excepciones](13-excepciones.md) | ✓ |
| **2.2.1** | Definir, lanzar y organizar excepciones propias | [Excepciones](13-excepciones.md) | ✓ |

### Sección 3 · Cadenas

4 preguntas del examen (9,5 %) · 10 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **3.1.1** | ASCII, Unicode, UTF-8, `str` frente a `bytes`, `ord()` y `chr()` | [Cadenas a fondo](19-cadenas-a-fondo.md) | ✓ |
| **3.2.1** | Inmutabilidad, cadenas nuevas, igualdad y orden entre cadenas | [Cadenas a fondo](19-cadenas-a-fondo.md) | ✓ |
| **3.2.2** | Los métodos `is…()` y cómo combinarlos | [Cadenas a fondo](19-cadenas-a-fondo.md) | ✓ |
| **3.2.3** | Buscar: `index`, `find`, `rindex`, `rfind`, `count`, `startswith`, `endswith` y `sorted()` | [Cadenas a fondo](19-cadenas-a-fondo.md) | ✓ |

### Sección 4 · Programación orientada a objetos

12 preguntas del examen (28,5 %) · 25 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **4.1.1** | Los cuatro pilares: abstracción, encapsulación, herencia y polimorfismo | [Clases y objetos](14-clases.md) · [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.1.2** | Clases, objetos, atributos, métodos y cómo se relacionan | [Clases y objetos](14-clases.md) | ✓ |
| **4.2.1** | Variables de clase y de instancia, y atributos que se tapan | [Clases y objetos](14-clases.md) · [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.2.2** | `__dict__` y la desfiguración de nombres | [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.3.1** | Métodos de instancia, `self`, argumentos y `__str__()` | [Clases y objetos](14-clases.md) · [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.4.1** | `hasattr()`, `getattr()` y la búsqueda de atributos por la jerarquía | [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.4.2** | Los metadatos de una clase: `__name__`, `__module__` y `__bases__` | [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.5.1** | Herencia simple, sobrescribir métodos y `super()` | [Clases y objetos](14-clases.md) · [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.5.2** | Herencia múltiple, el MRO, el rombo y `super()` cooperativo | [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.5.3** | `isinstance()`, `is` frente a `==`, y polimorfismo | [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.6.1** | `__init__()`, atributos, valores por defecto y `super().__init__()` | [Clases y objetos](14-clases.md) · [Clases a fondo](18-clases-a-fondo.md) | ✓ |
| **4.6.2** | Argumentos con nombre, validar con excepciones y valores por defecto mutables | [Clases a fondo](18-clases-a-fondo.md) | ✓ |

### Sección 5 · Construcciones avanzadas y entrada y salida

10 preguntas del examen (24 %) · 24 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **5.1.1** | Comprensiones de lista, conjunto y diccionario, con filtros y expresiones condicionales | [Comprensiones, for…else y match](15-comprensiones.md) | ✓ |
| **5.1.2** | Comprensiones anidadas, orden de los `for` y aplanar listas | [Comprensiones, for…else y match](15-comprensiones.md) | ✓ |
| **5.2.1** | `match-case` y sus diferencias con `if-elif-else` | [Comprensiones, for…else y match](15-comprensiones.md) | ✓ |
| **5.2.2** | El `else` de `while` y de `for`, y cuándo se ejecuta | [Comprensiones, for…else y match](15-comprensiones.md) | ✓ |
| **5.3.1** | Funciones `lambda` y cuándo es mejor una función con nombre | [Funciones como valores](16-funciones-valores.md) | ✓ |
| **5.3.2** | `map()` y `filter()` como iteradores, y convertir su resultado | [Funciones como valores](16-funciones-valores.md) | ✓ |
| **5.3.3** | Cierres, funciones que devuelven funciones y fábricas | [Funciones como valores](16-funciones-valores.md) | ✓ |
| **5.4.1** | Flujos estándar (`sys.stdin`, `sys.stdout`, `sys.stderr`), modo texto y binario, modos de apertura | [Ficheros y flujos](17-ficheros.md) | ✓ |
| **5.4.2** | Ficheros con `with`, leer y escribir, `bytearray` y excepciones de ficheros | [Ficheros y flujos](17-ficheros.md) | ✓ |
| **5.4.3** | `pathlib`: rutas, recorrer carpetas y leer y escribir texto y `bytes` | [Ficheros y flujos](17-ficheros.md) | ✓ |

### Sección 6 · Pruebas, depuración, trabajo en equipo e IA

6 preguntas del examen (14 %) · 13 preguntas en el banco del libro

| Objetivo | Qué pide | Dónde está en el libro | |
|---|---|---|---|
| **6.1.1** | Pruebas unitarias, casos de prueba, `assert`, aislamiento y regresiones | [Probar, depurar y trabajar en equipo](20-probar-y-depurar.md) | ✓ |
| **6.1.2** | Errores de sintaxis, de ejecución y de lógica; leer tracebacks y comprobar arreglos | [Probar, depurar y trabajar en equipo](20-probar-y-depurar.md) | ✓ |
| **6.2.1** | Repositorios compartidos, ramas, commits, pull requests y conflictos | [Probar, depurar y trabajar en equipo](20-probar-y-depurar.md) | ✓ |
| **6.2.2** | Issues, documentación, revisiones de código, pruebas automáticas e integración continua | [Probar, depurar y trabajar en equipo](20-probar-y-depurar.md) | ✓ |
| **6.3.1** | Pedir a la IA con contexto y restricciones, y evaluar y afinar lo que devuelve | [Probar, depurar y trabajar en equipo](20-probar-y-depurar.md) | ✓ |
| **6.3.2** | Revisión humana, probar el código de la IA, verificar referencias, proteger datos y responsabilidad | [Probar, depurar y trabajar en equipo](20-probar-y-depurar.md) | ✓ |

## Lo que no entra en el libro

Nada del temario oficial se queda fuera: todos los objetivos tienen al menos un capítulo. Lo que el libro **añade** por su cuenta, porque ayuda a entender, es la parte de pensar antes de programar (especificación, algoritmo y trazas), los generadores y el laboratorio.
