---
title: "Módulo 1 · De cero al PCEP"
subtitle: Sesiones 1 a 15, con su guion, su programa para predecir y su tarea
---

## Cómo leer esta página

Cada sesión tiene cuatro piezas:

- **Objetivo**: lo que el alumnado sabe hacer al salir, dicho en una frase.
- **Predice**: un programa corto que se proyecta al empezar. Cada alumno escribe en papel lo que cree que saldrá, y después se ejecuta y se mira en el visualizador del capítulo.
- **En clase**: el guion de las dos horas, con la situación cotidiana de partida y los ejercicios del capítulo que se hacen en el aula.
- **Tarea**: el trabajo semiguiado para casa, partido en pasos y con una comprobación final.

Las respuestas de los «Predice» y las soluciones de las tareas están juntas al final, en [Soluciones](#soluciones-modulo-1). Cuando se cita «§ 3» de un capítulo, se refiere al movimiento 3 de su construcción.

---

## Sesión 1 · Especificar un problema

**Objetivo.** Decir con precisión qué entra, qué sale y qué se supone antes de escribir una sola línea.

**En el libro.** [Cómo leer este libro](00-como-leer.md) y [Especificación](01-especificacion.md).

### Predice

Es la primera sesión: nadie ha programado. Se proyectan tres líneas y se pregunta qué escribirá cada una.

```python
print("Hola")
print(2 + 3)
print("2 + 3")
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Presentación del curso, del libro y de Colab. Cada alumno abre su cuaderno de clase. |
| 0:15 | **Situación**: pedir a alguien que nos compre «pan» por teléfono. ¿Qué puede salir mal? Cuántas barras, de qué tipo, qué hacer si no hay. |
| 0:30 | **Predice**: las tres líneas de arriba. Se ejecutan en Colab. La diferencia entre `2 + 3` y `"2 + 3"` es la primera grieta del curso. |
| 0:45 | Construcción: entradas, salida, precondición y ejemplos de prueba, con el capítulo. |
| 1:20 | Ejercicios del capítulo, por parejas: cada pareja especifica y la de al lado busca un caso que la rompa. |
| 1:45 | Cierre y presentación de la tarea 1. |

### Tarea 1 · El precio con descuento

Una tienda quiere un programa que calcule lo que paga un cliente con un descuento en porcentaje.

1. Escribe las **entradas**: qué datos necesita el programa y de qué tipo son.
2. Escribe la **salida**: qué devuelve y en qué unidad.
3. Escribe las **precondiciones**: qué valores no tienen sentido (¿un descuento del 150 %?).
4. Escribe **tres ejemplos de prueba** con su resultado, calculado a mano. Uno debe ser un caso límite.
5. Busca la **grieta**: un caso en el que la especificación no dice qué hacer.

**Comprobación.** Con precio 100 € y descuento 20 %, tu especificación debe dar 80 €.

---

## Sesión 2 · Diseñar el algoritmo

**Objetivo.** Escribir los pasos de una solución en lenguaje natural, numerados, y probarlos a mano.

**En el libro.** [Algoritmo](02-algoritmo.md).

### Predice

Sin código todavía: se lee en voz alta este algoritmo y se pregunta qué número dice al final si la lista es 4, 9, 2, 7.

> 1. Apunta el primer número en un papel.
> 2. Para cada número siguiente: si es mayor que el del papel, tacha el del papel y apunta este.
> 3. Di el número del papel.

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 1: cada alumno lee su caso límite. |
| 0:15 | **Situación**: buscar la carta más alta de un mazo boca abajo, mirando de una en una. |
| 0:25 | **Predice**: el algoritmo de arriba, a mano. |
| 0:40 | Construcción: secuencia, decisión y repetición, con el capítulo. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Cierre y tarea 2. |

### Tarea 2 · El menor de una lista

1. Escribe en lenguaje natural, con pasos numerados, un algoritmo que encuentre **el menor** de una lista de números.
2. Pruébalo a mano con la lista 7, 3, 9, 3, 5. Apunta qué hay en el papel después de cada paso.
3. ¿Qué hace tu algoritmo si la lista tiene un solo número? ¿Y si está vacía? Escríbelo como precondición.

**Comprobación.** Con 7, 3, 9, 3, 5 debe salir 3.

---

## Sesión 3 · Seguir un programa con una traza

**Objetivo.** Ejecutar un programa a mano, línea a línea, apuntando el valor de cada variable.

**En el libro.** [Trazas](03-trazas.md).

### Predice

```python
a = 1
b = 0
while a < 20:
    b = b + a
    a = a * 3
print(a, b)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 2. |
| 0:15 | **Situación**: el marcador de un partido; quien lo apunta en la pizarra siempre sabe cuánto va. |
| 0:25 | **Predice**: el programa de arriba, con una tabla de traza en papel. Después, el visualizador. |
| 0:45 | Construcción: la tabla de traza, con el capítulo. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Cierre y tarea 3. |

### Tarea 3 · Una traza completa

```python
x = 10
y = 3
while x > y:
    x = x - y
    y = y + 1
print(x, y)
```

1. Dibuja una tabla con una columna para `x`, otra para `y` y otra para la condición `x > y`.
2. Rellénala fila a fila, una por vuelta del bucle.
3. Escribe lo que imprime el programa.
4. Comprueba en Colab. Si no coincide, busca la primera fila en la que te equivocaste.

**Comprobación.** El bucle da exactamente dos vueltas.

---

## Sesión 4 · Variables, `input` y `print`

**Objetivo.** Guardar datos en variables, pedirlos al usuario y mostrarlos con el formato que se quiera.

**En el libro.** [Variables y asignación](04-variables-asignacion.md) y [Cómo funciona Python](21-como-funciona-python.md) § 1–2.

### Predice

```python
x = 5
y = x
x = x + 2
print(x, y)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 3. |
| 0:15 | **Situación**: una etiqueta con nombre pegada a una caja. Cambiar lo de dentro no cambia la etiqueta. |
| 0:25 | **Predice** y visualizador. |
| 0:40 | Construcción: asignación, `input`, conversión con `int` y `float`, `print` con `sep` y `end`. |
| 1:20 | Ejercicios de los dos capítulos, en Colab (aquí `input` sí funciona). |
| 1:45 | Preguntas tipo examen del capítulo 4 y tarea 4. |

### Tarea 4 · Tarjeta de presentación

1. Pide con `input` el nombre, el año de nacimiento y el año actual.
2. Convierte los dos años a `int` y calcula la edad que se cumple este año.
3. Muestra la tarjeta en tres líneas: el nombre entre guiones, la edad y una despedida.
4. Escribe la segunda línea con un solo `print` y el parámetro `sep`.

**Comprobación.** Con «Ada», 2008 y 2026, la segunda línea debe decir que cumple 18 años.

---

## Sesión 5 · Tipos, literales y operadores

**Objetivo.** Distinguir `int`, `float`, `str` y `bool`, y predecir el resultado de cualquier expresión con sus operadores y prioridades.

**En el libro.** [Tipos de datos](05-tipos-de-datos.md) y [Cómo funciona Python](21-como-funciona-python.md) § 3–5.

### Predice

```python
print(7 / 2, 7 // 2, 7 % 2)
print(2 ** 3 ** 2)
print("3" + "4", 3 + 4)
print(-7 // 2)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 4. |
| 0:15 | **Situación**: repartir 7 caramelos entre 2: a cada uno le tocan 3 y sobra 1. |
| 0:25 | **Predice**. Las dos últimas líneas suelen fallar casi a todos: es el momento de hablar de prioridades y de la división entera con negativos. |
| 0:45 | Construcción: tipos, literales (`0b`, `0o`, `0x`, `1e3`), operadores y su prioridad. |
| 1:20 | Ejercicios de los dos capítulos. |
| 1:45 | Preguntas tipo examen del capítulo 5 y tarea 5. |

### Tarea 5 · De segundos a horas, minutos y segundos

1. Pide un número entero de segundos.
2. Calcula las horas con `//`.
3. Calcula lo que sobra con `%`, y de ahí los minutos y los segundos.
4. Muestra el resultado con un f-string: `1 h 6 min 40 s`.
5. Prueba con 3600 y con 59 antes de dar la tarea por buena.

**Comprobación.** 4000 segundos son 1 h 6 min 40 s.

---

## Sesión 6 · Decidir: `if`, `elif`, `else`

**Objetivo.** Elegir entre varios caminos y saber exactamente cuál se toma.

**En el libro.** [Condicionales](06-condicionales.md).

### Predice

```python
nota = 7.5
if nota >= 5:
    print("Aprobado")
if nota >= 7:
    print("Notable")
elif nota >= 9:
    print("Sobresaliente")
else:
    print("Suficiente")
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 5. |
| 0:15 | **Situación**: un semáforo, y un cruce con dos semáforos seguidos. No es lo mismo dos preguntas que una pregunta con dos respuestas. |
| 0:25 | **Predice**. ¿Por qué no sale «Sobresaliente» con un 9,5? (Se cambia la nota y se vuelve a predecir.) |
| 0:45 | Construcción: `if` encadenados frente a `elif`, operadores lógicos, comparaciones encadenadas. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen y tarea 6. |

### Tarea 6 · Calificación con validación

1. Pide una nota con decimales.
2. Si no está entre 0 y 10, escribe `Nota no válida` y no sigas.
3. Si es válida, escribe la calificación: Suspenso (< 5), Suficiente (< 6), Bien (< 7), Notable (< 9) o Sobresaliente.
4. Ordena las condiciones para que cada una solo tenga que comprobar un límite.
5. Prueba los bordes: 4,99, 5, 9, 10 y 10,5.

**Comprobación.** Un 6,5 es Bien y un 9 es Sobresaliente.

---

## Sesión 7 · Repetir: `while`, `for` y `range`

**Objetivo.** Repetir un bloque un número fijo de veces o mientras se cumpla una condición, y saber cuál de los dos usar.

**En el libro.** [Bucles](07-bucles.md).

### Predice

```python
for i in range(1, 10, 3):
    print(i, end=" ")
print()
n = 0
while n < 3:
    n += 1
print(n)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 6. |
| 0:15 | **Situación**: dar 10 vueltas a la pista frente a correr hasta cansarse. |
| 0:25 | **Predice** y visualizador. |
| 0:40 | Construcción: `while`, `for`, `range` con uno, dos y tres argumentos, acumuladores. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen y tarea 7. |

### Tarea 7 · La tabla de multiplicar

1. Pide un número `n`.
2. Escribe su tabla del 1 al 10 con un `for` y `range`, con este formato: `7 x 3 = 21`.
3. Escríbela otra vez con un `while`. ¿Qué tienes que hacer a mano que el `for` hacía solo?
4. Ampliación: escribe solo las líneas cuyo resultado sea par.

**Comprobación.** La última línea de la tabla del 7 es `7 x 10 = 70`.

---

## Sesión 8 · `break`, `continue`, centinelas y bucles anidados

**Objetivo.** Salir de un bucle antes de tiempo, saltar una vuelta y repetir hasta que llegue un valor especial.

**En el libro.** [Bucles a fondo](25-bucles-a-fondo.md).

### Predice

```python
for n in range(1, 10):
    if n % 2 == 0:
        continue
    if n > 6:
        break
    print(n, end=" ")
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 7. |
| 0:15 | **Situación**: pasar lista y saltarse a quien ya se ha ido; cerrar el cuaderno cuando suena el timbre. |
| 0:25 | **Predice** y visualizador. |
| 0:40 | Construcción: `break`, `continue`, el valor centinela, `while True`, bucles anidados. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen y tarea 8. |

### Tarea 8 · La media con centinela

1. Pide notas una a una hasta que se escriba `-1`.
2. Si una nota no está entre 0 y 10, avisa y sáltala con `continue`.
3. Lleva dos acumuladores: la suma y cuántas notas válidas van.
4. Al terminar, escribe la media con dos decimales, o `No hay notas` si no se escribió ninguna válida.

**Comprobación.** Con 7, 12, 5, 8 y −1, el 12 se ignora y la media es 6,67.

---

## Sesión 9 · Recorrer y modificar listas

**Objetivo.** Guardar muchos datos en una lista, recorrerla, cambiarla y no confundir una copia con un alias.

**En el libro.** [Recorrer listas](08-recorrer-listas.md) y [Listas a fondo](22-listas-a-fondo.md) § 1–4.

### Predice

```python
a = [3, 1, 2]
b = a
b.append(4)
c = a[:]
c[0] = 99
print(a, b, c)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 8. |
| 0:15 | **Situación**: una lista de la compra compartida en el móvil frente a una foto de esa lista. |
| 0:25 | **Predice** y visualizador: el alias se ve con dos flechas hacia la misma caja. |
| 0:45 | Construcción: índices, rebanadas, `append`, `insert`, `pop`, `del`, `sort` y `sorted`. |
| 1:20 | Ejercicios de los dos capítulos. |
| 1:45 | Preguntas tipo examen y tarea 9. |

### Tarea 9 · Estadística sin atajos

Con la lista `datos = [4, 8, 15, 16, 23, 42]`, y **sin usar** `max`, `min` ni `sum`:

1. Recorre la lista una vez y calcula a la vez el máximo, el mínimo y la suma.
2. Calcula la media.
3. Recorre la lista otra vez y cuenta cuántos datos están por encima de la media.
4. Comprueba tus tres primeros resultados con `max`, `min` y `sum`.

**Comprobación.** La media es 18 y hay 2 datos por encima.

---

## Sesión 10 · Tablas, tuplas y conjuntos

**Objetivo.** Representar una tabla con una lista de listas y elegir entre lista, tupla y conjunto según lo que haga falta.

**En el libro.** [Listas a fondo](22-listas-a-fondo.md) § 5 y [Tuplas y conjuntos](23-tuplas-y-conjuntos.md).

### Predice

```python
t = (1, 2) + (3,)
s = {3, 1, 3, 2}
print(t, len(s), 2 in s)
m = [[0] * 3 for _ in range(2)]
m[1][2] = 5
print(m)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 9. |
| 0:15 | **Situación**: el plano de una sala de cine; una entrada dice fila y asiento. |
| 0:25 | **Predice**. Se compara `[[0] * 3 for _ in range(2)]` con `[[0] * 3] * 2`: el visualizador enseña por qué la segunda falla. |
| 0:45 | Construcción: tablas, tuplas y desempaquetado, conjuntos y sus operaciones. |
| 1:20 | Ejercicios de los dos capítulos. |
| 1:45 | Preguntas tipo examen y tarea 10. |

### Tarea 10 · Asientos de cine

1. Crea una sala de 5 filas y 8 asientos con una lista de listas: `0` es libre y `1` ocupado.
2. Ocupa la primera fila entera y los dos primeros asientos de la segunda.
3. Escribe una función `primera_libre(sala)` que devuelva la tupla `(fila, asiento)` del primer asiento libre, recorriendo por filas.
4. Escribe una función `libres(sala)` que cuente los asientos libres.
5. Reserva el asiento que te dé `primera_libre`, desempaquetando la tupla, y dibuja la sala con `X` y `·`.

**Comprobación.** Antes de reservar, el primer libre es `(1, 2)` y hay 30 libres.

---

## Sesión 11 · Cadenas y formato

**Objetivo.** Recorrer y trocear texto, usar sus métodos y presentar resultados con f-strings.

**En el libro.** [Cadenas](10-cadenas.md) y [Cadenas y formato](26-cadenas-y-formato.md).

### Predice

```python
s = "Programar"
print(s[0], s[-1], s[2:5], s[::-1])
print(s.upper().count("R"))
print(f"{3.14159:.2f}|{42:>5}|")
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 10. |
| 0:15 | **Situación**: una palabra escrita con letras de imán en la nevera; para cambiar una hay que componer otra palabra. |
| 0:25 | **Predice**. Las rebanadas se dibujan con los índices entre las letras. |
| 0:45 | Construcción: inmutabilidad, métodos, `in`, f-strings con anchura y decimales. |
| 1:20 | Ejercicios de los dos capítulos. |
| 1:45 | Preguntas tipo examen y tarea 11. |

### Tarea 11 · Validador de contraseñas

Una contraseña es válida si tiene al menos 8 caracteres, alguna mayúscula, alguna minúscula, alguna cifra y ningún espacio.

1. Pide una contraseña.
2. Recorre sus caracteres una vez y anota con tres variables `bool` si has visto mayúscula, minúscula y cifra.
3. Guarda en una lista el texto de cada regla que no se cumple.
4. Si la lista está vacía, escribe `válida`; si no, escribe cada fallo en una línea.

**Comprobación.** `Python2026` es válida; `python 2026A` solo falla por el espacio.

---

## Sesión 12 · Diccionarios

**Objetivo.** Guardar datos por nombre en vez de por posición, y contar con un diccionario.

**En el libro.** [Diccionarios](11-diccionarios.md). Al final de la sesión se presenta el [Proyecto 1](curso-proyecto-1.md).

### Predice

```python
stock = {"pan": 3, "leche": 0}
stock["huevos"] = 12
stock["pan"] -= 1
print(stock.get("queso", "no hay"), len(stock))
for k, v in stock.items():
    if v == 0:
        print(k)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 11. |
| 0:15 | **Situación**: una agenda de teléfonos: se busca por nombre, no por número de página. |
| 0:25 | **Predice** y visualizador. |
| 0:40 | Construcción: claves y valores, `get`, `items`, recorrer, contar. |
| 1:10 | Ejercicios del capítulo. |
| 1:35 | **Presentación del proyecto 1**: el enunciado, los hitos y la rúbrica. Se forman parejas si se trabaja así. |
| 1:50 | Tarea 12 y primer hito. |

### Tarea 12 · Frecuencia de palabras

1. Guarda un texto en una variable. Usa este: `El perro come. ¿El gato come? El perro duerme, y el gato también come.`
2. Pásalo a minúsculas y quita los signos `.,;:!?¿¡` con `replace` dentro de un bucle.
3. Parte el texto en palabras con `split`.
4. Cuenta cada palabra con un diccionario y `get(palabra, 0)`.
5. Recorre el diccionario para encontrar la palabra más repetida.

**Comprobación.** La más repetida es «el», 4 veces; «come» aparece 3.

**Hito 1 del proyecto.** La especificación y el algoritmo del gestor de notas (ver [Proyecto 1](curso-proyecto-1.md)).

---

## Sesión 13 · Funciones

**Objetivo.** Dar nombre a un trozo de programa, pasarle datos y recibir un resultado, y entender qué ve cada función.

**En el libro.** [Funciones](09-funciones.md) y [Funciones a fondo](24-funciones-a-fondo.md).

### Predice

```python
def doble(x):
    x = x * 2
    return x

n = 5
print(doble(n), n)

def saluda(nombre, saludo="Hola"):
    print(saludo, nombre)

saluda("Ana")
saluda("Luis", saludo="Buenas")
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 12 y repaso del hito 1. |
| 0:15 | **Situación**: una receta que se usa en muchos platos; «haz la bechamel» resume seis pasos. |
| 0:25 | **Predice** y visualizador: cada llamada abre su propio marco. |
| 0:40 | Construcción: parámetros, `return`, valores por defecto, argumentos con nombre, `*args`, ámbito, `global`, recursión. |
| 1:20 | Ejercicios de los dos capítulos. |
| 1:45 | Preguntas tipo examen y tarea 13. |

### Tarea 13 · Refactorizar en funciones

Vuelve a tres tareas anteriores y conviértelas en funciones que **devuelven** el resultado, sin `input` ni `print` dentro.

1. `segundos_a_hms(total)` devuelve una tupla `(h, m, s)` (tarea 5).
2. `calificacion(nota)` devuelve el texto de la calificación (tarea 6).
3. `media_de(*numeros)` acepta cualquier cantidad de números y devuelve su media, o `None` si no recibe ninguno.
4. Debajo, prueba cada función con los casos de las tareas originales.

**Comprobación.** `segundos_a_hms(4000)` devuelve `(1, 6, 40)` y `media_de()` devuelve `None`.

**Hito 2 del proyecto.** Las funciones del gestor de notas, probadas con datos escritos a mano.

---

## Sesión 14 · Errores, ficheros, CSV y módulos

**Objetivo.** Que un programa no se rompa con datos inesperados, leer y escribir ficheros CSV, y usar `math` y `random`.

**En el libro.** [Excepciones](13-excepciones.md) § 1–2 y [CSV, math y random](27-csv-math-random.md).

### Predice

```python
try:
    n = int("12a")
    print("convertido")
except ValueError:
    print("no es un número")
finally:
    print("fin")
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 13. |
| 0:15 | **Situación**: un cajero que, si la tarjeta falla, avisa y devuelve la tarjeta en vez de apagarse. |
| 0:25 | **Predice** y visualizador. |
| 0:40 | Construcción: `try`/`except`, el bucle que pide hasta que el dato es válido, leer y escribir un CSV, `math` y `random`. |
| 1:10 | Ejercicios de los dos capítulos. |
| 1:30 | **Taller del proyecto**: el profesor pasa por las parejas. |
| 1:50 | Hito 3. |

**Hito 3 del proyecto.** El gestor completo: lee el CSV, tiene el menú, no se rompe con datos malos y guarda los cambios.

---

## Sesión 15 · Proyecto 1 y simulacro PCEP

**Objetivo.** Presentar el proyecto y comprobar en condiciones de examen cuánto del PCEP está ya dominado.

**En el libro.** [Proyecto 1](curso-proyecto-1.md) y [Simulacro PCEP](simulacro-pcep.md).

| Tiempo | Qué se hace |
|---|---|
| 0:00 | **Exposiciones** del proyecto 1: 5 minutos por alumno o pareja, con demostración en directo y una pregunta del público. |
| 1:00 | **Simulacro PCEP**: 35 preguntas en 50 minutos, en silencio, con el temporizador del libro. |
| 1:50 | Cada alumno apunta su nota por secciones: es el diagnóstico con el que empieza el módulo 2. |

:::{tip} Si el grupo es grande
Con más de diez exposiciones no caben en una hora. Se pueden repartir entre las sesiones 15 y 16, y hacer el simulacro en casa con el compromiso de no pausar el temporizador.
:::

---

(soluciones-modulo-1)=
## Soluciones

### Lo que sale en los «Predice»

| Sesión | Salida | La clave |
|---|---|---|
| 1 | `Hola` · `5` · `2 + 3` | Entre comillas es texto: Python no lo calcula. |
| 2 | 9 | El papel siempre guarda el mayor visto hasta ahora. |
| 3 | `27 13` | Tres vueltas: (b, a) pasa por (1, 3), (4, 9) y (13, 27). |
| 4 | `7 5` | `y = x` copia el valor 5; cambiar `x` después no toca `y`. |
| 5 | `3.5 3 1` · `512` · `34 7` · `-4` | `**` se agrupa por la derecha (2⁹); `//` redondea hacia abajo, también con negativos. |
| 6 | `Aprobado` · `Notable` | Son dos `if` independientes. Con 9,5 tampoco sale Sobresaliente: el `elif` nunca se alcanza porque 9,5 ≥ 7 ya es cierto. |
| 7 | `1 4 7` · `3` | `range(1, 10, 3)` se para antes de 10. |
| 8 | `1 3 5` | Los pares se saltan; al llegar a 7 se sale. |
| 9 | `[3, 1, 2, 4] [3, 1, 2, 4] [99, 1, 2, 4]` | `b` es la misma lista que `a`; `c` es una copia. |
| 10 | `(1, 2, 3) 3 True` · `[[0, 0, 0], [0, 0, 5]]` | `(3,)` es una tupla de un elemento; el conjunto no repite. |
| 11 | `P r ogr ramargorP` · `3` · `3.14\|   42\|` | `s[2:5]` va del índice 2 al 4. |
| 12 | `no hay 3` · `leche` | `get` no falla si la clave no existe. |
| 13 | `10 5` · `Hola Ana` · `Buenas Luis` | La `x` de la función es otra variable: `n` sigue valiendo 5. |
| 14 | `no es un número` · `fin` | `finally` se ejecuta siempre. |

### Tarea 1

- **Entradas**: `precio`, un número real mayor o igual que 0, en euros; `descuento`, un número real entre 0 y 100, en porcentaje.
- **Salida**: el precio final en euros: `precio − precio · descuento / 100`.
- **Precondiciones**: `precio ≥ 0` y `0 ≤ descuento ≤ 100`.
- **Ejemplos**: (100, 20) → 80; (59,90, 15) → 50,915; (10, 0) → 10, caso límite sin descuento. Otro límite: (35, 100) → 0.
- **La grieta**: 50,915 € no se puede pagar. La especificación debe decir cómo se redondea a céntimos, y no da igual: `round(50.915, 2)` en Python da 50,91 porque 50,915 no se guarda exacto en binario.

### Tarea 2

> 1. Apunta el primer número de la lista.
> 2. Para cada número siguiente: si es **menor** que el apuntado, apunta este en su lugar.
> 3. Di el número apuntado.

Con 7, 3, 9, 3, 5 lo apuntado pasa por 7, 3, 3, 3, 3: sale 3. El segundo 3 no cambia nada porque no es *menor*. Con un solo número sale ese número; con la lista vacía el paso 1 no se puede hacer, así que la precondición es que la lista tenga al menos un número.

### Tarea 3

| x | y | ¿x > y? |
|---|---|---|
| 10 | 3 | sí |
| 7 | 4 | sí |
| 3 | 5 | no |

Imprime `3 5`.

### Tarea 4

```python
nombre = input("¿Cómo te llamas? ")
nacimiento = int(input("¿En qué año naciste? "))
actual = int(input("¿En qué año estamos? "))
edad = actual - nacimiento

print("---", nombre, "---")
print("Este año cumples", edad, "años", sep=" · ")
print("¡Encantado de conocerte!")
```

Con Ada, 2008 y 2026, la segunda línea es `Este año cumples · 18 · años`. El `sep` se pone entre cada par de argumentos: es una forma de ver cómo trabaja.

### Tarea 5

```python
total = int(input("Segundos: "))
h = total // 3600
resto = total % 3600
m = resto // 60
s = resto % 60
print(f"{h} h {m} min {s} s")
```

4000 → `1 h 6 min 40 s`; 3600 → `1 h 0 min 0 s`; 59 → `0 h 0 min 59 s`.

### Tarea 6

```python
nota = float(input("Nota: "))
if nota < 0 or nota > 10:
    print("Nota no válida")
elif nota < 5:
    print("Suspenso")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
```

Como cada `elif` solo se mira si los anteriores fallaron, basta con comprobar el límite superior. 4,99 → Suspenso; 5 → Suficiente; 9 → Sobresaliente; 10 → Sobresaliente; 10,5 → Nota no válida.

### Tarea 7

```python
n = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
```

Con `while` hay que crear el contador, comprobarlo y aumentarlo a mano; el `for` lo hace solo. Para la ampliación se añade `if n * i % 2 == 0:` antes del `print`.

### Tarea 8

```python
suma = 0
cuantas = 0
while True:
    nota = float(input("Nota (-1 para terminar): "))
    if nota == -1:
        break
    if nota < 0 or nota > 10:
        print("Fuera de rango, la ignoro")
        continue
    suma += nota
    cuantas += 1

if cuantas == 0:
    print("No hay notas")
else:
    print(f"Media de {cuantas} notas: {suma / cuantas:.2f}")
```

Con 7, 12, 5, 8, −1: `Media de 3 notas: 6.67`.

### Tarea 9

```python
datos = [4, 8, 15, 16, 23, 42]
maximo = datos[0]
minimo = datos[0]
suma = 0
for x in datos:
    if x > maximo:
        maximo = x
    if x < minimo:
        minimo = x
    suma += x
media = suma / len(datos)

encima = 0
for x in datos:
    if x > media:
        encima += 1

print(maximo, minimo, suma, media, encima)        # 42 4 108 18.0 2
print(max(datos), min(datos), sum(datos))         # 42 4 108
```

### Tarea 10

```python
sala = [[0] * 8 for _ in range(5)]
for a in range(8):
    sala[0][a] = 1
sala[1][0] = 1
sala[1][1] = 1

def primera_libre(sala):
    for f in range(len(sala)):
        for a in range(len(sala[f])):
            if sala[f][a] == 0:
                return (f, a)
    return None

def libres(sala):
    n = 0
    for fila in sala:
        for asiento in fila:
            if asiento == 0:
                n += 1
    return n

print(primera_libre(sala), libres(sala))   # (1, 2) 30
fila, asiento = primera_libre(sala)
sala[fila][asiento] = 1
for f in sala:
    linea = ""
    for a in f:
        if a == 1:
            linea += "X "
        else:
            linea += "· "
    print(linea)
```

Después de reservar, el primer libre es `(1, 3)` y quedan 29. El `return` dentro de los dos bucles sale de los dos a la vez: es la forma limpia de parar un bucle anidado.

### Tarea 11

```python
clave = input("Contraseña: ")
fallos = []
if len(clave) < 8:
    fallos.append("tiene menos de 8 caracteres")

mayus = minus = cifra = False
for c in clave:
    if c.isupper():
        mayus = True
    elif c.islower():
        minus = True
    elif c.isdigit():
        cifra = True

if not mayus:
    fallos.append("no tiene mayúsculas")
if not minus:
    fallos.append("no tiene minúsculas")
if not cifra:
    fallos.append("no tiene cifras")
if " " in clave:
    fallos.append("tiene espacios")

if fallos:
    for f in fallos:
        print("-", f)
else:
    print("válida")
```

`abc` falla por longitud, mayúsculas y cifras; `Python2026` es válida; `python 2026A` solo tiene espacios.

### Tarea 12

```python
texto = "El perro come. ¿El gato come? El perro duerme, y el gato también come."
limpio = texto.lower()
for signo in ".,;:!?¿¡":
    limpio = limpio.replace(signo, "")

frecuencia = {}
for palabra in limpio.split():
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

mas = None
for palabra, veces in frecuencia.items():
    if mas is None or veces > frecuencia[mas]:
        mas = palabra

print(frecuencia)
print(mas, frecuencia[mas])     # el 4
```

El diccionario queda `{'el': 4, 'perro': 2, 'come': 3, 'gato': 2, 'duerme': 1, 'y': 1, 'también': 1}`. Sin el `lower`, «El» y «el» contarían como palabras distintas.

### Tarea 13

```python
def segundos_a_hms(total):
    return total // 3600, total % 3600 // 60, total % 60

def calificacion(nota):
    if nota < 0 or nota > 10:
        return "Nota no válida"
    elif nota < 5:
        return "Suspenso"
    elif nota < 6:
        return "Suficiente"
    elif nota < 7:
        return "Bien"
    elif nota < 9:
        return "Notable"
    return "Sobresaliente"

def media_de(*numeros):
    if len(numeros) == 0:
        return None
    return sum(numeros) / len(numeros)

print(segundos_a_hms(4000))          # (1, 6, 40)
print(calificacion(6.5))             # Bien
print(media_de(7, 5, 8), media_de()) # 6.666666666666667 None
```

Dentro de `calificacion` el último `else` sobra: si se llega a esa línea es porque ningún `return` anterior se ejecutó.
