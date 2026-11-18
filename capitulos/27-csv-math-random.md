---
title: CSV, math y random
subtitle: Tablas en ficheros, redondeos y azar
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Cuando exportas las notas de una hoja de cálculo para usarlas en otro programa, casi siempre eliges el mismo formato: **CSV**. Es una tabla escrita como texto, que entiende cualquier programa. Saber leerla y escribirla desde Python abre la puerta a trabajar con datos reales.

## La pregunta

¿Cómo se guarda una tabla en un fichero de texto y cómo se recupera? Y ya puestos: ¿cómo se redondea siempre hacia arriba, o se elige algo al azar de una lista?

## La idea

Un fichero **CSV** (*comma-separated values*, valores separados por comas) guarda una fila por línea y separa las columnas con comas. La primera fila suele ser la **cabecera**, con el nombre de cada columna:

```text
nombre,nota
Ana,7
Biel,9
```

El módulo `csv` sabe leer y escribir este formato, incluidos los casos difíciles, como un dato que lleva una coma dentro (`"García, Ana"`), que va entre comillas.

Antes, lo justo sobre ficheros. Un fichero se abre con `open(nombre, modo)`:

| Modo | Para qué |
|---|---|
| `"r"` | leer (el modo por defecto); si el fichero no existe, `FileNotFoundError` |
| `"w"` | escribir; si el fichero existe, **lo vacía** |
| `"a"` | añadir al final, sin borrar lo que había |

Y se abre con `with`, que lo cierra solo al acabar el bloque, pase lo que pase. Todo esto, con el disco a la vista, se estudia a fondo en [Ficheros y flujos](17-ficheros.md).

## Construcción

### 1 · Un fichero de texto en dos minutos

```{code-cell} python
with open("diario.txt", "w", encoding="utf-8") as f:
    f.write("lunes: álgebra\n")
with open("diario.txt", "a", encoding="utf-8") as f:
    f.write("martes: funciones\n")
with open("diario.txt", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
try:
    open("no_existe.txt")
except FileNotFoundError as e:
    print("Error:", e)
```

Los errores más comunes al abrir: `FileNotFoundError` (el fichero no existe, o la ruta está mal escrita), `PermissionError` (no hay permiso) y `IsADirectoryError` (el nombre es el de una carpeta).

### 2 · Escribir y leer un CSV

:::{tip} Predice
Al leerlo, ¿en qué se convierte cada fila? ¿De qué tipo es la nota `'7'`?
:::

