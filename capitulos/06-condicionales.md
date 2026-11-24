---
title: Condicionales
subtitle: Hacer una cosa u otra según lo que pase
kernelspec:
  name: python3
  display_name: Python 3
description: "Condicionales: hacer una cosa u otra según lo que pase. Python paso a paso, con visualizadores y diagrama de flujo."
---

## Punto de partida

Por la mañana miras por la ventana: si llueve, coges el paraguas; si no, lo dejas en casa. No lo piensas dos veces. Has tomado una decisión con una pregunta de sí o no.

## La pregunta

Hasta ahora, los programas ejecutaban todas sus líneas, una detrás de otra. ¿Cómo hacemos que un programa **decida** qué líneas ejecutar según los datos?

## La idea

Una **condición** es una pregunta cuya respuesta es `True` o `False`. El `if` ejecuta un bloque solo si su condición es verdadera:

```python
if llueve:
    coger_paraguas()
else:
    dejar_paraguas()
```

:::{important} Las reglas del `if`
- El bloque que depende del `if` va **sangrado** (4 espacios). La sangría no es decoración: indica qué líneas están dentro.
- Con `elif` y `else`, las condiciones se comprueban **en orden, de arriba abajo**, y se ejecuta **solo la primera rama verdadera**. Las demás ni se miran.
:::

## Construcción

### 1 · ¿Aprobado o suspenso?

:::{tip} Predice
¿Qué rama se ejecutará con `nota = 6.5`? ¿Qué línea se salta el programa?
:::

```{code-cell} python
nota = 6.5
if nota >= 5:
    resultado = "aprobado"
else:
    resultado = "suspenso"
print(resultado)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"¿Aprobado o suspenso?","etiqueta":"if · else","idea":"La condición se evalúa con los valores del momento: 6.5 >= 5 es True. El programa entra en la primera rama y salta por encima del else.","columnas":["nota","resultado"],"fila_en":"cada_linea"},"traza":{"codigo":"nota = 6.5\nif nota >= 5:\n    resultado = \"aprobado\"\nelse:\n    resultado = \"suspenso\"\nprint(resultado)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"nota":6.5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"nota":"6.5"},"tipos":{"nota":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"nota":6.5},"salida":"","foco":null,"lee":false,"cond":{"expr":"nota >= 5","sust":"6.5 >= 5","valor":true},"vuelta":0,"fila":1,"repr":{"nota":"6.5"},"tipos":{"nota":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"nota":6.5,"resultado":"aprobado"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"nota":"6.5","resultado":"'aprobado'"},"tipos":{"nota":"float","resultado":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"nota":6.5,"resultado":"aprobado"},"salida":"aprobado\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"nota":"6.5","resultado":"'aprobado'"},"tipos":{"nota":"float","resultado":"str"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","6.5","—"],["2","6.5","—"],["3","6.5","'aprobado'"],["6","6.5","'aprobado'"]]}}
```

Mira la columna **Línea** de la tabla de traza: la línea 5 no aparece nunca. El programa no la ha ejecutado.

### 2 · La calificación: varias ramas

:::{tip} Predice
Con `nota = 8.2`, ¿cuántas condiciones se comprobarán antes de decidir?
:::

```{code-cell} python
nota = 8.2
if nota < 5:
    calificacion = "Insuficiente"
elif nota < 7:
    calificacion = "Aprobado"
elif nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"
print(calificacion)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"La calificación","etiqueta":"if · elif · else","idea":"Las condiciones se prueban en orden. 8.2 < 5 es False, 8.2 < 7 es False, 8.2 < 9 es True: entra en Notable y el else ya no se mira.","columnas":["nota","calificacion"],"fila_en":"cada_linea"},"traza":{"codigo":"nota = 8.2\nif nota < 5:\n    calificacion = \"Insuficiente\"\nelif nota < 7:\n    calificacion = \"Aprobado\"\nelif nota < 9:\n    calificacion = \"Notable\"\nelse:\n    calificacion = \"Sobresaliente\"\nprint(calificacion)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"nota":8.2},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"nota":"8.2"},"tipos":{"nota":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"nota":8.2},"salida":"","foco":null,"lee":false,"cond":{"expr":"nota < 5","sust":"8.2 < 5","valor":false},"vuelta":0,"fila":1,"repr":{"nota":"8.2"},"tipos":{"nota":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"nota":8.2},"salida":"","foco":null,"lee":false,"cond":{"expr":"nota < 7","sust":"8.2 < 7","valor":false},"vuelta":0,"fila":2,"repr":{"nota":"8.2"},"tipos":{"nota":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"nota":8.2},"salida":"","foco":null,"lee":false,"cond":{"expr":"nota < 9","sust":"8.2 < 9","valor":true},"vuelta":0,"fila":3,"repr":{"nota":"8.2"},"tipos":{"nota":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"nota":8.2,"calificacion":"Notable"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"nota":"8.2","calificacion":"'Notable'"},"tipos":{"nota":"float","calificacion":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":10,"estado":{"nota":8.2,"calificacion":"Notable"},"salida":"Notable\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"nota":"8.2","calificacion":"'Notable'"},"tipos":{"nota":"float","calificacion":"str"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","8.2","—"],["2","8.2","—"],["4","8.2","—"],["6","8.2","—"],["7","8.2","'Notable'"],["10","8.2","'Notable'"]]}}
```

