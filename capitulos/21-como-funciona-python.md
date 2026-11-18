---
title: Cómo funciona Python
subtitle: Del texto que escribes a lo que hace el ordenador
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Una receta escrita en castellano no sirve de nada a quien solo habla japonés. Hace falta alguien que la traduzca: o la traduce entera de una vez y se la da impresa, o se la va leyendo y traduciendo frase a frase mientras cocina. Con los programas pasa lo mismo.

## La pregunta

El procesador de un ordenador solo entiende instrucciones muy simples, en binario. ¿Cómo llega a ejecutarse algo como `print("hola")`? ¿Y qué reglas tiene que cumplir lo que escribimos para que Python lo acepte?

## La idea

Hay dos formas de traducir un programa:

| | Compilar | Interpretar |
|---|---|---|
| Cómo | se traduce **todo** el programa antes de ejecutarlo | se traduce y ejecuta **instrucción a instrucción** |
| Quién lo hace | un **compilador** | un **intérprete** |
| Resultado | un ejecutable que funciona sin el compilador | hace falta el intérprete cada vez |
| Ventaja | más rápido al ejecutarse | más cómodo para probar y corregir |
| Ejemplos | C, C++, Rust | Python, JavaScript |

Python es un lenguaje **interpretado**, aunque con un paso intermedio: el intérprete oficial, CPython, primero convierte tu código en **bytecode** (unas instrucciones sencillas propias de Python) y después lo va ejecutando. Por eso puedes probar una línea suelta y ver el resultado al momento.

Como cualquier lengua, un lenguaje de programación tiene tres niveles:

| Nivel | Qué fija | Un error de ese nivel | Ejemplo |
|---|---|---|---|
| **Léxico** | qué «palabras» existen: nombres, números, símbolos | un carácter que no pertenece al lenguaje | `precio€ = 3` |
| **Sintaxis** | cómo se combinan esas palabras | una frase mal construida | `if x > 3 print(x)` (falta `:`) |
| **Semántica** | qué significa lo que está bien construido | algo bien escrito que no tiene sentido | `"5" + 3`, o una fórmula equivocada |

Los errores léxicos y sintácticos los detecta Python **antes de empezar**: el programa no llega a ejecutarse. Los semánticos aparecen al ejecutar (un `TypeError`) o, peor, nunca avisan y solo se notan en el resultado.

## Construcción

### 1 · Pedir datos, convertirlos y mostrarlos

`input()` muestra un mensaje, espera a que el usuario escriba y pulse Intro, y devuelve lo que ha escrito. Siempre como **texto**, aunque sea un número.

:::{tip} Predice
El usuario teclea `7` y luego `3`. ¿Qué imprime `a * b`? ¿Por qué no es 21?
:::

```{code-cell} python
a = input("Primer número: ")
b = int(input("Segundo número: "))
print(a * b)
print(int(a) * b)
print(a, b, sep=" y ", end="!\n")
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Texto que parece número","etiqueta":"input · int · sep y end","idea":"a se queda como texto, '7', y b se convierte en el número 3. Por eso a * b repite la cadena tres veces: '777'. Para multiplicar hay que convertir antes con int(a).","entradas":["7","3"],"columnas":["a","b"],"fila_en":"cada_linea","mostrar_tipos":true},"traza":{"codigo":"a = input(\"Primer número: \")\nb = int(input(\"Segundo número: \"))\nprint(a * b)\nprint(int(a) * b)\nprint(a, b, sep=\" y \", end=\"!\\n\")","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"a":"7"},"salida":"Primer número: 7\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"a":"'7'"},"tipos":{"a":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"a":"7","b":3},"salida":"Primer número: 7\nSegundo número: 3\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"a":"'7'","b":"3"},"tipos":{"a":"str","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":"7","b":3},"salida":"Primer número: 7\nSegundo número: 3\n777\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"a":"'7'","b":"3"},"tipos":{"a":"str","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":"7","b":3},"salida":"Primer número: 7\nSegundo número: 3\n777\n21\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"a":"'7'","b":"3"},"tipos":{"a":"str","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":"7","b":3},"salida":"Primer número: 7\nSegundo número: 3\n777\n21\n7 y 3!\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"a":"'7'","b":"3"},"tipos":{"a":"str","b":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","'7'","—"],["2","'7'","3"],["3","'7'","3"],["4","'7'","3"],["5","'7'","3"]]}}
```

