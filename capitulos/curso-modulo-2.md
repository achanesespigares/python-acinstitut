---
title: "Módulo 2 · Del PCEP al PCAP"
subtitle: Sesiones 16 a 30, con su guion, su programa para predecir y su tarea
description: "Módulo 2 · Del PCEP al PCAP: sesiones 16 a 30, con su guion, su programa para predecir y su tarea. Python paso a paso, con visualizadores y diagrama de flujo."
---

## Cómo leer esta página

Las sesiones tienen la misma forma que en el [módulo 1](curso-modulo-1.md): **objetivo**, programa para **predecir**, guion de la sesión **en clase** y **tarea** semiguiada. Las respuestas y las soluciones están al final, en [Soluciones](#soluciones-modulo-2).

En este módulo el código crece. Desde la sesión 16, cada alumno guarda sus programas en módulos propios dentro de Colab (con `%%writefile`), y desde la sesión 26 trabaja en el proyecto 2 con un repositorio.

---

## Sesión 16 · Módulos y paquetes

**Objetivo.** Usar módulos de la biblioteca estándar con cualquier forma de `import`, y escribir un módulo propio que se pueda importar y también ejecutar.

**En el libro.** [Módulos](12-modulos.md).

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-16.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-16.pdf)

### Predice

```python
import math
from random import randint as r
print(math.floor(-2.5), math.ceil(-2.5), round(2.5))
print(type(r(1, 6)))
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Comentario del simulacro PCEP de la sesión 15: qué secciones fallaron más. Si quedan exposiciones del proyecto 1, se hacen ahora. |
| 0:20 | **Situación**: una caja de herramientas; no se saca todo para apretar un tornillo. |
| 0:30 | **Predice**. `round(2.5)` da 2: redondeo al par, una pregunta clásica de examen. |
| 0:45 | Construcción: formas de `import`, `dir`, `__name__`, `sys.path`, paquetes y subpaquetes, `pip` y PyPI, y qué pasa cuando importar falla. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen PCAP y tarea 16. |

### Tarea 16 · Tu primer módulo

1. En una celda de Colab escribe `%%writefile geometria.py` en la primera línea y debajo el módulo.
2. Define una constante `PI` tomada de `math` y las funciones `area_circulo(r)` y `area_rectangulo(base, altura)`.
3. Añade un bloque `if __name__ == "__main__":` con dos pruebas que impriman resultados.
4. En otra celda, haz `import geometria` y usa las dos funciones. ¿Se ejecutan las pruebas del bloque? ¿Por qué?
5. Ejecuta el módulo como programa con `!python geometria.py`. ¿Y ahora?

**Comprobación.** `geometria.area_rectangulo(3, 4)` devuelve 12, y al importarlo no se imprime nada.

---

## Sesión 17 · Excepciones a fondo

**Objetivo.** Lanzar excepciones, crear las propias y controlar exactamente qué parte de un `try` se ejecuta.

**En el libro.** [Excepciones](13-excepciones.md) § 3–6.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-17.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-17.pdf)

### Predice

```python
def f(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return "div0"
    finally:
        print("f", x)

print(f(2))
print(f(0))
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 16. |
| 0:15 | **Situación**: un parte de incidencias; cada tipo de avería va a un técnico distinto. |
| 0:25 | **Predice**. El `finally` imprime antes que el `print` de fuera, aunque haya un `return`. |
| 0:45 | Construcción: `raise`, `else`, `finally`, orden de los `except`, varios tipos en un `except`, jerarquía hasta `BaseException`, relanzar con `raise`, clases propias. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen y tarea 17. |

### Tarea 17 · Un entero en su rango

1. Crea la clase `FueraDeRango`, hija de `ValueError`, cuyo constructor reciba el valor, el mínimo y el máximo, y prepare un mensaje claro.
2. Escribe `a_entero(texto, minimo, maximo)`: convierte con `int` y, si el número no está en el rango, lanza `FueraDeRango`.
3. Escribe `pedir_entero(pregunta, minimo, maximo)`, que pregunta con `input` hasta recibir un dato válido. Captura primero `FueraDeRango` y después `ValueError`, con un aviso distinto para cada una.
4. Usa la rama `else` del `try` para devolver el número.
5. ¿Qué pasaría si capturaras `ValueError` antes que `FueraDeRango`?

**Comprobación.** Si se escribe `doce`, luego `150` y luego `15`, con el rango 0–120, salen dos avisos distintos y se devuelve 15.

---

## Sesión 18 · Clases y objetos

**Objetivo.** Definir una clase con su constructor y sus métodos, crear objetos y distinguir dos objetos iguales de dos nombres para el mismo objeto.

**En el libro.** [Clases y objetos](14-clases.md) § 1–2.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-18.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-18.pdf)

### Predice

