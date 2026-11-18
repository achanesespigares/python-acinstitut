---
title: Funciones a fondo
subtitle: Parámetros flexibles y el alcance de cada variable
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Cuando pides un café, puedes decir solo «un café», y te lo ponen como siempre; o «un café, con leche de avena y sin azúcar», y entonces cambian lo que indicas. El camarero tiene unas opciones por defecto y tú decides cuáles cambiar, nombrándolas.

## La pregunta

¿Cómo se escribe una función con opciones que tengan un valor por defecto? ¿Y una que acepte cualquier número de argumentos, como `print`? Si una variable se llama igual dentro y fuera de una función, ¿es la misma?

## La idea

- Un **parámetro** es el nombre que aparece en la definición: `def saludo(nombre):`.
- Un **argumento** es el valor que se pasa en la llamada: `saludo("Ana")`.

Los argumentos se pueden pasar **por posición** (en el orden de los parámetros) o **por nombre** (`nombre="Ana"`), y un parámetro puede tener un **valor por defecto**, que se usa si no llega argumento.

```python
def cafe(tipo, leche="entera", azucar=True):
    ...

cafe("solo")                          # leche y azucar por defecto
cafe("cortado", "avena")              # por posición
cafe("con leche", azucar=False)       # por nombre: se salta leche
```

:::{important} Las reglas del orden
- En la **definición**, los parámetros con valor por defecto van detrás de los que no tienen: `def f(a, b=2)` sí; `def f(a=1, b)` es un error de sintaxis.
- En la **llamada**, los argumentos por posición van antes que los argumentos por nombre: `f(1, b=3)` sí; `f(b=3, 1)` es un error.
- Un mismo parámetro no puede recibir dos valores: `f(1, a=2)` da `TypeError: got multiple values for argument 'a'`.
:::

## Construcción

### 1 · Valores por defecto y argumentos por nombre

```{code-cell} python
def precio_final(precio, iva=21, descuento=0):
    con_descuento = precio - precio * descuento / 100
    return round(con_descuento * (1 + iva / 100), 2)

print(precio_final(100))
print(precio_final(100, 10))
print(precio_final(100, descuento=20))
print(precio_final(descuento=50, precio=10))
```

Y los errores típicos al llamar mal:

```{code-cell} python
for llamada in ["precio_final()", "precio_final(100, 10, 5, 3)", "precio_final(100, precio=50)"]:
    try:
        eval(llamada)
    except TypeError as e:
        print(llamada, "→", e)
```

### 2 · Cualquier número de argumentos: `*args`

Un parámetro con `*` delante recoge en una **tupla** todos los argumentos sueltos que lleguen.

:::{tip} Predice
En la primera llamada, ¿qué valor tiene `notas` dentro de la función? ¿Y en la segunda?
:::

```{code-cell} python
def media(*notas):
    total = 0
    for n in notas:
        total += n
    return total / len(notas)

print(media(6, 8, 10))
print(media(5))
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Una media para cualquier número de notas","etiqueta":"*args · tupla","idea":"El * de *notas junta todos los argumentos sueltos en una tupla: (6, 8, 10) en la primera llamada y (5,) en la segunda. Dentro, notas se recorre como cualquier tupla.","columnas":["total"],"fila_en":"cada_linea"},"traza":{"codigo":"def media(*notas):\n    total = 0\n    for n in notas:\n        total += n\n    return total / len(notas)\n\nprint(media(6, 8, 10))\nprint(media(5))","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]}},"repr":{"notas":"(6, 8, 10)"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]},"total":0},"repr":{"notas":"(6, 8, 10)","total":"0"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]},"total":0,"n":6},"repr":{"notas":"(6, 8, 10)","total":"0","n":"6"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]},"total":6,"n":6},"repr":{"notas":"(6, 8, 10)","total":"6","n":"6"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]},"total":6,"n":8},"repr":{"notas":"(6, 8, 10)","total":"6","n":"8"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]},"total":14,"n":8},"repr":{"notas":"(6, 8, 10)","total":"14","n":"8"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]},"total":14,"n":10},"repr":{"notas":"(6, 8, 10)","total":"14","n":"10"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]},"total":24,"n":10},"repr":{"notas":"(6, 8, 10)","total":"24","n":"10"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":7,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]},"total":24,"n":10},"repr":{"notas":"(6, 8, 10)","total":"24","n":"10"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":8,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[6,8,10]},"total":24,"n":10},"repr":{"notas":"(6, 8, 10)","total":"24","n":"10"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{},"salida":"8.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":9,"repr":{},"tipos":{},"pila":[],"devuelve":{"funcion":"media","valor":"8.0","error":false},"excepcion":null},{"linea":8,"estado":{},"salida":"8.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[5]}},"repr":{"notas":"(5,)"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"8.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":10,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[5]},"total":0},"repr":{"notas":"(5,)","total":"0"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"8.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":11,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[5]},"total":0,"n":5},"repr":{"notas":"(5,)","total":"0","n":"5"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{},"salida":"8.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":12,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[5]},"total":5,"n":5},"repr":{"notas":"(5,)","total":"5","n":"5"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"8.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":13,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[5]},"total":5,"n":5},"repr":{"notas":"(5,)","total":"5","n":"5"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{},"salida":"8.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":14,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":[],"vars":{"notas":{"__tupla__":[5]},"total":5,"n":5},"repr":{"notas":"(5,)","total":"5","n":"5"},"estrella":{"notas":"*"}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{},"salida":"8.0\n5.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":15,"repr":{},"tipos":{},"pila":[],"devuelve":{"funcion":"media","valor":"5.0","error":false},"excepcion":null}],"filas":[["2","0"],["3","0"],["4","6"],["3","6"],["4","14"],["3","14"],["4","24"],["3","24"],["5","24"],["5 ↩","—"],["2","0"],["3","0"],["4","5"],["3","5"],["5","5"],["5 ↩","—"]]}}
```