```{code-cell} python
import csv
with open("notas.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["nombre", "nota"])
    w.writerow(["Ana", 7])
    w.writerow(["Biel", 9])
with open("notas.csv", newline="") as f:
    filas = list(csv.reader(f))
print(filas)
total = 0
for fila in filas[1:]:
    total += int(fila[1])
print(total)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Una tabla en un fichero","etiqueta":"csv.writer · csv.reader","idea":"writerow convierte cada lista en una línea separada por comas; mira el fichero en el disco al cerrarse. reader hace lo contrario: cada línea vuelve a ser una lista, pero todo llega como texto, y la nota hay que convertirla con int.","columnas":["total"],"fila_en":"cada_linea"},"traza":{"codigo":"import csv\nwith open(\"notas.csv\", \"w\", newline=\"\") as f:\n    w = csv.writer(f)\n    w.writerow([\"nombre\", \"nota\"])\n    w.writerow([\"Ana\", 7])\n    w.writerow([\"Biel\", 9])\nwith open(\"notas.csv\", newline=\"\") as f:\n    filas = list(csv.reader(f))\nprint(filas)\ntotal = 0\nfor fila in filas[1:]:\n    total += int(fila[1])\nprint(total)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":2,"estado":{"f":{"__txt__":"fichero 'notas.csv' abierto en modo 'w'"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.csv' abierto en modo 'w'"},"tipos":{"f":"TextIOWrapper"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":0,"contenido":"","binario":false}]},{"linea":3,"estado":{"f":{"__txt__":"fichero 'notas.csv' abierto en modo 'w'"},"w":{"__txt__":"<_csv.writer object>"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.csv' abierto en modo 'w'","w":"<_csv.writer object>"},"tipos":{"f":"TextIOWrapper","w":"writer"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":0,"contenido":"","binario":false}]},{"linea":4,"estado":{"f":{"__txt__":"fichero 'notas.csv' abierto en modo 'w'"},"w":{"__txt__":"<_csv.writer object>"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.csv' abierto en modo 'w'","w":"<_csv.writer object>"},"tipos":{"f":"TextIOWrapper","w":"writer"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":0,"contenido":"","binario":false}]},{"linea":5,"estado":{"f":{"__txt__":"fichero 'notas.csv' abierto en modo 'w'"},"w":{"__txt__":"<_csv.writer object>"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.csv' abierto en modo 'w'","w":"<_csv.writer object>"},"tipos":{"f":"TextIOWrapper","w":"writer"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":0,"contenido":"","binario":false}]},{"linea":6,"estado":{"f":{"__txt__":"fichero 'notas.csv' abierto en modo 'w'"},"w":{"__txt__":"<_csv.writer object>"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.csv' abierto en modo 'w'","w":"<_csv.writer object>"},"tipos":{"f":"TextIOWrapper","w":"writer"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":0,"contenido":"","binario":false}]},{"linea":2,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>"},"tipos":{"f":"TextIOWrapper","w":"writer"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":7,"estado":{"f":{"__txt__":"fichero 'notas.csv' abierto en modo 'r'"},"w":{"__txt__":"<_csv.writer object>"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.csv' abierto en modo 'r'","w":"<_csv.writer object>"},"tipos":{"f":"TextIOWrapper","w":"writer"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":8,"estado":{"f":{"__txt__":"fichero 'notas.csv' abierto en modo 'r'"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.csv' abierto en modo 'r'","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":7,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":9,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]]},"salida":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":10,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]],"total":0},"salida":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]","total":"0"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list","total":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":11,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]],"total":0,"fila":["Ana","7"]},"salida":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]","total":"0","fila":"['Ana', '7']"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list","total":"int","fila":"list"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":12,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]],"total":7,"fila":["Ana","7"]},"salida":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]","total":"7","fila":"['Ana', '7']"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list","total":"int","fila":"list"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":11,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]],"total":7,"fila":["Biel","9"]},"salida":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]","total":"7","fila":"['Biel', '9']"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list","total":"int","fila":"list"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":12,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]],"total":16,"fila":["Biel","9"]},"salida":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]","total":"16","fila":"['Biel', '9']"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list","total":"int","fila":"list"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":11,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]],"total":16,"fila":["Biel","9"]},"salida":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]","total":"16","fila":"['Biel', '9']"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list","total":"int","fila":"list"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]},{"linea":13,"estado":{"f":{"__txt__":"fichero 'notas.csv' (cerrado)"},"w":{"__txt__":"<_csv.writer object>"},"filas":[["nombre","nota"],["Ana","7"],["Biel","9"]],"total":16,"fila":["Biel","9"]},"salida":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]\n16\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":7,"repr":{"f":"fichero 'notas.csv' (cerrado)","w":"<_csv.writer object>","filas":"[['nombre', 'nota'], ['Ana', '7'], ['Biel', '9']]","total":"16","fila":"['Biel', '9']"},"tipos":{"f":"TextIOWrapper","w":"writer","filas":"list","total":"int","fila":"list"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.csv","tam":28,"contenido":"nombre,nota\r\nAna,7\r\nBiel,9\r\n","binario":false}]}],"filas":[["9","—"],["10","0"],["11","0"],["12","7"],["11","7"],["12","16"],["11","16"],["13","16"]]}}
```

Tres detalles:

- Se abre con **`newline=""`**, como pide la documentación del módulo `csv`: así el módulo controla él mismo los finales de línea. Por defecto termina cada fila en `\r\n`, el final de línea de Windows: en el disco lo verás como `␍↵`.
- Cada fila leída es una **lista de cadenas**: el `7` llega como `'7'`.
- `filas[1:]` se salta la cabecera.

Si el separador es otro, como el `;` que usan muchas hojas de cálculo en castellano, se indica con `delimiter=";"`: `csv.reader(f, delimiter=";")`.

### 3 · El módulo `math`: redondear de cuatro maneras

```{code-cell} python
import math
for x in [2.5, -2.5, 2.7]:
    print(x, math.ceil(x), math.floor(x), math.trunc(x), round(x))
print(math.sqrt(16), math.pi, math.factorial(5), math.hypot(3, 4))
```

