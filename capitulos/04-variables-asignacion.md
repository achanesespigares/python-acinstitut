---
title: Variables y asignación
subtitle: Guardar un dato y cambiarlo
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Estás llevando el marcador de un partido en una libreta. Arriba escribes «Local» y «Visitante», y debajo un 0 en cada lado. Cuando marca el local, tachas su número y escribes el siguiente. Al final del partido, lo que queda sin tachar es el resultado.

## La pregunta

La libreta hace dos cosas: **recuerda** un dato con un nombre al lado y **lo cambia** cuando pasa algo. ¿Cómo hace un programa esas dos cosas?

## La idea

Una **variable** es un nombre que guarda un valor. La línea que le da valor se llama **asignación**:

```python
local = 0
```

:::{important} El signo `=` no es una igualdad
En Python, `=` significa **«guarda»**, y se lee de derecha a izquierda. Primero se calcula todo lo que hay a la derecha. Después, el resultado se guarda en el nombre de la izquierda. Por eso `local = local + 1` tiene todo el sentido del mundo: toma el valor que tenía `local`, súmale 1 y guárdalo otra vez en `local`.
:::

## Construcción

### 1 · El marcador

:::{tip} Predice
Antes de pulsar «Paso»: ¿cómo quedará el marcador? ¿Qué número tachas en cada línea?
:::

```{code-cell} python
local = 0
visitante = 0
local = local + 1
visitante = visitante + 1
local = local + 1
print(local, "-", visitante)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El marcador","etiqueta":"asignación","idea":"Cada asignación calcula primero la derecha y después guarda el resultado en el nombre de la izquierda. El valor anterior se pierde: queda tachado.","columnas":["local","visitante"],"fila_en":"cada_linea"},"traza":{"codigo":"local = 0\nvisitante = 0\nlocal = local + 1\nvisitante = visitante + 1\nlocal = local + 1\nprint(local, \"-\", visitante)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"local":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"local":"0"},"tipos":{"local":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"local":0,"visitante":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"local":"0","visitante":"0"},"tipos":{"local":"int","visitante":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"local":1,"visitante":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"local":"1","visitante":"0"},"tipos":{"local":"int","visitante":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"local":1,"visitante":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"local":"1","visitante":"1"},"tipos":{"local":"int","visitante":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"local":2,"visitante":1},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"local":"2","visitante":"1"},"tipos":{"local":"int","visitante":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"local":2,"visitante":1},"salida":"2 - 1\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"local":"2","visitante":"1"},"tipos":{"local":"int","visitante":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","0","—"],["2","0","0"],["3","1","0"],["4","1","1"],["5","2","1"],["6","2","1"]]}}
```

Fíjate en la tabla de traza: cada fila es una foto de las variables justo después de ejecutar una línea. Es exactamente lo que hacías en la libreta.

### 2 · Intercambiar dos valores

Queremos que `a` y `b` se intercambien los valores. El primer intento que se le ocurre a casi todo el mundo es este:

:::{tip} Predice
¿Qué imprimirá? Piénsalo antes de mirar.
:::

```{code-cell} python
a = 5
b = 8
a = b
b = a
print(a, b)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El intercambio que falla","etiqueta":"asignación · error típico","idea":"En cuanto se ejecuta a = b, el 5 se pierde para siempre. Cuando después hacemos b = a, ya no queda ningún 5 que copiar.","columnas":["a","b"],"fila_en":"cada_linea"},"traza":{"codigo":"a = 5\nb = 8\na = b\nb = a\nprint(a, b)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"a":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"a":"5"},"tipos":{"a":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"a":5,"b":8},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"a":"5","b":"8"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":8,"b":8},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"a":"8","b":"8"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":8,"b":8},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"a":"8","b":"8"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":8,"b":8},"salida":"8 8\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"a":"8","b":"8"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","5","—"],["2","5","8"],["3","8","8"],["4","8","8"],["5","8","8"]]}}
```

La solución es la misma que usarías para intercambiar el contenido de dos vasos: un tercer vaso donde guardar uno de ellos mientras tanto.

```{code-cell} python
a = 5
b = 8
aux = a
a = b
b = aux
print(a, b)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El intercambio con variable auxiliar","etiqueta":"asignación · patrón","idea":"aux guarda una copia del 5 antes de que a lo pierda. Tres asignaciones, y cada valor acaba en su sitio.","columnas":["a","b","aux"],"fila_en":"cada_linea"},"traza":{"codigo":"a = 5\nb = 8\naux = a\na = b\nb = aux\nprint(a, b)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"a":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"a":"5"},"tipos":{"a":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"a":5,"b":8},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"a":"5","b":"8"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":5,"b":8,"aux":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"a":"5","b":"8","aux":"5"},"tipos":{"a":"int","b":"int","aux":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":8,"b":8,"aux":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"a":"8","b":"8","aux":"5"},"tipos":{"a":"int","b":"int","aux":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":8,"b":5,"aux":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"a":"8","b":"5","aux":"5"},"tipos":{"a":"int","b":"int","aux":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"a":8,"b":5,"aux":5},"salida":"8 5\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"a":"8","b":"5","aux":"5"},"tipos":{"a":"int","b":"int","aux":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","5","—","—"],["2","5","8","—"],["3","5","8","5"],["4","8","8","5"],["5","8","5","5"],["6","8","5","5"]]}}
```

Python tiene además un atajo para esto, la **asignación múltiple**: `a, b = b, a`. Calcula primero los dos valores de la derecha y después los guarda a la vez, así que no se pierde ninguno.

```{code-cell} python
a = 5
b = 8
a, b = b, a
print(a, b)
```

## Conexiones

- La asignación es la primera de las tres piezas con las que se construye cualquier algoritmo. Las otras dos son el **condicional** y la **iteración**, en los capítulos siguientes.
- El acumulador `total = total + nota` del capítulo [Recorrer listas](08-recorrer-listas.md) es el marcador de este capítulo dentro de un bucle.

## La grieta

Hemos imaginado las variables como cajas con un número dentro. Con números funciona, pero no es exactamente lo que hace Python: una variable es una **etiqueta** pegada a un valor. La diferencia no se nota con números, y sí con listas. Lo verás cuando dos nombres compartan la misma lista y cambiar una «cambie las dos».

## Ejercicios

1. **Traza a mano.** Haz la tabla de traza de este programa. ¿Qué imprime?

   ```python
   x = 3
   y = x * 2
   x = y - 1
   y = x + y
   print(x, y)
   ```

2. **¿Qué valor tiene `n` al final?**

   ```python
   n = 10
   n = n + 5
   n = n * 2
   n = n - n
   ```

3. **Rotar tres valores.** Con `a = 1`, `b = 2` y `c = 3`, escribe un programa que deje `a = 2`, `b = 3` y `c = 1` usando una sola variable auxiliar.

El solucionario está al final del capítulo.

## Solucionario

1. La tabla queda así: `x = 3`; `y = 6`; `x = 5`; `y = 11`. Imprime **5 11**. Ojo con la última línea: usa el `x` nuevo (5), no el original (3).
2. **0**. Los pasos son 10 → 15 → 30 → 0: cualquier número menos sí mismo da 0.
3. Una solución:

   ```python
   aux = a
   a = b
   b = c
   c = aux
   ```

   También vale la asignación múltiple: `a, b, c = b, c, a`.
