---
title: Recorrer listas
subtitle: Visitar cada casilla, una vez y en orden
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Tienes en la mano la hoja de notas de clase y te piden la suma. No lo piensas: pones el dedo en la primera nota, la sumas de cabeza, bajas el dedo a la siguiente, la sumas, y así hasta el final. Cuando el dedo se sale de la columna, has terminado.

## La pregunta

Tu dedo hace tres cosas sin que te des cuenta: **empieza** en la primera nota, **avanza** a la siguiente y **sabe parar** cuando no quedan más. ¿Cómo se le dice todo eso a un ordenador?

## La idea

Una lista de Python es una fila de casillas numeradas **desde 0**. Recorrerla es visitar cada casilla una vez, en orden. Hay dos maneras de hacerlo:

- **Por elemento**: el bucle te va dando el contenido de cada casilla. No sabes en qué posición estás, ni te hace falta.
- **Por posición**: el bucle te va dando los números de casilla (0, 1, 2…) y tú consultas la lista con `notas[i]`.

:::{important} El dedo es una variable
El dedo que avanza por la hoja es una variable que cambia en cada vuelta del bucle: `nota` si recorres por elemento, `i` si recorres por posición. En los visualizadores la verás como un puntero sobre las casillas.
:::

## Construcción

### 1 · Recorrer y sumar

:::{tip} Predice
Antes de ejecutar: ¿cuántas vueltas dará el bucle? ¿Cuánto valdrá `total` al terminar la tercera?
:::

```{code-cell} python
notas = [7, 4, 9, 6, 8]
total = 0
for nota in notas:
    total = total + nota
print("Suma:", total)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Recorrer una lista y sumar","etiqueta":"for · elemento a elemento","idea":"El bucle no usa posiciones: en cada vuelta, Python le entrega a la variable nota el siguiente elemento de la lista.","lista":"notas","cabecera":3,"puntero":"nota","foco":"vuelta","columnas":["nota","total"],"fila_en":"fin_iteracion"},"traza":{"codigo":"notas = [7, 4, 9, 6, 8]\ntotal = 0\nfor nota in notas:\n    total = total + nota\nprint(\"Suma:\", total)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{}},{"linea":1,"estado":{"notas":[7,4,9,6,8]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]"},"tipos":{"notas":"list"}},{"linea":2,"estado":{"notas":[7,4,9,6,8],"total":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"0"},"tipos":{"notas":"list","total":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":0,"nota":7},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"0","nota":"7"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":7,"nota":7},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"7","nota":"7"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":7,"nota":4},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"7","nota":"4"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":11,"nota":4},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"11","nota":"4"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":11,"nota":9},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"11","nota":"9"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":20,"nota":9},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"20","nota":"9"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":20,"nota":6},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"20","nota":"6"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":26,"nota":6},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"26","nota":"6"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":26,"nota":8},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":5,"fila":3,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"26","nota":"8"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":34,"nota":8},"salida":"","foco":4,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"34","nota":"8"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":34,"nota":8},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":4,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"34","nota":"8"},"tipos":{"notas":"list","total":"int","nota":"int"}},{"linea":5,"estado":{"notas":[7,4,9,6,8],"total":34,"nota":8},"salida":"Suma: 34\n","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"34","nota":"8"},"tipos":{"notas":"list","total":"int","nota":"int"}}],"filas":[["7","7"],["4","11"],["9","20"],["6","26"],["8","34"]]}}
```

`total` es un **acumulador**: empieza en 0 y en cada vuelta se le suma lo que trae `nota`. Fíjate en la tabla de traza: la columna `total` es la suma parcial hasta esa casilla.

### 2 · Recorrer por posición

:::{tip} Predice
En la tercera vuelta, ¿cuánto vale `i`? ¿Y `notas[i]`?
:::

```{code-cell} python
notas = [7, 4, 9, 6, 8]
total = 0
for i in range(len(notas)):
    total = total + notas[i]
print("Media:", total / len(notas))
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Recorrer por posición","etiqueta":"for · con índice","idea":"Aquí el bucle recorre posiciones: i vale 0, 1, 2… y notas[i] consulta la casilla de esa posición.","lista":"notas","cabecera":3,"puntero":"i","foco":"i","columnas":["i","notas[i]","total"],"fila_en":"fin_iteracion","soltar":5},"traza":{"codigo":"notas = [7, 4, 9, 6, 8]\ntotal = 0\nfor i in range(len(notas)):\n    total = total + notas[i]\nprint(\"Media:\", total / len(notas))","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{}},{"linea":1,"estado":{"notas":[7,4,9,6,8]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]"},"tipos":{"notas":"list"}},{"linea":2,"estado":{"notas":[7,4,9,6,8],"total":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"0"},"tipos":{"notas":"list","total":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":0,"i":0},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"0","i":"0"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":7,"i":0},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"7","i":"0"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":7,"i":1},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"7","i":"1"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":11,"i":1},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"11","i":"1"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":11,"i":2},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"11","i":"2"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":20,"i":2},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"20","i":"2"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":20,"i":3},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"20","i":"3"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":26,"i":3},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"26","i":"3"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":26,"i":4},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":5,"fila":3,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"26","i":"4"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"total":34,"i":4},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":5,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"34","i":"4"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"total":34,"i":4},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":6,"fila":4,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"34","i":"4"},"tipos":{"notas":"list","total":"int","i":"int"}},{"linea":5,"estado":{"notas":[7,4,9,6,8],"total":34,"i":4},"salida":"Media: 6.8\n","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","total":"34","i":"4"},"tipos":{"notas":"list","total":"int","i":"int"}}],"filas":[["0","7","7"],["1","4","11"],["2","9","20"],["3","6","26"],["4","8","34"]]}}
```

