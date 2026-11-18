---
title: Módulos y paquetes
subtitle: No hace falta fabricar cada herramienta
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Cuando tienes que colgar un cuadro, no te fabricas un martillo: abres la caja de herramientas y lo coges. Alguien lo hizo bien hace tiempo, y tú solo tienes que saber dónde está y cómo se usa.

## La pregunta

Calcular una raíz cuadrada, sacar un número al azar, saber la fecha de hoy… ¿Tenemos que programarlo todo desde cero? ¿Y cómo reutilizamos nuestras propias funciones en otros programas?

## La idea

Un **módulo** es un archivo `.py` con funciones, variables y clases listas para usar. Python trae muchos de serie, la **biblioteca estándar**: `math`, `random`, `datetime`, `statistics`… Para usar uno, se **importa**:

| Forma | Ejemplo | Cómo se usa después |
|---|---|---|
| `import módulo` | `import math` | `math.sqrt(16)` |
| `import módulo as alias` | `import math as m` | `m.sqrt(16)` |
| `from módulo import nombre` | `from math import sqrt, pi` | `sqrt(16)` |
| `from módulo import *` | `from math import *` | `sqrt(16)`, pero desaconsejado |

:::{important} Por qué se escribe `math.sqrt` y no solo `sqrt`
El prefijo `math.` dice de qué caja sale cada herramienta. Así, una función `sqrt` tuya y la de `math` pueden convivir sin pisarse: cada módulo es su propio **espacio de nombres**. Con `from math import *` metes todos los nombres de golpe en tu programa, y pueden chocar con los tuyos sin que te des cuenta.
:::

## Construcción

### 1 · Usar `math`

:::{tip} Predice
¿De qué tipo será `area`? ¿Y `redondeada`?
:::

```{code-cell} python
import math
radio = 3
area = math.pi * radio ** 2
redondeada = round(area, 2)
lado = math.sqrt(area)
print(redondeada, round(lado, 2))
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Usar math","etiqueta":"import · espacio de nombres","idea":"math.pi y math.sqrt son una constante y una función del módulo math. El visualizador no entra dentro de math.sqrt: es una herramienta cerrada que se usa sin mirar dentro.","columnas":["radio","area","redondeada","lado"],"fila_en":"cada_linea","mostrar_tipos":true},"traza":{"codigo":"import math\nradio = 3\narea = math.pi * radio ** 2\nredondeada = round(area, 2)\nlado = math.sqrt(area)\nprint(redondeada, round(lado, 2))","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"radio":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"radio":"3"},"tipos":{"radio":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"radio":3,"area":28.274333882308138},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"radio":"3","area":"28.274333882308138"},"tipos":{"radio":"int","area":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"radio":3,"area":28.274333882308138,"redondeada":28.27},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"radio":"3","area":"28.274333882308138","redondeada":"28.27"},"tipos":{"radio":"int","area":"float","redondeada":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"radio":3,"area":28.274333882308138,"redondeada":28.27,"lado":5.317361552716548},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"radio":"3","area":"28.274333882308138","redondeada":"28.27","lado":"5.317361552716548"},"tipos":{"radio":"int","area":"float","redondeada":"float","lado":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"radio":3,"area":28.274333882308138,"redondeada":28.27,"lado":5.317361552716548},"salida":"28.27 5.32\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"radio":"3","area":"28.274333882308138","redondeada":"28.27","lado":"5.317361552716548"},"tipos":{"radio":"int","area":"float","redondeada":"float","lado":"float"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["2","3","—","—","—"],["3","3","28.274333882308138","—","—"],["4","3","28.274333882308138","28.27","—"],["5","3","28.274333882308138","28.27","5.317361552716548"],["6","3","28.274333882308138","28.27","5.317361552716548"]]}}
```

`lado` es el lado del cuadrado con la misma área que el círculo: 5,32 aproximadamente. Es el viejo problema de la cuadratura del círculo, resuelto con una calculadora.

### 2 · Números al azar que se pueden repetir

:::{tip} Predice
Si ejecutas la celda dos veces, ¿saldrán las mismas tiradas? ¿Por qué crees que está la línea `random.seed(7)`?
:::