```python
class Contador:
    def __init__(self):
        self.n = 0

    def suma(self):
        self.n += 1
        return self

a = Contador()
b = a
a.suma().suma()
b.suma()
print(a.n, b.n, a is b)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 17. |
| 0:15 | **Situación**: el plano de una casa y las casas construidas con él. Pintar una no pinta las demás. |
| 0:25 | **Predice** y visualizador: solo hay un objeto con dos nombres. |
| 0:45 | Construcción: `class`, `__init__`, `self`, atributos, métodos, identidad. |
| 1:20 | Ejercicios del capítulo (los de las secciones 1 y 2). |
| 1:45 | Tarea 18. |

### Tarea 18 · Un termómetro

1. Crea la clase `Termometro` con un constructor que reciba los grados Celsius, 0 por defecto.
2. Guarda también la temperatura máxima registrada, que al principio es la inicial.
3. Añade `a_fahrenheit()`, que devuelve la temperatura en °F (por 9/5, más 32).
4. Añade `cambiar(grados)`, que sube o baja la temperatura y actualiza la máxima si hace falta.
5. Crea un termómetro a 20 °C, súbelo 5 y bájalo 8. Imprime la temperatura, la máxima y los °F.

**Comprobación.** Queda a 17 °C, con máxima de 25 °C, que son 62,6 °F.

---

## Sesión 19 · Atributos de clase, `__str__` y herencia

**Objetivo.** Compartir datos entre todos los objetos de una clase, darles una representación legible y reutilizar una clase con la herencia.

**En el libro.** [Clases y objetos](14-clases.md) § 3–4.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-19.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-19.pdf)

### Predice

```python
class Animal:
    patas = 4

    def habla(self):
        return "..."

    def __str__(self):
        return f"{type(self).__name__} que dice {self.habla()}"

class Perro(Animal):
    def habla(self):
        return "guau"

class Gallina(Animal):
    patas = 2

for a in [Perro(), Gallina()]:
    print(a, a.patas)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 18. |
| 0:15 | **Situación**: un formulario de matrícula general y el de una beca, que es el mismo con dos casillas más. |
| 0:25 | **Predice**. El `__str__` de `Animal` llama al `habla` de cada hijo: primer contacto con el polimorfismo. |
| 0:45 | Construcción: atributos de clase, `__str__`, herencia, `super()`. |
| 1:20 | Ejercicios del capítulo (secciones 3 y 4). |
| 1:45 | Preguntas tipo examen y tarea 19. |

### Tarea 19 · Figuras

1. Crea la clase `Figura` con un método `area()` que lance `NotImplementedError` y un `__str__` que escriba el nombre de la clase y el área con dos decimales.
2. Crea `Rectangulo(base, altura)` y `Circulo(radio)`, hijas de `Figura`, cada una con su `area()` y su `perimetro()`.
3. Haz una lista con dos rectángulos y dos círculos, ordénala por área con `sort` y `key`, e imprime cada figura.
4. ¿Por qué no hace falta escribir `__str__` en las hijas?

**Comprobación.** La figura más pequeña de la lista `[Rectangulo(3, 4), Circulo(1), Rectangulo(1, 1), Circulo(2)]` es el rectángulo de 1 × 1.

---

## Sesión 20 · Nombres ocultos y polimorfismo

**Objetivo.** Proteger los datos internos de un objeto y escribir código que funcione con cualquier clase que tenga los métodos adecuados.

**En el libro.** [Clases a fondo](18-clases-a-fondo.md) § 1–3.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-20.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-20.pdf)

### Predice

```python
class Caja:
    def __init__(self):
        self.__secreto = 42
        self._interno = 1

c = Caja()
print(c._interno)
print(hasattr(c, "__secreto"), hasattr(c, "_Caja__secreto"))
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 19. |
| 0:15 | **Situación**: la trastienda de una tienda; los clientes pueden entrar, pero hay un cartel de «solo personal». |
| 0:25 | **Predice** y visualizador: el atributo existe con otro nombre. |
| 0:45 | Construcción: atributos de clase e instancia, `__dict__`, desfiguración de nombres, sobrescritura, polimorfismo. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen y tarea 20. |

### Tarea 20 · Productos con precio protegido

1. Crea la clase `Producto` con dos atributos de clase: `creados = 0` e `IVA = 0.21`.
2. En el constructor guarda el nombre y llama a `set_precio(precio)`. Solo si el precio es válido, suma 1 a `Producto.creados`.
3. `set_precio` guarda el precio en `self.__precio` y lanza `ValueError` si no es positivo.
4. Añade `get_precio()` y `precio_con_iva()`, redondeado a céntimos.
5. Crea dos productos, intenta crear uno con precio 0 y comprueba cuántos se han creado.

**Comprobación.** Una libreta de 2 € cuesta 2,42 € con IVA, y el producto con precio 0 no cuenta.

---

## Sesión 21 · Herencia múltiple, MRO e introspección

**Objetivo.** Saber qué método se ejecuta cuando hay varias clases madre, y preguntar a un objeto por sus atributos y su clase.

**En el libro.** [Clases a fondo](18-clases-a-fondo.md) § 4–8.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-21.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-21.pdf)

### Predice

```python
class A:
    def quien(self):
        return "A"

