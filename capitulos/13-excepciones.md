---
title: Excepciones
subtitle: Tener un plan B cuando algo sale mal
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Vas a coger el metro y la estación está cerrada por obras. No te quedas paralizado en la puerta: coges el autobús. Tenías un plan B, aunque no lo hubieras pensado en voz alta.

## La pregunta

Hay errores que no son culpa del programa: el usuario escribe «doce» donde esperábamos un número, o un dato vale 0 y toca dividir entre él. Hasta ahora el programa se paraba de golpe. ¿Cómo le damos un plan B?

## La idea

Cuando algo falla durante la ejecución, Python **lanza una excepción**: un aviso con un tipo y un mensaje. Si nadie la atiende, el programa se detiene. Con `try` y `except` la atendemos:

```python
try:
    # lo que puede fallar
except ValueError:
    # el plan B si falla con ese tipo de error
```

:::{important} Cómo funciona `try` / `except`
1. Se ejecuta el bloque `try` línea a línea.
2. Si una línea lanza una excepción, **el resto del `try` se abandona**: esas líneas ya no se ejecutan.
3. Python busca, en orden, el primer `except` cuyo tipo encaje con el error, y ejecuta su bloque.
4. Si ninguno encaja, el error sigue hacia arriba, y si nadie lo atiende, el programa se detiene.
:::

Las excepciones más frecuentes:

| Excepción | Cuándo ocurre | Ejemplo |
|---|---|---|
| `ValueError` | el valor no sirve, aunque el tipo sea correcto | `int("doce")` |
| `ZeroDivisionError` | dividir entre 0 | `5 / 0` |
| `TypeError` | operar con tipos que no encajan | `"5" + 3` |
| `IndexError` | posición que no existe en una lista | `[1, 2][5]` |
| `KeyError` | clave que no existe en un diccionario | `{"a": 1}["b"]` |
| `NameError` | variable que no existe | `print(x)` sin haber creado `x` |

## Construcción

### 1 · El texto que no es un número

:::{tip} Predice
¿Se ejecutará la línea 4? ¿Qué valor acabará teniendo `doble`?
:::

```{code-cell} python
texto = "doce"
try:
    numero = int(texto)
    doble = numero * 2
except ValueError:
    doble = 0
    print("No es un número")
print(doble)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El texto que no es un número","etiqueta":"try · except","idea":"int('doce') lanza un ValueError. El resto del try se abandona: la línea 4 no se ejecuta nunca. Python salta al except, que encaja con ese tipo de error.","columnas":["texto","numero","doble"],"fila_en":"cada_linea"},"traza":{"codigo":"texto = \"doce\"\ntry:\n    numero = int(texto)\n    doble = numero * 2\nexcept ValueError:\n    doble = 0\n    print(\"No es un número\")\nprint(doble)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"texto":"doce"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"texto":"'doce'"},"tipos":{"texto":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"texto":"doce"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"texto":"'doce'"},"tipos":{"texto":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"doce"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{"texto":"'doce'"},"tipos":{"texto":"str"},"pila":[],"devuelve":null,"excepcion":"ValueError: invalid literal for int() with base 10: 'doce'"},{"linea":5,"estado":{"texto":"doce"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{"texto":"'doce'"},"tipos":{"texto":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"texto":"doce","doble":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"texto":"'doce'","doble":"0"},"tipos":{"texto":"str","doble":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"texto":"doce","doble":0},"salida":"No es un número\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"texto":"'doce'","doble":"0"},"tipos":{"texto":"str","doble":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{"texto":"doce","doble":0},"salida":"No es un número\n0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"texto":"'doce'","doble":"0"},"tipos":{"texto":"str","doble":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["1","'doce'","—","—"],["2","'doce'","—","—"],["3","'doce'","—","—"],["5","'doce'","—","—"],["6","'doce'","—","0"],["7","'doce'","—","0"],["8","'doce'","—","0"]]}}
```

Mira la columna **Línea** de la tabla de traza: después de la 3 viene la 5. La línea 4 se ha saltado, y `numero` no llega a existir.

### 2 · Seguir adelante dentro de un bucle

:::{tip} Predice
Uno de los datos es 0. ¿Se detendrá el bucle al llegar a él?
:::