### 3 · Argumentos con nombre libres: `**kwargs`

Dos asteriscos recogen en un **diccionario** los argumentos con nombre que no correspondan a ningún parámetro:

```{code-cell} python
def ficha(nombre, **datos):
    print("Ficha de", nombre)
    for clave, valor in datos.items():
        print(" ", clave, "→", valor)

ficha("Ana", edad=16, curso="1.º Bach", grupo="B")
```

Todos juntos, el orden es siempre este: los normales, los que tienen valor por defecto, `*args` y `**kwargs`.

```{code-cell} python
def todo(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

todo(1)
todo(1, 5, 7, 8, x=3)
```

Por convención se llaman `args` y `kwargs`, pero lo que importa son los asteriscos. Y al revés: un `*` en la **llamada** reparte una lista en argumentos sueltos: `media(*[6, 8, 10])` es lo mismo que `media(6, 8, 10)`.

### 4 · Devolver, o no devolver

- `return` termina la función **en ese momento**: lo que haya detrás no se ejecuta.
- `return a, b` devuelve varios valores en una tupla (lo viste en [Tuplas y conjuntos](23-tuplas-y-conjuntos.md)).
- Una función sin `return`, o con un `return` sin valor, devuelve `None`.

```{code-cell} python
def saluda(nombre):
    print("Hola,", nombre)

resultado = saluda("Ana")
print(resultado, resultado is None)
```

### 5 · El alcance de las variables

Cada llamada a una función tiene su propio **espacio de nombres local**: las variables que se crean dentro solo existen dentro, y desaparecen al terminar. Las de fuera son **globales**. Cuando una función usa un nombre, Python lo busca primero en lo local y, si no está, en lo global.

:::{tip} Predice
Al final, ¿cuánto vale el `contador` global? ¿Y `x`?
:::

```{code-cell} python
contador = 0

def sumar():
    global contador
    contador = contador + 1

def probar():
    contador = 100
    return contador

sumar()
sumar()
x = probar()
print(contador, x)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Dos variables con el mismo nombre","etiqueta":"global · local · ensombrecer","idea":"sumar declara global contador, así que cambia la de fuera. probar no lo declara: su contador = 100 crea una variable local nueva que tapa a la global solo mientras dura la función. Fuera, contador sigue valiendo 2.","columnas":["contador","x"],"fila_en":"cada_linea"},"traza":{"codigo":"contador = 0\n\ndef sumar():\n    global contador\n    contador = contador + 1\n\ndef probar():\n    contador = 100\n    return contador\n\nsumar()\nsumar()\nx = probar()\nprint(contador, x)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"contador":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"contador":"0"},"tipos":{"contador":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"contador":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"contador":"0"},"tipos":{"contador":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"contador":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"contador":"0"},"tipos":{"contador":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":11,"estado":{"contador":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"contador":"0"},"tipos":{"contador":"int"},"pila":[{"nombre":"sumar","args":[],"vars":{},"repr":{}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"contador":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"contador":"1"},"tipos":{"contador":"int"},"pila":[{"nombre":"sumar","args":[],"vars":{},"repr":{}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"contador":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"contador":"1"},"tipos":{"contador":"int"},"pila":[],"devuelve":{"funcion":"sumar","valor":"None","error":false},"excepcion":null},{"linea":12,"estado":{"contador":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"contador":"1"},"tipos":{"contador":"int"},"pila":[{"nombre":"sumar","args":[],"vars":{},"repr":{}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"contador":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":7,"repr":{"contador":"2"},"tipos":{"contador":"int"},"pila":[{"nombre":"sumar","args":[],"vars":{},"repr":{}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"contador":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":8,"repr":{"contador":"2"},"tipos":{"contador":"int"},"pila":[],"devuelve":{"funcion":"sumar","valor":"None","error":false},"excepcion":null},{"linea":13,"estado":{"contador":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":9,"repr":{"contador":"2"},"tipos":{"contador":"int"},"pila":[{"nombre":"probar","args":[],"vars":{},"repr":{}}],"devuelve":null,"excepcion":null},{"linea":8,"estado":{"contador":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":10,"repr":{"contador":"2"},"tipos":{"contador":"int"},"pila":[{"nombre":"probar","args":[],"vars":{"contador":100},"repr":{"contador":"100"}}],"devuelve":null,"excepcion":null},{"linea":9,"estado":{"contador":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":11,"repr":{"contador":"2"},"tipos":{"contador":"int"},"pila":[{"nombre":"probar","args":[],"vars":{"contador":100},"repr":{"contador":"100"}}],"devuelve":null,"excepcion":null},{"linea":9,"estado":{"contador":2,"x":100},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":12,"repr":{"contador":"2","x":"100"},"tipos":{"contador":"int","x":"int"},"pila":[],"devuelve":{"funcion":"probar","valor":"100","error":false},"excepcion":null},{"linea":14,"estado":{"contador":2,"x":100},"salida":"2 100\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":13,"repr":{"contador":"2","x":"100"},"tipos":{"contador":"int","x":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","0","—"],["3","0","—"],["7","0","—"],["11","0","—"],["5","1","—"],["5 ↩","1","—"],["12","1","—"],["5","2","—"],["5 ↩","2","—"],["13","2","—"],["8","100","—"],["9","100","—"],["9 ↩","2","100"],["14","2","100"]]}}
```

