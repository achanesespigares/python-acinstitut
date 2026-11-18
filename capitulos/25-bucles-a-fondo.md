---
title: Bucles a fondo
subtitle: Saltar, anidar y parar a tiempo
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Al corregir exámenes, saltas los que están en blanco, sigues con el siguiente montón cuando acabas uno y paras cuando llegas a la hoja que dice «fin». No es un recorrido rígido de principio a fin: tiene atajos, niveles y una señal de parada.

## La pregunta

¿Cómo se salta una vuelta sin salir del bucle? ¿Cómo se repite algo hasta que el usuario diga basta, sin saber cuántas veces será? ¿Y qué ocurre al meter un bucle dentro de otro?

## La idea

| Herramienta | Qué hace |
|---|---|
| `break` | sale del bucle de golpe |
| `continue` | se salta **el resto de esta vuelta** y pasa a la siguiente |
| `pass` | no hace nada: ocupa el sitio de un bloque que todavía está vacío |
| valor **centinela** | un valor especial que significa «ya está» (por ejemplo, `-1`) |
| bucles **anidados** | un bucle dentro de otro: el de dentro da todas sus vueltas por cada vuelta del de fuera |

## Construcción

### 1 · `continue`: saltar una vuelta

:::{tip} Predice
¿Qué números llegan a sumarse? ¿Cuántas veces se ejecuta la línea de la suma?
:::

```{code-cell} python
datos = [4, -2, 7, -5, 3]
suma = 0
for d in datos:
    if d < 0:
        continue
    suma += d
print(suma)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Sumar solo los positivos","etiqueta":"continue","idea":"Con un número negativo, continue se salta el resto de la vuelta: la suma no se ejecuta y el for pasa directamente al siguiente. Solo se suman 4, 7 y 3.","lista":"datos","cabecera":3,"puntero":"d","columnas":["d","suma"],"fila_en":"fin_iteracion"},"traza":{"codigo":"datos = [4, -2, 7, -5, 3]\nsuma = 0\nfor d in datos:\n    if d < 0:\n        continue\n    suma += d\nprint(suma)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"datos":[4,-2,7,-5,3]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]"},"tipos":{"datos":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"datos":[4,-2,7,-5,3],"suma":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"0"},"tipos":{"datos":"list","suma":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[4,-2,7,-5,3],"suma":0,"d":4},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"0","d":"4"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"datos":[4,-2,7,-5,3],"suma":0,"d":4},"salida":"","foco":0,"lee":false,"cond":{"expr":"d < 0","sust":"4 < 0","valor":false},"vuelta":1,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"0","d":"4"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"datos":[4,-2,7,-5,3],"suma":4,"d":4},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"4","d":"4"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[4,-2,7,-5,3],"suma":4,"d":-2},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"4","d":"-2"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"datos":[4,-2,7,-5,3],"suma":4,"d":-2},"salida":"","foco":1,"lee":false,"cond":{"expr":"d < 0","sust":"-2 < 0","valor":true},"vuelta":2,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"4","d":"-2"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"datos":[4,-2,7,-5,3],"suma":4,"d":-2},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"4","d":"-2"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[4,-2,7,-5,3],"suma":4,"d":7},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"4","d":"7"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"datos":[4,-2,7,-5,3],"suma":4,"d":7},"salida":"","foco":2,"lee":false,"cond":{"expr":"d < 0","sust":"7 < 0","valor":false},"vuelta":3,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"4","d":"7"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"datos":[4,-2,7,-5,3],"suma":11,"d":7},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"11","d":"7"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[4,-2,7,-5,3],"suma":11,"d":-5},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"11","d":"-5"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"datos":[4,-2,7,-5,3],"suma":11,"d":-5},"salida":"","foco":3,"lee":false,"cond":{"expr":"d < 0","sust":"-5 < 0","valor":true},"vuelta":4,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"11","d":"-5"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"datos":[4,-2,7,-5,3],"suma":11,"d":-5},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"11","d":"-5"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[4,-2,7,-5,3],"suma":11,"d":3},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":5,"fila":3,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"11","d":"3"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"datos":[4,-2,7,-5,3],"suma":11,"d":3},"salida":"","foco":4,"lee":false,"cond":{"expr":"d < 0","sust":"3 < 0","valor":false},"vuelta":5,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"11","d":"3"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"datos":[4,-2,7,-5,3],"suma":14,"d":3},"salida":"","foco":4,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"14","d":"3"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[4,-2,7,-5,3],"suma":14,"d":3},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":4,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"14","d":"3"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"datos":[4,-2,7,-5,3],"suma":14,"d":3},"salida":"14\n","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"datos":"[4, -2, 7, -5, 3]","suma":"14","d":"3"},"tipos":{"datos":"list","suma":"int","d":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["4","4"],["-2","4"],["7","11"],["-5","11"],["3","14"]]}}
```