class B(A):
    def quien(self):
        return "B"

class C(A):
    def quien(self):
        return "C"

class D(B, C):
    pass

print(D().quien())
print([k.__name__ for k in D.__mro__])
print(isinstance(D(), C), issubclass(C, B))
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 20. |
| 0:15 | **Situación**: preguntar una duda: primero al compañero de mesa, luego al profesor de la materia, luego al tutor. Siempre en el mismo orden. |
| 0:25 | **Predice**. El MRO se dibuja como un rombo. |
| 0:45 | Construcción: herencia múltiple, `__mro__`, `isinstance`, `issubclass`, `hasattr`, `getattr`, `is` frente a `==`, `__repr__`. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen y tarea 21. |

### Tarea 21 · El rombo y las órdenes por nombre

1. Crea cuatro clases en rombo: `Base`, `Izq(Base)`, `Der(Base)` y `Abajo(Izq, Der)`. Cada constructor imprime el nombre de su clase y llama a `super().__init__()`.
2. **Predice** en qué orden salen los cuatro nombres al crear un `Abajo()`, y después compruébalo con `Abajo.__mro__`.
3. Crea una clase `Robot` con los métodos `saluda()` y `avanza()`.
4. Con una lista de órdenes en texto, `["saluda", "baila", "avanza"]`, ejecuta cada una con `getattr` si el robot la tiene (`hasattr`), y si no, escribe `no sé baila`.

**Comprobación.** `Base` se imprime una sola vez, la última.

---

## Sesión 22 · Comprensiones y el `else` de los bucles

**Objetivo.** Construir listas, diccionarios y conjuntos en una línea, y saber cuándo un bucle terminó sin `break`.

**En el libro.** [Comprensiones](15-comprensiones.md) § 1–5.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-22.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-22.pdf)

### Predice

```python
print([x * x for x in range(6) if x % 2])
print({c: len(c) for c in ["sol", "luna"]})
for n in [3, 5, 7]:
    if n % 2 == 0:
        break
else:
    print("ningún par")
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 21. |
| 0:15 | **Situación**: «de los de la lista, los mayores de edad, en mayúsculas»: una frase que hace tres cosas. |
| 0:25 | **Predice** y visualizador. |
| 0:45 | Construcción: comprensiones con filtro, expresión condicional, de diccionario y de conjunto, anidadas, `for … else`. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen y tarea 22. |

### Tarea 22 · Del bucle a la comprensión

Con `numeros = [3, -1, 4, -1, 5, 9, -2, 6]` y `palabras = ["sol", "mar", "sol", "luz"]`, escribe cada resultado **primero con un bucle y después con una comprensión**:

1. Los números positivos.
2. Los cuadrados de todos los números.
3. La lista con `"par"` o `"impar"` para cada número (expresión condicional).
4. Un diccionario de cada palabra con su longitud.
5. El conjunto de las iniciales de las palabras.
6. Ampliación: la traspuesta de `[[1, 2, 3], [4, 5, 6]]` con una comprensión anidada.

**Comprobación.** El conjunto de iniciales tiene 3 elementos y la traspuesta es `[[1, 4], [2, 5], [3, 6]]`.

---

## Sesión 23 · `match` y lambdas

**Objetivo.** Elegir según la forma de un dato, y pasar funciones cortas como argumento para ordenar, transformar y filtrar.

**En el libro.** [Comprensiones](15-comprensiones.md) § 6 y [Funciones como valores](16-funciones-valores.md) § 1–2.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-23.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-23.pdf)

### Predice

```python
alumnos = [("Ana", 7), ("Luis", 9), ("Eva", 7)]
alumnos.sort(key=lambda a: (-a[1], a[0]))
print(alumnos)
print(list(map(lambda a: a[0][0], alumnos)))
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 22. |
| 0:15 | **Situación**: ordenar una clasificación por puntos y, si empatan, por orden alfabético. |
| 0:25 | **Predice**. El `-` delante de la nota invierte solo ese criterio. |
| 0:45 | Construcción: `match` con patrones de secuencia, `lambda`, `key`, `map`, `filter`. |
| 1:20 | Ejercicios de los dos capítulos. |
| 1:45 | Preguntas tipo examen y tarea 23. |

### Tarea 23 · Calculadora y clasificación

1. Escribe `calcula(linea)`: parte la línea con `split` y usa `match` sobre la lista de partes. Patrones: `[a, "+", b]`, `[a, "-", b]`, `[a, "*", b]`, `[a, "/", b]`, `["salir"]` y `_`.
2. Para la división, devuelve un aviso si el divisor es 0. Para `salir`, devuelve `None`. Para lo demás, `no entiendo`.
3. Con `notas = [("Eva", 7.5), ("Ana", 9), ("Luis", 7.5), ("Bea", 5)]`, ordena con `sorted` y una `lambda` de mayor a menor nota y, a igual nota, por nombre.
4. Con `filter` y una `lambda`, quédate con los que tienen 7 o más.

