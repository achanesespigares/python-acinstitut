---
title: Cadenas y formato
subtitle: Escribir, limpiar y presentar texto
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Los datos que escribe la gente llegan desordenados: «  aNA gaRCía  », con espacios de sobra y mayúsculas al azar. Y los resultados que da un programa tienen que salir presentables: «Ana García: 7,5», no «Ana García: 7.456666666». Limpiar la entrada y cuidar la salida es la mitad del trabajo con texto.

## La pregunta

¿Cómo se escriben en una cadena las comillas, los saltos de línea o los tabuladores? ¿Cómo se arregla un texto mal escrito? ¿Y cómo se mete un número en una frase con los decimales que queramos?

## La idea

Una cadena se puede escribir con comillas simples, dobles o triples. Dentro, la **barra invertida** `\` anuncia un carácter especial: es una **secuencia de escape**.

| Escape | Significa |
|---|---|
| `\n` | salto de línea |
| `\t` | tabulador |
| `\\` | una barra invertida |
| `\'` y `\"` | una comilla, sin cerrar la cadena |

Y todos los métodos de las cadenas **devuelven una cadena nueva**: la original nunca cambia, porque es inmutable.

## Construcción

### 1 · Comillas, escapes y varias líneas

```{code-cell} python
print('Dijo "hola" y se fue')        # comillas dobles dentro de simples
print("It's fine")                   # un apóstrofo dentro de dobles
print('It\'s fine')                  # o escapado
print("Columna1\tColumna2\nfila1\tfila2")
print("C:\\Users\\tony")
poema = """Primera línea
segunda línea
tercera línea"""
print(poema)
print(len("a\nb"))                   # \n es UN carácter
```

Las comillas triples (`"""` o `'''`) permiten escribir una cadena de varias líneas tal cual.

### 2 · Limpiar un texto

:::{tip} Predice
¿Cuántos caracteres tiene `bruto`? ¿Y `limpio`? ¿Cambia `bruto` en algún momento?
:::

```{code-cell} python
bruto = "  aNA gaRCía  "
limpio = bruto.strip()
nombre = limpio.title()
print(len(bruto), len(limpio), nombre)
print(bruto.upper(), bruto.lower(), bruto.swapcase())
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Arreglar un nombre","etiqueta":"strip · title · cadenas nuevas","idea":"strip quita los espacios de los extremos y title pone en mayúscula la primera letra de cada palabra. Cada método fabrica una cadena nueva: bruto se queda como estaba.","columnas":["bruto","limpio","nombre"],"fila_en":"cada_linea"},"traza":{"codigo":"bruto = \"  aNA gaRCía  \"\nlimpio = bruto.strip()\nnombre = limpio.title()\nprint(len(bruto), len(limpio), nombre)\nprint(bruto.upper(), bruto.lower(), bruto.swapcase())","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"bruto":"  aNA gaRCía  "},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"bruto":"'  aNA gaRCía  '"},"tipos":{"bruto":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"bruto":"  aNA gaRCía  ","limpio":"aNA gaRCía"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"bruto":"'  aNA gaRCía  '","limpio":"'aNA gaRCía'"},"tipos":{"bruto":"str","limpio":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"bruto":"  aNA gaRCía  ","limpio":"aNA gaRCía","nombre":"Ana García"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"bruto":"'  aNA gaRCía  '","limpio":"'aNA gaRCía'","nombre":"'Ana García'"},"tipos":{"bruto":"str","limpio":"str","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"bruto":"  aNA gaRCía  ","limpio":"aNA gaRCía","nombre":"Ana García"},"salida":"14 10 Ana García\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"bruto":"'  aNA gaRCía  '","limpio":"'aNA gaRCía'","nombre":"'Ana García'"},"tipos":{"bruto":"str","limpio":"str","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"bruto":"  aNA gaRCía  ","limpio":"aNA gaRCía","nombre":"Ana García"},"salida":"14 10 Ana García\n  ANA GARCÍA     ana garcía     Ana GArcÍA  \n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"bruto":"'  aNA gaRCía  '","limpio":"'aNA gaRCía'","nombre":"'Ana García'"},"tipos":{"bruto":"str","limpio":"str","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","'  aNA gaRCía  '","—","—"],["2","'  aNA gaRCía  '","'aNA gaRCía'","—"],["3","'  aNA gaRCía  '","'aNA gaRCía'","'Ana García'"],["4","'  aNA gaRCía  '","'aNA gaRCía'","'Ana García'"],["5","'  aNA gaRCía  '","'aNA gaRCía'","'Ana García'"]]}}
```

| Método | Qué hace | `"  hola MUNDO "` → |
|---|---|---|
| `upper()` | todo en mayúsculas | `'  HOLA MUNDO '` |
| `lower()` | todo en minúsculas | `'  hola mundo '` |
| `capitalize()` | primera letra en mayúscula, el resto en minúscula | `'  hola mundo '` (empieza por espacio) |
| `title()` | primera de cada palabra en mayúscula | `'  Hola Mundo '` |
| `swapcase()` | cambia mayúsculas por minúsculas y al revés | `'  HOLA mundo '` |
| `strip()` | quita espacios de los dos extremos | `'hola MUNDO'` |
| `lstrip()` / `rstrip()` | solo por la izquierda / solo por la derecha | `'hola MUNDO '` / `'  hola MUNDO'` |
| `replace(a, b)` | cambia cada `a` por `b` | con `("O", "0")`: `'  hola MUND0 '` |

