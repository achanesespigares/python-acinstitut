---
title: Clases a fondo
subtitle: Atributos compartidos, nombres ocultos, herencia múltiple y polimorfismo
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

En una familia, el apellido es de todos y el nombre es de cada uno. Hay cosas que se heredan de los padres, cosas que cada hijo hace a su manera y cosas que se guardan en el cajón propio. Las clases funcionan igual.

## La pregunta

¿Qué datos pertenecen a la clase y cuáles a cada objeto? ¿Cómo esconde una clase sus datos internos? Si una clase hereda de dos, y las dos tienen el mismo método, ¿cuál se usa?

## La idea

Cuando escribes `objeto.nombre`, Python busca `nombre` en este orden:

1. en el propio objeto (sus atributos de instancia, los de `objeto.__dict__`);
2. en su clase;
3. en las clases de las que hereda, en un orden fijo llamado **MRO** (*Method Resolution Order*, orden de resolución de métodos).

Usa lo primero que encuentra. Casi todo lo de este capítulo se explica con esa búsqueda.

## Construcción

### 1 · Atributos de clase y de instancia

Un atributo creado dentro de la clase, fuera de los métodos, es **de la clase**: hay uno solo, compartido por todos los objetos. Los que se crean con `self.algo = …` son de cada objeto.

:::{tip} Predice
Después de crear dos alumnos, ¿cuánto vale `Alumno.total`? ¿Y `a.total`, si `a` no tiene ningún atributo `total` propio?
:::

```{code-cell} python
class Alumno:
    total = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Alumno.total = Alumno.total + 1

a = Alumno("Ana")
b = Alumno("Biel")
print(Alumno.total, a.total)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Un contador para toda la clase","etiqueta":"atributo de clase","idea":"total vive en la clase, no en cada alumno: por eso no aparece en las tarjetas de a y b. a.total funciona porque Python no lo encuentra en el objeto y lo busca en su clase.","columnas":["Alumno.total"],"fila_en":"cada_linea"},"traza":{"codigo":"class Alumno:\n    total = 0\n    def __init__(self, nombre):\n        self.nombre = nombre\n        Alumno.total = Alumno.total + 1\n\na = Alumno(\"Ana\")\nb = Alumno(\"Biel\")\nprint(Alumno.total, a.total)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null,"clases":{"Alumno":{"total":0}}},{"linea":7,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Alumno.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":1,"__clase__":"Alumno","attrs":{}},"nombre":"Ana"},"repr":{"self":"Alumno nº1","nombre":"'Ana'"}}],"devuelve":null,"excepcion":null,"clases":{"Alumno":{"total":0}}},{"linea":4,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Alumno.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":1,"__clase__":"Alumno","attrs":{"nombre":"Ana"}},"nombre":"Ana"},"repr":{"self":"Alumno nº1","nombre":"'Ana'"}}],"devuelve":null,"excepcion":null,"clases":{"Alumno":{"total":0}}},{"linea":5,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Alumno.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":1,"__clase__":"Alumno","attrs":{"nombre":"Ana"}},"nombre":"Ana"},"repr":{"self":"Alumno nº1","nombre":"'Ana'"}}],"devuelve":null,"excepcion":null,"clases":{"Alumno":{"total":1}}},{"linea":5,"estado":{"a":{"__obj__":1,"__clase__":"Alumno","attrs":{"nombre":"Ana"}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"Alumno nº1"},"tipos":{"a":"Alumno"},"pila":[],"devuelve":{"funcion":"Alumno.__init__","valor":"None","error":false},"excepcion":null,"clases":{"Alumno":{"total":1}}},{"linea":8,"estado":{"a":{"__obj__":1,"__clase__":"Alumno","attrs":{"nombre":"Ana"}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"Alumno nº1"},"tipos":{"a":"Alumno"},"pila":[{"nombre":"Alumno.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":2,"__clase__":"Alumno","attrs":{}},"nombre":"Biel"},"repr":{"self":"Alumno nº2","nombre":"'Biel'"}}],"devuelve":null,"excepcion":null,"clases":{"Alumno":{"total":1}}},{"linea":4,"estado":{"a":{"__obj__":1,"__clase__":"Alumno","attrs":{"nombre":"Ana"}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"Alumno nº1"},"tipos":{"a":"Alumno"},"pila":[{"nombre":"Alumno.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":2,"__clase__":"Alumno","attrs":{"nombre":"Biel"}},"nombre":"Biel"},"repr":{"self":"Alumno nº2","nombre":"'Biel'"}}],"devuelve":null,"excepcion":null,"clases":{"Alumno":{"total":1}}},{"linea":5,"estado":{"a":{"__obj__":1,"__clase__":"Alumno","attrs":{"nombre":"Ana"}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"Alumno nº1"},"tipos":{"a":"Alumno"},"pila":[{"nombre":"Alumno.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":2,"__clase__":"Alumno","attrs":{"nombre":"Biel"}},"nombre":"Biel"},"repr":{"self":"Alumno nº2","nombre":"'Biel'"}}],"devuelve":null,"excepcion":null,"clases":{"Alumno":{"total":2}}},{"linea":5,"estado":{"a":{"__obj__":1,"__clase__":"Alumno","attrs":{"nombre":"Ana"}},"b":{"__obj__":2,"__clase__":"Alumno","attrs":{"nombre":"Biel"}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"Alumno nº1","b":"Alumno nº2"},"tipos":{"a":"Alumno","b":"Alumno"},"pila":[],"devuelve":{"funcion":"Alumno.__init__","valor":"None","error":false},"excepcion":null,"clases":{"Alumno":{"total":2}}},{"linea":9,"estado":{"a":{"__obj__":1,"__clase__":"Alumno","attrs":{"nombre":"Ana"}},"b":{"__obj__":2,"__clase__":"Alumno","attrs":{"nombre":"Biel"}}},"salida":"2 2\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"a":"Alumno nº1","b":"Alumno nº2"},"tipos":{"a":"Alumno","b":"Alumno"},"pila":[],"devuelve":null,"excepcion":null,"clases":{"Alumno":{"total":2}}}],"filas":[["9","—"]]}}
```

