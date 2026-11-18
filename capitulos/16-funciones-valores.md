---
title: Funciones como valores
subtitle: lambda, map, filter, cierres y generadores
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Cuando le dices a alguien «ordena estas fichas *por fecha*», no solo le das las fichas: le das también un criterio. El criterio es una pequeña regla que se aplica a cada ficha. En Python, esa regla es una función, y se puede pasar de un sitio a otro como cualquier otro dato.

## La pregunta

Hasta ahora las funciones eran recetas que se llaman. ¿Puede una función guardarse en una variable, viajar como argumento o incluso fabricar otras funciones?

## La idea

En Python, **una función es un valor**, como un número o una lista. Por eso:

- se puede guardar en una variable: `f = len`, y después `f("hola")` da `4`;
- se puede pasar como argumento: `sorted(datos, key=len)`;
- una función puede devolver otra función.

Para las funciones pequeñas que solo se usan una vez existe una forma corta, la **lambda**:

```python
lambda x: x * x          # una función sin nombre que recibe x y devuelve x * x
```

Una lambda tiene parámetros, dos puntos y **una sola expresión**, cuyo valor devuelve. No lleva `return` ni puede tener varias líneas.

## Construcción

### 1 · Ordenar con un criterio

`sorted` ordena de menor a mayor. Con tuplas `(nombre, nota)`, compararía primero los nombres. Para ordenar por nota, le pasamos un criterio con `key`: una función que, para cada elemento, dice **qué hay que comparar**.

:::{tip} Predice
¿Cuántas veces se llamará a la lambda? ¿Quién quedará primero?
:::

```{code-cell} python
alumnos = [("Ana", 7), ("Biel", 9), ("Carla", 5)]
por_nota = sorted(alumnos, key=lambda a: a[1])
print(por_nota)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Ordenar por nota","etiqueta":"lambda · key","idea":"sorted llama a la lambda una vez por alumno. La lambda devuelve a[1], la nota, y sorted ordena según esas notas: 5, 7, 9.","columnas":["por_nota"],"fila_en":"cada_linea"},"traza":{"codigo":"alumnos = [(\"Ana\", 7), (\"Biel\", 9), (\"Carla\", 5)]\npor_nota = sorted(alumnos, key=lambda a: a[1])\nprint(por_nota)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"alumnos":[{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]},{"__tupla__":["Carla",5]}]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"alumnos":"[('Ana', 7), ('Biel', 9), ('Carla', 5)]"},"tipos":{"alumnos":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"alumnos":[{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]},{"__tupla__":["Carla",5]}]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"alumnos":"[('Ana', 7), ('Biel', 9), ('Carla', 5)]"},"tipos":{"alumnos":"list"},"pila":[{"nombre":"<lambda>","args":["a"],"vars":{"a":{"__tupla__":["Ana",7]}},"repr":{"a":"('Ana', 7)"},"expr":"a[1]"}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"alumnos":[{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]},{"__tupla__":["Carla",5]}]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"alumnos":"[('Ana', 7), ('Biel', 9), ('Carla', 5)]"},"tipos":{"alumnos":"list"},"pila":[{"nombre":"<lambda>","args":["a"],"vars":{"a":{"__tupla__":["Ana",7]}},"repr":{"a":"('Ana', 7)"},"expr":"a[1]"}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"alumnos":[{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]},{"__tupla__":["Carla",5]}]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"alumnos":"[('Ana', 7), ('Biel', 9), ('Carla', 5)]"},"tipos":{"alumnos":"list"},"pila":[],"devuelve":{"funcion":"<lambda>","valor":"7","error":false},"excepcion":null},{"linea":2,"estado":{"alumnos":[{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]},{"__tupla__":["Carla",5]}]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"alumnos":"[('Ana', 7), ('Biel', 9), ('Carla', 5)]"},"tipos":{"alumnos":"list"},"pila":[{"nombre":"<lambda>","args":["a"],"vars":{"a":{"__tupla__":["Biel",9]}},"repr":{"a":"('Biel', 9)"},"expr":"a[1]"}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"alumnos":[{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]},{"__tupla__":["Carla",5]}]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"alumnos":"[('Ana', 7), ('Biel', 9), ('Carla', 5)]"},"tipos":{"alumnos":"list"},"pila":[],"devuelve":{"funcion":"<lambda>","valor":"9","error":false},"excepcion":null},{"linea":2,"estado":{"alumnos":[{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]},{"__tupla__":["Carla",5]}]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"alumnos":"[('Ana', 7), ('Biel', 9), ('Carla', 5)]"},"tipos":{"alumnos":"list"},"pila":[{"nombre":"<lambda>","args":["a"],"vars":{"a":{"__tupla__":["Carla",5]}},"repr":{"a":"('Carla', 5)"},"expr":"a[1]"}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"alumnos":[{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]},{"__tupla__":["Carla",5]}],"por_nota":[{"__tupla__":["Carla",5]},{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]}]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"alumnos":"[('Ana', 7), ('Biel', 9), ('Carla', 5)]","por_nota":"[('Carla', 5), ('Ana', 7), ('Biel', 9)]"},"tipos":{"alumnos":"list","por_nota":"list"},"pila":[],"devuelve":{"funcion":"<lambda>","valor":"5","error":false},"excepcion":null},{"linea":3,"estado":{"alumnos":[{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]},{"__tupla__":["Carla",5]}],"por_nota":[{"__tupla__":["Carla",5]},{"__tupla__":["Ana",7]},{"__tupla__":["Biel",9]}]},"salida":"[('Carla', 5), ('Ana', 7), ('Biel', 9)]\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"alumnos":"[('Ana', 7), ('Biel', 9), ('Carla', 5)]","por_nota":"[('Carla', 5), ('Ana', 7), ('Biel', 9)]"},"tipos":{"alumnos":"list","por_nota":"list"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["2 ↩","[('Carla', 5), ('Ana', 7), ('Biel', 9)]"],["3","[('Carla', 5), ('Ana', 7), ('Biel', 9)]"]]}}
```