```{code-cell} python
datos = [10, 0, 5]
resultados = []
for d in datos:
    try:
        resultados.append(100 // d)
    except ZeroDivisionError:
        resultados.append(None)
print(resultados)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Seguir adelante dentro de un bucle","etiqueta":"except · bucle","idea":"Con d = 0, la división lanza ZeroDivisionError. El except apunta None y el bucle sigue con el siguiente dato: el error de un dato no tumba todo el programa.","lista":"datos","cabecera":3,"puntero":"d","foco":"vuelta","columnas":["d","resultados"],"fila_en":"fin_iteracion"},"traza":{"codigo":"datos = [10, 0, 5]\nresultados = []\nfor d in datos:\n    try:\n        resultados.append(100 // d)\n    except ZeroDivisionError:\n        resultados.append(None)\nprint(resultados)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"datos":[10,0,5]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"datos":"[10, 0, 5]"},"tipos":{"datos":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"datos":[10,0,5],"resultados":[]},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[]"},"tipos":{"datos":"list","resultados":"list"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[10,0,5],"resultados":[],"d":10},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[]","d":"10"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"datos":[10,0,5],"resultados":[],"d":10},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[]","d":"10"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"datos":[10,0,5],"resultados":[10],"d":10},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[10]","d":"10"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[10,0,5],"resultados":[10],"d":0},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"datos":"[10, 0, 5]","resultados":"[10]","d":"0"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"datos":[10,0,5],"resultados":[10],"d":0},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[10]","d":"0"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"datos":[10,0,5],"resultados":[10],"d":0},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[10]","d":"0"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":"ZeroDivisionError: integer division or modulo by zero"},{"linea":6,"estado":{"datos":[10,0,5],"resultados":[10],"d":0},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[10]","d":"0"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"datos":[10,0,5],"resultados":[10,null],"d":0},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[10, None]","d":"0"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[10,0,5],"resultados":[10,null],"d":5},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"datos":"[10, 0, 5]","resultados":"[10, None]","d":"5"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"datos":[10,0,5],"resultados":[10,null],"d":5},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[10, None]","d":"5"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"datos":[10,0,5],"resultados":[10,null,20],"d":5},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[10, None, 20]","d":"5"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"datos":[10,0,5],"resultados":[10,null,20],"d":5},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":2,"repr":{"datos":"[10, 0, 5]","resultados":"[10, None, 20]","d":"5"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{"datos":[10,0,5],"resultados":[10,null,20],"d":5},"salida":"[10, None, 20]\n","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"datos":"[10, 0, 5]","resultados":"[10, None, 20]","d":"5"},"tipos":{"datos":"list","resultados":"list","d":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["10","[10]"],["0","[10, None]"],["5","[10, None, 20]"]]}}
```

### 3 · Lanzar tus propias excepciones

Una función también puede **lanzar** una excepción con `raise`, cuando recibe algo con lo que no puede trabajar. La excepción **se propaga**: sale de la función y la atiende quien la llamó.

:::{tip} Predice
¿Llega a ejecutarse el `return` de la función? ¿Qué valor tendrá `r` al final?
:::

```{code-cell} python
def raiz(x):
    if x < 0:
        raise ValueError("número negativo")
    return x ** 0.5

try:
    r = raiz(-4)
except ValueError as e:
    r = None
    print("Error:", e)
print(r)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Lanzar tus propias excepciones","etiqueta":"raise · propagación","idea":"raise lanza un ValueError dentro de raiz. La función se interrumpe sin llegar al return, su marco desaparece y el error sale hacia fuera, donde lo atiende el except.","columnas":["x","e","r"],"fila_en":"cada_linea"},"traza":{"codigo":"def raiz(x):\n    if x < 0:\n        raise ValueError(\"número negativo\")\n    return x ** 0.5\n\ntry:\n    r = raiz(-4)\nexcept ValueError as e:\n    r = None\n    print(\"Error:\", e)\nprint(r)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{},"tipos":{},"pila":[{"nombre":"raiz","args":["x"],"vars":{"x":-4},"repr":{"x":"-4"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":{"expr":"x < 0","sust":"-4 < 0","valor":true},"vuelta":0,"fila":1,"repr":{},"tipos":{},"pila":[{"nombre":"raiz","args":["x"],"vars":{"x":-4},"repr":{"x":"-4"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{},"tipos":{},"pila":[{"nombre":"raiz","args":["x"],"vars":{"x":-4},"repr":{"x":"-4"}}],"devuelve":null,"excepcion":"ValueError: número negativo"},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{},"tipos":{},"pila":[],"devuelve":{"funcion":"raiz","valor":"None","error":true},"excepcion":null},{"linea":8,"estado":{"e":{"__exc__":"ValueError('número negativo')"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{"e":"ValueError('número negativo')"},"tipos":{"e":"ValueError"},"pila":[],"devuelve":null,"excepcion":null},{"linea":9,"estado":{"e":{"__exc__":"ValueError('número negativo')"},"r":null},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{"e":"ValueError('número negativo')","r":"None"},"tipos":{"e":"ValueError","r":"NoneType"},"pila":[],"devuelve":null,"excepcion":null},{"linea":10,"estado":{"r":null},"salida":"Error: número negativo\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{"r":"None"},"tipos":{"r":"NoneType"},"pila":[],"devuelve":null,"excepcion":null},{"linea":11,"estado":{"r":null},"salida":"Error: número negativo\nNone\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":7,"repr":{"r":"None"},"tipos":{"r":"NoneType"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["7","-4","—","—"],["2","-4","—","—"],["3","-4","—","—"],["3 ↩","—","—","—"],["8","—","ValueError('número negativo')","—"],["9","—","ValueError('número negativo')","None"],["10","—","—","None"],["11","—","—","None"]]}}
```

