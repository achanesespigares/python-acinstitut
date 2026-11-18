---
title: Comprensiones, for…else y match
subtitle: Decir mucho con poco, y elegir por la forma
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

«De esta clase, quiero los nombres de los que han aprobado, en mayúsculas.» Lo dices en una frase. Programado con un bucle, son cuatro líneas: crear la lista vacía, recorrer, comprobar, añadir. Python tiene una forma de escribirlo casi como lo dices.

## La pregunta

¿Se puede construir una lista nueva a partir de otra en una sola línea, y que se siga leyendo bien? ¿Y elegir qué hacer según la *forma* de un dato, no solo según su valor?

## La idea

Una **comprensión de lista** es un bucle que fabrica una lista, comprimido en una línea:

```python
nueva = [expresión for elemento in secuencia if condición]
```

Es exactamente este bucle:

```python
nueva = []
for elemento in secuencia:
    if condición:
        nueva.append(expresión)
```

Se lee casi en castellano: «la expresión, para cada elemento de la secuencia, si cumple la condición». El `if` es opcional.

## Construcción

### 1 · Filtrar y transformar a la vez

:::{tip} Predice
¿Qué palabras pasan el filtro? ¿Cómo quedarán escritas?
:::

```{code-cell} python
palabras = ["sol", "camino", "luz", "montaña"]
largas = [p.upper() for p in palabras if len(p) > 3]
print(largas)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Filtrar y transformar a la vez","etiqueta":"comprensión de lista","idea":"La comprensión recorre palabras de una en una. Si la palabra cumple len(p) > 3, calcula p.upper() y lo añade a la lista que está fabricando. Si no, la salta.","columnas":["largas"],"fila_en":"cada_linea"},"traza":{"codigo":"palabras = [\"sol\", \"camino\", \"luz\", \"montaña\"]\nlargas = [p.upper() for p in palabras if len(p) > 3]\nprint(largas)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"palabras":["sol","camino","luz","montaña"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"palabras":"['sol', 'camino', 'luz', 'montaña']"},"tipos":{"palabras":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"palabras":["sol","camino","luz","montaña"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"palabras":"['sol', 'camino', 'luz', 'montaña']"},"tipos":{"palabras":"list"},"pila":[],"devuelve":null,"excepcion":null,"compr":{"var":"p","valor":"'sol'","expr":"p.upper()","res":null,"cond":"len(p) > 3","pasa":false,"parcial":"[]"}},{"linea":2,"estado":{"palabras":["sol","camino","luz","montaña"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"palabras":"['sol', 'camino', 'luz', 'montaña']"},"tipos":{"palabras":"list"},"pila":[],"devuelve":null,"excepcion":null,"compr":{"var":"p","valor":"'camino'","expr":"p.upper()","res":"'CAMINO'","cond":"len(p) > 3","pasa":true,"parcial":"['CAMINO']"}},{"linea":2,"estado":{"palabras":["sol","camino","luz","montaña"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"palabras":"['sol', 'camino', 'luz', 'montaña']"},"tipos":{"palabras":"list"},"pila":[],"devuelve":null,"excepcion":null,"compr":{"var":"p","valor":"'luz'","expr":"p.upper()","res":null,"cond":"len(p) > 3","pasa":false,"parcial":"['CAMINO']"}},{"linea":2,"estado":{"palabras":["sol","camino","luz","montaña"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"palabras":"['sol', 'camino', 'luz', 'montaña']"},"tipos":{"palabras":"list"},"pila":[],"devuelve":null,"excepcion":null,"compr":{"var":"p","valor":"'montaña'","expr":"p.upper()","res":"'MONTAÑA'","cond":"len(p) > 3","pasa":true,"parcial":"['CAMINO', 'MONTAÑA']"}},{"linea":2,"estado":{"palabras":["sol","camino","luz","montaña"],"largas":["CAMINO","MONTAÑA"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"palabras":"['sol', 'camino', 'luz', 'montaña']","largas":"['CAMINO', 'MONTAÑA']"},"tipos":{"palabras":"list","largas":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"palabras":["sol","camino","luz","montaña"],"largas":["CAMINO","MONTAÑA"]},"salida":"['CAMINO', 'MONTAÑA']\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"palabras":"['sol', 'camino', 'luz', 'montaña']","largas":"['CAMINO', 'MONTAÑA']"},"tipos":{"palabras":"list","largas":"list"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["2","['CAMINO', 'MONTAÑA']"],["3","['CAMINO', 'MONTAÑA']"]]}}
```

Mira la caja **Comprensión**: en cada paso enseña qué valor toma `p`, si cumple la condición y cómo va creciendo la lista. La variable `p` solo existe mientras se fabrica la lista: al terminar, desaparece.