`key` sirve igual en `max`, `min` y en el método `lista.sort()`. Y no hace falta que sea una lambda: `sorted(palabras, key=len)` ordena por longitud usando la función `len` tal cual.

:::{tip} ¿Lambda o `def`?
Una lambda es buena para un criterio corto que se usa una sola vez. Si no cabe cómoda en una línea, si la vas a usar en varios sitios o si quieres probarla por separado, dale nombre con `def`: se lee mejor y aparece con su nombre en los tracebacks.
:::

### 2 · `map` y `filter`

Dos funciones clásicas reciben una función y una secuencia:

- `map(f, datos)` aplica `f` a cada elemento;
- `filter(f, datos)` se queda con los elementos para los que `f` devuelve `True`.

Devuelven objetos perezosos, que calculan a medida que se piden; por eso se suelen envolver en `list(...)`:

```{code-cell} python
datos = [3, 8, 11, 6]
dobles = list(map(lambda x: x * 2, datos))
pares = list(filter(lambda x: x % 2 == 0, datos))
print(dobles, pares)
```

Si no los envuelves, lo que ves es el objeto, no los valores: `print(map(abs, datos))` escribe algo como `<map object at 0x…>`. Y un iterador se gasta: después de recorrerlo una vez, ya no entrega nada más.

Lo mismo con comprensiones: `[x * 2 for x in datos]` y `[x for x in datos if x % 2 == 0]`. Las dos formas son correctas y en el PCAP aparecen las dos.

### 3 · Funciones que fabrican funciones: los cierres

Una función puede definir otra dentro y devolverla. La función de dentro se lleva consigo las variables de fuera que usa, aunque la de fuera ya haya terminado. A eso se le llama **cierre** (*closure*).

:::{tip} Predice
Cuando se ejecuta `doble(5)`, la función `multiplicador` ya terminó hace rato. ¿De dónde sale `n`?
:::

