---
title: Tipos de datos
subtitle: No todo lo que parece un número es un número
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

En una calculadora, 5 + 3 da 8. Pero si escribes «5» en un formulario de la web, después «3», y el programa los junta, a lo mejor sale «53». Los mismos símbolos, dos resultados distintos.

## La pregunta

¿Cómo sabe Python si `5` es una cantidad con la que se puede hacer cuentas o un trozo de texto? ¿Y por qué importa?

## La idea

Cada valor tiene un **tipo**, y el tipo decide qué significa cada operación. Los cuatro tipos básicos son estos:

| Tipo | Qué guarda | Ejemplos |
|---|---|---|
| `int` | números enteros | `17`, `-3`, `0` |
| `float` | números con decimales | `1.75`, `4.0`, `-0.5` |
| `str` | texto (cadenas) | `"Lucía"`, `"5"`, `""` |
| `bool` | verdadero o falso | `True`, `False` |

:::{important} El tipo decide la operación
`+` suma si los dos valores son números, y **pega** si son textos: `"5" + "3"` da `"53"`. Las comillas son las que convierten algo en texto.
:::

## Construcción

### 1 · Cada valor con su tipo

:::{tip} Predice
¿De qué tipo será `mayor`? Fíjate en qué hay a la derecha del `=`.
:::

```{code-cell} python
edad = 17
altura = 1.75
nombre = "Lucía"
mayor = edad >= 18
print(nombre, mayor)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Cada valor con su tipo","etiqueta":"int · float · str · bool","idea":"Cada variable tiene un tipo, que se ve en su etiqueta. Una comparación como edad >= 18 no es un número: es una respuesta, True o False.","columnas":["edad","altura","nombre","mayor"],"fila_en":"cada_linea","mostrar_tipos":true},"traza":{"codigo":"edad = 17\naltura = 1.75\nnombre = \"Lucía\"\nmayor = edad >= 18\nprint(nombre, mayor)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"edad":17},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"edad":"17"},"tipos":{"edad":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"edad":17,"altura":1.75},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"edad":"17","altura":"1.75"},"tipos":{"edad":"int","altura":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"edad":17,"altura":1.75,"nombre":"Lucía"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"edad":"17","altura":"1.75","nombre":"'Lucía'"},"tipos":{"edad":"int","altura":"float","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"edad":17,"altura":1.75,"nombre":"Lucía","mayor":false},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"edad":"17","altura":"1.75","nombre":"'Lucía'","mayor":"False"},"tipos":{"edad":"int","altura":"float","nombre":"str","mayor":"bool"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"edad":17,"altura":1.75,"nombre":"Lucía","mayor":false},"salida":"Lucía False\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"edad":"17","altura":"1.75","nombre":"'Lucía'","mayor":"False"},"tipos":{"edad":"int","altura":"float","nombre":"str","mayor":"bool"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","17","—","—","—"],["2","17","1.75","—","—"],["3","17","1.75","'Lucía'","—"],["4","17","1.75","'Lucía'","False"],["5","17","1.75","'Lucía'","False"]]}}
```

### 2 · Texto que parece número

:::{tip} Predice
¿Qué valdrán `junto`, `suma` y `media`? Ojo con la última: ¿será `4` o `4.0`?
:::

```{code-cell} python
a = "5"
b = "3"
junto = a + b
suma = int(a) + int(b)
media = suma / 2
print(junto, suma, media)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Texto que parece número","etiqueta":"str → int · conversión","idea":"a y b son textos: + los pega. int() los convierte en números, y entonces + suma. Y la división / devuelve siempre un float, aunque el resultado sea exacto.","columnas":["a","b","junto","suma","media"],"fila_en":"cada_linea","mostrar_tipos":true},"traza":{"codigo":"a = \"5\"\nb = \"3\"\njunto = a + b\nsuma = int(a) + int(b)\nmedia = suma / 2\nprint(junto, suma, media)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"a":"5"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"a":"'5'"},"tipos":{"a":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"a":"5","b":"3"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"a":"'5'","b":"'3'"},"tipos":{"a":"str","b":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":"5","b":"3","junto":"53"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"a":"'5'","b":"'3'","junto":"'53'"},"tipos":{"a":"str","b":"str","junto":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":"5","b":"3","junto":"53","suma":8},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"a":"'5'","b":"'3'","junto":"'53'","suma":"8"},"tipos":{"a":"str","b":"str","junto":"str","suma":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":"5","b":"3","junto":"53","suma":8,"media":4.0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"a":"'5'","b":"'3'","junto":"'53'","suma":"8","media":"4.0"},"tipos":{"a":"str","b":"str","junto":"str","suma":"int","media":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"a":"5","b":"3","junto":"53","suma":8,"media":4.0},"salida":"53 8 4.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"a":"'5'","b":"'3'","junto":"'53'","suma":"8","media":"4.0"},"tipos":{"a":"str","b":"str","junto":"str","suma":"int","media":"float"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","'5'","—","—","—","—"],["2","'5'","'3'","—","—","—"],["3","'5'","'3'","'53'","—","—"],["4","'5'","'3'","'53'","8","—"],["5","'5'","'3'","'53'","8","4.0"],["6","'5'","'3'","'53'","8","4.0"]]}}
```