`range(len(notas))` produce los números 0, 1, 2, 3 y 4: justo las posiciones de una lista de 5 casillas. El último es 4, no 5. Por eso las posiciones empiezan en 0.

### 3 · El campeón provisional

:::{tip} Predice
¿En qué vueltas cambiará `maximo`? Señálalas antes de pulsar «Paso».
:::

```{code-cell} python
notas = [7, 4, 9, 6, 8]
maximo = notas[0]
for i in range(1, len(notas)):
    if notas[i] > maximo:
        maximo = notas[i]
print("Máximo:", maximo)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El campeón provisional","etiqueta":"for + if · el máximo","idea":"maximo guarda al campeón provisional. Cada casilla nueva lo reta: si es mayor, ocupa su puesto.","lista":"notas","cabecera":3,"puntero":"i","foco":"i","columnas":["i","notas[i]","maximo"],"fila_en":"fin_iteracion","soltar":6},"traza":{"codigo":"notas = [7, 4, 9, 6, 8]\nmaximo = notas[0]\nfor i in range(1, len(notas)):\n    if notas[i] > maximo:\n        maximo = notas[i]\nprint(\"Máximo:\", maximo)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{}},{"linea":1,"estado":{"notas":[7,4,9,6,8]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]"},"tipos":{"notas":"list"}},{"linea":2,"estado":{"notas":[7,4,9,6,8],"maximo":7},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"7"},"tipos":{"notas":"list","maximo":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"maximo":7,"i":1},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"7","i":"1"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"maximo":7,"i":1},"salida":"","foco":1,"lee":true,"cond":{"expr":"notas[i] > maximo","sust":"4 > 7","valor":false},"vuelta":1,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"7","i":"1"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"maximo":7,"i":2},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"7","i":"2"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"maximo":7,"i":2},"salida":"","foco":2,"lee":true,"cond":{"expr":"notas[i] > maximo","sust":"9 > 7","valor":true},"vuelta":2,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"7","i":"2"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":5,"estado":{"notas":[7,4,9,6,8],"maximo":9,"i":2},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":2,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"9","i":"2"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"maximo":9,"i":3},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"9","i":"3"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"maximo":9,"i":3},"salida":"","foco":3,"lee":true,"cond":{"expr":"notas[i] > maximo","sust":"6 > 9","valor":false},"vuelta":3,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"9","i":"3"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"maximo":9,"i":4},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"9","i":"4"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"maximo":9,"i":4},"salida":"","foco":4,"lee":true,"cond":{"expr":"notas[i] > maximo","sust":"8 > 9","valor":false},"vuelta":4,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"9","i":"4"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"maximo":9,"i":4},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":5,"fila":3,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"9","i":"4"},"tipos":{"notas":"list","maximo":"int","i":"int"}},{"linea":6,"estado":{"notas":[7,4,9,6,8],"maximo":9,"i":4},"salida":"Máximo: 9\n","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","maximo":"9","i":"4"},"tipos":{"notas":"list","maximo":"int","i":"int"}}],"filas":[["1","4","7"],["2","9","9"],["3","6","9"],["4","8","9"]]}}
```

El bucle empieza en la posición 1 porque la casilla 0 ya es el campeón inicial. Dentro del bucle hay un `if`: el visualizador te muestra la condición con los valores sustituidos, por ejemplo `4 > 7 → False`.

### 4 · Buscar un valor

:::{tip} Predice
¿Cuántas veces se comprobará la condición del `while` antes de encontrar el 6?
:::