```{code-cell} python
def multiplicador(n):
    def por(x):
        return x * n
    return por

doble = multiplicador(2)
triple = multiplicador(3)
print(doble(5), triple(5))
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Una fábrica de funciones","etiqueta":"cierre · closure","idea":"Cada llamada a multiplicador fabrica una función por distinta, que recuerda su propia n. doble recuerda n = 2 y triple recuerda n = 3: por eso el mismo código da 10 y 15.","columnas":["doble(1)","triple(1)"],"fila_en":"cada_linea"},"traza":{"codigo":"def multiplicador(n):\n    def por(x):\n        return x * n\n    return por\n\ndoble = multiplicador(2)\ntriple = multiplicador(3)\nprint(doble(5), triple(5))","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"multiplicador","args":["n"],"vars":{"n":2},"repr":{"n":"2"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"multiplicador","args":["n"],"vars":{"n":2,"por":{"__txt__":"función por(x) · recuerda n = 2"}},"repr":{"n":"2","por":"función por(x) · recuerda n = 2"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"multiplicador","args":["n"],"vars":{"n":2,"por":{"__txt__":"función por(x) · recuerda n = 2"}},"repr":{"n":"2","por":"función por(x) · recuerda n = 2"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"doble":"función por(x) · recuerda n = 2"},"tipos":{"doble":"function"},"pila":[],"devuelve":{"funcion":"multiplicador","valor":"función por(x) · recuerda n = 2","error":false},"excepcion":null},{"linea":7,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"doble":"función por(x) · recuerda n = 2"},"tipos":{"doble":"function"},"pila":[{"nombre":"multiplicador","args":["n"],"vars":{"n":3},"repr":{"n":"3"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"doble":"función por(x) · recuerda n = 2"},"tipos":{"doble":"function"},"pila":[{"nombre":"multiplicador","args":["n"],"vars":{"n":3,"por":{"__txt__":"función por(x) · recuerda n = 3"}},"repr":{"n":"3","por":"función por(x) · recuerda n = 3"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"doble":"función por(x) · recuerda n = 2"},"tipos":{"doble":"function"},"pila":[{"nombre":"multiplicador","args":["n"],"vars":{"n":3,"por":{"__txt__":"función por(x) · recuerda n = 3"}},"repr":{"n":"3","por":"función por(x) · recuerda n = 3"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"},"triple":{"__txt__":"función por(x) · recuerda n = 3"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"doble":"función por(x) · recuerda n = 2","triple":"función por(x) · recuerda n = 3"},"tipos":{"doble":"function","triple":"function"},"pila":[],"devuelve":{"funcion":"multiplicador","valor":"función por(x) · recuerda n = 3","error":false},"excepcion":null},{"linea":8,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"},"triple":{"__txt__":"función por(x) · recuerda n = 3"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"doble":"función por(x) · recuerda n = 2","triple":"función por(x) · recuerda n = 3"},"tipos":{"doble":"function","triple":"function"},"pila":[{"nombre":"por","args":["x"],"vars":{"x":5,"n":2},"repr":{"x":"5","n":"2"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"},"triple":{"__txt__":"función por(x) · recuerda n = 3"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"doble":"función por(x) · recuerda n = 2","triple":"función por(x) · recuerda n = 3"},"tipos":{"doble":"function","triple":"function"},"pila":[{"nombre":"por","args":["x"],"vars":{"x":5,"n":2},"repr":{"x":"5","n":"2"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"},"triple":{"__txt__":"función por(x) · recuerda n = 3"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":7,"repr":{"doble":"función por(x) · recuerda n = 2","triple":"función por(x) · recuerda n = 3"},"tipos":{"doble":"function","triple":"function"},"pila":[],"devuelve":{"funcion":"por","valor":"10","error":false},"excepcion":null},{"linea":3,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"},"triple":{"__txt__":"función por(x) · recuerda n = 3"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":8,"repr":{"doble":"función por(x) · recuerda n = 2","triple":"función por(x) · recuerda n = 3"},"tipos":{"doble":"function","triple":"function"},"pila":[{"nombre":"por","args":["x"],"vars":{"x":5,"n":3},"repr":{"x":"5","n":"3"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"doble":{"__txt__":"función por(x) · recuerda n = 2"},"triple":{"__txt__":"función por(x) · recuerda n = 3"}},"salida":"10 15\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":9,"repr":{"doble":"función por(x) · recuerda n = 2","triple":"función por(x) · recuerda n = 3"},"tipos":{"doble":"function","triple":"function"},"pila":[],"devuelve":{"funcion":"por","valor":"15","error":false},"excepcion":null}],"filas":[["4 ↩","2","—"],["7","2","—"],["2","2","—"],["4","2","—"],["4 ↩","2","3"],["8","2","3"],["3","2","3"],["3 ↩","2","3"],["3","2","3"],["3 ↩","2","3"]]}}
```