| Función | Qué hace | `2.7` | `-2.5` |
|---|---|---|---|
| `math.ceil(x)` | redondea **hacia arriba** (al entero mayor o igual) | `3` | `-2` |
| `math.floor(x)` | redondea **hacia abajo** (al entero menor o igual) | `2` | `-3` |
| `math.trunc(x)` | **quita** los decimales | `2` | `-2` |
| `round(x)` | redondea al más cercano | `3` | `-2` |

:::{warning} Trampa · los negativos y `round`
Con negativos, «hacia abajo» significa hacia el más pequeño: `floor(-2.5)` es `-3`, mientras que `trunc(-2.5)` es `-2`. Y `round` redondea los empates (`.5`) al **par** más cercano: `round(2.5)` da `2` y `round(3.5)` da `4`.
:::

### 4 · El módulo `random`: azar que se puede repetir

```{code-cell} python
import random
random.seed(42)
print(random.random())                 # un decimal en [0, 1)
print(random.randint(1, 6))            # un entero entre 1 y 6, ambos incluidos
alumnos = ["Ana", "Biel", "Carla", "Dani", "Eva"]
print(random.choice(alumnos))          # uno al azar
print(random.sample(alumnos, 3))       # tres distintos al azar
random.shuffle(alumnos)                # baraja la lista en su sitio
print(alumnos)
```

| Función | Qué da |
|---|---|
| `random()` | un `float` entre 0 (incluido) y 1 (excluido) |
| `randint(a, b)` | un entero entre `a` y `b`, **los dos incluidos** |
| `randrange(a, b)` | un entero entre `a` y `b`, sin incluir `b`, como `range` |
| `choice(secuencia)` | un elemento al azar |
| `sample(secuencia, k)` | `k` elementos distintos, sin repetir |
| `shuffle(lista)` | baraja la lista en su sitio (devuelve `None`) |
| `seed(n)` | fija el punto de partida: misma semilla, mismos resultados |

La semilla hace el azar **reproducible** (en [Módulos](12-modulos.md) verás por qué): si ejecutas la celda dos veces, sale lo mismo. Quita la línea `random.seed(42)` y cada vez saldrá distinto.

## Conexiones

- Un CSV es un fichero de texto con una regla para las columnas; cada fila es una lista, como en [Listas a fondo](22-listas-a-fondo.md).
- `int(fila[1])` es la conversión de `input()`: todo lo que viene de fuera llega como texto.
- `random.sample` sirve para sacar alumnos al azar sin repetir, y `shuffle` para hacer grupos.

## La grieta

Hasta aquí llega todo el temario del PCEP. Lo que viene es el PCAP, y empieza por una pregunta de organización: cuando un programa crece, ¿cómo se reparte en varios ficheros y se reutiliza lo que ya está hecho? Son los módulos y los paquetes.

## Ejercicios

1. **Nota media.** Escribe un programa que lea `notas.csv` (el del apartado 1) y calcule la media de la columna `nota`.
2. **Añadir una fila.** Añade la fila `Carla,8` al final de `notas.csv` sin borrar las anteriores.
3. **¿Qué imprime?** `print(math.ceil(4.01), math.floor(-0.5), math.trunc(9.99), round(0.5))`
4. **Equipos.** Con `random`, reparte `["Ana", "Biel", "Carla", "Dani"]` en dos equipos de dos, al azar.
5. **Dado trucado.** Simula 1000 tiradas de un dado con `randint` y cuenta cuántas veces sale cada número usando un diccionario.

El solucionario está al final del capítulo.

## Solucionario

1. Una solución:

   ```python
   import csv
   with open("notas.csv", newline="") as f:
       filas = list(csv.reader(f))[1:]
   notas = [int(fila[1]) for fila in filas]
   print(sum(notas) / len(notas))
   ```

2. Con el modo `"a"`:

   ```python
   with open("notas.csv", "a", newline="") as f:
       csv.writer(f).writerow(["Carla", 8])
   ```

3. Imprime **5 -1 9 0**. `round(0.5)` da `0` porque los empates se redondean al par.
4. Una solución:

   ```python
   import random
   grupo = ["Ana", "Biel", "Carla", "Dani"]
   random.shuffle(grupo)
   print(grupo[:2], grupo[2:])
   ```

5. Una solución:

   ```python
   import random
   cuenta = {}
   for _ in range(1000):
       t = random.randint(1, 6)
       cuenta[t] = cuenta.get(t, 0) + 1
   print(cuenta)
   ```
