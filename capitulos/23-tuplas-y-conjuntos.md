---
title: Tuplas y conjuntos
subtitle: Colecciones que no se tocan y colecciones sin repetidos
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Una fecha de nacimiento no cambia: si cambiara, sería otra persona. En cambio, la lista de la compra cambia cada día. Y en la lista de invitados de una fiesta no tiene sentido apuntar a nadie dos veces. Cada tipo de colección responde a una de estas necesidades.

## La pregunta

¿Cómo se guarda un grupo de valores que no debe cambiar nunca? ¿Y cómo se guarda una colección en la que cada elemento aparece una sola vez, sin importar el orden?

## La idea

| | Lista | Tupla | Conjunto |
|---|---|---|---|
| Se escribe | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
| ¿Tiene orden y posiciones? | sí | sí | **no** |
| ¿Se puede modificar? | sí | **no** | sí (añadir y quitar) |
| ¿Admite repetidos? | sí | sí | **no** |
| Para qué | datos que cambian | datos fijos, varios valores juntos | pertenencia, quitar repetidos |

## Construcción

### 1 · Tuplas: crearlas y leerlas

```{code-cell} python
vacia = ()
uno = (5,)               # la coma es la que hace la tupla
no_es_tupla = (5)        # esto es solo el número 5 entre paréntesis
fecha = (18, 11, 2026)
punto = 3, 7             # los paréntesis se pueden omitir
print(type(uno).__name__, type(no_es_tupla).__name__, len(fecha))
print(fecha[0], fecha[-1], fecha[1:])
print(fecha.count(18), fecha.index(2026), 2026 in fecha)
```

:::{warning} Trampa · la tupla de un elemento
`(5)` es el número 5. Para una tupla de un solo elemento hace falta la coma: `(5,)`. Es una pregunta clásica de examen.
:::

### 2 · Inmutables

Una tupla no se puede cambiar: ni modificar una posición, ni añadir, ni quitar.

```{code-cell} python
fecha = (18, 11, 2026)
try:
    fecha[0] = 19
except TypeError as e:
    print("Error:", e)
fecha = (19, 11, 2026)    # sí se puede pegar la etiqueta a una tupla nueva
print(fecha)
```

Una tupla puede contener listas, y esas listas sí se pueden cambiar: la tupla solo garantiza que sus casillas apuntan siempre a los mismos objetos.

```{code-cell} python
alumno = ("Ana", [7, 9])
alumno[1].append(8)       # la lista de dentro sí cambia
print(alumno, alumno[1][0])
```

### 3 · Empaquetar y desempaquetar

Python junta valores en una tupla automáticamente (los **empaqueta**) y los puede repartir entre varias variables (los **desempaqueta**). Así una función puede devolver varios valores a la vez.

:::{tip} Predice
`minmax` devuelve dos cosas. ¿Cómo llegan a `bajo` y `alto`?
:::

```{code-cell} python
def minmax(datos):
    return min(datos), max(datos)

notas = [6, 9, 4, 7]
bajo, alto = minmax(notas)
print(bajo, alto)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Devolver dos valores","etiqueta":"tupla · desempaquetar","idea":"return min(datos), max(datos) empaqueta los dos valores en una tupla, (4, 9). Al recibirla, bajo, alto = … la desempaqueta: el primero va a bajo y el segundo a alto.","columnas":["bajo","alto"],"fila_en":"cada_linea"},"traza":{"codigo":"def minmax(datos):\n    return min(datos), max(datos)\n\nnotas = [6, 9, 4, 7]\nbajo, alto = minmax(notas)\nprint(bajo, alto)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"notas":[6,9,4,7]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[6, 9, 4, 7]"},"tipos":{"notas":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":[6,9,4,7]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[6, 9, 4, 7]"},"tipos":{"notas":"list"},"pila":[{"nombre":"minmax","args":["datos"],"vars":{"datos":[6,9,4,7]},"repr":{"datos":"[6, 9, 4, 7]"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"notas":[6,9,4,7]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[6, 9, 4, 7]"},"tipos":{"notas":"list"},"pila":[{"nombre":"minmax","args":["datos"],"vars":{"datos":[6,9,4,7]},"repr":{"datos":"[6, 9, 4, 7]"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"notas":[6,9,4,7],"bajo":4,"alto":9},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"notas":"[6, 9, 4, 7]","bajo":"4","alto":"9"},"tipos":{"notas":"list","bajo":"int","alto":"int"},"pila":[],"devuelve":{"funcion":"minmax","valor":"(4, 9)","error":false},"excepcion":null},{"linea":6,"estado":{"notas":[6,9,4,7],"bajo":4,"alto":9},"salida":"4 9\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"notas":"[6, 9, 4, 7]","bajo":"4","alto":"9"},"tipos":{"notas":"list","bajo":"int","alto":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["2 ↩","4","9"],["6","4","9"]]}}
```