Los cierres sirven para fabricar funciones configuradas (un `doble`, un `triple`, un `con_iva`…) y para dar a una función una memoria pequeña sin necesidad de una clase. En las variables globales, `doble` y `triple` aparecen como funciones que **recuerdan** su `n`. Y en el marco de `por`, `n` aparece junto a `x` aunque no sea un parámetro.

### 4 · Ampliación · generadores

:::{note} Fuera del temario actual
El temario PCAP-31-04 no incluye los generadores, pero sí estaban en el anterior y aparecen en cualquier código real. Merece la pena verlos.
:::

Un **generador** es una función con `yield` en lugar de `return`. Al llamarla no se ejecuta nada: devuelve un objeto que va **entregando valores de uno en uno**, cada vez que se le pide el siguiente. Después de cada `yield` se queda en pausa, con sus variables intactas, y se reanuda justo ahí.

:::{tip} Predice
¿Cuántas veces entra y sale el programa del generador? ¿Qué valor tiene `n` cuando se reanuda?
:::

```{code-cell} python
def cuenta_atras(n):
    while n > 0:
        yield n
        n = n - 1

for v in cuenta_atras(3):
    print(v)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"La cuenta atrás perezosa","etiqueta":"yield · pausa y reanuda","idea":"Cada vuelta del for pide un valor. El generador corre hasta el yield, entrega n y se congela. En la vuelta siguiente se reanuda en la línea 4, con su n intacta.","columnas":["v"],"fila_en":"cada_linea"},"traza":{"codigo":"def cuenta_atras(n):\n    while n > 0:\n        yield n\n        n = n - 1\n\nfor v in cuenta_atras(3):\n    print(v)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":3},"repr":{"n":"3"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"3 > 0","valor":true},"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":3},"repr":{"n":"3"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":3},"repr":{"n":"3"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"v":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"v":"3"},"tipos":{"v":"int"},"pila":[],"devuelve":{"funcion":"cuenta_atras","valor":"3","error":false,"pausa":true,"gen":true},"excepcion":null},{"linea":7,"estado":{"v":3},"salida":"3\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"v":"3"},"tipos":{"v":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"v":3},"salida":"3\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"v":"3"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":3},"repr":{"n":"3"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"v":3},"salida":"3\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"v":"3"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":2},"repr":{"n":"2"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"v":3},"salida":"3\n","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"2 > 0","valor":true},"vuelta":0,"fila":4,"repr":{"v":"3"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":2},"repr":{"n":"2"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"v":3},"salida":"3\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"v":"3"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":2},"repr":{"n":"2"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"v":2},"salida":"3\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"v":"2"},"tipos":{"v":"int"},"pila":[],"devuelve":{"funcion":"cuenta_atras","valor":"2","error":false,"pausa":true,"gen":true},"excepcion":null},{"linea":7,"estado":{"v":2},"salida":"3\n2\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":7,"repr":{"v":"2"},"tipos":{"v":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"v":2},"salida":"3\n2\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":8,"repr":{"v":"2"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":2},"repr":{"n":"2"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"v":2},"salida":"3\n2\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":9,"repr":{"v":"2"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":1},"repr":{"n":"1"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"v":2},"salida":"3\n2\n","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"1 > 0","valor":true},"vuelta":0,"fila":10,"repr":{"v":"2"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":1},"repr":{"n":"1"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"v":2},"salida":"3\n2\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":11,"repr":{"v":"2"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":1},"repr":{"n":"1"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"v":1},"salida":"3\n2\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":12,"repr":{"v":"1"},"tipos":{"v":"int"},"pila":[],"devuelve":{"funcion":"cuenta_atras","valor":"1","error":false,"pausa":true,"gen":true},"excepcion":null},{"linea":7,"estado":{"v":1},"salida":"3\n2\n1\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":13,"repr":{"v":"1"},"tipos":{"v":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"v":1},"salida":"3\n2\n1\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":14,"repr":{"v":"1"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":1},"repr":{"n":"1"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"v":1},"salida":"3\n2\n1\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":15,"repr":{"v":"1"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":0},"repr":{"n":"0"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"v":1},"salida":"3\n2\n1\n","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"0 > 0","valor":false},"vuelta":0,"fila":16,"repr":{"v":"1"},"tipos":{"v":"int"},"pila":[{"nombre":"cuenta_atras","args":["n"],"vars":{"n":0},"repr":{"n":"0"},"gen":true}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"v":1},"salida":"3\n2\n1\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":17,"repr":{"v":"1"},"tipos":{"v":"int"},"pila":[],"devuelve":{"funcion":"cuenta_atras","valor":"None","error":false,"gen":true},"excepcion":null}],"filas":[["3 ↩","3"],["7","3"],["6","3"],["4","3"],["2","3"],["3","3"],["3 ↩","2"],["7","2"],["6","2"],["4","2"],["2","2"],["3","2"],["3 ↩","1"],["7","1"],["6","1"],["4","1"],["2","1"],["2 ↩","1"]]}}
```

