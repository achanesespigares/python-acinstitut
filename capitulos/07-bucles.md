---
title: Bucles while y for
subtitle: Repetir sin copiar
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Antes de un despegue, alguien cuenta hacia atrás: cinco, cuatro, tres, dos, uno… ¡despegue! Nadie le dice cada número por separado. Sabe tres cosas: **por dónde empezar**, **cuándo parar** y **cómo pasar al siguiente** (restar uno).

## La pregunta

¿Cómo le pedimos a un programa que repita algo sin escribir la misma línea una y otra vez?

## La idea

Un **bucle** repite un bloque de código. Todo bucle tiene tres partes, como la cuenta atrás:

1. **Inicio**: el valor con el que se empieza (`n = 5`).
2. **Condición**: la pregunta que decide si se da otra vuelta (`n > 0`).
3. **Avance**: lo que cambia en cada vuelta para acercarse al final (`n = n - 1`).

Python tiene dos bucles:

- `while` repite **mientras** una condición sea cierta. Se usa cuando no sabemos cuántas vueltas habrá.
- `for` recorre una **secuencia conocida** de valores, por ejemplo los números que da `range`.

## Construcción

### 1 · La cuenta atrás con `while`

:::{tip} Predice
¿Cuántas veces se comprobará la condición `n > 0`? Ojo: no son 5.
:::

```{code-cell} python
n = 5
while n > 0:
    print(n)
    n = n - 1
print("¡Despegue!")
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"La cuenta atrás","etiqueta":"while · inicio, condición, avance","idea":"Antes de cada vuelta se comprueba n > 0. Dentro, n baja de uno en uno. Cuando n llega a 0, la condición es False y el bucle termina.","cabecera":2,"puntero":"n","columnas":["n"],"fila_en":"comprobacion"},"traza":{"codigo":"n = 5\nwhile n > 0:\n    print(n)\n    n = n - 1\nprint(\"¡Despegue!\")","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{}},{"linea":1,"estado":{"n":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"n":"5"},"tipos":{"n":"int"}},{"linea":2,"estado":{"n":5},"salida":"","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"5 > 0","valor":true},"vuelta":1,"fila":0,"repr":{"n":"5"},"tipos":{"n":"int"}},{"linea":3,"estado":{"n":5},"salida":"5\n","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"n":"5"},"tipos":{"n":"int"}},{"linea":4,"estado":{"n":4},"salida":"5\n","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"n":"4"},"tipos":{"n":"int"}},{"linea":2,"estado":{"n":4},"salida":"5\n","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"4 > 0","valor":true},"vuelta":2,"fila":1,"repr":{"n":"4"},"tipos":{"n":"int"}},{"linea":3,"estado":{"n":4},"salida":"5\n4\n","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"n":"4"},"tipos":{"n":"int"}},{"linea":4,"estado":{"n":3},"salida":"5\n4\n","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"n":"3"},"tipos":{"n":"int"}},{"linea":2,"estado":{"n":3},"salida":"5\n4\n","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"3 > 0","valor":true},"vuelta":3,"fila":2,"repr":{"n":"3"},"tipos":{"n":"int"}},{"linea":3,"estado":{"n":3},"salida":"5\n4\n3\n","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"n":"3"},"tipos":{"n":"int"}},{"linea":4,"estado":{"n":2},"salida":"5\n4\n3\n","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"n":"2"},"tipos":{"n":"int"}},{"linea":2,"estado":{"n":2},"salida":"5\n4\n3\n","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"2 > 0","valor":true},"vuelta":4,"fila":3,"repr":{"n":"2"},"tipos":{"n":"int"}},{"linea":3,"estado":{"n":2},"salida":"5\n4\n3\n2\n","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"n":"2"},"tipos":{"n":"int"}},{"linea":4,"estado":{"n":1},"salida":"5\n4\n3\n2\n","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"n":"1"},"tipos":{"n":"int"}},{"linea":2,"estado":{"n":1},"salida":"5\n4\n3\n2\n","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"1 > 0","valor":true},"vuelta":5,"fila":4,"repr":{"n":"1"},"tipos":{"n":"int"}},{"linea":3,"estado":{"n":1},"salida":"5\n4\n3\n2\n1\n","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"n":"1"},"tipos":{"n":"int"}},{"linea":4,"estado":{"n":0},"salida":"5\n4\n3\n2\n1\n","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"n":"0"},"tipos":{"n":"int"}},{"linea":2,"estado":{"n":0},"salida":"5\n4\n3\n2\n1\n","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"0 > 0","valor":false},"vuelta":6,"fila":5,"repr":{"n":"0"},"tipos":{"n":"int"}},{"linea":5,"estado":{"n":0},"salida":"5\n4\n3\n2\n1\n¡Despegue!\n","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"n":"0"},"tipos":{"n":"int"}}],"filas":[["5","Sí"],["4","Sí"],["3","Sí"],["2","Sí"],["1","Sí"],["0","No"]]}}
```