Con `strip`, `lstrip` y `rstrip` se pueden quitar también otros caracteres: `"--hola--".strip("-")` da `'hola'`.

### 3 · Partir y unir

```{code-cell} python
frase = "el sol sale por el este"
palabras = frase.split()
print(palabras, len(palabras))
print("2026-11-18".split("-"))
print(" ".join(palabras[::-1]))
print(", ".join(["pan", "leche", "huevos"]))
```

`split()` sin argumentos trocea por espacios; con un argumento, por ese separador. `join` es su inverso: se llama **sobre el separador** y recibe la lista.

### 4 · Dar formato: f-strings

Una **f-string** es una cadena con una `f` delante; lo que va entre llaves `{}` se calcula y se mete en el texto. Después de `:`, se puede indicar el formato:

```{code-cell} python
nombre, nota, n = "Ana", 7.456, 42
print(f"{nombre} ha sacado un {nota}")
print(f"{nombre} ha sacado un {nota:.1f}")       # 1 decimal
print(f"Doble: {nota * 2:.2f}")                   # expresiones dentro
print(f"[{n:5}] [{n:<5}] [{n:^5}] [{n:05}]")      # ancho, alineación y ceros
print(f"{0.256:.1%}  {1234567:,}")                 # porcentaje y miles
```

| Formato | Significa | Ejemplo con `x = 7.456` |
|---|---|---|
| `{x:.2f}` | 2 decimales | `7.46` |
| `{x:8.2f}` | ancho 8, 2 decimales | `'    7.46'` |
| `{x:<8}` / `{x:>8}` / `{x:^8}` | alinear a la izquierda / derecha / centro | |
| `{n:05}` | rellenar con ceros hasta 5 cifras | `00042` |
| `{x:.1%}` | como porcentaje | `745.6%` |

### 5 · Otras dos formas que verás: `format()` y `%`

Antes de las f-strings existían dos formas, que siguen apareciendo en código antiguo y en los exámenes:

```{code-cell} python
nombre, nota = "Ana", 7.456
print("{} ha sacado un {:.1f}".format(nombre, nota))
print("{1} sacó {0:.1f}".format(nota, nombre))     # por posición
print("%s ha sacado un %.1f" % (nombre, nota))     # el estilo antiguo, con %
```

En el estilo `%`, `%s` es una cadena, `%d` un entero y `%.1f` un decimal con una cifra. Para código nuevo, usa f-strings: son las más legibles.

## Conexiones

- Que los métodos devuelvan cadenas nuevas es consecuencia de la inmutabilidad, que estudiarás a fondo, con Unicode y los puntos de código, en [Cadenas a fondo](19-cadenas-a-fondo.md).
- `split` convierte una línea de texto en una lista: es el primer paso para leer datos de un fichero.
- El formato `:.2f` es el que se usa en cualquier informe con dinero o notas.

## La grieta

Partir líneas por comas con `split(",")` funciona… hasta que un dato lleva una coma dentro, como `"García, Ana"`. Para las tablas guardadas en ficheros existe un formato estándar y un módulo que lo resuelve: CSV.

## Preguntas tipo examen

Preguntas como las del examen PCEP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","capitulo":"26","titulo":"Preguntas tipo examen","etiqueta":"PCEP"}}
```

## Ejercicios

1. **Escapes.** Escribe con un solo `print` y una sola cadena:

   ```text
   Ruta:	C:\datos
   "Listo"
   ```

   (entre `Ruta:` y `C:` hay un tabulador).
2. **¿Qué imprime?** a) `"python".capitalize()`; b) `"Hola Mundo".swapcase()`; c) `"  a b  ".strip().split()`.
3. **Iniciales.** Escribe una función que reciba `"ana garcía lópez"` y devuelva `"AGL"`.
4. **Ticket.** Con `producto = "Café"` y `precio = 1.5`, escribe una f-string que imprima `Café......  1.50 €`: el nombre alineado a la izquierda en 10 caracteres, rellenos de puntos, un espacio, y el precio con dos decimales en un ancho de 5.
5. **Tres formas.** Escribe `Biel: 9.0` de tres maneras: con f-string, con `format()` y con `%`, a partir de `n = "Biel"` y `x = 9`.

El solucionario está al final del capítulo.

## Solucionario

1. `print("Ruta:\tC:\\datos\n\"Listo\"")`.
2. a) `'Python'`; b) `'hOLA mUNDO'`; c) `['a', 'b']`.
3. Una solución:

   ```python
   def iniciales(nombre):
       return "".join(p[0].upper() for p in nombre.split())

   print(iniciales("ana garcía lópez"))
   ```

4. `print(f"{producto:.<10} {precio:5.2f} €")`. El `.` antes de `<` es el carácter de relleno.
5. `f"{n}: {x:.1f}"`, `"{}: {:.1f}".format(n, x)` y `"%s: %.1f" % (n, x)`.
