---
title: Listas a fondo
subtitle: Copiar, insertar, quitar y guardar tablas enteras
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Si le dejas a un amigo la llave de tu casa, no tiene otra casa: tiene otra forma de entrar en la misma. Si cambia los muebles de sitio, tú te los encuentras cambiados. Con las listas pasa exactamente eso, y es una de las sorpresas más frecuentes al empezar.

## La pregunta

¿Qué pasa cuando escribes `b = a` con una lista? ¿Cómo se hace una copia de verdad? ¿Cómo se mete un elemento en medio o se quita uno? ¿Y cómo se guarda una tabla con filas y columnas?

## La idea

Una lista guarda valores en orden, cada uno en una posición. Se puede contar **desde el principio** (0, 1, 2…) o **desde el final** (-1 es el último, -2 el penúltimo…):

```text
          'a'   'b'   'c'   'd'   'e'
desde 0:   0     1     2     3     4
desde -1: -5    -4    -3    -2    -1
```

Y lo más importante: una variable no contiene la lista, **apunta** a ella. `b = a` no copia nada; pega una segunda etiqueta a la misma lista.

## Construcción

### 1 · Índices negativos y rebanadas

Las rebanadas funcionan como en las cadenas: `lista[inicio:fin:paso]`, con el `fin` sin incluir.

```{code-cell} python
letras = ["a", "b", "c", "d", "e"]
print(letras[-1], letras[-2])
print(letras[1:4], letras[:2], letras[3:])
print(letras[::2], letras[::-1])
print(letras[-3:])
```

### 2 · Alias o copia

:::{tip} Predice
Al final, ¿cuántos elementos tiene `a`? ¿Le afecta el `c[0] = 99`?
:::

```{code-cell} python
a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c[0] = 99
print(a, b, c)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Dos etiquetas, una lista","etiqueta":"alias · copia con [:]","idea":"b = a no copia: a y b son la misma lista. Por eso, al hacer b.append(4), también cambia a. En cambio, a[:] fabrica una lista nueva: c es independiente, y cambiarla no toca a.","columnas":["a","b","c"],"fila_en":"cada_linea"},"traza":{"codigo":"a = [1, 2, 3]\nb = a\nc = a[:]\nb.append(4)\nc[0] = 99\nprint(a, b, c)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"a":[1,2,3]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"a":"[1, 2, 3]"},"tipos":{"a":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"a":[1,2,3],"b":[1,2,3]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"a":"[1, 2, 3]","b":"[1, 2, 3]"},"tipos":{"a":"list","b":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":[1,2,3],"b":[1,2,3],"c":[1,2,3]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"a":"[1, 2, 3]","b":"[1, 2, 3]","c":"[1, 2, 3]"},"tipos":{"a":"list","b":"list","c":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":[1,2,3,4],"b":[1,2,3,4],"c":[1,2,3]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"a":"[1, 2, 3, 4]","b":"[1, 2, 3, 4]","c":"[1, 2, 3]"},"tipos":{"a":"list","b":"list","c":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":[1,2,3,4],"b":[1,2,3,4],"c":[99,2,3]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"a":"[1, 2, 3, 4]","b":"[1, 2, 3, 4]","c":"[99, 2, 3]"},"tipos":{"a":"list","b":"list","c":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"a":[1,2,3,4],"b":[1,2,3,4],"c":[99,2,3]},"salida":"[1, 2, 3, 4] [1, 2, 3, 4] [99, 2, 3]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"a":"[1, 2, 3, 4]","b":"[1, 2, 3, 4]","c":"[99, 2, 3]"},"tipos":{"a":"list","b":"list","c":"list"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","[1, 2, 3]","—","—"],["2","[1, 2, 3]","[1, 2, 3]","—"],["3","[1, 2, 3]","[1, 2, 3]","[1, 2, 3]"],["4","[1, 2, 3, 4]","[1, 2, 3, 4]","[1, 2, 3]"],["5","[1, 2, 3, 4]","[1, 2, 3, 4]","[99, 2, 3]"],["6","[1, 2, 3, 4]","[1, 2, 3, 4]","[99, 2, 3]"]]}}
```