**Comprobación.** `calcula("10 / 4")` da 2,5 y el orden empieza por Ana, Eva, Luis.

---

## Sesión 24 · Cierres y generadores

**Objetivo.** Fabricar funciones que recuerdan un dato, y producir valores uno a uno sin guardarlos todos.

**En el libro.** [Funciones como valores](16-funciones-valores.md) § 3–4. Los generadores son ampliación en el PCAP: se ven si el grupo va a buen ritmo.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-24.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-24.pdf)

### Predice

```python
def multiplicador(k):
    def f(x):
        return k * x
    return f

doble = multiplicador(2)
triple = multiplicador(3)
print(doble(5), triple(doble(1)))

def cuenta(n):
    while n > 0:
        yield n
        n -= 1

print(list(cuenta(3)), sum(cuenta(4)))
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 23. |
| 0:15 | **Situación**: un sello de goma con la fecha ya puesta; cada sello recuerda su fecha. |
| 0:25 | **Predice** y visualizador: el marco de `multiplicador` sigue vivo después de terminar. |
| 0:45 | Construcción: funciones dentro de funciones, cierres, `yield`, `next`. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen y tarea 24. |

### Tarea 24 · Descuentos y Fibonacci

1. Escribe `descuento(pct)`, que devuelve una función `aplica(precio)` con el precio rebajado y redondeado a céntimos.
2. Crea `rebajas = descuento(20)` y `black_friday = descuento(35)` y aplícalas a 50 €.
3. Escribe el generador `fibonacci(limite)`, que produce los términos de la sucesión (0, 1, 1, 2, 3…) mientras no pasen del límite.
4. Convierte en lista los de hasta 100, y saca los tres primeros de otro generador con `next`.

**Comprobación.** Las rebajas dejan 50 € en 40 €; el último término hasta 100 es 89.

---

## Sesión 25 · Ficheros, bytes y rutas

**Objetivo.** Leer y escribir ficheros de texto y binarios con `with`, y moverse por carpetas con `pathlib`.

**En el libro.** [Ficheros y flujos](17-ficheros.md).

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-25.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-25.pdf)

### Predice

```python
with open("prueba.txt", "w") as f:
    f.write("uno\ndos\n")
with open("prueba.txt", "a") as f:
    print("tres", file=f)
with open("prueba.txt") as f:
    lineas = f.readlines()
print(len(lineas), lineas[-1].strip())
b = bytearray(b"abc")
b[0] = 65
print(b)
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 24. |
| 0:15 | **Situación**: un cuaderno: se puede empezar de cero, añadir al final o solo leer. |
| 0:25 | **Predice** y visualizador: se ve el disco cambiar. |
| 0:45 | Construcción: modos `r`, `w`, `a`, `b`, `with`, `read`, `readline`, `readlines`, `bytes`, `bytearray`, `pathlib`, `errno`. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen y tarea 25. |

### Tarea 25 · Un diario y una copia

1. Con `pathlib`, crea la carpeta `diario` si no existe.
2. Escribe `escribe(fecha, texto)`, que añade el texto al fichero `diario/<fecha>.txt`.
3. Escribe `entradas()`, que devuelve las fechas con entrada, ordenadas (usa `glob` y `stem`).
4. Escribe `lee(fecha)`, que devuelve el texto o `None` si ese día no hay fichero.
5. Escribe `copia(origen, destino)`, que copia un fichero binario en bloques de 1024 bytes y devuelve cuántos bytes copió. Comprueba que la copia es idéntica.

**Comprobación.** Dos llamadas a `escribe` con la misma fecha dejan dos líneas en el mismo fichero.

---

## Sesión 26 · Cadenas a fondo

**Objetivo.** Trabajar con códigos de caracteres, comparar cadenas y usar los métodos de comprobación y troceado.

**En el libro.** [Cadenas a fondo](19-cadenas-a-fondo.md). Al final de la sesión se presenta el [Proyecto 2](curso-proyecto-2.md).

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-26.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-26.pdf) · [Cuaderno del proyecto](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-2.ipynb)

### Predice

```python
print(ord("A"), chr(98), "abc" < "abd", "Zeta" < "alfa")
print("a,b,,c".split(","), "-".join("xyz"))
print("3".isdigit(), "3.5".isdigit(), " hola ".strip().title())
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 25. |
| 0:15 | **Situación**: un diccionario de papel: «Zeta» va antes que «alfa» si las mayúsculas cuentan primero. |
| 0:25 | **Predice**. |
| 0:40 | Construcción: Unicode, `ord`, `chr`, comparación, métodos `is…`, `split`, `join`, `find`, `index`. |
| 1:10 | Ejercicios del capítulo. |
| 1:30 | **Presentación del proyecto 2**: enunciado, hitos y rúbrica. |
| 1:50 | Tarea 26 y hito 1. |

### Tarea 26 · El cifrado César

1. Escribe `cesar(texto, k)`, que desplaza cada letra `k` posiciones en el alfabeto inglés, dando la vuelta al llegar a la z.
2. Las mayúsculas siguen siendo mayúsculas y las minúsculas, minúsculas. Lo que no es letra se queda igual.
3. Usa `ord`, `chr` y el resto `%` 26.
4. Comprueba que `cesar(cesar(t, k), -k)` devuelve `t`.

**Comprobación.** `cesar("Hola, Mundo!", 3)` es `Krod, Pxqgr!`.

**Hito 1 del proyecto.** El diseño de las clases de la biblioteca (ver [Proyecto 2](curso-proyecto-2.md)).

---

## Sesión 27 · Probar y depurar

**Objetivo.** Leer un traceback de abajo arriba, escribir pruebas unitarias y buscar el porqué de un error con método.

**En el libro.** [Probar y depurar](20-probar-y-depurar.md) § 1–4.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-27.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-27.pdf) · [Cuaderno del proyecto](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-2.ipynb)

### Predice

¿Qué sale, y en qué línea dirá Python que está el error?

```python
def media(lista):
    return sum(lista) / len(lista)