Cuando una variable local se llama igual que una global, la **ensombrece** (*shadowing*): dentro de la función, ese nombre se refiere a la local.

:::{warning} Trampa · leer y asignar la misma variable
Si una función **asigna** una variable en algún punto, Python la considera local en **toda** la función. Por eso esto falla:

```python
total = 0
def suma(x):
    total = total + x     # UnboundLocalError: total local aún no tiene valor
```

O se declara `global total`, o, mucho mejor, se pasa el valor como argumento y se devuelve el resultado.
:::

:::{important} Pocas globales
Que una función cambie variables globales hace el programa difícil de seguir: para entender qué vale `contador`, hay que leer todas las funciones que lo tocan. Lo recomendable es que cada función reciba lo que necesita por sus parámetros y entregue su resultado con `return`.
:::

## Conexiones

- `print(*valores, sep=" ", end="\n")` es una función con `*args` y dos parámetros por nombre con valor por defecto: ahora entiendes su firma.
- Los marcos de función de los visualizadores son exactamente los espacios de nombres locales.
- Más adelante, los cierres de [Funciones como valores](16-funciones-valores.md) añadirán un nivel intermedio: lo local de la función que encierra a otra.

## La grieta

En la `media` recorríamos `notas` con un `for`. Los bucles tienen más herramientas de las que hemos usado: saltarse una vuelta, anidarlos, parar con un valor centinela…

## Ejercicios

1. **¿Válido o no?** a) `def f(a, b=1, c):`; b) `f(1, c=3)` para `def f(a, b=1, c=2)`; c) `f(a=1, 2)`.
2. **¿Qué imprime?**

   ```python
   def f(a, b=10, *args):
       return a + b + len(args)

   print(f(1), f(1, 2), f(1, 2, 3, 4))
   ```

3. **Suma flexible.** Escribe `suma_todo(*numeros)` que devuelva la suma de todos los números que reciba, y `0` si no recibe ninguno.
4. **¿Qué imprime?**

   ```python
   x = 5

   def cambia():
       x = 10
       return x

   print(cambia(), x)
   ```

5. **Sin globales.** Reescribe la función `sumar` del apartado 5 para que no use `global`: que reciba el contador y devuelva el nuevo valor.

El solucionario está al final del capítulo.

## Solucionario

1. a) **No**: un parámetro sin valor por defecto no puede ir detrás de uno que lo tiene. b) **Sí**: `a = 1`, `b = 1` por defecto y `c = 3`. c) **No**: un argumento por posición no puede ir detrás de uno por nombre.
2. Imprime **11 3 5**: `1 + 10 + 0`, `1 + 2 + 0` y `1 + 2 + 2`.
3. Una solución:

   ```python
   def suma_todo(*numeros):
       total = 0
       for n in numeros:
           total += n
       return total
   ```

   `sum(numeros)` también vale.
4. Imprime **10 5**. El `x` de dentro es local y no toca al global.
5. Una solución:

   ```python
   def sumar(contador):
       return contador + 1

   contador = 0
   contador = sumar(contador)
   contador = sumar(contador)
   print(contador)
   ```