La condición se comprueba **6 veces**: cinco veces sale `True` (con n = 5, 4, 3, 2, 1) y la sexta sale `False` (con n = 0). Esa última comprobación es la que hace salir del bucle.

:::{warning} Trampa · el bucle infinito
Si olvidas la línea del avance (`n = n - 1`), `n` vale 5 para siempre, la condición nunca se vuelve falsa y el programa no termina. Cuando escribas un `while`, comprueba siempre que algo dentro del bucle acerca la condición a `False`.
:::

### 2 · Sumar de 1 a 5 con `for`

:::{tip} Predice
¿Qué números da `range(1, 6)`? ¿Incluye el 6?
:::

```{code-cell} python
suma = 0
for k in range(1, 6):
    suma = suma + k
print(suma)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Sumar de 1 a 5","etiqueta":"for · range","idea":"range(1, 6) da 1, 2, 3, 4 y 5: empieza en el primero y se detiene antes del segundo. El for se encarga solo del inicio, la condición y el avance.","cabecera":2,"puntero":"k","columnas":["k","suma"],"fila_en":"fin_iteracion"},"traza":{"codigo":"suma = 0\nfor k in range(1, 6):\n    suma = suma + k\nprint(suma)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{}},{"linea":1,"estado":{"suma":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"suma":"0"},"tipos":{"suma":"int"}},{"linea":2,"estado":{"suma":0,"k":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"suma":"0","k":"1"},"tipos":{"suma":"int","k":"int"}},{"linea":3,"estado":{"suma":1,"k":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"suma":"1","k":"1"},"tipos":{"suma":"int","k":"int"}},{"linea":2,"estado":{"suma":1,"k":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":0,"repr":{"suma":"1","k":"2"},"tipos":{"suma":"int","k":"int"}},{"linea":3,"estado":{"suma":3,"k":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"suma":"3","k":"2"},"tipos":{"suma":"int","k":"int"}},{"linea":2,"estado":{"suma":3,"k":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":1,"repr":{"suma":"3","k":"3"},"tipos":{"suma":"int","k":"int"}},{"linea":3,"estado":{"suma":6,"k":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"suma":"6","k":"3"},"tipos":{"suma":"int","k":"int"}},{"linea":2,"estado":{"suma":6,"k":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":2,"repr":{"suma":"6","k":"4"},"tipos":{"suma":"int","k":"int"}},{"linea":3,"estado":{"suma":10,"k":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"suma":"10","k":"4"},"tipos":{"suma":"int","k":"int"}},{"linea":2,"estado":{"suma":10,"k":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":3,"repr":{"suma":"10","k":"5"},"tipos":{"suma":"int","k":"int"}},{"linea":3,"estado":{"suma":15,"k":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"suma":"15","k":"5"},"tipos":{"suma":"int","k":"int"}},{"linea":2,"estado":{"suma":15,"k":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":4,"repr":{"suma":"15","k":"5"},"tipos":{"suma":"int","k":"int"}},{"linea":4,"estado":{"suma":15,"k":5},"salida":"15\n","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"suma":"15","k":"5"},"tipos":{"suma":"int","k":"int"}}],"filas":[["1","1"],["2","3"],["3","6"],["4","10"],["5","15"]]}}
```

Con `for` no hay que escribir ni la condición ni el avance: `range` ya sabe por dónde empezar, cómo avanzar y dónde parar. Por eso, cuando sabes cuántas vueltas habrá, `for` es más seguro: no puede quedarse en un bucle infinito.