`continue` evita meter todo el resto del bucle dentro de un `if`. Igual que `break`, se puede usar en un `for` y en un `while`.

### 2 · `while` con centinela

Cuando no sabes cuántos datos van a llegar, se usa un `while` que para al recibir un valor especial, el **centinela**. El esquema tiene tres partes: leer el primer dato **antes** del bucle, comprobarlo en la condición, y leer el siguiente **al final** de cada vuelta.

:::{tip} Predice
Se teclean `7`, `9` y `-1`. ¿Se suma el `-1`? ¿Cuántas vueltas da el bucle?
:::

```{code-cell} python
total = 0
dato = int(input("Nota (-1 para acabar): "))
while dato != -1:
    total += dato
    dato = int(input("Nota (-1 para acabar): "))
print("Total:", total)
```

:::{note} `input()` en el navegador
Al ejecutar las celdas aquí, en el navegador, `input()` no funciona: la celda se queda esperando sin mostrar dónde escribir. El visualizador de abajo simula lo que se teclea. Para probarlo de verdad, copia el código en Google Colab, en Thonny o en tu Jupyter.
:::

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Sumar hasta el centinela","etiqueta":"while · centinela · input","idea":"El primer dato se lee antes del bucle. En cada vuelta se suma el dato y se lee el siguiente. Cuando llega el -1, la condición es False y el bucle termina sin sumarlo.","entradas":["7","9","-1"],"cabecera":3,"columnas":["dato","total"],"fila_en":"comprobacion"},"traza":{"codigo":"total = 0\ndato = int(input(\"Nota (-1 para acabar): \"))\nwhile dato != -1:\n    total += dato\n    dato = int(input(\"Nota (-1 para acabar): \"))\nprint(\"Total:\", total)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"total":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"total":"0"},"tipos":{"total":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"total":0,"dato":7},"salida":"Nota (-1 para acabar): 7\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"total":"0","dato":"7"},"tipos":{"total":"int","dato":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"total":0,"dato":7},"salida":"Nota (-1 para acabar): 7\n","foco":null,"lee":false,"cond":{"expr":"dato != -1","sust":"7 != -1","valor":true},"vuelta":1,"fila":0,"repr":{"total":"0","dato":"7"},"tipos":{"total":"int","dato":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"total":7,"dato":7},"salida":"Nota (-1 para acabar): 7\n","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"total":"7","dato":"7"},"tipos":{"total":"int","dato":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"total":7,"dato":9},"salida":"Nota (-1 para acabar): 7\nNota (-1 para acabar): 9\n","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"total":"7","dato":"9"},"tipos":{"total":"int","dato":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"total":7,"dato":9},"salida":"Nota (-1 para acabar): 7\nNota (-1 para acabar): 9\n","foco":null,"lee":false,"cond":{"expr":"dato != -1","sust":"9 != -1","valor":true},"vuelta":2,"fila":1,"repr":{"total":"7","dato":"9"},"tipos":{"total":"int","dato":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"total":16,"dato":9},"salida":"Nota (-1 para acabar): 7\nNota (-1 para acabar): 9\n","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"total":"16","dato":"9"},"tipos":{"total":"int","dato":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"total":16,"dato":-1},"salida":"Nota (-1 para acabar): 7\nNota (-1 para acabar): 9\nNota (-1 para acabar): -1\n","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"total":"16","dato":"-1"},"tipos":{"total":"int","dato":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"total":16,"dato":-1},"salida":"Nota (-1 para acabar): 7\nNota (-1 para acabar): 9\nNota (-1 para acabar): -1\n","foco":null,"lee":false,"cond":{"expr":"dato != -1","sust":"-1 != -1","valor":false},"vuelta":3,"fila":2,"repr":{"total":"16","dato":"-1"},"tipos":{"total":"int","dato":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"total":16,"dato":-1},"salida":"Nota (-1 para acabar): 7\nNota (-1 para acabar): 9\nNota (-1 para acabar): -1\nTotal: 16\n","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"total":"16","dato":"-1"},"tipos":{"total":"int","dato":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["7","0","Sí"],["9","7","Sí"],["-1","16","No"]]}}
```

:::{warning} Trampa · el bucle infinito
Si dentro del `while` nada cambia la variable de la condición, la condición nunca se vuelve falsa y el programa no termina. En el ejemplo, si olvidaras la última línea (leer el siguiente dato), el bucle sumaría el 7 para siempre. En un cuaderno, se para con el botón de detener; en la terminal, con `Ctrl+C`.
:::

### 3 · El operador morsa `:=`

El operador `:=` (llamado morsa por su forma) asigna un valor **dentro de una expresión**. Permite leer y comprobar en la misma línea:

```{code-cell} python
datos = [3, 8, 1]
if (n := len(datos)) > 2:
    print("Hay", n, "datos")