Fíjate en que la segunda condición es solo `nota < 7`, sin decir `nota >= 5`. No hace falta: si el programa llega a ese `elif`, ya sabe que la primera condición era falsa.

### 3 · Cuando el orden falla

:::{tip} Predice
Con `nota = 9.5`, ¿qué imprimirá este programa? ¿Es lo que querríamos?
:::

```{code-cell} python
nota = 9.5
calificacion = "?"
if nota >= 5:
    calificacion = "Aprobado"
elif nota >= 9:
    calificacion = "Sobresaliente"
print(calificacion)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Cuando el orden falla","etiqueta":"elif · error típico","idea":"9.5 >= 5 es True, así que entra en la primera rama. El elif de Sobresaliente nunca llega a comprobarse: con este orden es inalcanzable.","columnas":["nota","calificacion"],"fila_en":"cada_linea"},"traza":{"codigo":"nota = 9.5\ncalificacion = \"?\"\nif nota >= 5:\n    calificacion = \"Aprobado\"\nelif nota >= 9:\n    calificacion = \"Sobresaliente\"\nprint(calificacion)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"nota":9.5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"nota":"9.5"},"tipos":{"nota":"float"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"nota":9.5,"calificacion":"?"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"nota":"9.5","calificacion":"'?'"},"tipos":{"nota":"float","calificacion":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"nota":9.5,"calificacion":"?"},"salida":"","foco":null,"lee":false,"cond":{"expr":"nota >= 5","sust":"9.5 >= 5","valor":true},"vuelta":0,"fila":2,"repr":{"nota":"9.5","calificacion":"'?'"},"tipos":{"nota":"float","calificacion":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"nota":9.5,"calificacion":"Aprobado"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"nota":"9.5","calificacion":"'Aprobado'"},"tipos":{"nota":"float","calificacion":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"nota":9.5,"calificacion":"Aprobado"},"salida":"Aprobado\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"nota":"9.5","calificacion":"'Aprobado'"},"tipos":{"nota":"float","calificacion":"str"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","9.5","—"],["2","9.5","'?'"],["3","9.5","'?'"],["4","9.5","'Aprobado'"],["7","9.5","'Aprobado'"]]}}
```

:::{warning} Trampa · el orden de las ramas
Si una condición general va antes que una más concreta, la concreta no se ejecutará nunca. Ordena las ramas de la más exigente a la menos (o de la menor a la mayor, como en el ejemplo anterior).
:::

### 4 · ¿Es bisiesto?

Un año es bisiesto si es múltiplo de 4, salvo los múltiplos de 100, que no lo son, salvo a su vez los múltiplos de 400, que sí. Dicho así cuesta. Descompuesto en preguntas ordenadas, de la más particular a la más general, se vuelve un algoritmo:

:::{tip} Predice
¿Fue 1900 bisiesto? Recorre las preguntas a mano antes de ejecutar.
:::