| Llamada | Valores que da |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

### 3 · Duplicar hasta pasarse de 100

Aquí no sabemos de antemano cuántas vueltas hacen falta: ese es el trabajo del `while`.

:::{tip} Predice
Antes de calcular: ¿cuántas veces hay que duplicar 1 para pasar de 100? Pista: 2 elevado a cuánto.
:::

```{code-cell} python
x = 1
pasos = 0
while x <= 100:
    x = x * 2
    pasos = pasos + 1
print(pasos, x)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Duplicar hasta pasarse de 100","etiqueta":"while · vueltas desconocidas","idea":"No sabemos cuántas vueltas dará: se repite mientras x no pase de 100. pasos es un contador que cuenta las vueltas.","cabecera":3,"puntero":"x","columnas":["x","pasos"],"fila_en":"comprobacion"},"traza":{"codigo":"x = 1\npasos = 0\nwhile x <= 100:\n    x = x * 2\n    pasos = pasos + 1\nprint(pasos, x)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{}},{"linea":1,"estado":{"x":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"x":"1"},"tipos":{"x":"int"}},{"linea":2,"estado":{"x":1,"pasos":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"x":"1","pasos":"0"},"tipos":{"x":"int","pasos":"int"}},{"linea":3,"estado":{"x":1,"pasos":0},"salida":"","foco":null,"lee":false,"cond":{"expr":"x <= 100","sust":"1 <= 100","valor":true},"vuelta":1,"fila":0,"repr":{"x":"1","pasos":"0"},"tipos":{"x":"int","pasos":"int"}},{"linea":4,"estado":{"x":2,"pasos":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"x":"2","pasos":"0"},"tipos":{"x":"int","pasos":"int"}},{"linea":5,"estado":{"x":2,"pasos":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"x":"2","pasos":"1"},"tipos":{"x":"int","pasos":"int"}},{"linea":3,"estado":{"x":2,"pasos":1},"salida":"","foco":null,"lee":false,"cond":{"expr":"x <= 100","sust":"2 <= 100","valor":true},"vuelta":2,"fila":1,"repr":{"x":"2","pasos":"1"},"tipos":{"x":"int","pasos":"int"}},{"linea":4,"estado":{"x":4,"pasos":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"x":"4","pasos":"1"},"tipos":{"x":"int","pasos":"int"}},{"linea":5,"estado":{"x":4,"pasos":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"x":"4","pasos":"2"},"tipos":{"x":"int","pasos":"int"}},{"linea":3,"estado":{"x":4,"pasos":2},"salida":"","foco":null,"lee":false,"cond":{"expr":"x <= 100","sust":"4 <= 100","valor":true},"vuelta":3,"fila":2,"repr":{"x":"4","pasos":"2"},"tipos":{"x":"int","pasos":"int"}},{"linea":4,"estado":{"x":8,"pasos":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"x":"8","pasos":"2"},"tipos":{"x":"int","pasos":"int"}},{"linea":5,"estado":{"x":8,"pasos":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"x":"8","pasos":"3"},"tipos":{"x":"int","pasos":"int"}},{"linea":3,"estado":{"x":8,"pasos":3},"salida":"","foco":null,"lee":false,"cond":{"expr":"x <= 100","sust":"8 <= 100","valor":true},"vuelta":4,"fila":3,"repr":{"x":"8","pasos":"3"},"tipos":{"x":"int","pasos":"int"}},{"linea":4,"estado":{"x":16,"pasos":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"x":"16","pasos":"3"},"tipos":{"x":"int","pasos":"int"}},{"linea":5,"estado":{"x":16,"pasos":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"x":"16","pasos":"4"},"tipos":{"x":"int","pasos":"int"}},{"linea":3,"estado":{"x":16,"pasos":4},"salida":"","foco":null,"lee":false,"cond":{"expr":"x <= 100","sust":"16 <= 100","valor":true},"vuelta":5,"fila":4,"repr":{"x":"16","pasos":"4"},"tipos":{"x":"int","pasos":"int"}},{"linea":4,"estado":{"x":32,"pasos":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"x":"32","pasos":"4"},"tipos":{"x":"int","pasos":"int"}},{"linea":5,"estado":{"x":32,"pasos":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"x":"32","pasos":"5"},"tipos":{"x":"int","pasos":"int"}},{"linea":3,"estado":{"x":32,"pasos":5},"salida":"","foco":null,"lee":false,"cond":{"expr":"x <= 100","sust":"32 <= 100","valor":true},"vuelta":6,"fila":5,"repr":{"x":"32","pasos":"5"},"tipos":{"x":"int","pasos":"int"}},{"linea":4,"estado":{"x":64,"pasos":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"x":"64","pasos":"5"},"tipos":{"x":"int","pasos":"int"}},{"linea":5,"estado":{"x":64,"pasos":6},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"x":"64","pasos":"6"},"tipos":{"x":"int","pasos":"int"}},{"linea":3,"estado":{"x":64,"pasos":6},"salida":"","foco":null,"lee":false,"cond":{"expr":"x <= 100","sust":"64 <= 100","valor":true},"vuelta":7,"fila":6,"repr":{"x":"64","pasos":"6"},"tipos":{"x":"int","pasos":"int"}},{"linea":4,"estado":{"x":128,"pasos":6},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":7,"fila":null,"repr":{"x":"128","pasos":"6"},"tipos":{"x":"int","pasos":"int"}},{"linea":5,"estado":{"x":128,"pasos":7},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":7,"fila":null,"repr":{"x":"128","pasos":"7"},"tipos":{"x":"int","pasos":"int"}},{"linea":3,"estado":{"x":128,"pasos":7},"salida":"","foco":null,"lee":false,"cond":{"expr":"x <= 100","sust":"128 <= 100","valor":false},"vuelta":8,"fila":7,"repr":{"x":"128","pasos":"7"},"tipos":{"x":"int","pasos":"int"}},{"linea":6,"estado":{"x":128,"pasos":7},"salida":"7 128\n","foco":null,"lee":false,"cond":null,"vuelta":8,"fila":null,"repr":{"x":"128","pasos":"7"},"tipos":{"x":"int","pasos":"int"}}],"filas":[["1","0","Sí"],["2","1","Sí"],["4","2","Sí"],["8","3","Sí"],["16","4","Sí"],["32","5","Sí"],["64","6","Sí"],["128","7","No"]]}}
```