pila = [1, 2, 3]
while (cima := pila.pop()) != 1:
    print("saco", cima)
```

Con el centinela, quedaría `while (dato := int(input("Nota: "))) != -1:`, sin repetir la lectura. Úsalo cuando ahorre una línea repetida, no por costumbre: a veces se lee peor.

### 4 · `range` con paso, también hacia atrás

`range(inicio, fin, paso)` genera desde `inicio` hasta antes de `fin`, de `paso` en `paso`. Con un paso negativo, cuenta hacia atrás, y entonces `fin` tiene que ser **menor** que `inicio`.

```{code-cell} python
print(list(range(0, 10, 3)))
print(list(range(10, 0, -2)))
print(list(range(5, 0, -1)))
print(list(range(0, 5, -1)))      # vacío: con paso negativo, hacia 5 no se llega
```

### 5 · Bucles anidados

En un bucle anidado, **el de dentro da todas sus vueltas por cada vuelta del de fuera**. Si el de fuera da 3 vueltas y el de dentro 4, el cuerpo interior se ejecuta 3 × 4 = 12 veces.

```{code-cell} python
for fila in range(1, 4):
    for col in range(1, 5):
        print(fila * col, end="\t")
    print()
```

El `print()` vacío del final está en el bucle de fuera: hace el salto de línea después de cada fila. El recorrido de una tabla casilla a casilla, con su visualizador, está en [Listas a fondo](22-listas-a-fondo.md).

:::{important} `break` solo sale de un bucle
En bucles anidados, `break` y `continue` actúan sobre el bucle **más interior** en el que están. Para salir de los dos a la vez, lo habitual es meter los bucles en una función y usar `return`.
:::

### 6 · `pass`: el hueco que Python exige

Un bloque no puede estar vacío. Mientras escribes un programa, `pass` sirve para dejar un hueco que rellenarás después:

```{code-cell} python
for n in range(3):
    pass                  # aquí irá algo más adelante

def calcular_nota():
    pass                  # función pendiente de escribir

print(calcular_nota())
```

## Conexiones

- A `break` y `continue` se les sumará el `else` de los bucles, en [Comprensiones, for…else y match](15-comprensiones.md): un bloque que solo se ejecuta si el bucle termina sin `break`.
- El esquema del centinela es la plantilla de cualquier programa que lee datos hasta que se acaban: de un teclado, de un fichero o de una red.
- Dos bucles anidados recorren una tabla; tres, un cubo.

## La grieta

Muchos datos llegan como texto que hay que limpiar y presentar: nombres con espacios de más, mayúsculas desordenadas, números con demasiados decimales. Toca mirar las herramientas de formato de las cadenas.

## Ejercicios

1. **¿Qué imprime?**

   ```python
   for i in range(5):
       if i == 2:
           continue
       if i == 4:
           break
       print(i, end=" ")
   ```

2. **Contar vueltas.** ¿Cuántas veces se imprime `"*"`?

   ```python
   for i in range(3):
       for j in range(i):
           print("*")
   ```

3. **Adivina el número.** Escribe un programa que pida números hasta que el usuario acierte el `7`, y diga cuántos intentos ha necesitado.
4. **Hacia atrás.** Escribe con `range` la lista `[20, 15, 10, 5, 0]`.
5. **Tabla de multiplicar.** Escribe las tablas del 1 al 3, del 1 al 10, separando cada tabla con una línea en blanco.

El solucionario está al final del capítulo.

## Solucionario

1. Imprime **0 1 3**. Con `i == 2`, `continue` se salta el `print`; con `i == 4`, `break` sale antes de imprimir.
2. **3 veces**: el bucle interior da 0 vueltas con `i = 0`, 1 con `i = 1` y 2 con `i = 2`.
3. Una solución:

   ```python
   intentos = 1
   n = int(input("Adivina: "))
   while n != 7:
       intentos += 1
       n = int(input("Adivina: "))
   print("¡Bien! Lo has conseguido en", intentos, "intentos")
   ```

4. `list(range(20, -1, -5))`. El fin tiene que ser `-1` (o cualquier número entre `-5` y `-1`) para que el `0` entre.
5. Una solución:

   ```python
   for tabla in range(1, 4):
       for n in range(1, 11):
           print(tabla, "x", n, "=", tabla * n)
       print()
   ```