### 2 · La expresión condicional

A veces no quieres filtrar, sino elegir entre dos valores. Para eso está la **expresión condicional**, un `if` que cabe dentro de una expresión:

```python
valor_si_cumple if condición else valor_si_no
```

:::{tip} Predice
¿Cuántos elementos tendrá `etiquetas`? ¿Alguna nota se queda fuera?
:::

```{code-cell} python
notas = [4, 7, 5, 9]
etiquetas = ["aprobado" if n >= 5 else "suspenso" for n in notas]
print(etiquetas)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Etiquetar notas","etiqueta":"if … else dentro de la expresión","idea":"Aquí no hay filtro: todas las notas producen un elemento. La expresión condicional elige cuál: 'aprobado' si n >= 5, 'suspenso' si no.","columnas":["etiquetas"],"fila_en":"cada_linea"},"traza":{"codigo":"notas = [4, 7, 5, 9]\netiquetas = [\"aprobado\" if n >= 5 else \"suspenso\" for n in notas]\nprint(etiquetas)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"notas":[4,7,5,9]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[4, 7, 5, 9]"},"tipos":{"notas":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"notas":[4,7,5,9]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[4, 7, 5, 9]"},"tipos":{"notas":"list"},"pila":[],"devuelve":null,"excepcion":null,"compr":{"var":"n","valor":"4","expr":"'aprobado' if n >= 5 else 'suspenso'","res":"'suspenso'","cond":null,"pasa":true,"parcial":"['suspenso']"}},{"linea":2,"estado":{"notas":[4,7,5,9]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[4, 7, 5, 9]"},"tipos":{"notas":"list"},"pila":[],"devuelve":null,"excepcion":null,"compr":{"var":"n","valor":"7","expr":"'aprobado' if n >= 5 else 'suspenso'","res":"'aprobado'","cond":null,"pasa":true,"parcial":"['suspenso', 'aprobado']"}},{"linea":2,"estado":{"notas":[4,7,5,9]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[4, 7, 5, 9]"},"tipos":{"notas":"list"},"pila":[],"devuelve":null,"excepcion":null,"compr":{"var":"n","valor":"5","expr":"'aprobado' if n >= 5 else 'suspenso'","res":"'aprobado'","cond":null,"pasa":true,"parcial":"['suspenso', 'aprobado', 'aprobado']"}},{"linea":2,"estado":{"notas":[4,7,5,9]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[4, 7, 5, 9]"},"tipos":{"notas":"list"},"pila":[],"devuelve":null,"excepcion":null,"compr":{"var":"n","valor":"9","expr":"'aprobado' if n >= 5 else 'suspenso'","res":"'aprobado'","cond":null,"pasa":true,"parcial":"['suspenso', 'aprobado', 'aprobado', 'aprobado']"}},{"linea":2,"estado":{"notas":[4,7,5,9],"etiquetas":["suspenso","aprobado","aprobado","aprobado"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"notas":"[4, 7, 5, 9]","etiquetas":"['suspenso', 'aprobado', 'aprobado', 'aprobado']"},"tipos":{"notas":"list","etiquetas":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"notas":[4,7,5,9],"etiquetas":["suspenso","aprobado","aprobado","aprobado"]},"salida":"['suspenso', 'aprobado', 'aprobado', 'aprobado']\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"notas":"[4, 7, 5, 9]","etiquetas":"['suspenso', 'aprobado', 'aprobado', 'aprobado']"},"tipos":{"notas":"list","etiquetas":"list"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["2","['suspenso', 'aprobado', 'aprobado', 'aprobado']"],["3","['suspenso', 'aprobado', 'aprobado', 'aprobado']"]]}}
```

:::{warning} Trampa · dónde va el `if`
- `[x for x in datos if x > 0]` → **filtra**: el `if` va al final y no lleva `else`.
- `[x if x > 0 else 0 for x in datos]` → **elige**: el `if … else` va delante del `for`, y el `else` es obligatorio.

`[x if x > 0 for x in datos]` es un error de sintaxis.
:::

### 3 · Diccionarios y conjuntos por comprensión

Con llaves en lugar de corchetes se fabrican diccionarios (`clave: valor`) y conjuntos:

```{code-cell} python
palabras = ["sol", "camino", "luz", "montaña"]
longitudes = {p: len(p) for p in palabras}
iniciales = {p[0] for p in palabras}
print(longitudes)
print(sorted(iniciales))
```

### 4 · Comprensiones anidadas

Con dos `for` se recorren dos secuencias anidadas. Se leen **en el mismo orden en que escribirías los bucles**: el primer `for` es el de fuera.