El mismo truco sirve para intercambiar dos variables sin una auxiliar, y para recorrer listas de tuplas:

```{code-cell} python
a, b = 1, 2
a, b = b, a
print(a, b)
for nombre, nota in [("Ana", 7), ("Biel", 9)]:
    print(nombre, "ha sacado un", nota)
```

Si el número de variables no coincide con el de valores, salta `ValueError: too many values to unpack`.

### 4 · Conjuntos: sin repetidos y sin orden

Un **conjunto** (`set`) guarda cada elemento una sola vez y no tiene posiciones: no existe `conjunto[0]`. A cambio, comprobar si algo está dentro es rapidísimo, aunque tenga millones de elementos.

:::{tip} Predice
¿Qué nombres acabarán en `repetidos`? ¿Cuántos elementos tendrá `vistos`?
:::

```{code-cell} python
nombres = ["Ana", "Biel", "Ana", "Carla", "Biel"]
vistos = set()
repetidos = []
for n in nombres:
    if n in vistos:
        repetidos.append(n)
    else:
        vistos.add(n)
print(len(vistos), repetidos)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"¿Quién está repetido?","etiqueta":"set · in · add","idea":"vistos guarda cada nombre la primera vez que aparece. Cuando un nombre ya está en vistos, es un repetido. Al final, vistos tiene 3 nombres distintos.","lista":"nombres","cabecera":4,"puntero":"n","columnas":["n","vistos","repetidos"],"fila_en":"fin_iteracion"},"traza":{"codigo":"nombres = [\"Ana\", \"Biel\", \"Ana\", \"Carla\", \"Biel\"]\nvistos = set()\nrepetidos = []\nfor n in nombres:\n    if n in vistos:\n        repetidos.append(n)\n    else:\n        vistos.add(n)\nprint(len(vistos), repetidos)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']"},"tipos":{"nombres":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"set()"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"set()"},"tipos":{"nombres":"list","vistos":"set"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"set()"},"repetidos":[]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"set()","repetidos":"[]"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"set()"},"repetidos":[],"n":"Ana"},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"set()","repetidos":"[]","n":"'Ana'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"set()"},"repetidos":[],"n":"Ana"},"salida":"","foco":0,"lee":false,"cond":{"expr":"n in vistos","sust":"'Ana' in vistos","valor":false},"vuelta":1,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"set()","repetidos":"[]","n":"'Ana'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana'}"},"repetidos":[],"n":"Ana"},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana'}","repetidos":"[]","n":"'Ana'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana'}"},"repetidos":[],"n":"Biel"},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana'}","repetidos":"[]","n":"'Biel'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana'}"},"repetidos":[],"n":"Biel"},"salida":"","foco":1,"lee":false,"cond":{"expr":"n in vistos","sust":"'Biel' in vistos","valor":false},"vuelta":2,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana'}","repetidos":"[]","n":"'Biel'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel'}"},"repetidos":[],"n":"Biel"},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel'}","repetidos":"[]","n":"'Biel'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel'}"},"repetidos":[],"n":"Ana"},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel'}","repetidos":"[]","n":"'Ana'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel'}"},"repetidos":[],"n":"Ana"},"salida":"","foco":2,"lee":false,"cond":{"expr":"n in vistos","sust":"'Ana' in vistos","valor":true},"vuelta":3,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel'}","repetidos":"[]","n":"'Ana'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel'}"},"repetidos":["Ana"],"n":"Ana"},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel'}","repetidos":"['Ana']","n":"'Ana'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel'}"},"repetidos":["Ana"],"n":"Carla"},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel'}","repetidos":"['Ana']","n":"'Carla'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel'}"},"repetidos":["Ana"],"n":"Carla"},"salida":"","foco":3,"lee":false,"cond":{"expr":"n in vistos","sust":"'Carla' in vistos","valor":false},"vuelta":4,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel'}","repetidos":"['Ana']","n":"'Carla'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel', 'Carla'}"},"repetidos":["Ana"],"n":"Carla"},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel', 'Carla'}","repetidos":"['Ana']","n":"'Carla'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel', 'Carla'}"},"repetidos":["Ana"],"n":"Biel"},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":5,"fila":3,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel', 'Carla'}","repetidos":"['Ana']","n":"'Biel'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel', 'Carla'}"},"repetidos":["Ana"],"n":"Biel"},"salida":"","foco":4,"lee":false,"cond":{"expr":"n in vistos","sust":"'Biel' in vistos","valor":true},"vuelta":5,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel', 'Carla'}","repetidos":"['Ana']","n":"'Biel'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel', 'Carla'}"},"repetidos":["Ana","Biel"],"n":"Biel"},"salida":"","foco":4,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel', 'Carla'}","repetidos":"['Ana', 'Biel']","n":"'Biel'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel', 'Carla'}"},"repetidos":["Ana","Biel"],"n":"Biel"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":4,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel', 'Carla'}","repetidos":"['Ana', 'Biel']","n":"'Biel'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":9,"estado":{"nombres":["Ana","Biel","Ana","Carla","Biel"],"vistos":{"__txt__":"{'Ana', 'Biel', 'Carla'}"},"repetidos":["Ana","Biel"],"n":"Biel"},"salida":"3 ['Ana', 'Biel']\n","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"nombres":"['Ana', 'Biel', 'Ana', 'Carla', 'Biel']","vistos":"{'Ana', 'Biel', 'Carla'}","repetidos":"['Ana', 'Biel']","n":"'Biel'"},"tipos":{"nombres":"list","vistos":"set","repetidos":"list","n":"str"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["'Ana'","{'Ana'}","[]"],["'Biel'","{'Ana', 'Biel'}","[]"],["'Ana'","{'Ana', 'Biel'}","['Ana']"],["'Carla'","{'Ana', 'Biel', 'Carla'}","['Ana']"],["'Biel'","{'Ana', 'Biel', 'Carla'}","['Ana', 'Biel']"]]}}
```