Tres maneras de copiar una lista: `a[:]`, `list(a)` y `a.copy()`. Para comprobar si dos variables son la misma lista, usa `is`: `a is b` da `True`, `a is c` da `False`.

:::{warning} Una copia con `[:]` es superficial
Si la lista contiene otras listas, `[:]` copia la lista de fuera, pero las de dentro siguen compartidas. Para copiarlo todo, hasta el fondo, existe `copy.deepcopy`.
:::

### 3 · Insertar, buscar y quitar

:::{tip} Predice
¿Quién queda primero en la cola después de cada línea? ¿Qué se guarda en `atendida`?
:::

```{code-cell} python
cola = ["Ana", "Biel", "Carla"]
cola.insert(1, "Dani")
cola.append("Eva")
del cola[0]
atendida = cola.pop(0)
print(cola, atendida, "Eva" in cola)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"La cola del comedor","etiqueta":"insert · append · del · pop","idea":"insert mete un elemento en medio y corre los demás a la derecha; del y pop quitan uno y corren los demás a la izquierda. La diferencia: pop además devuelve lo que quita.","lista":"cola","foco":"ninguno","columnas":["cola","atendida"],"fila_en":"cada_linea"},"traza":{"codigo":"cola = [\"Ana\", \"Biel\", \"Carla\"]\ncola.insert(1, \"Dani\")\ncola.append(\"Eva\")\ndel cola[0]\natendida = cola.pop(0)\nprint(cola, atendida, \"Eva\" in cola)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"cola":["Ana","Biel","Carla"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"cola":"['Ana', 'Biel', 'Carla']"},"tipos":{"cola":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"cola":["Ana","Dani","Biel","Carla"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"cola":"['Ana', 'Dani', 'Biel', 'Carla']"},"tipos":{"cola":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"cola":["Ana","Dani","Biel","Carla","Eva"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"cola":"['Ana', 'Dani', 'Biel', 'Carla', 'Eva']"},"tipos":{"cola":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"cola":["Dani","Biel","Carla","Eva"]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"cola":"['Dani', 'Biel', 'Carla', 'Eva']"},"tipos":{"cola":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"cola":["Biel","Carla","Eva"],"atendida":"Dani"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"cola":"['Biel', 'Carla', 'Eva']","atendida":"'Dani'"},"tipos":{"cola":"list","atendida":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"cola":["Biel","Carla","Eva"],"atendida":"Dani"},"salida":"['Biel', 'Carla', 'Eva'] Dani True\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"cola":"['Biel', 'Carla', 'Eva']","atendida":"'Dani'"},"tipos":{"cola":"list","atendida":"str"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","['Ana', 'Biel', 'Carla']","—"],["2","['Ana', 'Dani', 'Biel', 'Carla']","—"],["3","['Ana', 'Dani', 'Biel', 'Carla', 'Eva']","—"],["4","['Dani', 'Biel', 'Carla', 'Eva']","—"],["5","['Biel', 'Carla', 'Eva']","'Dani'"],["6","['Biel', 'Carla', 'Eva']","'Dani'"]]}}
```

| Operación | Qué hace | Devuelve |
|---|---|---|
| `lista.append(x)` | añade `x` al final | `None` |
| `lista.insert(i, x)` | mete `x` en la posición `i` | `None` |
| `lista.index(x)` | busca la posición de la primera `x` (error si no está) | la posición |
| `lista.count(x)` | cuenta cuántas `x` hay | un número |
| `lista.remove(x)` | quita la primera `x` (error si no está) | `None` |
| `lista.pop(i)` | quita la de la posición `i` (sin `i`, la última) | el elemento quitado |
| `del lista[i]` | quita la de la posición `i`; también rebanadas: `del lista[1:3]` | (es una sentencia) |
| `x in lista`, `x not in lista` | ¿está o no está? | `True` o `False` |
| `len(lista)` | cuántos elementos tiene | un número |

### 4 · Ordenar: `sort` o `sorted`

```{code-cell} python
notas = [7, 4, 9, 5]
ordenadas = sorted(notas)        # fabrica una lista nueva; notas no cambia
print(notas, ordenadas)
notas.sort(reverse=True)         # ordena notas en su sitio
print(notas)
resultado = notas.sort()
print(resultado)                 # sort no devuelve la lista: devuelve None
```

