---
title: Funciones
subtitle: Ponerle nombre a un trozo de programa
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

En la calculadora hay una tecla √. La pulsas, le das un número y te devuelve su raíz. No sabes qué cuentas hace por dentro, ni te hace falta: sabes **qué le das** y **qué te devuelve**. Y la puedes usar tantas veces como quieras.

## La pregunta

Cuando un mismo cálculo aparece varias veces en un programa, ¿tenemos que escribirlo otra vez cada vez? ¿Podemos fabricar nuestras propias teclas?

## La idea

Una **función** es un trozo de programa con nombre. Se define una vez y se **llama** tantas veces como haga falta:

```python
def area_rectangulo(base, altura):    # parámetros: lo que le das
    area = base * altura
    return area                       # lo que te devuelve
```

:::{important} Lo que pasa al llamar a una función
1. Python crea un **marco** nuevo: un espacio de trabajo propio de esa llamada.
2. Los **parámetros** reciben los valores con los que se ha llamado.
3. Se ejecuta el cuerpo. Las variables que se crean dentro son **locales**: solo existen en ese marco.
4. Con `return`, la función **devuelve** un valor y su marco desaparece.
:::

Fíjate en que una función es una especificación con nombre: los parámetros son la entrada y el `return` es la salida.

## Construcción

### 1 · El área del rectángulo

:::{tip} Predice
Cuando se ejecuta la línea 5, ¿qué valen `base` y `altura`? ¿Y en la línea 6?
:::

```{code-cell} python
def area_rectangulo(base, altura):
    area = base * altura
    return area

a = area_rectangulo(3, 4)
b = area_rectangulo(2, 5)
print(a + b)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El área del rectángulo","etiqueta":"def · return · marcos","idea":"Cada llamada crea su propio marco, con base y altura recibiendo los valores de esa llamada. Al llegar al return, el marco desaparece y el valor devuelto se guarda en a (o en b).","columnas":["base","altura","area","a","b"],"fila_en":"cada_linea"},"traza":{"codigo":"def area_rectangulo(base, altura):\n    area = base * altura\n    return area\n\na = area_rectangulo(3, 4)\nb = area_rectangulo(2, 5)\nprint(a + b)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{},"tipos":{},"pila":[{"nombre":"area_rectangulo","args":["base","altura"],"vars":{"base":3,"altura":4},"repr":{"base":"3","altura":"4"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{},"tipos":{},"pila":[{"nombre":"area_rectangulo","args":["base","altura"],"vars":{"base":3,"altura":4,"area":12},"repr":{"base":"3","altura":"4","area":"12"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{},"tipos":{},"pila":[{"nombre":"area_rectangulo","args":["base","altura"],"vars":{"base":3,"altura":4,"area":12},"repr":{"base":"3","altura":"4","area":"12"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":12},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"a":"12"},"tipos":{"a":"int"},"pila":[],"devuelve":{"funcion":"area_rectangulo","valor":"12","error":false},"excepcion":null},{"linea":6,"estado":{"a":12},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"a":"12"},"tipos":{"a":"int"},"pila":[{"nombre":"area_rectangulo","args":["base","altura"],"vars":{"base":2,"altura":5},"repr":{"base":"2","altura":"5"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"a":12},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"a":"12"},"tipos":{"a":"int"},"pila":[{"nombre":"area_rectangulo","args":["base","altura"],"vars":{"base":2,"altura":5,"area":10},"repr":{"base":"2","altura":"5","area":"10"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":12},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"a":"12"},"tipos":{"a":"int"},"pila":[{"nombre":"area_rectangulo","args":["base","altura"],"vars":{"base":2,"altura":5,"area":10},"repr":{"base":"2","altura":"5","area":"10"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":12,"b":10},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":7,"repr":{"a":"12","b":"10"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":{"funcion":"area_rectangulo","valor":"10","error":false},"excepcion":null},{"linea":7,"estado":{"a":12,"b":10},"salida":"22\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":8,"repr":{"a":"12","b":"10"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["5","3","4","—","—","—"],["2","3","4","12","—","—"],["3","3","4","12","—","—"],["3 ↩","—","—","—","12","—"],["6","2","5","—","12","—"],["2","2","5","10","12","—"],["3","2","5","10","12","—"],["3 ↩","—","—","—","12","10"],["7","—","—","—","12","10"]]}}
```

Mira el visualizador en la segunda llamada: el marco vuelve a aparecer, pero ahora con `base = 2` y `altura = 5`. La variable `area` de la primera llamada ya no existe; cada llamada empieza de cero.

### 2 · `print` no es `return`

Este es el error más frecuente al empezar con funciones:

:::{tip} Predice
¿Qué dos cosas se verán en pantalla?
:::

```{code-cell} python
def suma_mal(a, b):
    print(a + b)

r = suma_mal(2, 3)
print(r)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"print no es return","etiqueta":"return · error típico","idea":"suma_mal enseña el 5 en pantalla, pero no lo devuelve. Una función sin return devuelve None, así que r se queda con None.","columnas":["a","b","r"],"fila_en":"cada_linea"},"traza":{"codigo":"def suma_mal(a, b):\n    print(a + b)\n\nr = suma_mal(2, 3)\nprint(r)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{},"tipos":{},"pila":[{"nombre":"suma_mal","args":["a","b"],"vars":{"a":2,"b":3},"repr":{"a":"2","b":"3"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"5\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{},"tipos":{},"pila":[{"nombre":"suma_mal","args":["a","b"],"vars":{"a":2,"b":3},"repr":{"a":"2","b":"3"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"r":null},"salida":"5\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"r":"None"},"tipos":{"r":"NoneType"},"pila":[],"devuelve":{"funcion":"suma_mal","valor":"None","error":false},"excepcion":null},{"linea":5,"estado":{"r":null},"salida":"5\nNone\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"r":"None"},"tipos":{"r":"NoneType"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["4","2","3","—"],["2","2","3","—"],["2 ↩","—","—","None"],["5","—","—","None"]]}}
```