```{code-cell} python
año = 1900
if año % 400 == 0:
    bisiesto = True
elif año % 100 == 0:
    bisiesto = False
elif año % 4 == 0:
    bisiesto = True
else:
    bisiesto = False
print(año, "bisiesto:", bisiesto)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"¿Es bisiesto?","etiqueta":"elif · descomposición","idea":"Cada pregunta usa el resto % para saber si año es múltiplo de algo. 1900 no es múltiplo de 400, pero sí de 100: no es bisiesto, y ahí termina.","columnas":["año","bisiesto"],"fila_en":"cada_linea","mostrar_tipos":true},"traza":{"codigo":"año = 1900\nif año % 400 == 0:\n    bisiesto = True\nelif año % 100 == 0:\n    bisiesto = False\nelif año % 4 == 0:\n    bisiesto = True\nelse:\n    bisiesto = False\nprint(año, \"bisiesto:\", bisiesto)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"año":1900},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"año":"1900"},"tipos":{"año":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"año":1900},"salida":"","foco":null,"lee":false,"cond":{"expr":"año % 400 == 0","sust":"1900 % 400 == 0","valor":false},"vuelta":0,"fila":1,"repr":{"año":"1900"},"tipos":{"año":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"año":1900},"salida":"","foco":null,"lee":false,"cond":{"expr":"año % 100 == 0","sust":"1900 % 100 == 0","valor":true},"vuelta":0,"fila":2,"repr":{"año":"1900"},"tipos":{"año":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"año":1900,"bisiesto":false},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"año":"1900","bisiesto":"False"},"tipos":{"año":"int","bisiesto":"bool"},"pila":[],"devuelve":null,"excepcion":null},{"linea":10,"estado":{"año":1900,"bisiesto":false},"salida":"1900 bisiesto: False\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"año":"1900","bisiesto":"False"},"tipos":{"año":"int","bisiesto":"bool"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","1900","—"],["2","1900","—"],["4","1900","—"],["5","1900","False"],["10","1900","False"]]}}
```

Cambia el año en la celda (prueba 2000, 2024 y 2026) y vuelve a ejecutarla.

### Condiciones compuestas

Varias condiciones se pueden combinar en una sola con `and` (las dos tienen que cumplirse), `or` (basta con una) y `not` (le da la vuelta). El año bisiesto cabe en una línea:

```{code-cell} python
año = 2024
bisiesto = (año % 4 == 0 and año % 100 != 0) or año % 400 == 0
print(bisiesto)
```

### Condiciones anidadas

Un `if` puede ir **dentro** de otro: la pregunta de dentro solo se hace si la de fuera ha tomado ese camino.

```{code-cell} python
edad = 16
con_permiso = True
if edad >= 18:
    print("Puede entrar")
else:
    if con_permiso:
        print("Puede entrar con permiso")
    else:
        print("No puede entrar")
```

Imprime `Puede entrar con permiso`. Un `if` dentro de un `else` es un `elif` disfrazado: se podría escribir `elif con_permiso:` con una sangría menos. Pero a veces la pregunta de dentro es una **segunda** pregunta, no otra rama:

```{code-cell} python
nota = 9.5
if nota >= 5:
    print("Aprobado")
    if nota >= 9:
        print("Y con matrícula")
print("Fin")
```

Con 9,5 imprime las tres líneas; con un 7, solo `Aprobado` y `Fin`; con un 3, solo `Fin`. Lo que decide qué pregunta está dentro de cuál es la **sangría**.

## Conexiones

- El `if` es la segunda pieza de todo algoritmo. Con la asignación y la iteración ya tienes las tres.
- Dentro de un bucle, un `if` se convierte en un filtro o en un campeón provisional, como verás en [Recorrer listas](08-recorrer-listas.md).

## La grieta

¿Y si hubiera que poner la calificación a los 30 alumnos de la clase? ¿Copiarías el `if` treinta veces? Esa pregunta abre los bucles.

## Preguntas tipo examen

Preguntas como las del examen PCEP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","capitulo":"06","titulo":"Preguntas tipo examen","etiqueta":"PCEP"}}
```

## Ejercicios

1. **¿Qué imprime?** con `x = 7`:

   ```python
   if x > 5:
       print("A")
   if x > 6:
       print("B")
   else:
       print("C")
   ```

2. **Par o impar.** Escribe un programa que, dado `n`, imprima `"par"` o `"impar"`.
3. **Corrige el orden** del programa «Cuando el orden falla» para que con `nota = 9.5` imprima `Sobresaliente`.

El solucionario está al final del capítulo.

## Solucionario

1. Imprime **A** y **B**. Son dos `if` independientes, no un `if`/`elif`: se comprueban los dos. El `else` pertenece solo al segundo `if`, que es verdadero, así que `C` no se imprime.
2. Una solución:

   ```python
   n = 17
   if n % 2 == 0:
       print("par")
   else:
       print("impar")
   ```

3. Basta con poner primero la condición más exigente:

   ```python
   if nota >= 9:
       calificacion = "Sobresaliente"
   elif nota >= 5:
       calificacion = "Aprobado"
   ```
