---
title: Trazas a mano
subtitle: Ser el ordenador por un rato
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Un mapa del tesoro dice: «Desde el árbol, diez pasos al norte. Gira a la derecha y cuenta cinco. Si ves una roca, cava; si no, avanza tres más». No hace falta ir a la isla para saber dónde acabarás: puedes seguir las instrucciones con el dedo sobre el mapa.

## La pregunta

¿Podemos saber qué hace un programa sin ejecutarlo? ¿Y para qué querríamos hacerlo, si el ordenador lo ejecuta en un instante?

## La idea

Una **traza** es la ejecución de un programa hecha a mano, en una tabla:

- **una columna por variable** (y otra para lo que se imprime);
- **una fila por cada línea ejecutada**, con los valores justo después de ejecutarla.

:::{important} Por qué merece la pena
Hacer una traza te obliga a **predecir antes de ejecutar**. Si tu traza y el ordenador no coinciden, has encontrado algo: un error en el programa o un error en lo que creías que hacía. Las dos cosas son valiosas. Es la manera más rápida de entender un programa ajeno y de encontrar errores en el propio.
:::

**El método, paso a paso:**

1. Dibuja la tabla: una columna para el número de línea, una por variable y una para la pantalla.
2. Ejecuta las líneas **en el orden en que se ejecutan**, que no siempre es de arriba abajo.
3. Antes de una asignación, calcula la parte derecha con los valores **actuales**; después, apunta el resultado en la columna de la izquierda.
4. Apunta en cada fila solo lo que cambia, o repite los valores si te resulta más claro.

## Construcción

### 1 · El programa misterioso

:::{tip} Predice
Haz la traza en papel antes de pulsar «Paso». ¿Qué hace este programa? Pista: mira cómo empiezan `a` y `b`, y cómo terminan.
:::

```{code-cell} python
a = 7
b = 3
a = a + b
b = a - b
a = a - b
print(a, b)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El programa misterioso","etiqueta":"traza de una secuencia","idea":"Tres sumas y restas que parecen no llevar a ningún sitio. Sigue la tabla fila a fila: al final, a y b han intercambiado sus valores sin usar ninguna variable auxiliar.","columnas":["a","b"],"fila_en":"cada_linea"},"traza":{"codigo":"a = 7\nb = 3\na = a + b\nb = a - b\na = a - b\nprint(a, b)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null},{"linea":1,"estado":{"a":7},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"a":"7"},"tipos":{"a":"int"},"pila":[],"devuelve":null},{"linea":2,"estado":{"a":7,"b":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"a":"7","b":"3"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null},{"linea":3,"estado":{"a":10,"b":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"a":"10","b":"3"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null},{"linea":4,"estado":{"a":10,"b":7},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"a":"10","b":"7"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null},{"linea":5,"estado":{"a":3,"b":7},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"a":"3","b":"7"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null},{"linea":6,"estado":{"a":3,"b":7},"salida":"3 7\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"a":"3","b":"7"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null}],"filas":[["1","7","—"],["2","7","3"],["3","10","3"],["4","10","7"],["5","3","7"],["6","3","7"]]}}
```

Es un **intercambio sin variable auxiliar**: `a` guarda la suma, y de ella se recuperan los dos valores originales con dos restas. Sin la traza, no es nada evidente.

### 2 · ¿Qué calcula este bucle?

:::{tip} Predice
Este es más difícil: hay un bucle, y los operadores `%` (resto) y `//` (división entera). Recuerda que `472 % 10` es 2 y `472 // 10` es 47. Haz la traza y descubre qué calcula.
:::

```{code-cell} python
n = 472
suma = 0
while n > 0:
    suma = suma + n % 10
    n = n // 10
print(suma)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"¿Qué calcula este bucle?","etiqueta":"traza de un bucle","idea":"n % 10 es la última cifra de n, y n // 10 le quita esa cifra. Cada vuelta suma una cifra y la elimina, hasta que n se queda en 0.","cabecera":3,"puntero":"n","columnas":["n","suma"],"fila_en":"comprobacion"},"traza":{"codigo":"n = 472\nsuma = 0\nwhile n > 0:\n    suma = suma + n % 10\n    n = n // 10\nprint(suma)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null},{"linea":1,"estado":{"n":472},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"n":"472"},"tipos":{"n":"int"},"pila":[],"devuelve":null},{"linea":2,"estado":{"n":472,"suma":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"n":"472","suma":"0"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":3,"estado":{"n":472,"suma":0},"salida":"","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"472 > 0","valor":true},"vuelta":1,"fila":0,"repr":{"n":"472","suma":"0"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":4,"estado":{"n":472,"suma":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"n":"472","suma":"2"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":5,"estado":{"n":47,"suma":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"n":"47","suma":"2"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":3,"estado":{"n":47,"suma":2},"salida":"","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"47 > 0","valor":true},"vuelta":2,"fila":1,"repr":{"n":"47","suma":"2"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":4,"estado":{"n":47,"suma":9},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"n":"47","suma":"9"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":5,"estado":{"n":4,"suma":9},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"n":"4","suma":"9"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":3,"estado":{"n":4,"suma":9},"salida":"","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"4 > 0","valor":true},"vuelta":3,"fila":2,"repr":{"n":"4","suma":"9"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":4,"estado":{"n":4,"suma":13},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"n":"4","suma":"13"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":5,"estado":{"n":0,"suma":13},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"n":"0","suma":"13"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":3,"estado":{"n":0,"suma":13},"salida":"","foco":null,"lee":false,"cond":{"expr":"n > 0","sust":"0 > 0","valor":false},"vuelta":4,"fila":3,"repr":{"n":"0","suma":"13"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null},{"linea":6,"estado":{"n":0,"suma":13},"salida":"13\n","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"n":"0","suma":"13"},"tipos":{"n":"int","suma":"int"},"pila":[],"devuelve":null}],"filas":[["472","0","Sí"],["47","2","Sí"],["4","9","Sí"],["0","13","No"]]}}
```