def informe(datos):
    return f"Media: {media(datos):.1f}"

print(informe([4, 6]))
print(informe([]))
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 26. |
| 0:15 | **Situación**: una avería en cadena: el coche no arranca porque la batería no carga porque la correa está rota. |
| 0:25 | **Predice** y visualizador: el traceback enseña la pila de llamadas al revés. |
| 0:45 | Construcción: `assert`, tracebacks, `unittest`, depuración por hipótesis. |
| 1:20 | Ejercicios del capítulo. |
| 1:45 | Preguntas tipo examen, tarea 27 y hito 2. |

### Tarea 27 · Pruebas para la calificación

1. Toma `calificacion(nota)` de la tarea 13 y cámbiala para que **lance** `ValueError` si la nota no está entre 0 y 10, en vez de devolver un texto.
2. Escribe una clase `PruebaCalificacion(unittest.TestCase)` con tres pruebas: los bordes (5, 9, 10), justo por debajo (4,99, 8,99) y fuera de rango, con `assertRaises`.
3. En Colab, ejecútalas con `unittest.main(argv=["ignorado"], exit=False)`.
4. Rompe a propósito la función (cambia un `<` por `<=`) y mira qué prueba falla.

**Comprobación.** Las tres pruebas pasan con la función correcta; con `nota <= 5` falla la de los bordes.

**Hito 2 del proyecto.** Clases, excepciones y pruebas del proyecto.

---

## Sesión 28 · Trabajar en equipo y con IA

**Objetivo.** Usar ramas, commits y revisiones, y validar código generado por una IA antes de darlo por bueno.

**En el libro.** [Probar y depurar](20-probar-y-depurar.md) § 5–6.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-28.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-28.pdf) · [Cuaderno del proyecto](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-2.ipynb)

### Predice

Una IA ha propuesto esta función. ¿Qué devuelven las tres llamadas?

```python
def es_primo(n):
    for d in range(2, n):
        if n % d == 0:
            return False
        return True

print(es_primo(9), es_primo(7), es_primo(2))
```

### En clase

| Tiempo | Qué se hace |
|---|---|
| 0:00 | Corrección de la tarea 27. |
| 0:15 | **Situación**: escribir un trabajo en grupo con un único documento: cada cual en su copia, y alguien revisa antes de juntar. |
| 0:25 | **Predice**. La sangría del `return True` lo cambia todo; y con 2 no se entra en el bucle. |
| 0:40 | Construcción: repositorio, rama, commit, pull request, revisión; el ciclo pedir, leer, probar y corregir con la IA. |
| 1:10 | Taller del proyecto: cada equipo abre su primera rama y su primera revisión. |
| 1:45 | Tarea 28 y hito 3. |

### Tarea 28 · Validar el código de la IA

1. Escribe pruebas para `es_primo` con estos casos: 0, 1, 2, 3, 9, 25 y 97. Usa `self.subTest(n=n)` dentro de un bucle para ver todos los fallos a la vez.
2. Ejecuta las pruebas sobre la versión de la IA y apunta qué casos fallan y por qué.
3. Corrige la función. Ampliación: que solo pruebe divisores hasta la raíz cuadrada de `n`.
4. Escribe en tres líneas cómo lo harías en un equipo: en qué rama, qué diría el commit y qué pediría la revisión.

**Comprobación.** La versión de la IA falla en 5 de los 7 casos.

**Hito 3 del proyecto.** Ficheros, flujo de git y uso de la IA documentado.

---

## Sesión 29 · Taller del proyecto y simulacro PCAP

**Objetivo.** Dejar el proyecto listo para exponer y comprobar en condiciones de examen el nivel PCAP.

**En el libro.** [Proyecto 2](curso-proyecto-2.md) y [Simulacro PCAP](simulacro-pcap.md).

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-29.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-29.pdf) · [Cuaderno del proyecto](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-2.ipynb)