:::{warning} Trampa · `self.total = self.total + 1`
Si en `__init__` escribieras `self.total = self.total + 1`, el lado derecho leería el `total` de la clase (0), pero la asignación crearía un atributo **nuevo** en el objeto. La clase seguiría valiendo 0 y cada alumno tendría su propio `total = 1`. Para cambiar el de la clase hay que nombrarla: `Alumno.total`.
:::

### 2 · Nombres ocultos: la desfiguración de nombres

Python no tiene atributos privados de verdad, pero tiene dos convenciones:

- `_saldo`, con **un** guion bajo: «esto es interno, no lo toques». Es solo un aviso.
- `__saldo`, con **dos** guiones bajos (y sin dos al final): Python le cambia el nombre a `_Clase__saldo`. Es la **desfiguración de nombres** (*name mangling*).

:::{tip} Predice
¿Con qué nombre aparecerá el saldo en la tarjeta del objeto?
:::

```{code-cell} python
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def saldo(self):
        return self.__saldo

c = Cuenta(100)
print(c.saldo())
print(c.__dict__)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El saldo escondido","etiqueta":"name mangling","idea":"Dentro de la clase se escribe self.__saldo, pero el objeto lo guarda como _Cuenta__saldo. Desde dentro de la clase funciona igual; desde fuera, c.__saldo no existe.","columnas":["c.saldo()"],"fila_en":"cada_linea"},"traza":{"codigo":"class Cuenta:\n    def __init__(self, saldo):\n        self.__saldo = saldo\n\n    def saldo(self):\n        return self.__saldo\n\nc = Cuenta(100)\nprint(c.saldo())\nprint(c.__dict__)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Cuenta.__init__","args":["self","saldo"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{}},"saldo":100},"repr":{"self":"Cuenta nº1","saldo":"100"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Cuenta.__init__","args":["self","saldo"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"_Cuenta__saldo":100}},"saldo":100},"repr":{"self":"Cuenta nº1","saldo":"100"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"_Cuenta__saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[],"devuelve":{"funcion":"Cuenta.__init__","valor":"None","error":false},"excepcion":null},{"linea":9,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"_Cuenta__saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[{"nombre":"Cuenta.saldo","args":["self"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"_Cuenta__saldo":100}}},"repr":{"self":"Cuenta nº1"}}],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"_Cuenta__saldo":100}}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[{"nombre":"Cuenta.saldo","args":["self"],"vars":{"self":{"__obj__":1,"__clase__":"Cuenta","attrs":{"_Cuenta__saldo":100}}},"repr":{"self":"Cuenta nº1"}}],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"_Cuenta__saldo":100}}},"salida":"100\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[],"devuelve":{"funcion":"Cuenta.saldo","valor":"100","error":false},"excepcion":null},{"linea":10,"estado":{"c":{"__obj__":1,"__clase__":"Cuenta","attrs":{"_Cuenta__saldo":100}}},"salida":"100\n{'_Cuenta__saldo': 100}\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"c":"Cuenta nº1"},"tipos":{"c":"Cuenta"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["3 ↩","100"],["9","100"],["6","100"],["6 ↩","100"],["10","100"]]}}
```