:::{important} `{}` no es un conjunto vacío
`{}` crea un **diccionario** vacío. El conjunto vacío se escribe `set()`. Con elementos, sí se usan llaves: `{1, 2, 3}`.
:::

| Operación | Qué hace |
|---|---|
| `c.add(x)` | añade `x` (si ya estaba, no pasa nada) |
| `c.remove(x)` | quita `x`; error `KeyError` si no está |
| `c.discard(x)` | quita `x` si está; si no, no hace nada |
| `x in c`, `x not in c` | ¿está o no? |
| `set(lista)` | un conjunto con los elementos de la lista, sin repetidos |
| `a \| b`, `a & b`, `a - b` | unión, intersección y diferencia |

```{code-cell} python
mates = {"Ana", "Biel", "Carla"}
fisica = {"Biel", "Dani"}
print(sorted(mates | fisica), sorted(mates & fisica), sorted(mates - fisica))
print(len(set([3, 1, 3, 2, 1])))
try:
    mates[0]
except TypeError as e:
    print("Error:", e)
```

Usamos `sorted` para imprimir porque un conjunto no garantiza ningún orden: el mismo conjunto puede salir escrito en un orden distinto en otro ordenador.

## Conexiones

- Las tuplas reaparecerán a menudo: como parejas `("Ana", 7)` que se ordenan en [Funciones como valores](16-funciones-valores.md) y como patrones `case (0, y)` en [Comprensiones, for…else y match](15-comprensiones.md).
- Las claves de un diccionario se comportan como un conjunto: sin repetidos y con búsqueda rápida.
- Una tupla puede ser clave de un diccionario; una lista no, precisamente porque puede cambiar.

## La grieta

`minmax` devolvía dos valores. ¿Y si queremos una función que acepte cualquier número de argumentos, como `print`? ¿Y qué pasa con una variable que se llama igual dentro y fuera de una función?

## Preguntas tipo examen

Preguntas como las del examen PCEP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","capitulo":"23","titulo":"Preguntas tipo examen","etiqueta":"PCEP"}}
```

## Ejercicios

1. **¿Qué tipo es?** a) `(3)`; b) `(3,)`; c) `3, 4`; d) `{}`; e) `set()`.
2. **¿Qué imprime?**

   ```python
   t = (1, 2, 3)
   a, *resto = t
   print(a, resto)
   ```

3. **Sin repetidos, con orden.** A partir de `datos = [5, 3, 5, 1, 3]`, obtén la lista ordenada de los valores distintos.
4. **Comunes.** Dadas dos listas de alumnos, escribe una expresión que dé los que están en las dos.
5. **Suma y media.** Escribe una función `extremos(t)` que reciba una tupla de números y devuelva a la vez la suma y la media.

El solucionario está al final del capítulo.

## Solucionario

1. a) `int`; b) `tuple`; c) `tuple`; d) `dict`; e) `set`.
2. Imprime **1 [2, 3]**. El `*` recoge en una **lista** todos los valores que sobran.
3. `sorted(set(datos))` da `[1, 3, 5]`.
4. `set(lista1) & set(lista2)`, o `sorted(set(lista1) & set(lista2))` si se quiere ordenada.
5. Una solución:

   ```python
   def extremos(t):
       suma = sum(t)
       return suma, suma / len(t)

   s, m = extremos((4, 6, 8))
   print(s, m)
   ```

   Imprime `18 6.0`.