Calcula la **suma de las cifras**: 4 + 7 + 2 = 13. La tabla de traza lo deja a la vista: la columna `n` pierde una cifra en cada fila, y `suma` la va recogiendo.

### 3 · Una traza para encontrar un error

Este programa debería calcular la media de 4, 8 y 6, que es 6. Pero no da 6.

:::{tip} Predice
Haz la traza y encuentra la línea que falla antes de ejecutar.
:::

```{code-cell} python
total = 0
total = total + 4
total = total + 8
media = total / 3
total = total + 6
print(media)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Una traza para encontrar un error","etiqueta":"traza · depurar","idea":"La media se calcula en la línea 4, cuando total solo vale 12. El 6 se suma después, demasiado tarde: el orden de las líneas importa.","columnas":["total","media"],"fila_en":"cada_linea"},"traza":{"codigo":"total = 0\ntotal = total + 4\ntotal = total + 8\nmedia = total / 3\ntotal = total + 6\nprint(media)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null},{"linea":1,"estado":{"total":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"total":"0"},"tipos":{"total":"int"},"pila":[],"devuelve":null},{"linea":2,"estado":{"total":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"total":"4"},"tipos":{"total":"int"},"pila":[],"devuelve":null},{"linea":3,"estado":{"total":12},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"total":"12"},"tipos":{"total":"int"},"pila":[],"devuelve":null},{"linea":4,"estado":{"total":12,"media":4.0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"total":"12","media":"4.0"},"tipos":{"total":"int","media":"float"},"pila":[],"devuelve":null},{"linea":5,"estado":{"total":18,"media":4.0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"total":"18","media":"4.0"},"tipos":{"total":"int","media":"float"},"pila":[],"devuelve":null},{"linea":6,"estado":{"total":18,"media":4.0},"salida":"4.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"total":"18","media":"4.0"},"tipos":{"total":"int","media":"float"},"pila":[],"devuelve":null}],"filas":[["1","0","—"],["2","4","—"],["3","12","—"],["4","12","4.0"],["5","18","4.0"],["6","18","4.0"]]}}
```

Imprime `4.0`: la división se hace antes de sumar la última nota. Basta con mover la línea 4 al final. Este tipo de error, de **orden**, es de los más comunes, y una traza lo descubre enseguida.

## Conexiones

- Todos los visualizadores de este libro son trazas automáticas. Úsalos para **comprobar** tus trazas a mano, no para sustituirlas: activa el modo predicción y apuesta antes de cada paso.
- Hacer trazas es la mejor preparación para los ejercicios de examen del tipo «¿qué imprime este programa?», que aparecen en la certificación PCEP.

## La grieta

Hemos hecho trazas de programas con unas pocas variables. ¿Qué pasa cuando el programa maneja cien datos? Hacerlo a mano sería eterno. Por eso necesitamos estructuras como las listas, y aprender a razonar sobre «una vuelta cualquiera» en lugar de sobre todas.

## Ejercicios

1. **Traza** este programa y di qué imprime:

   ```python
   x = 2
   y = x + 3
   x = x * y
   y = y - x
   print(x, y)
   ```

2. **¿Qué calcula?** Haz la traza con `n = 5`:

   ```python
   n = 5
   r = 1
   while n > 1:
       r = r * n
       n = n - 1
   print(r)
   ```

3. **Encuentra el error.** Este programa debería imprimir los números del 1 al 3, pero no lo hace. Haz la traza y corrígelo.

   ```python
   i = 1
   while i <= 3:
       i = i + 1
       print(i)
   ```

El solucionario está al final del capítulo.

## Solucionario

1. `x = 2`; `y = 5`; `x = 10`; `y = -5`. Imprime **10 -5**.
2. `r` vale 1 → 5 → 20 → 60 → 120 mientras `n` baja de 5 a 1. Imprime **120**: es el **factorial** de 5 (5 · 4 · 3 · 2 · 1).
3. Imprime 2, 3 y 4: el `print` va después de sumar. Se arregla intercambiando las dos líneas del bucle: primero `print(i)` y después `i = i + 1`.