```{code-cell} python
try:
    print(c.__saldo)
except AttributeError as e:
    print("Error:", e)
print(c._Cuenta__saldo)    # posible, pero es saltarse la protección a propósito
```

### 3 · Herencia, sobrescritura y polimorfismo

Una subclase puede **sobrescribir** un método de su madre: definir uno con el mismo nombre que hace otra cosa. Y entonces la misma llamada, `a.habla()`, hace algo distinto según el objeto. Eso es el **polimorfismo**.

:::{tip} Predice
`Perro` no define `__init__`. ¿Cuál se ejecuta al crear `Perro("Rex")`? ¿Qué dirá `Animal("Bicho")`?
:::

```{code-cell} python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def habla(self):
        return "..."

class Perro(Animal):
    def habla(self):
        return "¡Guau!"

class Gato(Animal):
    def habla(self):
        return "¡Miau!"

animales = [Perro("Rex"), Gato("Misi"), Animal("Bicho")]
for a in animales:
    print(a.nombre, a.habla())
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Cada uno habla a su manera","etiqueta":"herencia · polimorfismo","idea":"Perro y Gato heredan el __init__ de Animal, pero cada uno sobrescribe habla. El for hace la misma llamada, a.habla(), y Python elige el método según la clase del objeto.","lista":"animales","cabecera":16,"puntero":"a","columnas":["a.nombre","a.habla()"],"fila_en":"fin_iteracion"},"traza":{"codigo":"class Animal:\n    def __init__(self, nombre):\n        self.nombre = nombre\n    def habla(self):\n        return \"...\"\n\nclass Perro(Animal):\n    def habla(self):\n        return \"¡Guau!\"\n\nclass Gato(Animal):\n    def habla(self):\n        return \"¡Miau!\"\n\nanimales = [Perro(\"Rex\"), Gato(\"Misi\"), Animal(\"Bicho\")]\nfor a in animales:\n    print(a.nombre, a.habla())","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":11,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":15,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Animal.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":1,"__clase__":"Perro","attrs":{}},"nombre":"Rex"},"repr":{"self":"Perro nº1","nombre":"'Rex'"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Animal.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},"nombre":"Rex"},"repr":{"self":"Perro nº1","nombre":"'Rex'"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":{"funcion":"Animal.__init__","valor":"None","error":false},"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Animal.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},"nombre":"Misi"},"repr":{"self":"Gato nº2","nombre":"'Misi'"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":{"funcion":"Animal.__init__","valor":"None","error":false},"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[{"nombre":"Animal.__init__","args":["self","nombre"],"vars":{"self":{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}},"nombre":"Bicho"},"repr":{"self":"Animal nº3","nombre":"'Bicho'"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]"},"tipos":{"animales":"list"},"pila":[],"devuelve":{"funcion":"Animal.__init__","valor":"None","error":false},"excepcion":null},{"linea":16,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}}},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Perro nº1"},"tipos":{"animales":"list","a":"Perro"},"pila":[],"devuelve":null,"excepcion":null},{"linea":17,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}}},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Perro nº1"},"tipos":{"animales":"list","a":"Perro"},"pila":[{"nombre":"Perro.habla","args":["self"],"vars":{"self":{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}}},"repr":{"self":"Perro nº1"}}],"devuelve":null,"excepcion":null},{"linea":9,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}}},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Perro nº1"},"tipos":{"animales":"list","a":"Perro"},"pila":[{"nombre":"Perro.habla","args":["self"],"vars":{"self":{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}}},"repr":{"self":"Perro nº1"}}],"devuelve":null,"excepcion":null},{"linea":9,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}}},"salida":"Rex ¡Guau!\n","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Perro nº1"},"tipos":{"animales":"list","a":"Perro"},"pila":[],"devuelve":{"funcion":"Perro.habla","valor":"'¡Guau!'","error":false},"excepcion":null},{"linea":16,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}}},"salida":"Rex ¡Guau!\n","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Gato nº2"},"tipos":{"animales":"list","a":"Gato"},"pila":[],"devuelve":null,"excepcion":null},{"linea":17,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}}},"salida":"Rex ¡Guau!\n","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Gato nº2"},"tipos":{"animales":"list","a":"Gato"},"pila":[{"nombre":"Gato.habla","args":["self"],"vars":{"self":{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}}},"repr":{"self":"Gato nº2"}}],"devuelve":null,"excepcion":null},{"linea":13,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}}},"salida":"Rex ¡Guau!\n","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Gato nº2"},"tipos":{"animales":"list","a":"Gato"},"pila":[{"nombre":"Gato.habla","args":["self"],"vars":{"self":{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}}},"repr":{"self":"Gato nº2"}}],"devuelve":null,"excepcion":null},{"linea":13,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}}},"salida":"Rex ¡Guau!\nMisi ¡Miau!\n","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Gato nº2"},"tipos":{"animales":"list","a":"Gato"},"pila":[],"devuelve":{"funcion":"Gato.habla","valor":"'¡Miau!'","error":false},"excepcion":null},{"linea":16,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}},"salida":"Rex ¡Guau!\nMisi ¡Miau!\n","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Animal nº3"},"tipos":{"animales":"list","a":"Animal"},"pila":[],"devuelve":null,"excepcion":null},{"linea":17,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}},"salida":"Rex ¡Guau!\nMisi ¡Miau!\n","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Animal nº3"},"tipos":{"animales":"list","a":"Animal"},"pila":[{"nombre":"Animal.habla","args":["self"],"vars":{"self":{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}},"repr":{"self":"Animal nº3"}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}},"salida":"Rex ¡Guau!\nMisi ¡Miau!\n","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Animal nº3"},"tipos":{"animales":"list","a":"Animal"},"pila":[{"nombre":"Animal.habla","args":["self"],"vars":{"self":{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}},"repr":{"self":"Animal nº3"}}],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}},"salida":"Rex ¡Guau!\nMisi ¡Miau!\nBicho ...\n","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Animal nº3"},"tipos":{"animales":"list","a":"Animal"},"pila":[],"devuelve":{"funcion":"Animal.habla","valor":"'...'","error":false},"excepcion":null},{"linea":16,"estado":{"animales":[{"__obj__":1,"__clase__":"Perro","attrs":{"nombre":"Rex"}},{"__obj__":2,"__clase__":"Gato","attrs":{"nombre":"Misi"}},{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}],"a":{"__obj__":3,"__clase__":"Animal","attrs":{"nombre":"Bicho"}}},"salida":"Rex ¡Guau!\nMisi ¡Miau!\nBicho ...\n","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":2,"repr":{"animales":"[Perro nº1, Gato nº2, Animal nº3]","a":"Animal nº3"},"tipos":{"animales":"list","a":"Animal"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["'Rex'","'¡Guau!'"],["'Misi'","'¡Miau!'"],["'Bicho'","'...'"]]}}
```