```{code-cell} python
notas = [7, 4, 9, 6, 8]
buscada = 6
i = 0
while i < len(notas) and notas[i] != buscada:
    i = i + 1
if i < len(notas):
    print("Está en la posición", i)
else:
    print("No está")
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Buscar un valor","etiqueta":"while · búsqueda lineal","idea":"El while no sabe cuántas vueltas dará: se repite mientras queden casillas y la actual no sea la buscada.","lista":"notas","cabecera":4,"puntero":"i","foco":"i","columnas":["i","notas[i]"],"fila_en":"comprobacion"},"traza":{"codigo":"notas = [7, 4, 9, 6, 8]\nbuscada = 6\ni = 0\nwhile i < len(notas) and notas[i] != buscada:\n    i = i + 1\nif i < len(notas):\n    print(\"Está en la posición\", i)\nelse:\n    print(\"No está\")","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{}},{"linea":1,"estado":{"notas":[7,4,9,6,8]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]"},"tipos":{"notas":"list"}},{"linea":2,"estado":{"notas":[7,4,9,6,8],"buscada":6},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6"},"tipos":{"notas":"list","buscada":"int"}},{"linea":3,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":0},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"0"},"tipos":{"notas":"list","buscada":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":0},"salida":"","foco":0,"lee":true,"cond":{"expr":"i < len(notas) and notas[i] != buscada","sust":"0 < 5 and 7 != 6","valor":true},"vuelta":1,"fila":0,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"0"},"tipos":{"notas":"list","buscada":"int","i":"int"}},{"linea":5,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":1},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"1"},"tipos":{"notas":"list","buscada":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":1},"salida":"","foco":1,"lee":true,"cond":{"expr":"i < len(notas) and notas[i] != buscada","sust":"1 < 5 and 4 != 6","valor":true},"vuelta":2,"fila":1,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"1"},"tipos":{"notas":"list","buscada":"int","i":"int"}},{"linea":5,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":2},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"2"},"tipos":{"notas":"list","buscada":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":2},"salida":"","foco":2,"lee":true,"cond":{"expr":"i < len(notas) and notas[i] != buscada","sust":"2 < 5 and 9 != 6","valor":true},"vuelta":3,"fila":2,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"2"},"tipos":{"notas":"list","buscada":"int","i":"int"}},{"linea":5,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":3},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"3"},"tipos":{"notas":"list","buscada":"int","i":"int"}},{"linea":4,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":3},"salida":"","foco":3,"lee":true,"cond":{"expr":"i < len(notas) and notas[i] != buscada","sust":"3 < 5 and 6 != 6","valor":false},"vuelta":4,"fila":3,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"3"},"tipos":{"notas":"list","buscada":"int","i":"int"}},{"linea":6,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":3},"salida":"","foco":3,"lee":false,"cond":{"expr":"i < len(notas)","sust":"3 < 5","valor":true},"vuelta":4,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"3"},"tipos":{"notas":"list","buscada":"int","i":"int"}},{"linea":7,"estado":{"notas":[7,4,9,6,8],"buscada":6,"i":3},"salida":"Está en la posición 3\n","foco":3,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"notas":"[7, 4, 9, 6, 8]","buscada":"6","i":"3"},"tipos":{"notas":"list","buscada":"int","i":"int"}}],"filas":[["0","7","Sí"],["1","4","Sí"],["2","9","Sí"],["3","6","No"]]}}
```

Aquí el bucle es un `while`, porque no sabemos de antemano cuántas casillas hará falta mirar. En cuanto encuentra el 6, deja de buscar.

## Conexiones

- La **suma** lleva a la media, y la media a la estadística: el capítulo de funciones empezará por `media(lista)`.
- El **campeón provisional** es la semilla de los algoritmos de ordenación: ordenar es buscar el máximo una y otra vez.
- El **acumulador**, el **contador** y el **campeón provisional** son los tres patrones que vas a reconocer en casi todos los programas que recorren datos.

## La grieta

Para buscar el 6 hemos mirado las casillas una a una. Si la lista estuviera **ordenada**, ¿haría falta mirarlas todas? Piensa en cómo buscas una palabra en el diccionario. Esa pregunta abre la búsqueda binaria.

## Ejercicios

1. **Traza a mano.** Haz la tabla de traza de este programa con `notas = [7, 4, 9, 6, 3]`. ¿Qué imprime?

   ```python
   aprobados = 0
   for nota in notas:
       if nota >= 5:
           aprobados = aprobados + 1
   print(aprobados)
   ```

2. **¿Qué imprime?** Con la misma lista:

   ```python
   for i in range(len(notas)):
       if notas[i] < 5:
           print(i)
   ```

3. **Buscar lo que no está.** En el programa de búsqueda, cambia `buscada = 6` por `buscada = 5`. ¿Qué imprime? ¿Por qué no da error al llegar a `i = 5`, si la lista no tiene casilla 5?

El solucionario está al final del capítulo.

## Solucionario

1. La tabla tiene 5 vueltas: `nota` vale 7, 4, 9, 6, 3 y `aprobados` vale 1, 1, 2, 3, 3. Imprime **3**. `aprobados` es un **contador**: suma 1 cada vez que se cumple la condición.
2. Imprime **1** y **4**: las posiciones de las notas menores que 5 (el 4 y el 3). Ojo: imprime posiciones, no notas.
3. Imprime **No está**. Cuando `i` llega a 5, la primera parte del `and`, `i < len(notas)`, ya es `False`, y Python no evalúa la segunda: nunca intenta leer `notas[5]`. Si escribieras las dos condiciones al revés, el programa daría `IndexError`. El orden importa.
