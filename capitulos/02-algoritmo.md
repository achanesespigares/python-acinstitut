---
title: Diseñar el algoritmo
subtitle: Tres piezas bastan para cualquier programa
kernelspec:
  name: python3
  display_name: Python 3
description: "Diseñar el algoritmo: tres piezas bastan para cualquier programa. Python paso a paso, con visualizadores y diagrama de flujo."
---

## Punto de partida

Una receta de cocina dice: «Pon el agua a hervir. Cuando hierva, echa la pasta. Remueve de vez en cuando hasta que esté al dente». Son pasos precisos, en un orden, con una decisión y una repetición, y la receta termina. Eso es un algoritmo, aunque nadie lo llame así en la cocina.

## La pregunta

La especificación dice **qué** hay que conseguir. ¿Cómo describimos **los pasos** para conseguirlo, de forma que cualquiera (también un ordenador) pueda seguirlos sin dudar?

## La idea

Un **algoritmo** es una secuencia finita de pasos precisos que lleva de la entrada a la salida. Y para escribir cualquier algoritmo bastan **tres piezas**:

| Pieza | Qué hace | En la receta | En Python |
|---|---|---|---|
| **Secuencia** (asignación) | hacer un paso tras otro, guardando resultados | «pon el agua» | `x = ...` |
| **Decisión** (condicional) | elegir según una condición | «cuando hierva…» | `if` |
| **Repetición** (iteración) | repetir mientras se cumpla algo | «remueve hasta que…» | `while`, `for` |

:::{important} Primero en tu idioma, después en Python
Un algoritmo se puede escribir en **pseudocódigo**: frases cortas y precisas, sin la gramática estricta de un lenguaje de programación. Cuando el pseudocódigo funciona, traducirlo a Python es la parte fácil. En este capítulo verás el Python ya traducido: no hace falta que entiendas cada detalle todavía, léelo como un pseudocódigo un poco más estricto.
:::

## Construcción

### 1 · El mayor de tres números

**Especificación:** entrada, tres números `a`, `b` y `c`; salida, el mayor.

Pseudocódigo:

```text
mayor ← a
si b > mayor, entonces mayor ← b
si c > mayor, entonces mayor ← c
devolver mayor
```

Es la estrategia del **campeón provisional**: el primero es el campeón hasta que alguien lo supera. El mismo algoritmo como diagrama de flujo:

```{mermaid}
flowchart TD
    A([Inicio]) --> B[mayor ← a]
    B --> C{¿b > mayor?}
    C -- sí --> D[mayor ← b]
    C -- no --> E{¿c > mayor?}
    D --> E
    E -- sí --> F[mayor ← c]
    E -- no --> G([Devolver mayor])
    F --> G
```

:::{tip} Predice
Con `a = 4`, `b = 9` y `c = 7`, ¿cuántas veces cambia `mayor`?
:::

```{code-cell} python
a = 4
b = 9
c = 7
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print(mayor)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El mayor de tres números","etiqueta":"secuencia + decisión","idea":"mayor empieza siendo a, el campeón provisional. Cada número nuevo lo reta: si es mayor, ocupa su puesto. Al final, mayor es el máximo.","columnas":["mayor"],"fila_en":"cada_linea"},"traza":{"codigo":"a = 4\nb = 9\nc = 7\nmayor = a\nif b > mayor:\n    mayor = b\nif c > mayor:\n    mayor = c\nprint(mayor)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"a":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"4"},"tipos":{"a":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"a":4,"b":9},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"4","b":"9"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":4,"b":9,"c":7},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"4","b":"9","c":"7"},"tipos":{"a":"int","b":"int","c":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":4,"b":9,"c":7,"mayor":4},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"a":"4","b":"9","c":"7","mayor":"4"},"tipos":{"a":"int","b":"int","c":"int","mayor":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":4,"b":9,"c":7,"mayor":4},"salida":"","foco":null,"lee":false,"cond":{"expr":"b > mayor","sust":"9 > 4","valor":true},"vuelta":0,"fila":1,"repr":{"a":"4","b":"9","c":"7","mayor":"4"},"tipos":{"a":"int","b":"int","c":"int","mayor":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"a":4,"b":9,"c":7,"mayor":9},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"a":"4","b":"9","c":"7","mayor":"9"},"tipos":{"a":"int","b":"int","c":"int","mayor":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"a":4,"b":9,"c":7,"mayor":9},"salida":"","foco":null,"lee":false,"cond":{"expr":"c > mayor","sust":"7 > 9","valor":false},"vuelta":0,"fila":3,"repr":{"a":"4","b":"9","c":"7","mayor":"9"},"tipos":{"a":"int","b":"int","c":"int","mayor":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":9,"estado":{"a":4,"b":9,"c":7,"mayor":9},"salida":"9\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"a":"4","b":"9","c":"7","mayor":"9"},"tipos":{"a":"int","b":"int","c":"int","mayor":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["4","4"],["5","4"],["6","9"],["7","9"],["9","9"]]}}
```

### 2 · El algoritmo de Euclides

Uno de los algoritmos más antiguos que se conocen: el máximo común divisor de dos números, descrito por Euclides hace más de dos mil años.

**Especificación:** entrada, dos enteros positivos `a` y `b`; salida, su máximo común divisor.

La idea: el mcd de `a` y `b` es el mismo que el de `b` y el resto de dividir `a` entre `b`. Los números se van haciendo más pequeños hasta que el resto es 0.