Para llamar desde la subclase al método de la madre que has sobrescrito se usa `super()`:

```{code-cell} python
class Cachorro(Perro):
    def habla(self):
        return super().habla() + " (flojito)"

print(Cachorro("Toby").habla())
```

### 4 · Herencia múltiple y MRO

Una clase puede heredar de varias: `class D(B, C):`. Si dos de ellas tienen el mismo método, Python sigue el **MRO**, que se puede consultar:

```{code-cell} python
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

print([k.__name__ for k in D.__mro__])
print(D().quien())
```

La regla práctica: **de izquierda a derecha, y cada clase antes que sus madres**. En `D(B, C)` se mira `D`, luego `B`, luego `C` y al final `A`, y por último `object`, la madre de todas las clases. Esta forma de rombo se llama **herencia en diamante**: `A` aparece una sola vez, al final, aunque se llegue a ella por dos caminos.

:::{important} El MRO también decide `super()`
`super()` no significa «mi madre», sino «la siguiente clase en el MRO del objeto». En un diamante, el `super()` de `B` puede llevar a `C`, no a `A`. Así cada clase de la jerarquía se ejecuta una sola vez.
:::

### 5 · Introspección: el objeto se describe a sí mismo

Python permite preguntar a objetos y clases por sí mismos:

| Expresión | Qué da | Ejemplo con `p = Perro("Rex")` |
|---|---|---|
| `type(p)` o `p.__class__` | la clase del objeto | `Perro` |
| `p.__class__.__name__` | el nombre de la clase | `'Perro'` |
| `p.__dict__` | los atributos del objeto | `{'nombre': 'Rex'}` |
| `Perro.__bases__` | las clases madre directas | `(Animal,)` |
| `isinstance(p, Animal)` | ¿es un `Animal`, o hereda de él? | `True` |
| `issubclass(Perro, Animal)` | ¿la clase hereda de esa otra? | `True` |
| `hasattr(p, "nombre")` | ¿tiene ese atributo? | `True` |
| `getattr(p, "nombre")` | el atributo, por su nombre en texto | `'Rex'` |
| `setattr(p, "edad", 3)` | crea o cambia un atributo por su nombre | |

