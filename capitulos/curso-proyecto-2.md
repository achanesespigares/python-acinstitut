---
title: "Proyecto 2 · Una biblioteca orientada a objetos"
subtitle: El proyecto de cierre del módulo 2, de la sesión 26 a la 30
description: "Proyecto 2 · Una biblioteca orientada a objetos: el proyecto de cierre del módulo 2, de la sesión 26 a la 30."
---

## El encargo

La biblioteca del centro presta libros y revistas. Hay que escribir un **paquete de Python** llamado `biblioteca` que la gestione:

- cada **recurso** tiene un código único, un título y un año, y sabe si está prestado;
- hay dos clases de recurso: **libros**, con autor, y **revistas**, con número;
- un **catálogo** guarda los recursos, presta y devuelve por código, busca por texto en el título, recorre los disponibles y los ordena por cualquier campo;
- los errores tienen **excepciones propias**: un código que no existe, un recurso ya prestado, un código repetido;
- el catálogo se **guarda** en un fichero CSV y se **carga** de él, sin perder qué está prestado;
- todo está cubierto por **pruebas unitarias**.

El trabajo se hace **en equipo** (dos o tres personas) con un repositorio de git, ramas y revisiones, y con un **registro del uso de la IA**: qué se le pidió, qué devolvió y qué hubo que corregir.

## Lo que se practica

| Del curso | Dónde aparece en el proyecto |
|---|---|
| Módulos y paquetes | `biblioteca/` con su `__init__.py` y un módulo por responsabilidad |
| Excepciones propias | `BibliotecaError` y sus dos hijas |
| Clases, herencia, `super()` | `Recurso`, `Libro` y `Revista` |
| Nombres ocultos | El estado de préstamo, solo accesible con métodos |
| Polimorfismo | `__str__` en la madre, `detalle()` en cada hija |
| Atributos de clase | El contador de recursos creados |
| Comprensiones, lambdas, generadores | Buscar, ordenar y recorrer los disponibles |
| `match` | Reconstruir cada recurso al cargar el CSV |
| Ficheros y `pathlib` | Guardar y cargar el catálogo |
| `unittest` | Las pruebas del paquete |
| Git e IA | El flujo de trabajo del equipo |

## Cómo se trabaja en Colab

Cada módulo del paquete se escribe en su propia celda con `%%writefile`. La carpeta se crea una vez con `!mkdir -p biblioteca`. Las pruebas se ejecutan con:

```python
!python -m unittest test_biblioteca -v
```

Si se cambia un módulo después de importarlo en el cuaderno, hay que reiniciar el entorno (o usar `importlib.reload`) para que Python lo lea de nuevo. Las pruebas con `!python` no tienen ese problema: arrancan un Python nuevo cada vez.

## Los hitos

| Sesión | Hito | Qué se entrega |
|---|---|---|
| 26 | **1 · Diseño** | Un esquema de las clases: atributos, métodos y quién hereda de quién. La lista de excepciones y cuándo salta cada una. El reparto del trabajo en el equipo. |
| 27 | **2 · Clases y pruebas** | `errores.py` y `modelos.py` terminados, y las primeras pruebas en verde. |
| 28 | **3 · Catálogo, ficheros y git** | `catalogo.py` con guardar y cargar; el trabajo hecho en ramas, con al menos una revisión entre compañeros; el registro de la IA empezado. |
| 29 | **4 · Entrega** | Todas las pruebas en verde, el registro de la IA completo y la exposición ensayada. |
| 30 | **Exposición** | 7 minutos por equipo. |

## El registro de la IA

Cada vez que el equipo use una IA, apunta una fila:

| Fecha | Qué se pidió | Qué devolvió (resumen) | Qué se comprobó | Qué se corrigió |
|---|---|---|---|---|

Usar la IA no resta. Lo que cuenta es **haber comprobado** lo que devolvió: una prueba que lo confirme o un caso que lo rompa.

## La versión mínima y las ampliaciones

La **versión mínima** es la de la solución de referencia: las tres clases de recurso, el catálogo con sus siete operaciones, las tres excepciones, guardar y cargar, y al menos cuatro pruebas.

Ampliaciones:

- una tercera clase de recurso (por ejemplo `Pelicula`, con duración);
- socios: quién tiene cada préstamo y cuántos puede tener a la vez;
- fecha de préstamo y aviso de los que llevan más de 15 días (`datetime`);
- un pequeño menú de consola en un `__main__.py`, para ejecutar el paquete con `python -m biblioteca`;
- `__repr__` en las clases, y una prueba que lo use.

## La rúbrica