```text
mientras b ≠ 0:
    r ← resto de dividir a entre b
    a ← b
    b ← r
devolver a
```

Tiene también una lectura geométrica: es como embaldosar un rectángulo de `a × b` con las baldosas cuadradas más grandes posibles. El lado del último cuadrado que encaja sin sobrar nada es el mcd.

:::{tip} Predice
mcd(48, 18): ¿cuántas veces se repetirá el bucle? ¿Qué valor tendrá `a` al final?
:::

```{code-cell} python
a = 48
b = 18
while b != 0:
    r = a % b
    a = b
    b = r
print(a)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El algoritmo de Euclides","etiqueta":"secuencia + repetición","idea":"Cada vuelta cambia (a, b) por (b, resto). Los números bajan: 48, 18 → 18, 12 → 12, 6 → 6, 0. Cuando b llega a 0, a es el mcd.","cabecera":3,"puntero":"b","columnas":["a","b"],"fila_en":"comprobacion"},"traza":{"codigo":"a = 48\nb = 18\nwhile b != 0:\n    r = a % b\n    a = b\n    b = r\nprint(a)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"a":48},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"48"},"tipos":{"a":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"a":48,"b":18},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"48","b":"18"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":48,"b":18},"salida":"","foco":null,"lee":false,"cond":{"expr":"b != 0","sust":"18 != 0","valor":true},"vuelta":1,"fila":0,"repr":{"a":"48","b":"18"},"tipos":{"a":"int","b":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":48,"b":18,"r":12},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"a":"48","b":"18","r":"12"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":18,"b":18,"r":12},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"a":"18","b":"18","r":"12"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"a":18,"b":12,"r":12},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"a":"18","b":"12","r":"12"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":18,"b":12,"r":12},"salida":"","foco":null,"lee":false,"cond":{"expr":"b != 0","sust":"12 != 0","valor":true},"vuelta":2,"fila":1,"repr":{"a":"18","b":"12","r":"12"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":18,"b":12,"r":6},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"a":"18","b":"12","r":"6"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":12,"b":12,"r":6},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"a":"12","b":"12","r":"6"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"a":12,"b":6,"r":6},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"a":"12","b":"6","r":"6"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":12,"b":6,"r":6},"salida":"","foco":null,"lee":false,"cond":{"expr":"b != 0","sust":"6 != 0","valor":true},"vuelta":3,"fila":2,"repr":{"a":"12","b":"6","r":"6"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":12,"b":6,"r":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"a":"12","b":"6","r":"0"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":6,"b":6,"r":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"a":"6","b":"6","r":"0"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"a":6,"b":0,"r":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"a":"6","b":"0","r":"0"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":6,"b":0,"r":0},"salida":"","foco":null,"lee":false,"cond":{"expr":"b != 0","sust":"0 != 0","valor":false},"vuelta":4,"fila":3,"repr":{"a":"6","b":"0","r":"0"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"a":6,"b":0,"r":0},"salida":"6\n","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"a":"6","b":"0","r":"0"},"tipos":{"a":"int","b":"int","r":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["48","18","Sí"],["18","12","Sí"],["12","6","Sí"],["6","0","No"]]}}
```

### 3 · ¿Termina siempre? ¿Es correcto?

Diseñar un algoritmo no es solo escribir los pasos. Hay que poder responder dos preguntas:

- **¿Termina?** En Euclides, `b` es siempre más pequeño en cada vuelta (el resto es menor que el divisor) y nunca negativo, así que tarde o temprano llega a 0.
- **¿Da el resultado correcto?** Cada vuelta conserva el mcd: mcd(48, 18) = mcd(18, 12) = mcd(12, 6) = mcd(6, 0) = 6.

## Conexiones

- Las tres piezas son exactamente los tres capítulos del bloque 1 y el bloque 2: asignación, condicionales y bucles.
- El campeón provisional volverá en [Recorrer listas](08-recorrer-listas.md), para encontrar el máximo de una lista entera.

## La grieta

Hemos dicho que Euclides «da el resultado correcto», y lo hemos comprobado con el visualizador. Pero ¿cómo comprobarías tú, solo con papel y lápiz, que un programa hace lo que dices, antes de ejecutarlo? Esa es la técnica del capítulo siguiente: las trazas a mano.

## Ejercicios

1. **Pseudocódigo.** Escribe el algoritmo para decidir si un alumno aprueba: entrada, una nota; salida, «aprobado» si es al menos 5 y «suspenso» si no.
2. **Euclides a mano.** Calcula mcd(35, 21) siguiendo el pseudocódigo. Escribe los valores de `a` y `b` en cada vuelta.
3. **Tres piezas.** En el algoritmo «cuenta cuántos números pares hay entre 1 y 20», ¿dónde está cada una de las tres piezas?

El solucionario está al final del capítulo.

## Solucionario

1. Una solución:

   ```text
   si nota ≥ 5, entonces resultado ← "aprobado"
   si no, resultado ← "suspenso"
   devolver resultado
   ```

2. (35, 21) → (21, 14) → (14, 7) → (7, 0). El mcd es **7**.
3. **Secuencia:** empezar el contador en 0 y sumarle 1 cuando toca. **Decisión:** comprobar si cada número es par. **Repetición:** recorrer los números del 1 al 20. Resultado: 10 pares.
