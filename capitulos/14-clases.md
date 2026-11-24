---
title: Clases y objetos
subtitle: Fabricar tus propios tipos de datos
kernelspec:
  name: python3
  display_name: Python 3
description: "Clases y objetos: fabricar tus propios tipos de datos. Python paso a paso, con visualizadores y diagrama de flujo."
---

## Punto de partida

Con un molde de galletas en forma de estrella puedes hacer cien galletas. Todas tienen la misma forma, pero cada una es una galleta distinta: a una le pones chocolate, a otra azúcar, y si te comes una, las demás siguen ahí.

## La pregunta

Hasta ahora hemos usado los tipos que trae Python: números, cadenas, listas, diccionarios. ¿Y si queremos un tipo que no existe, como una cuenta bancaria, que tiene un titular y un saldo y sabe hacer ingresos?

## La idea

Una **clase** es el molde; un **objeto** (o **instancia**) es cada galleta. La clase define dos cosas:

- los **atributos**: los datos que tiene cada objeto (el titular, el saldo);
- los **métodos**: las funciones que sabe hacer cada objeto (ingresar, retirar).

```python
class Cuenta:
    def __init__(self, titular, saldo):     # se ejecuta al crear cada objeto
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):           # un método
        self.saldo = self.saldo + cantidad
```

:::{important} `__init__` y `self`
- `__init__` es el método que se ejecuta automáticamente al crear un objeto: `Cuenta("Ana", 100)`. Su trabajo es dar a los atributos sus primeros valores.
- `self` es **el objeto concreto** con el que se está trabajando. Cuando escribes `c.ingresar(50)`, Python llama a `ingresar` con `self = c` y `cantidad = 50`. Por eso `self.saldo` es el saldo de *esa* cuenta, no de otra.
:::

## Construcción

### 1 · Una cuenta bancaria

:::{tip} Predice
Cuando se ejecuta `c.ingresar(50)`, ¿quién es `self`? ¿Cuánto valdrá `c.saldo` al final?
:::

```{code-cell} python
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

c = Cuenta("Ana", 100)
c.ingresar(50)
print(c.titular, c.saldo)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Una cuenta bancaria","etiqueta":"class · __init__ · self","idea":"Cuenta('Ana', 100) fabrica un objeto nuevo y llama a __init__ para rellenarlo. Dentro de los métodos, self es ese mismo objeto: fíjate en que self y c llevan el mismo número.","columnas":["c.titular","c.saldo"],"fila_en":"cada_linea"},"traza":{"codigo":"class Cuenta:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n\n    def ingresar(self, cantidad):\n        self.saldo = self.saldo + cantidad\n\nc = Cuenta(\"Ana\", 100)\nc.ingresar(50)\nprint(c.titular, c.saldo)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":9,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Cuenta.__init__","args":["self","titular","saldo"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{}},"titular":"Ana","saldo":100},"repr":{"self":"Cuenta nº1","titular":"'Ana'","saldo":"100"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Cuenta.__init__","args":["self","titular","saldo"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana"}},"titular":"Ana","saldo":100},"repr":{"self":"Cuenta nº1","titular":"'Ana'","saldo":"100"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Cuenta.__init__","args":["self","titular","saldo"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}},"titular":"Ana","saldo":100},"repr":{"self":"Cuenta nº1","titular":"'Ana'","saldo":"100"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[],"devuelve":{"funcion":"Cuenta.__init__","valor":"None","error":false},"excepcion":null},{"linea":10,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[{"nombre":"Cuenta.ingresar","args":["self","cantidad"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}},"cantidad":50},"repr":{"self":"Cuenta nº1","cantidad":"50"}}],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":150}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[{"nombre":"Cuenta.ingresar","args":["self","cantidad"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":150}},"cantidad":50},"repr":{"self":"Cuenta nº1","cantidad":"50"}}],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":150}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[],"devuelve":{"funcion":"Cuenta.ingresar","valor":"None","error":false},"excepcion":null},{"linea":11,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":150}}},"salida":"Ana 150\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["4 ↩","'Ana'","100"],["10","'Ana'","100"],["7","'Ana'","150"],["7 ↩","'Ana'","150"],["11","'Ana'","150"]]}}
```

El visualizador numera cada objeto: **Cuenta nº1**. Dentro de `ingresar`, `self` también es Cuenta nº1. No es una copia: es el mismo objeto con otro nombre.

### 2 · Dos cuentas y un alias

:::{tip} Predice
Después de `c = a` y `c.ingresar(30)`, ¿cuánto tiene `a`? ¿Y `b`?
:::