```{code-cell} python
p = Perro("Rex")
print(type(p).__name__, Perro.__bases__, Perro.__module__)
print(isinstance(p, Animal), issubclass(Perro, Animal), issubclass(Perro, Gato))
setattr(p, "edad", 3)
print(p.__dict__, getattr(p, "edad"))
```

### 6 · Construir objetos con cuidado

`__init__` es la puerta de entrada del objeto: conviene que reciba bien los datos y que rechace los imposibles.

```{code-cell} python
class Cuenta:
    def __init__(self, titular, saldo=0, movimientos=None):
        if saldo < 0:
            raise ValueError("el saldo inicial no puede ser negativo")
        self.titular = titular
        self.saldo = saldo
        self.movimientos = [] if movimientos is None else movimientos

c = Cuenta("Ana", saldo=50)        # argumento por nombre: se lee solo
print(c.titular, c.saldo, c.movimientos)
try:
    Cuenta("Biel", -10)
except ValueError as e:
    print("Error:", e)
```

- **Valores por defecto** (`saldo=0`): el argumento se puede omitir.
- **Argumentos por nombre** (`saldo=50`): la llamada se entiende sin mirar la definición.
- **Validar y lanzar** una excepción si el dato es imposible: mejor un error al crear el objeto que un objeto estropeado.

:::{warning} Trampa · una lista como valor por defecto
`def __init__(self, movimientos=[])` parece inofensivo, pero la lista se crea **una sola vez**, cuando se define la función, y la comparten todos los objetos que no pasen la suya: lo que apunta uno aparece en los demás. Por eso se escribe `movimientos=None` y se crea una lista nueva dentro, como arriba.
:::