:::{warning} Trampa · `input()` siempre devuelve texto
Lo que el usuario escribe con `input()` llega como `str`, aunque sea un número. Si vas a hacer cuentas con ello, conviértelo primero: `edad = int(input("¿Cuántos años tienes? "))`.
:::

### 3 · Horas y minutos: división entera y resto

:::{tip} Predice
135 minutos, ¿cuántas horas y minutos son? Calcúlalo de cabeza antes de ejecutar.
:::

```{code-cell} python
minutos = 135
horas = minutos // 60
resto = minutos % 60
print(horas, "h", resto, "min")
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Horas y minutos","etiqueta":"// y % · división entera","idea":"// da el cociente entero de la división y % da el resto. Juntos parten una cantidad en unidades grandes y lo que sobra.","columnas":["minutos","horas","resto"],"fila_en":"cada_linea","mostrar_tipos":true},"traza":{"codigo":"minutos = 135\nhoras = minutos // 60\nresto = minutos % 60\nprint(horas, \"h\", resto, \"min\")","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"minutos":135},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"minutos":"135"},"tipos":{"minutos":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"minutos":135,"horas":2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"minutos":"135","horas":"2"},"tipos":{"minutos":"int","horas":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"minutos":135,"horas":2,"resto":15},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"minutos":"135","horas":"2","resto":"15"},"tipos":{"minutos":"int","horas":"int","resto":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"minutos":135,"horas":2,"resto":15},"salida":"2 h 15 min\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"minutos":"135","horas":"2","resto":"15"},"tipos":{"minutos":"int","horas":"int","resto":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","135","—","—"],["2","135","2","—"],["3","135","2","15"],["4","135","2","15"]]}}
```

| Operador | Qué hace | Ejemplo |
|---|---|---|
| `/` | división, siempre `float` | `7 / 2` → `3.5` |
| `//` | cociente entero | `7 // 2` → `3` |
| `%` | resto | `7 % 2` → `1` |
| `**` | potencia | `2 ** 3` → `8` |

## Conexiones

- El resto `%` sirve para mucho más que horas: un número es par si `n % 2 == 0`. Lo usarás en el capítulo de condicionales para saber si un año es bisiesto.
- Los `bool` son la materia prima de las decisiones: toda condición de un `if` o de un `while` acaba siendo `True` o `False`.

## La grieta

`0.1 + 0.2` no da exactamente `0.3` en Python: da `0.30000000000000004`. Pruébalo en una celda. ¿Por qué un ordenador se equivoca sumando decimales tan sencillos? La respuesta está en cómo guarda los `float` en binario.

## Preguntas tipo examen

Preguntas como las del examen PCEP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","capitulo":"05","titulo":"Preguntas tipo examen","etiqueta":"PCEP"}}
```

## Ejercicios

1. **Predice el tipo y el valor** de cada expresión: `7 / 7`, `7 // 2`, `"7" * 3`, `3 > 2`.
2. **Encuentra el error.** Este programa falla. ¿Por qué? ¿Cómo lo arreglas?

   ```python
   edad = "17"
   el_año_que_viene = edad + 1
   ```

3. **Segundos a h:m:s.** Escribe un programa que pase `segundos = 4000` a horas, minutos y segundos usando `//` y `%`.

El solucionario está al final del capítulo.

## Solucionario

1. `7 / 7` → `1.0` (`float`: la división `/` siempre da `float`). `7 // 2` → `3` (`int`). `"7" * 3` → `"777"` (`str`: repetir un texto). `3 > 2` → `True` (`bool`).
2. `edad` es un texto (`"17"`), y Python no sabe sumar un texto y un número: da un `TypeError`. Se arregla convirtiendo: `el_año_que_viene = int(edad) + 1`, que da `18`.
3. Una solución:

   ```python
   segundos = 4000
   horas = segundos // 3600
   minutos = (segundos % 3600) // 60
   seg = segundos % 60
   print(horas, minutos, seg)
   ```

   Imprime `1 6 40`: 4000 s son 1 h, 6 min y 40 s.