:::{warning} Trampa · `lista = lista.sort()`
`sort()` cambia la lista y devuelve `None`. Si escribes `notas = notas.sort()`, acabas con `notas = None` y has perdido la lista. Usa `notas.sort()` a secas, o `notas = sorted(notas)`.
:::

`reverse()` le da la vuelta a una lista en su sitio; `lista[::-1]` fabrica una nueva al revés.

### 5 · Tablas: listas de listas

Una tabla con filas y columnas es una lista cuyos elementos son listas: cada una, una fila. Para llegar a una casilla se usan **dos índices**: primero la fila, luego la columna.

:::{tip} Predice
¿Por qué casillas pasa el recorrido, y en qué orden? ¿Qué medias saldrán?
:::

```{code-cell} python
notas = [[7, 5, 9], [6, 8, 4]]
medias = []
for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma = suma + notas[i][j]
    medias.append(suma / len(notas[i]))
print(medias)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Las medias de cada alumno","etiqueta":"lista de listas · dos índices","idea":"Cada fila es un alumno y cada columna, un examen. El bucle de fuera elige la fila con i; el de dentro recorre sus columnas con j. notas[i][j] es la casilla de la fila i y la columna j.","matriz":"notas","fila":"i","col":"j","columnas":["i","j","suma","medias"],"fila_en":"cada_linea"},"traza":{"codigo":"notas = [[7, 5, 9], [6, 8, 4]]\nmedias = []\nfor i in range(len(notas)):\n    suma = 0\n    for j in range(len(notas[i])):\n        suma = suma + notas[i][j]\n    medias.append(suma / len(notas[i]))\nprint(medias)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"notas":[[7,5,9],[6,8,4]]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]"},"tipos":{"notas":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]"},"tipos":{"notas":"list","medias":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[],"i":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]","i":"0"},"tipos":{"notas":"list","medias":"list","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[],"i":0,"suma":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]","i":"0","suma":"0"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[],"i":0,"suma":0,"j":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]","i":"0","suma":"0","j":"0"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[],"i":0,"suma":7,"j":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]","i":"0","suma":"7","j":"0"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[],"i":0,"suma":7,"j":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]","i":"0","suma":"7","j":"1"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[],"i":0,"suma":12,"j":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]","i":"0","suma":"12","j":"1"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[],"i":0,"suma":12,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":7,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]","i":"0","suma":"12","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[],"i":0,"suma":21,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":8,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]","i":"0","suma":"21","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[],"i":0,"suma":21,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":9,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[]","i":"0","suma":"21","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":0,"suma":21,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":10,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"0","suma":"21","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":1,"suma":21,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":11,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"1","suma":"21","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":1,"suma":0,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":12,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"1","suma":"0","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":1,"suma":0,"j":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":13,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"1","suma":"0","j":"0"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":1,"suma":6,"j":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":14,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"1","suma":"6","j":"0"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":1,"suma":6,"j":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":15,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"1","suma":"6","j":"1"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":1,"suma":14,"j":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":16,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"1","suma":"14","j":"1"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":1,"suma":14,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":17,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"1","suma":"14","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":1,"suma":18,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":18,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"1","suma":"18","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0],"i":1,"suma":18,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":19,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0]","i":"1","suma":"18","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0,6.0],"i":1,"suma":18,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":20,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0, 6.0]","i":"1","suma":"18","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0,6.0],"i":1,"suma":18,"j":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":21,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0, 6.0]","i":"1","suma":"18","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{"notas":[[7,5,9],[6,8,4]],"medias":[7.0,6.0],"i":1,"suma":18,"j":2},"salida":"[7.0, 6.0]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":22,"repr":{"notas":"[[7, 5, 9], [6, 8, 4]]","medias":"[7.0, 6.0]","i":"1","suma":"18","j":"2"},"tipos":{"notas":"list","medias":"list","i":"int","suma":"int","j":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["2","—","—","—","[]"],["3","0","—","—","[]"],["4","0","—","0","[]"],["5","0","0","0","[]"],["6","0","0","7","[]"],["5","0","1","7","[]"],["6","0","1","12","[]"],["5","0","2","12","[]"],["6","0","2","21","[]"],["5","0","2","21","[]"],["7","0","2","21","[7.0]"],["3","1","2","21","[7.0]"],["4","1","2","0","[7.0]"],["5","1","0","0","[7.0]"],["6","1","0","6","[7.0]"],["5","1","1","6","[7.0]"],["6","1","1","14","[7.0]"],["5","1","2","14","[7.0]"],["6","1","2","18","[7.0]"],["5","1","2","18","[7.0]"],["7","1","2","18","[7.0, 6.0]"],["3","1","2","18","[7.0, 6.0]"],["8","1","2","18","[7.0, 6.0]"]]}}
```