```{code-cell} python
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

a = Cuenta("Ana", 100)
b = Cuenta("Biel", 20)
c = a
c.ingresar(30)
print(a.saldo, b.saldo)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Dos cuentas y un alias","etiqueta":"objetos · etiquetas","idea":"a y b son dos objetos distintos (nº1 y nº2). Pero c = a no fabrica nada: c es otra etiqueta pegada al objeto nº1. Por eso, al ingresar en c, cambia a.","columnas":["a.saldo","b.saldo","c.saldo"],"fila_en":"cada_linea"},"traza":{"codigo":"class Cuenta:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n\n    def ingresar(self, cantidad):\n        self.saldo = self.saldo + cantidad\n\na = Cuenta(\"Ana\", 100)\nb = Cuenta(\"Biel\", 20)\nc = a\nc.ingresar(30)\nprint(a.saldo, b.saldo)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":9,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Cuenta.__init__","args":["self","titular","saldo"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{}},"titular":"Ana","saldo":100},"repr":{"self":"Cuenta nº1","titular":"'Ana'","saldo":"100"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Cuenta.__init__","args":["self","titular","saldo"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana"}},"titular":"Ana","saldo":100},"repr":{"self":"Cuenta nº1","titular":"'Ana'","saldo":"100"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Cuenta.__init__","args":["self","titular","saldo"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}},"titular":"Ana","saldo":100},"repr":{"self":"Cuenta nº1","titular":"'Ana'","saldo":"100"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"a":"Cuenta nº1"},"tipos":{"a":"Cuenta"},"pila":[],"devuelve":{"funcion":"Cuenta.__init__","valor":"None","error":false},"excepcion":null},{"linea":10,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"a":"Cuenta nº1"},"tipos":{"a":"Cuenta"},"pila":[{"nombre":"Cuenta.__init__","args":["self","titular","saldo"],"vars":{"self":{"__obj__":2,"__clase__":"Cuenta","attrs":{}},"titular":"Biel","saldo":20},"repr":{"self":"Cuenta nº2","titular":"'Biel'","saldo":"20"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"a":"Cuenta nº1"},"tipos":{"a":"Cuenta"},"pila":[{"nombre":"Cuenta.__init__","args":["self","titular","saldo"],"vars":{"self":{"__obj__":2,"__clase__":"Cuenta","attrs":{"titular":"Biel"}},"titular":"Biel","saldo":20},"repr":{"self":"Cuenta nº2","titular":"'Biel'","saldo":"20"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"a":"Cuenta nº1"},"tipos":{"a":"Cuenta"},"pila":[{"nombre":"Cuenta.__init__","args":["self","titular","saldo"],"vars":{"self":{"__obj__":2,"__clase__":"Cuenta","attrs":{"titular":"Biel","saldo":20}},"titular":"Biel","saldo":20},"repr":{"self":"Cuenta nº2","titular":"'Biel'","saldo":"20"}}],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}},"b":{"__obj__":2,"__clase__":"Cuenta","attrs":{"titular":"Biel","saldo":20}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"a":"Cuenta nº1","b":"Cuenta nº2"},"tipos":{"a":"Cuenta","b":"Cuenta"},"pila":[],"devuelve":{"funcion":"Cuenta.__init__","valor":"None","error":false},"excepcion":null},{"linea":11,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}},"b":{"__obj__":2,"__clase__":"Cuenta","attrs":{"titular":"Biel","saldo":20}},"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"a":"Cuenta nº1","b":"Cuenta nº2","c":"Cuenta nº1"},"tipos":{"a":"Cuenta","b":"Cuenta","c":"Cuenta"},"pila":[],"devuelve":null,"excepcion":null},{"linea":12,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}},"b":{"__obj__":2,"__clase__":"Cuenta","attrs":{"titular":"Biel","saldo":20}},"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"a":"Cuenta nº1","b":"Cuenta nº2","c":"Cuenta nº1"},"tipos":{"a":"Cuenta","b":"Cuenta","c":"Cuenta"},"pila":[{"nombre":"Cuenta.ingresar","args":["self","cantidad"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":100}},"cantidad":30},"repr":{"self":"Cuenta nº1","cantidad":"30"}}],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":130}},"b":{"__obj__":2,"__clase__":"Cuenta","attrs":{"titular":"Biel","saldo":20}},"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":130}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":7,"repr":{"a":"Cuenta nº1","b":"Cuenta nº2","c":"Cuenta nº1"},"tipos":{"a":"Cuenta","b":"Cuenta","c":"Cuenta"},"pila":[{"nombre":"Cuenta.ingresar","args":["self","cantidad"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":130}},"cantidad":30},"repr":{"self":"Cuenta nº1","cantidad":"30"}}],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":130}},"b":{"__obj__":2,"__clase__":"Cuenta","attrs":{"titular":"Biel","saldo":20}},"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":130}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":8,"repr":{"a":"Cuenta nº1","b":"Cuenta nº2","c":"Cuenta nº1"},"tipos":{"a":"Cuenta","b":"Cuenta","c":"Cuenta"},"pila":[],"devuelve":{"funcion":"Cuenta.ingresar","valor":"None","error":false},"excepcion":null},{"linea":13,"estado":{"a":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":130}},"b":{"__obj__":2,"__clase__":"Cuenta","attrs":{"titular":"Biel","saldo":20}},"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"titular":"Ana","saldo":130}}},"salida":"130 20\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":9,"repr":{"a":"Cuenta nº1","b":"Cuenta nº2","c":"Cuenta nº1"},"tipos":{"a":"Cuenta","b":"Cuenta","c":"Cuenta"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["4 ↩","100","—","—"],["10","100","—","—"],["3","100","—","—"],["4","100","—","—"],["4 ↩","100","20","—"],["11","100","20","100"],["12","100","20","100"],["7","130","20","130"],["7 ↩","130","20","130"],["13","130","20","130"]]}}
```