| Tiempo | Qué se hace |
|---|---|
| 0:00 | **Simulacro PCAP**: 42 preguntas en 65 minutos, con el temporizador del libro. |
| 1:10 | Revisión del simulacro: cada alumno apunta las tres preguntas que más le enseñaron. |
| 1:25 | **Taller del proyecto**: últimas revisiones, pruebas en verde y ensayo de la exposición. |
| 1:55 | Hito 4: el proyecto, entregado. |

---

## Sesión 30 · Proyecto 2: exposiciones

**Objetivo.** Explicar a otros un programa propio, su diseño y sus decisiones.

**Material.** [Cuaderno en Colab](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-30.ipynb) · [Diapositivas en PDF](https://python.antonychanes.com/diapositivas/sesion-30.pdf) · [Cuaderno del proyecto](https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/proyecto-2.ipynb)

| Tiempo | Qué se hace |
|---|---|
| 0:00 | **Exposiciones**: 7 minutos por equipo. Demostración, una clase por dentro, una prueba que falló y cómo se arregló, y qué se pidió a la IA y qué se corrigió. |
| 1:30 | Preguntas cruzadas: cada equipo hace una pregunta a otro. |
| 1:45 | Cierre del curso: cómo presentarse al PCEP y al PCAP, y por dónde seguir. |

---

(soluciones-modulo-2)=
## Soluciones

### Lo que sale en los «Predice»

| Sesión | Salida | La clave |
|---|---|---|
| 16 | `-3 -2 2` · `<class 'int'>` | `floor` baja, `ceil` sube; `round` redondea al par cuando está a mitad. |
| 17 | `f 2` · `5.0` · `f 0` · `div0` | `finally` se ejecuta antes de que el valor devuelto llegue al `print`. |
| 18 | `3 3 True` | `a` y `b` son el mismo objeto; `suma` devuelve `self` y se puede encadenar. |
| 19 | `Perro que dice guau 4` · `Gallina que dice ... 2` | Cada objeto usa el `habla` y el `patas` más cercano en su clase. |
| 20 | `1` · `False True` | `__secreto` se guarda como `_Caja__secreto`. |
| 21 | `B` · `['D', 'B', 'C', 'A', 'object']` · `True False` | El MRO recorre de izquierda a derecha y deja `A` para el final. |
| 22 | `[1, 9, 25]` · `{'sol': 3, 'luna': 4}` · `ningún par` | El `else` del `for` se ejecuta porque no hubo `break`. |
| 23 | `[('Luis', 9), ('Ana', 7), ('Eva', 7)]` · `['L', 'A', 'E']` | Primero por nota descendente; a igual nota, por nombre. |
| 24 | `10 6` · `[3, 2, 1] 10` | `triple(doble(1))` es 3 · 2; 4 + 3 + 2 + 1 = 10. |
| 25 | `3 tres` · `bytearray(b'Abc')` | 65 es el código de `A`. |
| 26 | `65 b True True` · `['a', 'b', '', 'c'] x-y-z` · `True False Hola` | Las mayúsculas tienen códigos menores que las minúsculas. |
| 27 | `Media: 5.0` y después `ZeroDivisionError` | El traceback acaba en la línea de `media`, la división; la causa está en quien la llamó con una lista vacía. |
| 28 | `True True None` | `return True` está dentro del bucle: solo se mira el divisor 2. Con 2 el bucle no da ninguna vuelta y la función devuelve `None`. |

### Tarea 16

```python
%%writefile geometria.py
"""Áreas de figuras sencillas."""
import math

PI = math.pi


def area_circulo(r):
    return PI * r ** 2


def area_rectangulo(base, altura):
    return base * altura


if __name__ == "__main__":
    print(round(area_circulo(1), 4))     # 3.1416
    print(area_rectangulo(3, 4))         # 12
```

```python
import geometria
print(round(geometria.area_circulo(2), 2), geometria.area_rectangulo(3, 4))   # 12.57 12
```

Al importarlo, `__name__` vale `"geometria"` y el bloque de pruebas no se ejecuta. Con `!python geometria.py` vale `"__main__"` y sí. Si se cambia el módulo después de importarlo, Colab no lo vuelve a leer: hay que reiniciar el entorno o usar `importlib.reload(geometria)`.

### Tarea 17

```python
class FueraDeRango(ValueError):
    def __init__(self, valor, minimo, maximo):
        super().__init__(f"{valor} no está entre {minimo} y {maximo}")
        self.valor = valor


def a_entero(texto, minimo, maximo):
    n = int(texto)
    if not minimo <= n <= maximo:
        raise FueraDeRango(n, minimo, maximo)
    return n


def pedir_entero(pregunta, minimo, maximo):
    while True:
        texto = input(pregunta)
        try:
            n = a_entero(texto, minimo, maximo)
        except FueraDeRango as e:
            print("Fuera de rango:", e)
        except ValueError:
            print("Eso no es un número entero")
        else:
            return n
```

Con `doce`, `150` y `15`: «Eso no es un número entero», «Fuera de rango: 150 no está entre 0 y 120», y devuelve 15. Como `FueraDeRango` es hija de `ValueError`, si `except ValueError` fuera primero capturaría las dos y el aviso de rango nunca saldría.

### Tarea 18

```python
class Termometro:
    def __init__(self, celsius=0):
        self.celsius = celsius
        self.maxima = celsius

    def a_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def cambiar(self, grados):
        self.celsius += grados
        if self.celsius > self.maxima:
            self.maxima = self.celsius


t = Termometro(20)
t.cambiar(5)
t.cambiar(-8)
print(t.celsius, t.maxima, t.a_fahrenheit())    # 17 25 62.6
```

### Tarea 19

```python
import math


class Figura:
    def area(self):
        raise NotImplementedError

    def __str__(self):
        return f"{type(self).__name__} de área {self.area():.2f}"


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


figuras = [Rectangulo(3, 4), Circulo(1), Rectangulo(1, 1), Circulo(2)]
figuras.sort(key=lambda f: f.area())
for f in figuras:
    print(f)
```

Sale, en orden: Rectangulo de área 1.00, Circulo de área 3.14, Rectangulo de área 12.00 y Circulo de área 12.57. Las hijas heredan el `__str__` de `Figura`, y ese `__str__` llama al `area()` de cada una: eso es el polimorfismo. (La `lambda` del `key` se ve a fondo en la sesión 23; aquí basta con leerla como «ordena por el área».)

### Tarea 20

```python
class Producto:
    creados = 0
    IVA = 0.21

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.set_precio(precio)
        Producto.creados += 1

    def set_precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser positivo")
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def precio_con_iva(self):
        return round(self.__precio * (1 + Producto.IVA), 2)


libreta = Producto("libreta", 2)
boli = Producto("bolígrafo", 1.20)
try:
    Producto("roto", 0)
except ValueError as e:
    print(e)

print(libreta.precio_con_iva(), Producto.creados)   # 2.42 2
```

El contador se suma **después** de `set_precio`: si el precio no es válido, la excepción sale antes y el producto roto no cuenta. Hay que escribir `Producto.creados += 1`; con `self.creados += 1` cada objeto crearía su propio atributo y el de la clase seguiría en 0.

### Tarea 21

```python
class Base:
    def __init__(self):
        print("Base")

class Izq(Base):
    def __init__(self):
        print("Izq")
        super().__init__()

class Der(Base):
    def __init__(self):
        print("Der")
        super().__init__()

class Abajo(Izq, Der):
    def __init__(self):
        print("Abajo")
        super().__init__()

Abajo()                                        # Abajo, Izq, Der, Base
print([c.__name__ for c in Abajo.__mro__])     # ['Abajo', 'Izq', 'Der', 'Base', 'object']


class Robot:
    def saluda(self):
        return "hola"

    def avanza(self):
        return "avanzo"

r = Robot()
for orden in ["saluda", "baila", "avanza"]:
    if hasattr(r, orden):
        print(getattr(r, orden)())
    else:
        print(f"no sé {orden}")
```

El `super()` de `Izq` no llama a `Base` sino al siguiente del MRO de `Abajo`, que es `Der`. Por eso `Base` sale una sola vez.

### Tarea 22

```python
numeros = [3, -1, 4, -1, 5, 9, -2, 6]
palabras = ["sol", "mar", "sol", "luz"]

positivos = [n for n in numeros if n > 0]                       # [3, 4, 5, 9, 6]
cuadrados = [n * n for n in numeros]                            # [9, 1, 16, 1, 25, 81, 4, 36]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
longitudes = {p: len(p) for p in palabras}                      # {'sol': 3, 'mar': 3, 'luz': 3}
iniciales = {p[0] for p in palabras}                            # {'s', 'm', 'l'}, en cualquier orden

m = [[1, 2, 3], [4, 5, 6]]
traspuesta = [[fila[j] for fila in m] for j in range(len(m[0]))]   # [[1, 4], [2, 5], [3, 6]]
```

Las versiones con bucle son las del módulo 1: una lista vacía y un `append` en cada vuelta. El diccionario tiene 3 claves aunque haya 4 palabras, porque «sol» se repite. El conjunto no tiene orden: puede imprimirse en cualquiera.

### Tarea 23

```python
def calcula(linea):
    match linea.split():
        case [a, "+", b]:
            return float(a) + float(b)
        case [a, "-", b]:
            return float(a) - float(b)
        case [a, "*", b]:
            return float(a) * float(b)
        case [a, "/", b]:
            if float(b) == 0:
                return "no se puede dividir entre 0"
            return float(a) / float(b)
        case ["salir"]:
            return None
        case _:
            return "no entiendo"


print(calcula("3 + 4"), calcula("10 / 4"), calcula("7 % 2"))   # 7.0 2.5 no entiendo

notas = [("Eva", 7.5), ("Ana", 9), ("Luis", 7.5), ("Bea", 5)]
print(sorted(notas, key=lambda a: (-a[1], a[0])))
# [('Ana', 9), ('Eva', 7.5), ('Luis', 7.5), ('Bea', 5)]
print(list(filter(lambda a: a[1] >= 7, notas)))
# [('Eva', 7.5), ('Ana', 9), ('Luis', 7.5)]
```

`filter` conserva el orden de la lista original, no el de la ordenada.

### Tarea 24

```python
def descuento(pct):
    def aplica(precio):
        return round(precio * (1 - pct / 100), 2)
    return aplica

rebajas = descuento(20)
black_friday = descuento(35)
print(rebajas(50), black_friday(50))     # 40.0 32.5


def fibonacci(limite):
    a, b = 0, 1
    while a <= limite:
        yield a
        a, b = b, a + b

print(list(fibonacci(100)))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
g = fibonacci(100)
print(next(g), next(g), next(g))   # 0 1 1
```

Cada función que devuelve `descuento` recuerda su propio `pct`: eso es el cierre.

### Tarea 25

```python
from pathlib import Path

carpeta = Path("diario")
carpeta.mkdir(exist_ok=True)


def escribe(fecha, texto):
    with open(carpeta / f"{fecha}.txt", "a", encoding="utf-8") as f:
        f.write(texto + "\n")


def entradas():
    return sorted(p.stem for p in carpeta.glob("*.txt"))


def lee(fecha):
    ruta = carpeta / f"{fecha}.txt"
    if not ruta.exists():
        return None
    return ruta.read_text(encoding="utf-8")


def copia(origen, destino, bloque=1024):
    copiados = 0
    with open(origen, "rb") as fo, open(destino, "wb") as fd:
        while True:
            trozo = fo.read(bloque)
            if not trozo:
                break
            fd.write(trozo)
            copiados += len(trozo)
    return copiados


escribe("2026-11-17", "Empiezo el diario.")
escribe("2026-11-18", "Hoy: ficheros y rutas.")
escribe("2026-11-18", "Y bytes.")
print(entradas())          # ['2026-11-17', '2026-11-18']
print(lee("2026-11-18"))   # dos líneas

Path("datos.bin").write_bytes(bytes(range(256)) * 40)
print(copia("datos.bin", "copia.bin"))                                       # 10240
print(Path("datos.bin").read_bytes() == Path("copia.bin").read_bytes())     # True
```

`read` devuelve `b""` al llegar al final: así sabe el bucle cuándo parar.

### Tarea 26

```python
def cesar(texto, k):
    resultado = ""
    for c in texto:
        if "a" <= c <= "z":
            resultado += chr((ord(c) - ord("a") + k) % 26 + ord("a"))
        elif "A" <= c <= "Z":
            resultado += chr((ord(c) - ord("A") + k) % 26 + ord("A"))
        else:
            resultado += c
    return resultado

secreto = cesar("Hola, Mundo!", 3)
print(secreto, cesar(secreto, -3), cesar("xyz", 3))   # Krod, Pxqgr! Hola, Mundo! abc
```

El `% 26` da la vuelta al alfabeto, también con `k` negativo: en Python `-1 % 26` es 25.

### Tarea 27

```python
import unittest


def calificacion(nota):
    if not 0 <= nota <= 10:
        raise ValueError(f"Nota fuera de rango: {nota}")
    if nota < 5:
        return "Suspenso"
    if nota < 6:
        return "Suficiente"
    if nota < 7:
        return "Bien"
    if nota < 9:
        return "Notable"
    return "Sobresaliente"


class PruebaCalificacion(unittest.TestCase):
    def test_bordes(self):
        self.assertEqual(calificacion(5), "Suficiente")
        self.assertEqual(calificacion(9), "Sobresaliente")
        self.assertEqual(calificacion(10), "Sobresaliente")

    def test_justo_por_debajo(self):
        self.assertEqual(calificacion(4.99), "Suspenso")
        self.assertEqual(calificacion(8.99), "Notable")

    def test_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            calificacion(10.5)
        with self.assertRaises(ValueError):
            calificacion(-1)


unittest.main(argv=["ignorado"], exit=False)   # Ran 3 tests ... OK
```

Con `if nota <= 5:` en la primera rama, un 5 daría Suspenso y fallaría `test_bordes`: las pruebas de bordes son las que cazan los `<` cambiados por `<=`.

### Tarea 28

```python
import unittest


def es_primo(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


class PruebaPrimo(unittest.TestCase):
    def test_casos(self):
        casos = [(0, False), (1, False), (2, True), (3, True), (9, False), (25, False), (97, True)]
        for n, esperado in casos:
            with self.subTest(n=n):
                self.assertIs(es_primo(n), esperado)


unittest.main(argv=["ignorado"], exit=False)
```

La versión de la IA falla con 0, 1 y 2 (devuelve `None`, no `False` ni `True`) y con 9 y 25 (dice que son primos porque solo prueba el 2). Acierta con 3 y 97 por casualidad.

En equipo: una rama `arregla-es-primo`; un commit «Corrige es_primo: comprueba todos los divisores hasta la raíz y los casos menores que 2»; y una revisión que pida ver las pruebas en verde y un caso con un cuadrado de primo, como 49.