Una casilla se cambia igual que en una lista normal, con sus dos índices. Y si se anidan más niveles, se obtienen «cubos»: `cubo[capa][fila][columna]`.

```{code-cell} python
notas = [[7, 5, 9], [6, 8, 4]]
notas[1][2] = 10
print(notas, len(notas), len(notas[0]))

tablero = [[0] * 3 for _ in range(3)]       # 3 × 3 de ceros, filas independientes
tablero[1][1] = "X"
print(tablero)

cubo = [[[0] * 2 for _ in range(2)] for _ in range(2)]
cubo[1][0][1] = 5
print(cubo)
```

:::{warning} Trampa · `[[0] * 3] * 3`
Parece un tablero de 3 × 3, pero son **tres etiquetas de la misma fila**: al cambiar una casilla, cambia en las tres filas. Por eso las filas se fabrican con una comprensión, como arriba, para que cada una sea una lista distinta.
:::

## Conexiones

- La idea de las etiquetas reaparecerá con los objetos, en [Clases y objetos](14-clases.md): las variables nunca son cajas, siempre etiquetas.
- `sorted` y `sort` aceptan además un criterio de orden, `key`, que verás en [Funciones como valores](16-funciones-valores.md).
- Las rebanadas de listas funcionan igual que las de [Cadenas](10-cadenas.md); la diferencia es que una lista sí se puede modificar.

## La grieta

Una lista se puede cambiar en cualquier momento, y a veces eso es un peligro. ¿Hay una lista que no se pueda tocar? ¿Y una colección que no admita repetidos? Son las tuplas y los conjuntos.

## Preguntas tipo examen

Preguntas como las del examen PCEP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","capitulo":"22","titulo":"Preguntas tipo examen","etiqueta":"PCEP"}}
```

## Ejercicios

1. **Índices negativos.** Con `dias = ["lun", "mar", "mié", "jue", "vie"]`, escribe las expresiones que dan: el último, los dos últimos y la lista al revés.
2. **¿Qué imprime?**

   ```python
   x = [1, 2]
   y = x
   y = y + [3]
   print(x, y)
   ```

3. **Quitar todos.** Escribe un programa que quite todos los `0` de `datos = [3, 0, 5, 0, 0, 2]` usando `remove` y `in`.
4. **El total de la tabla.** Suma todas las casillas de `notas = [[7, 5, 9], [6, 8, 4]]` con dos bucles anidados.
5. **La diagonal.** Para la tabla `m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, escribe una comprensión que dé su diagonal, `[1, 5, 9]`.

El solucionario está al final del capítulo.

## Solucionario

1. `dias[-1]` da `'vie'`; `dias[-2:]` da `['jue', 'vie']`; `dias[::-1]` da la lista al revés.
2. Imprime **[1, 2] [1, 2, 3]**. `y + [3]` **fabrica una lista nueva** y le pega la etiqueta `y`; `x` sigue apuntando a la vieja. Con `y.append(3)` sí habría cambiado `x`.
3. Una solución:

   ```python
   datos = [3, 0, 5, 0, 0, 2]
   while 0 in datos:
       datos.remove(0)
   print(datos)
   ```

   Imprime `[3, 5, 2]`. También vale `datos = [d for d in datos if d != 0]`.
4. Una solución:

   ```python
   total = 0
   for fila in notas:
       for nota in fila:
           total = total + nota
   print(total)
   ```

   Imprime `39`.
5. `[m[i][i] for i in range(len(m))]`.