Aquí se resuelve la grieta del capítulo de variables: las variables no son cajas que guardan copias, son **etiquetas** pegadas a objetos. `c = a` pega una segunda etiqueta al mismo objeto. Para tener una cuenta distinta hay que fabricarla con `Cuenta(...)`.

### 3 · Atributos de clase y `__str__`

Un atributo definido directamente en la clase es **de la clase**: lo comparten todos los objetos. Y el método especial `__str__` decide qué se ve al imprimir un objeto:

```{code-cell} python
class Cuenta:
    banco = "Banco AC"                  # atributo de clase: común a todas

    def __init__(self, titular, saldo):
        self.titular = titular          # atributos de instancia: propios de cada una
        self.saldo = saldo

    def __str__(self):
        return f"{self.titular}: {self.saldo} € ({Cuenta.banco})"

a = Cuenta("Ana", 130)
print(a)
print(a.__dict__)                       # los atributos de instancia de a
print(hasattr(a, "saldo"), isinstance(a, Cuenta))
```

### 4 · Herencia

Una clase puede **heredar** de otra: recibe todos sus atributos y métodos, y añade o cambia los que necesite. Una cuenta de ahorro *es una* cuenta, con algo más:

```{code-cell} python
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

class CuentaAhorro(Cuenta):             # hereda de Cuenta
    def __init__(self, titular, saldo, interes):
        super().__init__(titular, saldo)    # reutiliza el __init__ de Cuenta
        self.interes = interes

    def aplicar_interes(self):
        self.ingresar(self.saldo * self.interes)   # usa un método heredado

ah = CuentaAhorro("Carla", 1000, 0.02)
ah.aplicar_interes()
print(ah.saldo)
print(isinstance(ah, Cuenta))           # True: una CuentaAhorro también es una Cuenta
```

`Cuenta` es la **superclase** y `CuentaAhorro` la **subclase**. `super()` llama al método de la superclase: así no hay que repetir lo que ya hace `Cuenta.__init__`.

:::{important} Los cuatro principios de la programación orientada a objetos
- **Encapsulación**: cada objeto guarda sus datos y los métodos que trabajan con ellos.
- **Abstracción**: usas `c.ingresar(50)` sin preocuparte de cómo está hecho por dentro.
- **Herencia**: una clase nueva reutiliza lo que ya hace otra.
- **Polimorfismo**: objetos de clases distintas pueden responder al mismo método, cada uno a su manera.
:::

## Conexiones

- Ya usabas objetos sin saberlo: una lista es un objeto de la clase `list`, y `append` es uno de sus métodos. `notas.append(8)` es lo mismo que `c.ingresar(50)`.
- Las excepciones son clases: `NotaInvalida(Exception)` del capítulo anterior era herencia.

## La grieta

Hemos encapsulado los datos, pero nada impide escribir `c.saldo = -1000000` desde fuera. ¿Cómo protege un objeto sus propios datos? Python tiene una convención para eso: los atributos que empiezan por `_` o por `__`, y las propiedades. Ese es el siguiente nivel.

## Preguntas tipo examen

Preguntas como las del examen PCAP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcap","capitulo":"14","titulo":"Preguntas tipo examen","etiqueta":"PCAP"}}
```

## Ejercicios

1. **Añade un método** `retirar(self, cantidad)` a `Cuenta` que reste la cantidad solo si hay saldo suficiente, y que lance un `ValueError` si no lo hay.
2. **¿Qué imprime?**

   ```python
   class Contador:
       def __init__(self):
           self.n = 0
       def sumar(self):
           self.n = self.n + 1

   x = Contador()
   y = Contador()
   x.sumar()
   x.sumar()
   y.sumar()
   print(x.n, y.n)
   ```

3. **Un rectángulo.** Escribe una clase `Rectangulo` con atributos `base` y `altura` y un método `area()`. Crea uno de 3 × 4 e imprime su área.

El solucionario está al final del capítulo.

## Solucionario

1. Una solución:

   ```python
   def retirar(self, cantidad):
       if cantidad > self.saldo:
           raise ValueError("saldo insuficiente")
       self.saldo = self.saldo - cantidad
   ```

2. Imprime **2 1**. `x` e `y` son dos objetos distintos, cada uno con su propio `n`: sumar en uno no toca el otro.
3. Una solución:

   ```python
   class Rectangulo:
       def __init__(self, base, altura):
           self.base = base
           self.altura = altura

       def area(self):
           return self.base * self.altura

   r = Rectangulo(3, 4)
   print(r.area())
   ```

   Imprime `12`.