:::{warning} Trampa · `print` enseña, `return` entrega
`print` muestra un valor en la pantalla, pero el programa no se lo queda. `return` entrega el valor a quien llamó a la función, que puede guardarlo, sumarlo o pasárselo a otra función. Si una función tiene que calcular algo, casi siempre necesita `return`.
:::

### 3 · Funciones que usan funciones

:::{tip} Predice
¿Cuántos marcos llegará a haber a la vez en el momento de más trabajo?
:::

```{code-cell} python
def cuadrado(x):
    return x * x

def hipotenusa(a, b):
    suma = cuadrado(a) + cuadrado(b)
    return suma ** 0.5

h = hipotenusa(3, 4)
print(h)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Funciones que usan funciones","etiqueta":"llamadas anidadas","idea":"hipotenusa llama dos veces a cuadrado. Mientras cuadrado trabaja, el marco de hipotenusa sigue ahí esperando su resultado: los marcos se apilan.","columnas":["x","suma","h"],"fila_en":"cada_linea"},"traza":{"codigo":"def cuadrado(x):\n    return x * x\n\ndef hipotenusa(a, b):\n    suma = cuadrado(a) + cuadrado(b)\n    return suma ** 0.5\n\nh = hipotenusa(3, 4)\nprint(h)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"hipotenusa","args":["a","b"],"vars":{"a":3,"b":4},"repr":{"a":"3","b":"4"}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{},"tipos":{},"pila":[{"nombre":"hipotenusa","args":["a","b"],"vars":{"a":3,"b":4},"repr":{"a":"3","b":"4"}},{"nombre":"cuadrado","args":["x"],"vars":{"x":3},"repr":{"x":"3"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{},"tipos":{},"pila":[{"nombre":"hipotenusa","args":["a","b"],"vars":{"a":3,"b":4},"repr":{"a":"3","b":"4"}},{"nombre":"cuadrado","args":["x"],"vars":{"x":3},"repr":{"x":"3"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"hipotenusa","args":["a","b"],"vars":{"a":3,"b":4},"repr":{"a":"3","b":"4"}}],"devuelve":{"funcion":"cuadrado","valor":"9","error":false},"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{},"tipos":{},"pila":[{"nombre":"hipotenusa","args":["a","b"],"vars":{"a":3,"b":4},"repr":{"a":"3","b":"4"}},{"nombre":"cuadrado","args":["x"],"vars":{"x":4},"repr":{"x":"4"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{},"tipos":{},"pila":[{"nombre":"hipotenusa","args":["a","b"],"vars":{"a":3,"b":4,"suma":25},"repr":{"a":"3","b":"4","suma":"25"}}],"devuelve":{"funcion":"cuadrado","valor":"16","error":false},"excepcion":null},{"linea":6,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{},"tipos":{},"pila":[{"nombre":"hipotenusa","args":["a","b"],"vars":{"a":3,"b":4,"suma":25},"repr":{"a":"3","b":"4","suma":"25"}}],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"h":5.0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"h":"5.0"},"tipos":{"h":"float"},"pila":[],"devuelve":{"funcion":"hipotenusa","valor":"5.0","error":false},"excepcion":null},{"linea":9,"estado":{"h":5.0},"salida":"5.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"h":"5.0"},"tipos":{"h":"float"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["5","3","—","—"],["2","3","—","—"],["2","4","—","—"],["2 ↩","—","25","—"],["6","—","25","—"],["6 ↩","—","—","5.0"],["9","—","—","5.0"]]}}
```

Hay momentos con **dos marcos a la vez**: el de `hipotenusa`, que espera, y el de `cuadrado`, que trabaja. Esa pila de marcos es lo que Python llama la *pila de llamadas*.

## Conexiones

- Una función es una **especificación** convertida en código: los parámetros son la entrada, el `return` es la salida.
- `len`, `print`, `range` o `int` son funciones que ya traía Python. Ahora sabes fabricar las tuyas.
- Descomponer un problema en funciones pequeñas es la **descomposición** del pensamiento computacional hecha código.

## La grieta

¿Y si una función se llamara a sí misma? Parece un círculo vicioso, pero si cada llamada trabaja con un caso más pequeño, la pila de marcos crece y luego se deshace sola. Es la **recursión**, y con ella se calcula, por ejemplo, el factorial.

## Preguntas tipo examen

Preguntas como las del examen PCEP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","capitulo":"09","titulo":"Preguntas tipo examen","etiqueta":"PCEP"}}
```

## Ejercicios

1. **Escribe** una función `celsius_a_fahrenheit(c)` que devuelva `c * 9 / 5 + 32`. Úsala para convertir 100 °C.
2. **¿Qué imprime?**

   ```python
   def misterio(n):
       n = n + 1
       return n * 2

   x = 5
   y = misterio(x)
   print(x, y)
   ```

3. **Corrige** `suma_mal` para que `r` valga 5.

El solucionario está al final del capítulo.

## Solucionario

1. Una solución:

   ```python
   def celsius_a_fahrenheit(c):
       return c * 9 / 5 + 32

   print(celsius_a_fahrenheit(100))
   ```

   Imprime `212.0`.
2. Imprime **5 12**. Dentro de la función, `n` es una variable local: cambiarla no toca la `x` de fuera, que sigue valiendo 5. La función devuelve (5 + 1) · 2 = 12.
3. Basta con cambiar `print` por `return`:

   ```python
   def suma(a, b):
       return a + b
   ```