La ventaja es que no fabrica la lista entera: calcula cada valor cuando hace falta. Por eso `range(1_000_000)` no ocupa un millón de números en memoria. También se puede pedir un valor a mano con `next(g)`, y cuando no quedan más, lanza `StopIteration`.

## Conexiones

- `key=lambda …` es la misma idea que el método genético de este libro: no damos el resultado, damos la regla que lo produce.
- Un cierre recuerda su entorno igual que un objeto guarda sus atributos. Muchas veces son dos maneras de resolver lo mismo.
- El `for` funciona con cualquier cosa que entregue valores de uno en uno: listas, cadenas, ficheros, `range` y generadores.

## La grieta

Todo lo que hemos calculado se pierde al cerrar el programa. ¿Cómo guarda un programa sus datos para la próxima vez? Escribiéndolos en un fichero.

## Preguntas tipo examen

Preguntas como las del examen PCAP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcap","capitulo":"16","titulo":"Preguntas tipo examen","etiqueta":"PCAP"}}
```

## Ejercicios

1. **La más larga.** Usa `max` con `key` para encontrar la palabra más larga de `["sol", "camino", "luz"]`.
2. **Ordenar al revés.** Ordena `alumnos = [("Ana", 7), ("Biel", 9), ("Carla", 5)]` de mayor a menor nota. Pista: `sorted` tiene un parámetro `reverse`.
3. **De `map` a comprensión.** Reescribe `list(map(lambda s: s.strip(), lineas))` como comprensión.
4. **¿Qué imprime?**

   ```python
   def sumador(a):
       return lambda b: a + b

   mas10 = sumador(10)
   print(mas10(5), sumador(1)(1))
   ```

5. **Un generador de pares.** Escribe un generador `pares(n)` que entregue los números pares de 0 a `n`, ambos incluidos. Pruébalo con `list(pares(8))`.

El solucionario está al final del capítulo.

## Solucionario

1. `max(["sol", "camino", "luz"], key=len)` da `'camino'`.
2. `sorted(alumnos, key=lambda a: a[1], reverse=True)` da `[('Biel', 9), ('Ana', 7), ('Carla', 5)]`.
3. `[s.strip() for s in lineas]`.
4. Imprime **15 2**. `sumador(10)` devuelve una lambda que recuerda `a = 10`; `sumador(1)(1)` fabrica otra que recuerda `a = 1` y la llama al momento.
5. Una solución:

   ```python
   def pares(n):
       x = 0
       while x <= n:
           yield x
           x = x + 2

   print(list(pares(8)))
   ```

   Imprime `[0, 2, 4, 6, 8]`.