| Criterio | 0 | 1 | 2 |
|---|---|---|---|
| **Funciona** | Falla alguna operación mínima | Todo funciona con datos buenos | Todo funciona, también al cargar un fichero que no existe |
| **Diseño de clases** | Sin herencia | Herencia, pero con código repetido en las hijas | Herencia limpia: lo común en la madre, lo propio en cada hija |
| **Excepciones** | Errores genéricos | Excepciones propias, pero sin jerarquía | Jerarquía propia, con mensajes claros |
| **Pruebas** | Ninguna | Pruebas que solo cubren lo que funciona | Pruebas de los casos de error y de guardar y cargar |
| **Paquete y estilo** | Todo en un fichero | Paquete con módulos | Paquete con módulos, nombres claros y docstrings |
| **Git y equipo** | Sin repositorio | Repositorio con commits | Ramas, revisiones y commits con mensajes que explican |
| **Uso de la IA** | Sin registro | Registro incompleto | Registro con lo comprobado y lo corregido |
| **Exposición** | No se entiende | Se entiende el uso | Se entiende el diseño y se explica un error y su arreglo |
| **Ampliaciones** | Ninguna | Una | Dos o más |

Nota del proyecto: la suma de los nueve criterios, sobre 18, pasada a 10.

:::{tip} Cómo acompañar el proyecto
El momento delicado es la sesión 28: los equipos que no han repartido bien el trabajo chocan al juntar sus ramas. Conviene pedir en el hito 1 qué módulo escribe cada persona, y que las pruebas se escriban antes que el código que prueban.
:::

---

## Solución de referencia

Una posible solución, solo para el profesor. Son cinco ficheros, cada uno en su celda de Colab. Las cuatro pruebas pasan.

### `biblioteca/__init__.py`

```python
%%writefile biblioteca/__init__.py
"""Paquete biblioteca: recursos, catálogo y errores."""
from .errores import BibliotecaError, NoEncontrado, NoDisponible
from .modelos import Recurso, Libro, Revista
from .catalogo import Catalogo, cargar
```

### `biblioteca/errores.py`

```python
%%writefile biblioteca/errores.py
class BibliotecaError(Exception):
    """Cualquier error propio de la biblioteca."""


class NoEncontrado(BibliotecaError):
    def __init__(self, codigo):
        super().__init__(f"No hay ningún recurso con el código {codigo}")
        self.codigo = codigo


class NoDisponible(BibliotecaError):
    def __init__(self, recurso):
        super().__init__(f"«{recurso.titulo}» ya está prestado")
        self.recurso = recurso
```

### `biblioteca/modelos.py`

```python
%%writefile biblioteca/modelos.py
from .errores import NoDisponible, BibliotecaError


class Recurso:
    creados = 0

    def __init__(self, codigo, titulo, anio):
        if not titulo.strip():
            raise BibliotecaError("El título no puede estar vacío")
        self.codigo = codigo
        self.titulo = titulo
        self.anio = anio
        self.__prestado = False
        Recurso.creados += 1

    def esta_prestado(self):
        return self.__prestado

    def prestar(self):
        if self.__prestado:
            raise NoDisponible(self)
        self.__prestado = True

    def devolver(self):
        self.__prestado = False

    def detalle(self):
        return ""

    def __str__(self):
        estado = "prestado" if self.__prestado else "disponible"
        return f"[{self.codigo}] {self.titulo} ({self.anio}){self.detalle()} · {estado}"


class Libro(Recurso):
    def __init__(self, codigo, titulo, anio, autor):
        super().__init__(codigo, titulo, anio)
        self.autor = autor

    def detalle(self):
        return f", de {self.autor}"


class Revista(Recurso):
    def __init__(self, codigo, titulo, anio, numero):
        super().__init__(codigo, titulo, anio)
        self.numero = numero

    def detalle(self):
        return f", n.º {self.numero}"
```

### `biblioteca/catalogo.py`

```python
%%writefile biblioteca/catalogo.py
import csv
from pathlib import Path

from .errores import BibliotecaError, NoEncontrado
from .modelos import Libro, Revista


class Catalogo:
    def __init__(self):
        self.recursos = {}

    def anade(self, recurso):
        if recurso.codigo in self.recursos:
            raise BibliotecaError(f"El código {recurso.codigo} ya existe")
        self.recursos[recurso.codigo] = recurso

    def busca(self, codigo):
        try:
            return self.recursos[codigo]
        except KeyError:
            raise NoEncontrado(codigo) from None

    def prestar(self, codigo):
        self.busca(codigo).prestar()

    def devolver(self, codigo):
        self.busca(codigo).devolver()

    def con_texto(self, texto):
        texto = texto.lower()
        return [r for r in self.recursos.values() if texto in r.titulo.lower()]

    def disponibles(self):
        for r in self.recursos.values():
            if not r.esta_prestado():
                yield r

    def ordenados(self, campo="titulo"):
        return sorted(self.recursos.values(), key=lambda r: getattr(r, campo))

    def guarda(self, ruta):
        ruta = Path(ruta)
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            for r in self.recursos.values():
                extra = r.autor if isinstance(r, Libro) else r.numero
                escritor.writerow([type(r).__name__, r.codigo, r.titulo, r.anio, extra,
                                   int(r.esta_prestado())])


def cargar(ruta):
    catalogo = Catalogo()
    ruta = Path(ruta)
    if not ruta.exists():
        return catalogo
    with open(ruta, newline="", encoding="utf-8") as f:
        for fila in csv.reader(f):
            match fila:
                case ["Libro", codigo, titulo, anio, autor, prestado]:
                    r = Libro(codigo, titulo, int(anio), autor)
                case ["Revista", codigo, titulo, anio, numero, prestado]:
                    r = Revista(codigo, titulo, int(anio), int(numero))
                case _:
                    continue
            if prestado == "1":
                r.prestar()
            catalogo.anade(r)
    return catalogo
```