Con `except ValueError as e`, la variable `e` guarda el **objeto excepción**, y su mensaje se puede imprimir. Su atributo `e.args` es la tupla con los argumentos con los que se creó: aquí, `('número negativo',)`.

### 4 · `else`, `finally` y el orden de los `except`

Un `try` completo puede tener cuatro partes:

```{code-cell} python
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    else:
        print("Resultado:", resultado)    # solo si NO hubo error
    finally:
        print("Fin del intento")          # SIEMPRE, haya error o no

dividir(10, 2)
dividir(10, 0)
```

| Parte | Cuándo se ejecuta |
|---|---|
| `try` | siempre, hasta la primera línea que falle |
| `except` | solo si hubo un error de ese tipo |
| `else` | solo si **no** hubo ningún error |
| `finally` | **siempre**, al final, haya error o no |

:::{warning} Trampa · el orden de los `except`
Las excepciones forman una **jerarquía**: `ZeroDivisionError` es un tipo de `ArithmeticError`, que es un tipo de `Exception`. Un `except` atiende su tipo **y todos los que cuelgan de él**. Por eso el más general va el último: si pones `except Exception:` primero, atrapa todos los errores y los `except` concretos de debajo no se ejecutan nunca. Es el mismo error de orden que en los `if`/`elif`.
:::

### 5 · Tus propias clases de excepción

Puedes crear tus propios tipos de error heredando de `Exception` (las clases y la herencia, en el capítulo siguiente):

```{code-cell} python
class NotaInvalida(Exception):
    pass

def comprobar(nota):
    if not 0 <= nota <= 10:
        raise NotaInvalida(f"{nota} no está entre 0 y 10")
    return nota

try:
    comprobar(12)
except NotaInvalida as e:
    print("Error:", e)
```

## Conexiones

- `try`/`except` es un condicional especial: en lugar de preguntar antes, se intenta y se reacciona si falla. En Python se dice que es mejor pedir perdón que pedir permiso.
- Las excepciones atraviesan la pila de marcos del capítulo de funciones: suben de marco en marco hasta que alguien las atiende.

## La grieta

`NotaInvalida` hereda de `Exception`. ¿Qué es exactamente una clase, y qué significa heredar? Es la puerta de la programación orientada a objetos, el bloque con más peso del PCAP.

## Preguntas tipo examen

Preguntas como las del examen PCEP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","capitulo":"13","titulo":"Preguntas tipo examen","etiqueta":"PCEP"}}
```

Y estas, como las del examen PCAP, que va más a fondo:

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcap","capitulo":"13","titulo":"Preguntas tipo examen","etiqueta":"PCAP"}}
```

## Ejercicios

1. **¿Qué imprime?**

   ```python
   try:
       print("A")
       x = [1, 2, 3][5]
       print("B")
   except IndexError:
       print("C")
   print("D")
   ```

2. **Pedir un número.** Escribe un programa que convierta `texto = "3,5"` a `float` y, si falla, imprima «Usa punto decimal».
3. **El orden.** ¿Qué imprime este programa? ¿Cómo lo arreglarías?

   ```python
   try:
       10 / 0
   except Exception:
       print("Algo ha fallado")
   except ZeroDivisionError:
       print("División entre 0")
   ```

El solucionario está al final del capítulo.

## Solucionario

1. Imprime **A**, **C** y **D**. La línea de `[5]` lanza `IndexError`, así que `B` no se imprime; el `except` imprime `C`, y después el programa sigue con `D`.
2. Una solución:

   ```python
   texto = "3,5"
   try:
       numero = float(texto)
   except ValueError:
       print("Usa punto decimal")
   ```

   `float("3,5")` da `ValueError`: Python espera un punto, como en `"3.5"`.
3. Imprime **Algo ha fallado**: `ZeroDivisionError` cuelga de `Exception`, así que el primer `except` lo atrapa y el segundo nunca se ejecuta. Se arregla poniendo primero `except ZeroDivisionError:` y después el general.