### 7 · Identidad e igualdad: `is` y `==`

- `a == b` pregunta si **valen lo mismo**.
- `a is b` pregunta si son **el mismo objeto**, la misma tarjeta con el mismo número.

```{code-cell} python
x = [1, 2]
y = [1, 2]
z = x
print(x == y, x is y, x is z)
print(x is not y)
```

En los objetos de tus clases, `==` compara identidad mientras no definas `__eq__`. Y para comprobar `None` se usa siempre `is`: `if valor is None:`.

### 8 · `__str__`, `__repr__` y propiedades

- `__str__` decide qué sale con `print(objeto)` y `str(objeto)`: un texto para personas.
- `__repr__` decide qué sale en la consola y dentro de listas: un texto para programadores, idealmente como el código que crearía el objeto.
- Con `@property`, un método se usa como si fuera un atributo, sin paréntesis. Sirve para dar acceso de solo lectura a un dato escondido.

:::{warning} Trampa · la firma de `__str__`
`__str__` recibe solo `self` y **tiene que devolver una cadena**. Si le añades parámetros, `print(objeto)` lanza `TypeError` porque Python lo llama sin argumentos; y si devuelve un número, también: `__str__ returned non-string`.
:::

```{code-cell} python
class Punto:
    def __init__(self, x, y):
        self.__x, self.__y = x, y

    @property
    def x(self):
        return self.__x

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"Punto({self.__x}, {self.__y})"

p = Punto(2, 5)
print(p, [p], p.x)
```

## Conexiones

- La búsqueda objeto → clase → MRO explica a la vez los atributos de clase, la herencia, la sobrescritura y `super()`.
- La desfiguración de nombres evita choques de nombres entre una clase y sus subclases. No es una caja fuerte: es una cerradura de cortesía.
- El polimorfismo es lo que hace que un mismo `for` trate igual a objetos distintos, como `print` trata igual a números, cadenas y listas.

## La grieta

Las cadenas parecían sencillas: letras en fila. Pero, ¿qué es *de verdad* una letra para el ordenador? ¿Por qué `"Zorro" < "abeja"` da `True`? Hay que mirar debajo de los caracteres.

## Preguntas tipo examen

Preguntas como las del examen PCAP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcap","capitulo":"18","titulo":"Preguntas tipo examen","etiqueta":"PCAP"}}
```

## Ejercicios

1. **¿Qué imprime?**

   ```python
   class X:
       valor = 1

   a = X()
   b = X()
   a.valor = 5
   print(a.valor, b.valor, X.valor)
   ```

2. **Desfiguración.** Para `class Caja:` con `self.__secreto = 7` en su `__init__`, ¿qué nombre tiene el atributo en `Caja().__dict__`?
3. **Polimorfismo.** Añade una clase `Vaca(Animal)` que diga «¡Muu!» y métela en la lista `animales` del apartado 3.
4. **MRO.** Con las clases `A`, `B`, `C` del apartado 4, ¿qué imprime `print(D().quien())` si cambias la definición a `class D(C, B):`?
5. **Introspección.** Escribe una expresión que diga si un objeto `p` tiene un atributo llamado `"edad"` sin provocar error si no lo tiene.

El solucionario está al final del capítulo.

## Solucionario

1. Imprime **5 1 1**. `a.valor = 5` crea un atributo nuevo en `a`, que tapa al de la clase solo para `a`. `b` y la clase siguen con 1.
2. `{'_Caja__secreto': 7}`.
3. Una solución:

   ```python
   class Vaca(Animal):
       def habla(self):
           return "¡Muu!"

   animales = [Perro("Rex"), Gato("Misi"), Vaca("Lola"), Animal("Bicho")]
   ```

4. Imprime **C**. El MRO pasa a ser `D, C, B, A, object`, y `C` es la primera que tiene `quien`.
5. `hasattr(p, "edad")`. También vale `getattr(p, "edad", None)`, que devuelve `None` si no existe.