```{code-cell} python
import random
random.seed(7)
tiradas = []
for i in range(5):
    tiradas.append(random.randint(1, 6))
print(tiradas)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Tirar un dado cinco veces","etiqueta":"random · semilla","idea":"random.randint(1, 6) da un entero al azar entre 1 y 6, ambos incluidos. La semilla fija el punto de partida: con la misma semilla salen siempre las mismas tiradas.","lista":"tiradas","foco":"ninguno","cabecera":4,"puntero":"i","columnas":["i","tiradas"],"fila_en":"fin_iteracion"},"traza":{"codigo":"import random\nrandom.seed(7)\ntiradas = []\nfor i in range(5):\n    tiradas.append(random.randint(1, 6))\nprint(tiradas)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"tiradas":[]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"tiradas":"[]"},"tipos":{"tiradas":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"tiradas":[],"i":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"tiradas":"[]","i":"0"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"tiradas":[3],"i":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"tiradas":"[3]","i":"0"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"tiradas":[3],"i":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":0,"repr":{"tiradas":"[3]","i":"1"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"tiradas":[3,2],"i":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"tiradas":"[3, 2]","i":"1"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"tiradas":[3,2],"i":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":1,"repr":{"tiradas":"[3, 2]","i":"2"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"tiradas":[3,2,4],"i":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"tiradas":"[3, 2, 4]","i":"2"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"tiradas":[3,2,4],"i":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":2,"repr":{"tiradas":"[3, 2, 4]","i":"3"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"tiradas":[3,2,4,6],"i":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"tiradas":"[3, 2, 4, 6]","i":"3"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"tiradas":[3,2,4,6],"i":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":3,"repr":{"tiradas":"[3, 2, 4, 6]","i":"4"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"tiradas":[3,2,4,6,1],"i":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"tiradas":"[3, 2, 4, 6, 1]","i":"4"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"tiradas":[3,2,4,6,1],"i":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":4,"repr":{"tiradas":"[3, 2, 4, 6, 1]","i":"4"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"tiradas":[3,2,4,6,1],"i":4},"salida":"[3, 2, 4, 6, 1]\n","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"tiradas":"[3, 2, 4, 6, 1]","i":"4"},"tipos":{"tiradas":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["0","[3]"],["1","[3, 2]"],["2","[3, 2, 4]"],["3","[3, 2, 4, 6]"],["4","[3, 2, 4, 6, 1]"]]}}
```

Los números de `random` no son azar de verdad: salen de una fórmula a partir de una **semilla**. Fijarla con `random.seed(...)` hace el programa reproducible, algo muy útil para comprobarlo. Si quitas esa línea, cada ejecución dará tiradas distintas.

### 3 · Tu propio módulo

Cualquier archivo `.py` es un módulo. Si guardas tus funciones en `geometria.py`:

```python
# geometria.py
import math

def area_circulo(r):
    return math.pi * r ** 2

def perimetro_circulo(r):
    return 2 * math.pi * r

if __name__ == "__main__":
    print("Probando:", area_circulo(1))
```

puedes usarlas desde otro archivo de la misma carpeta:

```python
# programa.py
import geometria

print(geometria.area_circulo(3))
```

:::{important} `if __name__ == "__main__":`
Cada módulo tiene una variable `__name__`. Si ejecutas el archivo directamente, vale `"__main__"`; si otro programa lo importa, vale el nombre del módulo (`"geometria"`). Por eso el código de prueba que va dentro de ese `if` se ejecuta cuando lanzas `geometria.py`, pero no cuando lo importas.
:::

La primera vez que se importa un módulo, Python lo compila y guarda el resultado en una carpeta `__pycache__`, para cargarlo más rápido la siguiente vez.

### 4 · Paquetes y dónde busca Python

Un **paquete** es una carpeta de módulos. Se reconoce por un archivo `__init__.py`, que se ejecuta al importar el paquete:

```text
mis_utiles/
├── __init__.py
├── geometria.py
└── textos.py
```

Se importa con puntos: `import mis_utiles.geometria` o `from mis_utiles import textos`.

Para encontrar un módulo, Python busca en las carpetas de la lista `sys.path`, en orden: primero la del programa, después las de la biblioteca estándar y las de los paquetes instalados. Y `dir(módulo)` lista todo lo que contiene:

```{code-cell} python
import math
import sys
print([nombre for nombre in dir(math) if not nombre.startswith("_")][:10])
print(sys.path[0])
```

Los módulos que no vienen con Python, como `numpy` o `matplotlib`, se instalan con **pip**: `pip install numpy`.

## Conexiones

- Un módulo es la versión grande de una función: una caja con nombre, que se usa sin mirar dentro.
- Los nombres que empiezan por `_` se consideran **privados** por convención: son de uso interno del módulo, aunque Python no impide usarlos.

## La grieta

Hasta ahora, si algo salía mal (un `int("hola")`, una división entre 0), el programa se paraba de golpe con un mensaje en rojo. ¿Podemos prever esos fallos y decirle al programa qué hacer cuando ocurran? Eso son las excepciones.

## Preguntas tipo examen

Preguntas como las del examen PCEP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","capitulo":"12","titulo":"Preguntas tipo examen","etiqueta":"PCEP"}}
```

## Ejercicios

1. **Tres formas.** Escribe de tres maneras distintas un programa que imprima la raíz cuadrada de 2 usando `math`.
2. **¿Qué pasa?** Este programa da un error. ¿Por qué?

   ```python
   import math
   print(sqrt(25))
   ```

3. **Media con `statistics`.** El módulo `statistics` tiene una función `mean`. Úsala para calcular la media de `[7, 4, 9, 6, 8]`.

El solucionario está al final del capítulo.

## Solucionario

1. `import math` y `math.sqrt(2)`; `import math as m` y `m.sqrt(2)`; `from math import sqrt` y `sqrt(2)`. Las tres imprimen `1.4142135623730951`.
2. Con `import math`, la función se llama `math.sqrt`. El nombre `sqrt` a secas no existe en el programa: da `NameError`. Se arregla con `math.sqrt(25)` o con `from math import sqrt`.
3. Una solución:

   ```python
   from statistics import mean
   print(mean([7, 4, 9, 6, 8]))
   ```

   Imprime `6.8`.