```{code-cell} python
casillas = [(fila, col) for fila in range(2) for col in range(3)]
print(casillas)
```

El uso más típico es **aplanar** una lista de listas, y se puede filtrar a la vez:

```{code-cell} python
grupos = [[7, 4], [9], [3, 8, 6]]
todas = [n for g in grupos for n in g]
aprobadas = [n for g in grupos for n in g if n >= 5]
print(todas, aprobadas)
```

Equivale a `for g in grupos:` y, dentro, `for n in g:`. Si lo escribes al revés (`for n in g for g in grupos`), Python protesta porque `g` aún no existe.

Y una comprensión puede tener dentro otra, para fabricar listas de listas, como una tabla:

```{code-cell} python
tabla = [[f * c for c in range(1, 4)] for f in range(1, 4)]
print(tabla)
```

### 5 · `for … else`: el bucle que sabe si encontró algo

Un bucle `for` (o `while`) puede llevar un `else`. Parece raro, pero su regla es sencilla: **el `else` se ejecuta si el bucle termina por sí solo, sin `break`**. Sirve para las búsquedas: «si recorro todo y no encuentro nada, entonces…».

:::{tip} Predice
¿Se imprimirá «es primo»? ¿En qué vuelta se para el bucle?
:::

```{code-cell} python
n = 15
for d in range(2, n):
    if n % d == 0:
        print(n, "no es primo: es divisible entre", d)
        break
else:
    print(n, "es primo")
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"¿Es primo?","etiqueta":"for … else · break","idea":"El bucle busca un divisor. Al encontrar el 3, break lo corta de golpe, y por eso el else no se ejecuta. Con un número primo, el bucle llegaría al final sin break y sí se ejecutaría el else.","cabecera":2,"puntero":"d","columnas":["d","n % d"],"fila_en":"cada_linea"},"traza":{"codigo":"n = 15\nfor d in range(2, n):\n    if n % d == 0:\n        print(n, \"no es primo: es divisible entre\", d)\n        break\nelse:\n    print(n, \"es primo\")","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"n":15},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"n":"15"},"tipos":{"n":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"n":15,"d":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":0,"repr":{"n":"15","d":"2"},"tipos":{"n":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"n":15,"d":2},"salida":"","foco":null,"lee":false,"cond":{"expr":"n % d == 0","sust":"15 % 2 == 0","valor":false},"vuelta":1,"fila":1,"repr":{"n":"15","d":"2"},"tipos":{"n":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"n":15,"d":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":2,"repr":{"n":"15","d":"3"},"tipos":{"n":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"n":15,"d":3},"salida":"","foco":null,"lee":false,"cond":{"expr":"n % d == 0","sust":"15 % 3 == 0","valor":true},"vuelta":2,"fila":3,"repr":{"n":"15","d":"3"},"tipos":{"n":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"n":15,"d":3},"salida":"15 no es primo: es divisible entre 3\n","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":4,"repr":{"n":"15","d":"3"},"tipos":{"n":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"n":15,"d":3},"salida":"15 no es primo: es divisible entre 3\n","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":5,"repr":{"n":"15","d":"3"},"tipos":{"n":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["2","2","1"],["3","2","1"],["2","3","0"],["3","3","0"],["4","3","0"],["5","3","0"]]}}
```

Prueba a cambiar `n = 15` por `n = 13` en la celda: el bucle recorre del 2 al 12 sin encontrar divisor, termina solo y se ejecuta el `else`.

El `while` también admite `else`, con la misma regla: se ejecuta cuando la condición pasa a ser falsa, pero no si se sale con `break`.

```{code-cell} python
intentos = 3
while intentos > 0:
    intentos = intentos - 1
else:
    print("Se acabaron los intentos")
```

### 6 · `match`: elegir por la forma

El `match` (desde Python 3.10) compara un valor con una lista de **patrones**, de arriba abajo, y ejecuta el primero que encaja. Un patrón puede describir la forma del dato y, a la vez, **capturar** sus partes en variables.

:::{tip} Predice
El punto es `(0, 3)`. ¿Qué `case` encaja? ¿Qué valor tendrá `y`?
:::