Si habías predicho 7, acertaste: 2⁶ = 64 todavía no pasa de 100, y 2⁷ = 128 sí. Predecir antes de ejecutar te permite comprobar que el programa hace lo que crees.

## ¿`while` o `for`?

| Si… | Usa |
|---|---|
| sabes cuántas vueltas habrá, o vas a recorrer una secuencia | `for` |
| repites hasta que pase algo, sin saber cuándo | `while` |

## Conexiones

- El contador `pasos = pasos + 1` y el acumulador `suma = suma + k` son el marcador del capítulo de variables, repetido dentro de un bucle.
- Un bucle con un `if` dentro ya es un algoritmo completo: asignación, condicional e iteración, las tres piezas.

## La grieta

Hemos repetido cosas con números que generábamos nosotros. ¿Y si los datos ya existen, como las notas de toda una clase? Para eso Python tiene las listas, y recorrerlas es el tema del capítulo siguiente: [Recorrer listas](08-recorrer-listas.md).

## Ejercicios

1. **Traza a mano** este bucle. ¿Qué imprime?

   ```python
   i = 1
   while i < 20:
       i = i * 3
   print(i)
   ```

2. **Escribe con `for`** un programa que imprima los múltiplos de 5 desde 5 hasta 50.
3. **El bucle roto.** ¿Por qué este programa no termina nunca? Arréglalo.

   ```python
   n = 10
   while n != 0:
       n = n - 3
   ```

El solucionario está al final del capítulo.

## Solucionario

1. `i` vale 1 → 3 → 9 → 27. Con `i = 27`, la condición `27 < 20` es falsa y sale. Imprime **27**.
2. Una solución:

   ```python
   for m in range(5, 51, 5):
       print(m)
   ```

   El final es 51 porque `range` se detiene antes del segundo número.
3. `n` vale 10, 7, 4, 1, −2, −5… y nunca es exactamente 0, así que `n != 0` es siempre verdadera. Se arregla usando una condición que sí llegue a fallar: `while n > 0:`.
