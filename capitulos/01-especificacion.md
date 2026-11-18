---
title: Especificar el problema
subtitle: Qué entra, qué sale y cómo lo compruebo
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Le pides a un amigo que te traiga fruta del mercado y vuelve con tres kilos de kiwis. Ha cumplido el encargo, pero no era lo que querías. La culpa no es suya: no le dijiste qué fruta, ni cuánta, ni para qué.

## La pregunta

Un ordenador es un amigo extremadamente obediente y nada imaginativo: hace exactamente lo que le dices, ni más ni menos. ¿Qué hay que dejar claro **antes** de escribir una sola línea de código?

## La idea

Crear un programa tiene tres fases: **analizar**, **diseñar** e **implementar**. Este capítulo trata de la primera: analizar el problema hasta tener una **especificación**.

Una especificación responde a tres preguntas:

| Pregunta | Qué escribir |
|---|---|
| **Entrada** | Qué datos recibe el programa, de qué tipo y qué valores admite |
| **Salida** | Qué resultado debe dar, y de qué tipo |
| **Ejemplos** | Casos concretos con su resultado esperado, incluidos los casos límite |

:::{important} Los ejemplos son la parte más valiosa
Una frase se puede entender de varias maneras; un ejemplo, no. Si escribes «media de [5, 7] → 6» antes de programar, ya sabes cómo comprobar después si el programa funciona. Los ejemplos de una especificación se convierten en las **pruebas** del programa.
:::

## Construcción

### 1 · La media de las notas

El encargo dice: «Calcula la nota media de un alumno». Parece claro, pero en cuanto intentas especificarlo aparecen preguntas.

:::{tip} Predice
Antes de leer la especificación: ¿qué preguntas le harías a quien te hace el encargo?
:::

:::{card} Especificación · Media de las notas
**Entrada:** una lista de notas. Cada nota es un número entre 0 y 10. La lista tiene **al menos una** nota.

**Salida:** un número (`float`): la suma de las notas dividida entre cuántas hay.

**Ejemplos:**

| Entrada | Salida esperada | Por qué este ejemplo |
|---|---|---|
| `[5, 7]` | `6.0` | caso normal |
| `[10]` | `10.0` | una sola nota |
| `[4, 5, 5]` | `4.666…` | media no entera |
| `[]` | — | **caso límite**: lo excluimos en la entrada |
:::

La lista vacía es el ejemplo más importante de la tabla: obliga a tomar una decisión. Sin notas no hay media (dividiríamos entre 0). La especificación lo resuelve diciendo que la entrada tiene al menos una nota. Otra opción válida sería decidir que, con la lista vacía, el programa avise con un mensaje. Lo que no vale es no haberlo pensado.

### 2 · De los ejemplos a las pruebas

Este es un adelanto: todavía no sabes escribir funciones, pero mira cómo los ejemplos de la especificación se convierten en comprobaciones automáticas. Si todo es correcto, cada línea imprime `True`.

```{code-cell} python
def media(notas):
    return sum(notas) / len(notas)

print(media([5, 7]) == 6.0)
print(media([10]) == 10.0)
print(abs(media([4, 5, 5]) - 4.6667) < 0.001)
```

Cuando cambies el programa más adelante, vuelves a ejecutar estas líneas: si alguna da `False`, sabes enseguida que has roto algo.

### 3 · El precio con descuento

Otro encargo: «Calcula el precio final de un producto con su descuento».

:::{card} Especificación · Precio con descuento
**Entrada:** el precio (un número mayor o igual que 0, en euros) y el descuento (un porcentaje entre 0 y 100).

**Salida:** el precio final, redondeado a céntimos.

**Ejemplos:**

| Precio | Descuento | Salida | Por qué |
|---|---|---|---|
| 100 | 20 | 80.00 | caso normal |
| 59.99 | 0 | 59.99 | sin descuento |
| 40 | 100 | 0.00 | caso límite: gratis |
| 19.99 | 15 | 16.99 | obliga a redondear: 16.9915 |
:::

Fíjate en el último ejemplo: sin él, nadie se habría acordado de decir que el resultado se redondea.

## Conexiones

- Las **funciones** del bloque 3 son especificaciones convertidas en código: los parámetros son la entrada y el `return` es la salida.
- Los casos límite (la lista vacía, el descuento del 100 %) son los que más errores destapan. En el capítulo de bucles verás un programa que falla justo en uno.

## La grieta

Ya sabemos **qué** tiene que hacer el programa. Pero una especificación no dice **cómo** hacerlo. ¿Cómo se describen los pasos para pasar de la entrada a la salida? Eso es un algoritmo, y es el tema del capítulo siguiente.

## Ejercicios

1. **Especifica** este encargo: «Di si un número es par». Escribe la entrada, la salida y al menos tres ejemplos, uno de ellos con el 0.
2. **Encuentra el hueco.** ¿Qué falta en esta especificación? «Entrada: dos números. Salida: el primero dividido entre el segundo.»
3. **Casos límite.** Para el encargo «Calcula la nota media quitando la peor nota», escribe dos casos límite y decide qué debe pasar en cada uno.

El solucionario está al final del capítulo.

## Solucionario

1. **Entrada:** un número entero. **Salida:** `True` si es par y `False` si no. **Ejemplos:** `4 → True`, `7 → False`, `0 → True` (el 0 es par: el resto de dividirlo entre 2 es 0) y `-2 → True`.
2. Falta qué pasa si el segundo número es **0**: no se puede dividir entre 0. Hay que excluirlo en la entrada («el segundo número es distinto de 0») o decir qué hace el programa en ese caso.
3. Por ejemplo: **una sola nota** (si quitas la peor, no queda ninguna: habría que exigir al menos dos notas, o devolver esa nota sin quitar nada) y **varias notas iguales a la peor**, como `[3, 3, 8]` (hay que decidir si se quita una sola o todas; lo habitual es quitar una: media de `[3, 8]` = 5.5).