### `test_biblioteca.py`

```python
%%writefile test_biblioteca.py
import tempfile
import unittest
from pathlib import Path

from biblioteca import (Catalogo, Libro, Revista, cargar,
                        BibliotecaError, NoDisponible, NoEncontrado)


class PruebaCatalogo(unittest.TestCase):
    def setUp(self):
        self.c = Catalogo()
        self.c.anade(Libro("L1", "Cien años de soledad", 1967, "García Márquez"))
        self.c.anade(Libro("L2", "El Aleph", 1949, "Borges"))
        self.c.anade(Revista("R1", "Investigación y Ciencia", 2026, 590))

    def test_prestar_y_devolver(self):
        self.c.prestar("L1")
        self.assertTrue(self.c.busca("L1").esta_prestado())
        with self.assertRaises(NoDisponible):
            self.c.prestar("L1")
        self.c.devolver("L1")
        self.assertFalse(self.c.busca("L1").esta_prestado())

    def test_errores(self):
        with self.assertRaises(NoEncontrado):
            self.c.prestar("X9")
        with self.assertRaises(BibliotecaError):
            self.c.anade(Libro("L1", "Repetido", 2000, "Nadie"))
        with self.assertRaises(BibliotecaError):
            Libro("L3", "  ", 2000, "Nadie")

    def test_busquedas(self):
        self.assertEqual([r.codigo for r in self.c.con_texto("ALEPH")], ["L2"])
        self.c.prestar("L2")
        self.assertEqual([r.codigo for r in self.c.disponibles()], ["L1", "R1"])
        self.assertEqual([r.codigo for r in self.c.ordenados("anio")], ["L2", "L1", "R1"])

    def test_guardar_y_cargar(self):
        self.c.prestar("R1")
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "catalogo.csv"
            self.c.guarda(ruta)
            otro = cargar(ruta)
        self.assertEqual(len(otro.recursos), 3)
        self.assertTrue(otro.busca("R1").esta_prestado())
        self.assertEqual(str(otro.busca("L2")), str(self.c.busca("L2")))


if __name__ == "__main__":
    unittest.main()
```

### Una prueba en directo

```python
from biblioteca import Catalogo, Libro, Revista, BibliotecaError

c = Catalogo()
c.anade(Libro("L2", "El Aleph", 1949, "Borges"))
c.anade(Revista("R1", "Investigación y Ciencia", 2026, 590))
c.prestar("R1")
for r in c.ordenados():
    print(r)
try:
    c.prestar("R1")
except BibliotecaError as e:
    print("Error:", e)
```

```text
[L2] El Aleph (1949), de Borges · disponible
[R1] Investigación y Ciencia (2026), n.º 590 · prestado
Error: «Investigación y Ciencia» ya está prestado
```

### Decisiones que conviene comentar en clase

- **Las importaciones con punto** (`from .errores import …`) buscan dentro del propio paquete. El `__init__.py` reúne lo importante para que fuera baste con `from biblioteca import Catalogo`.
- **`__prestado` está oculto**: nadie puede marcar un libro como prestado sin pasar por `prestar()`, que es quien comprueba si ya lo estaba.
- **`detalle()` es el gancho del polimorfismo**: la madre escribe la línea completa y cada hija solo aporta su trozo. Añadir `Pelicula` no obliga a tocar `__str__`.
- **`raise NoEncontrado(codigo) from None`** cambia el `KeyError` del diccionario por el error propio, y el `from None` evita que el traceback muestre los dos.
- **`disponibles()` es un generador**: no construye ninguna lista, y por eso en las pruebas se recorre con una comprensión.
- **`match` al cargar** comprueba a la vez el tipo de recurso y que la fila tenga seis columnas; una fila rara se salta con `case _`.
- **`setUp`** en las pruebas crea un catálogo nuevo antes de cada prueba, para que ninguna dependa de lo que hizo otra.