`print` tiene dos parámetros con nombre muy útiles:

- `sep` es lo que se pone **entre** los valores (por defecto, un espacio);
- `end` es lo que se pone **al final** (por defecto, un salto de línea `"\n"`).

```{code-cell} python
print(1, 2, 3)
print(1, 2, 3, sep="-")
print("sin salto", end=" ")
print("de línea")
```

### 2 · Palabras reservadas, sentencias y expresiones

Las **palabras reservadas** (*keywords*) son las del propio lenguaje, y no se pueden usar como nombres de variables:

```{code-cell} python
import keyword
print(len(keyword.kwlist))
print(keyword.kwlist)
```

- Una **expresión** es algo que se calcula y da un valor: `3 + 4`, `len(nombre)`, `x > 0`.
- Una **sentencia** es una orden completa: `x = 3 + 4`, `if x > 0:`, `import math`.

Python marca los bloques con la **sangría**: todas las líneas de un mismo bloque deben empezar exactamente en la misma columna. Lo habitual son 4 espacios. Si una línea se descoloca, aparece `IndentationError`.

Todo lo que va detrás de `#` es un **comentario**: Python lo ignora. Sirve para explicar el código y también para «apagar» una línea sin borrarla.

```{code-cell} python
# Esto es un comentario: no se ejecuta
precio = 20      # un comentario puede ir al final de una línea
# print("esta línea está apagada")
print(precio)
```

### 3 · Literales: escribir valores directamente

Un **literal** es un valor escrito tal cual en el código:

| Tipo | Literales | Notas |
|---|---|---|
| `int` | `17`, `-3`, `1_000_000` | los `_` solo ayudan a leer |
| `float` | `2.5`, `.5`, `4.`, `1e3`, `1.5e-3` | `1e3` es 1000.0 y `1.5e-3` es 0.0015 |
| `str` | `'hola'`, `"hola"`, `"""varias líneas"""` | comillas simples o dobles, iguales |
| `bool` | `True`, `False` | con mayúscula inicial |

Los enteros también se pueden escribir en binario (`0b1010`), octal (`0o12`) o hexadecimal (`0xA`): los tres valen 10.

:::{warning} Los decimales no son exactos
Un `float` se guarda en binario y muchos decimales no tienen representación exacta, igual que 1/3 no la tiene en decimal. Por eso `0.1 + 0.2` da `0.30000000000000004` y `0.1 + 0.2 == 0.3` es `False`. Para comparar decimales, usa una tolerancia o `round`.
:::

```{code-cell} python
print(0.1 + 0.2, 0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3, abs((0.1 + 0.2) - 0.3) < 1e-9)
```

### 4 · Operadores: quién va primero

Cuando una expresión tiene varios operadores, Python sigue un orden de **prioridad** (precedencia), de mayor a menor:

| Prioridad | Operadores | Asociatividad |
|---|---|---|
| 1 | `**` | de derecha a izquierda |
| 2 | `+x`, `-x` (unarios: un solo operando) | |
| 3 | `*`, `/`, `//`, `%` | de izquierda a derecha |
| 4 | `+`, `-` (binarios: dos operandos) | de izquierda a derecha |
| 5 | `==`, `!=`, `<`, `<=`, `>`, `>=` | |
| 6 | `not` | |
| 7 | `and` | |
| 8 | `or` | |

Los paréntesis mandan sobre todo. Tres casos que caen en los exámenes:

```{code-cell} python
print(2 ** 3 ** 2)      # 2 ** 9 = 512: la potencia se agrupa por la derecha
print(-2 ** 2)          # -(2 ** 2) = -4: la potencia va antes que el signo
print(10 - 4 - 3)       # (10 - 4) - 3 = 3: la resta, por la izquierda
print(True or False and False)   # and antes que or: True
```

En `-2 ** 2`, el `-` es un operador **unario** (actúa sobre un solo valor), y tiene menos prioridad que `**`. En `10 - 4`, el `-` es **binario**.

Los **operadores de asignación aumentada** combinan una operación y una asignación:

:::{tip} Predice
¿Cuánto vale `x` al final?
:::