```{code-cell} python
punto = (0, 3)
match punto:
    case (0, 0):
        print("el origen")
    case (0, y):
        print("en el eje vertical, a altura", y)
    case (x, 0):
        print("en el eje horizontal, en", x)
    case _:
        print("fuera de los ejes")
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"¿Dónde está el punto?","etiqueta":"match · case · captura","idea":"(0, 0) no encaja porque el segundo número no es 0. (0, y) sí: el 0 coincide y la y captura el 3. Los case de debajo ya no se miran.","columnas":["punto","y"],"fila_en":"cada_linea"},"traza":{"codigo":"punto = (0, 3)\nmatch punto:\n    case (0, 0):\n        print(\"el origen\")\n    case (0, y):\n        print(\"en el eje vertical, a altura\", y)\n    case (x, 0):\n        print(\"en el eje horizontal, en\", x)\n    case _:\n        print(\"fuera de los ejes\")","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"punto":{"__tupla__":[0,3]}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"punto":"(0, 3)"},"tipos":{"punto":"tuple"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"punto":{"__tupla__":[0,3]}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"punto":"(0, 3)"},"tipos":{"punto":"tuple"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"punto":{"__tupla__":[0,3]}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"punto":"(0, 3)"},"tipos":{"punto":"tuple"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"punto":{"__tupla__":[0,3]},"y":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"punto":"(0, 3)","y":"3"},"tipos":{"punto":"tuple","y":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"punto":{"__tupla__":[0,3]},"y":3},"salida":"en el eje vertical, a altura 3\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"punto":"(0, 3)","y":"3"},"tipos":{"punto":"tuple","y":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","(0, 3)","—"],["2","(0, 3)","—"],["3","(0, 3)","—"],["5","(0, 3)","3"],["6","(0, 3)","3"]]}}
```

Los patrones más útiles:

| Patrón | Encaja con | Ejemplo |
|---|---|---|
| un literal | ese valor exacto | `case "salir":` |
| varios con `\|` | cualquiera de ellos | `case "s" \| "salir":` |
| un nombre | cualquier valor, y lo captura | `case (0, y):` |
| `_` | cualquier cosa, sin capturar | `case _:` |
| con guarda `if` | el patrón, si además se cumple la condición | `case (x, y) if x == y:` |

:::{important} `match` no es un `if` disfrazado
Un `if … elif` evalúa condiciones; un `match` compara **la forma** de un solo valor con patrones, y de paso puede sacar sus piezas. Para preguntar «¿es mayor que 10?» sigue siendo mejor un `if`.

`case (0, y):` no compara con una variable `y` que ya existiera: **crea** `y` con lo que haya en esa posición. Si quieres comparar con el valor de una variable, usa una guarda: `case (0, v) if v == limite:`.
:::

## Conexiones

- Una comprensión es el patrón del acumulador de [Recorrer listas](08-recorrer-listas.md), escrito en una línea. Si la línea se vuelve difícil de leer, vuelve al bucle: la claridad manda.
- El `else` del `for` evita la típica variable bandera (`encontrado = False`) de las búsquedas.
- `match` brilla con datos que tienen estructura: tuplas, listas, diccionarios y objetos.

## La grieta

En `sorted(alumnos, key=…)` hay que pasar **una función** como dato, para decir por qué criterio ordenar. ¿Se puede guardar una función en una variable o pasarla a otra función, como si fuera un número? Sí, y eso abre una puerta enorme.

## Ejercicios

1. **Del bucle a la comprensión.** Reescribe en una línea:

   ```python
   cuadrados = []
   for x in range(1, 6):
       cuadrados.append(x * x)
   ```

2. **Solo los pares.** A partir de `datos = [3, 8, 11, 6, 2]`, crea con una comprensión la lista de los pares.
3. **Sin negativos.** A partir de `temperaturas = [3, -2, 5, -7]`, crea una lista en la que cada negativo se cambie por 0 y los demás se queden igual.
4. **¿Qué imprime?**

   ```python
   for x in [1, 3, 5]:
       if x % 2 == 0:
           print("hay un par")
           break
   else:
       print("ninguno es par")
   ```

5. **Comandos.** Con `match`, escribe un programa que, para `orden = "n"`, imprima «norte»; para `"s"`, «sur»; para `"salir"` o `"q"`, «adiós»; y para cualquier otra cosa, «no te entiendo».

El solucionario está al final del capítulo.

## Solucionario

1. `cuadrados = [x * x for x in range(1, 6)]`, que da `[1, 4, 9, 16, 25]`.
2. `pares = [d for d in datos if d % 2 == 0]`, que da `[8, 6, 2]`.
3. `[t if t >= 0 else 0 for t in temperaturas]`, que da `[3, 0, 5, 0]`. Aquí no se filtra: se elige, así que el `if … else` va delante del `for`.
4. Imprime **ninguno es par**. El bucle recorre los tres números sin encontrar un par, termina sin `break` y se ejecuta el `else`.
5. Una solución:

   ```python
   orden = "n"
   match orden:
       case "n":
           print("norte")
       case "s":
           print("sur")
       case "salir" | "q":
           print("adiós")
       case _:
           print("no te entiendo")
   ```