```{code-cell} python
x = 5
x += 3
x *= 2
x //= 3
x **= 2
print(x)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Asignación aumentada","etiqueta":"+= · *= · //= · **=","idea":"Cada operador aumentado es una abreviatura: x += 3 es x = x + 3. El valor viejo de x se usa para calcular el nuevo: 5, 8, 16, 5 y 25.","columnas":["x"],"fila_en":"cada_linea","mostrar_tipos":true},"traza":{"codigo":"x = 5\nx += 3\nx *= 2\nx //= 3\nx **= 2\nprint(x)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"x":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"x":"5"},"tipos":{"x":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"x":8},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"x":"8"},"tipos":{"x":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"x":16},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"x":"16"},"tipos":{"x":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"x":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"x":"5"},"tipos":{"x":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"x":25},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"x":"25"},"tipos":{"x":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"x":25},"salida":"25\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"x":"25"},"tipos":{"x":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","5"],["2","8"],["3","16"],["4","5"],["5","25"],["6","25"]]}}
```

### 5 · Nombres válidos y nombres buenos

Un nombre (identificador) puede llevar letras, dígitos y `_`, pero **no puede empezar por un dígito** ni ser una palabra reservada. Python distingue mayúsculas: `nota` y `Nota` son variables distintas.

| Nombre | ¿Válido? | Por qué |
|---|---|---|
| `nota_final` | sí | |
| `_privado` | sí | |
| `nota2` | sí | |
| `2nota` | no | empieza por un dígito |
| `nota-final` | no | el `-` es la resta |
| `class` | no | palabra reservada |

Además de válidos, los nombres deben ser **claros**. La guía de estilo de Python, el **PEP 8**, recomienda:

- variables y funciones en minúsculas con `_`: `nota_media`, `calcular_total`;
- constantes en mayúsculas: `IVA = 0.21`;
- clases con cada palabra en mayúscula: `CuentaAhorro`;
- un espacio a cada lado del `=` y de los operadores: `x = a + b`.

## Conexiones

- Los tres tipos de error volverán al final del libro, en [Probar y depurar](20-probar-y-depurar.md): los léxicos y sintácticos los caza Python antes de empezar; los semánticos, tus pruebas.
- `input()` devuelve texto: es la misma trampa del capítulo [Tipos de datos](05-tipos-de-datos.md), ahora con datos que llegan del teclado.

## La grieta

Ya sabemos cómo se escribe cada pieza. Las listas son la estructura que más usaremos: ¿cómo se copian, cómo se insertan y quitan elementos, y cómo se guarda una tabla entera?

## Ejercicios

1. **¿Compilado o interpretado?** Explica con tus palabras por qué en Python puedes ejecutar una línea suelta y ver el resultado al momento.
2. **Clasifica el error** (léxico, sintáctico o semántico): a) `print("hola"`; b) `nota = "8" + 1`; c) `total@ = 5`.
3. **¿Qué imprime?** a) `print(3 + 2 * 2 ** 2)`; b) `print(-3 ** 2)`; c) `print(7 // 2 * 2 + 7 % 2)`.
4. **Edad dentro de diez años.** Escribe un programa que pida la edad con `input`, la convierta y escriba «Dentro de 10 años tendrás 26» si se teclea 16.
5. **Separadores.** Con un solo `print`, escribe `2026-11-18` a partir de las variables `a = 2026`, `m = 11`, `d = 18`.

El solucionario está al final del capítulo.

## Solucionario

1. Porque Python es interpretado: el intérprete traduce y ejecuta cada instrucción en el momento, sin tener que traducir antes un programa completo.
2. a) **Sintáctico**: falta cerrar el paréntesis. b) **Semántico**: está bien escrito, pero no se puede sumar texto y número (`TypeError`). c) **Léxico**: `@` no puede formar parte de un nombre.
3. a) **11**: primero `2 ** 2 = 4`, luego `2 * 4 = 8` y `3 + 8 = 11`. b) **-9**: es `-(3 ** 2)`. c) **7**: `7 // 2 = 3`, `3 * 2 = 6`, `7 % 2 = 1` y `6 + 1 = 7`.
4. Una solución:

   ```python
   edad = int(input("¿Cuántos años tienes? "))
   print("Dentro de 10 años tendrás", edad + 10)
   ```

5. `print(a, m, d, sep="-")`.
