---
title: Probar, depurar y trabajar en equipo
subtitle: Saber que el programa funciona, y no programar solo
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Un puente no se inaugura porque el ingeniero «cree» que aguanta: se le pasan camiones cargados y se miden las flechas. Un programa tampoco funciona porque lo parezca. Funciona cuando lo has comprobado, y lo sigues comprobando cada vez que lo cambias.

## La pregunta

¿Cómo se comprueba que un programa hace lo que debe? Cuando falla, ¿cómo se encuentra el porqué? ¿Y cómo trabajan varias personas, y ahora también asistentes de IA, sobre el mismo código sin pisarse?

## La idea

Hay tres clases de errores, y cada una se descubre de una manera:

| Error | Cuándo aparece | Ejemplo | Cómo se descubre |
|---|---|---|---|
| **de sintaxis** | antes de ejecutar nada | `print("hola"` sin cerrar | Python se niega a empezar: `SyntaxError` |
| **de ejecución** | al llegar a la línea | `int("doce")`, `10 / 0` | se lanza una excepción y sale un traceback |
| **de lógica** | nunca avisa | `media = suma / 2` cuando había 3 notas | solo con **pruebas**: el resultado no es el esperado |

Los errores de lógica son los peligrosos, porque el programa no se queja. Para cazarlos se escriben **pruebas**: casos con una entrada conocida y su **resultado esperado**, que se comparan con el **resultado real**.

## Construcción

### 1 · `assert`: una comprobación en una línea

`assert condición, "mensaje"` no hace nada si la condición se cumple. Si no se cumple, lanza `AssertionError` con ese mensaje. Sirve para comprobar resultados y para vigilar condiciones que **siempre** deberían ser ciertas, los invariantes.

:::{tip} Predice
La primera llamada va bien. ¿Qué pasa en la segunda? ¿Llega a ejecutarse el `return`?
:::

```{code-cell} python
def media(notas):
    assert len(notas) > 0, "la lista está vacía"
    return sum(notas) / len(notas)

print(media([6, 8]))
print(media([]))
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Un assert que salta","etiqueta":"assert · traceback","idea":"Con [6, 8] el assert se cumple y no hace nada. Con [] es False: lanza AssertionError, la función se interrumpe sin llegar a dividir entre cero, nadie atiende el error y el programa se detiene con un traceback.","columnas":["notas"],"fila_en":"cada_linea"},"traza":{"codigo":"def media(notas):\n    assert len(notas) > 0, \"la lista está vacía\"\n    return sum(notas) / len(notas)\n\nprint(media([6, 8]))\nprint(media([]))","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":["notas"],"vars":{"notas":[6,8]},"repr":{"notas":"[6, 8]"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":["notas"],"vars":{"notas":[6,8]},"repr":{"notas":"[6, 8]"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":2,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":["notas"],"vars":{"notas":[6,8]},"repr":{"notas":"[6, 8]"}}],"devuelve":null,"excepcion":null},{"linea":3,"estado":{},"salida":"7.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":3,"repr":{},"tipos":{},"pila":[],"devuelve":{"funcion":"media","valor":"7.0","error":false},"excepcion":null},{"linea":6,"estado":{},"salida":"7.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":4,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":["notas"],"vars":{"notas":[]},"repr":{"notas":"[]"}}],"devuelve":null,"excepcion":null},{"linea":2,"estado":{},"salida":"7.0\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":5,"repr":{},"tipos":{},"pila":[{"nombre":"media","args":["notas"],"vars":{"notas":[]},"repr":{"notas":"[]"}}],"devuelve":null,"excepcion":"AssertionError: la lista está vacía"},{"linea":2,"estado":{},"salida":"7.0\nTraceback (most recent call last):\n  File \"programa.py\", line 6, in <module>\n    print(media([]))\n          ~~~~~^^^^\n  File \"programa.py\", line 2, in media\n    assert len(notas) > 0, \"la lista está vacía\"\n           ^^^^^^^^^^^^^^\nAssertionError: la lista está vacía\n","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":6,"repr":{},"tipos":{},"pila":[],"devuelve":{"funcion":"media","valor":"None","error":true},"excepcion":null}],"filas":[["5","[6, 8]"],["2","[6, 8]"],["3","[6, 8]"],["3 ↩","—"],["6","[]"],["2","[]"],["2 ↩","—"]]}}
```

Sin el `assert`, la segunda llamada también fallaría, pero con un `ZeroDivisionError` que no explica el problema. El `assert` falla antes y dice qué ha pasado.

### 2 · Leer un traceback

El traceback que acaba de aparecer en la pantalla del visualizador se lee **de abajo arriba**:

```text
Traceback (most recent call last):
  File "programa.py", line 6, in <module>
    print(media([]))
  File "programa.py", line 2, in media
    assert len(notas) > 0, "la lista está vacía"
AssertionError: la lista está vacía
```

1. **La última línea** dice qué ha pasado: el tipo de error y su mensaje.
2. **Justo encima**, dónde ha saltado: el fichero, la línea 2, dentro de la función `media`.
3. **Más arriba**, cómo se llegó hasta ahí: la línea 6, en el programa principal (`<module>`), llamó a `media`.

Es la pila de marcos que has visto en los visualizadores, escrita en texto, con la llamada más reciente abajo.

### 3 · Pruebas unitarias con `unittest`

Una **prueba unitaria** comprueba una sola pieza, normalmente una función. Un **caso de prueba** es una clase con varias pruebas, y una **batería** (*test suite*) agrupa muchas. Python trae el módulo `unittest`:

```{code-cell} python
import unittest

def media(notas):
    if len(notas) == 0:
        raise ValueError("la lista está vacía")
    return sum(notas) / len(notas)

class PruebasMedia(unittest.TestCase):
    def test_caso_tipico(self):
        self.assertEqual(media([6, 8]), 7)

    def test_un_solo_valor(self):            # caso límite
        self.assertEqual(media([5]), 5)

    def test_decimales(self):
        self.assertAlmostEqual(media([1, 2, 2]), 5 / 3)

    def test_lista_vacia(self):              # entrada no válida
        with self.assertRaises(ValueError):
            media([])

unittest.main(argv=["ignorado"], exit=False, verbosity=2)
```

Cada método que empieza por `test_` es una prueba. Al ejecutar, cada una sale como `ok`, `FAIL` (el resultado no es el esperado) o `ERROR` (ha saltado una excepción imprevista).

:::{important} Cómo elegir los casos
Para cada función, al menos:
- un **caso típico**, el uso normal;
- los **casos límite**: lista vacía, un solo elemento, el 0, el valor más grande permitido;
- las **entradas no válidas**: qué debe pasar si llega algo imposible.

Las pruebas deben ser **repetibles** (dan lo mismo cada vez) y **aisladas** (una no depende de otra). Y se vuelven a ejecutar después de cada cambio: así se cazan las **regresiones**, lo que funcionaba y se ha roto al tocar otra cosa.
:::

En proyectos de verdad, las pruebas van en ficheros aparte y se ejecutan desde la terminal con `python -m unittest`. Muchos proyectos usan también `pytest`, que se instala con `pip` y permite escribir las pruebas con `assert` a secas.

### 4 · Depurar: encontrar el porqué

Cuando una prueba falla, hay que encontrar la causa. Las herramientas, de la más sencilla a la más potente:

1. **Leer el traceback** entero, de abajo arriba.
2. **Salida de diagnóstico**: un `print` provisional que enseñe el valor de las variables en el punto sospechoso. Con `print(f"{total=}")` sale el nombre y el valor.
3. **Seguir el programa paso a paso** y **hacer una traza**: exactamente lo que hacen los visualizadores de este libro, y lo que aprendiste a hacer a mano en el capítulo [Trazas](03-trazas.md).
4. **Un depurador**: la función `breakpoint()` detiene el programa en esa línea y deja inspeccionar las variables y avanzar línea a línea. Los editores como VS Code o Thonny tienen el suyo, con botones.

Y al final, **comprobar el arreglo con una prueba**: si escribes primero la prueba que reproduce el fallo, sabrás con certeza cuándo está resuelto, y ese fallo ya no volverá sin que te enteres.

### 5 · Trabajar en equipo: repositorios, ramas y revisiones

Cuando varias personas tocan el mismo código, hace falta un sistema que guarde el historial y permita trabajar en paralelo. El más usado es **Git**, normalmente con un repositorio compartido en GitHub o GitLab.

| Concepto | Qué es |
|---|---|
| **repositorio** | el proyecto con todo su historial |
| **commit** | una foto del proyecto con un mensaje que explica el cambio: «Añade el cálculo de la media», no «cambios» |
| **rama** (*branch*) | una línea de trabajo paralela: cada mejora se hace en su rama, sin tocar la principal |
| **pull request** (o *merge request*) | la petición de unir una rama a la principal; es donde se revisa |
| **revisión de código** (*code review*) | otra persona lee el cambio, pregunta y sugiere antes de aceptarlo |
| **conflicto** (*merge conflict*) | dos ramas cambiaron las mismas líneas y Git no sabe cuál vale: decide una persona |
| **issue** | una entrada para apuntar un fallo, una tarea o una decisión |
| **integración continua** (CI) | un servicio que, en cada cambio, ejecuta las pruebas automáticamente |

```text
git switch -c media-ponderada        # crea una rama y se cambia a ella
git add notas.py                     # prepara el cambio
git commit -m "Añade la media ponderada"
git push                             # lo sube al repositorio compartido
                                     # … y en GitHub se abre el pull request
```

Los conflictos se evitan con ramas pequeñas que duran poco, uniendo los cambios a menudo y hablando con el equipo de quién toca qué. Al revisar, se comenta el código, no a la persona; al recibir comentarios, se responde a cada uno, se arregla o se explica por qué no.

:::{note} Este libro es un ejemplo
Este libro vive en un repositorio de GitHub. Cada vez que se sube un cambio, un sistema de integración continua vuelve a generar las trazas de todos los visualizadores, construye el libro y, solo si todo sale bien, lo publica. Si algo se rompe, el cambio no llega a la web. Así, el resultado de las pruebas decide si un cambio se une o no.
:::

### 6 · Programar con ayuda de la IA

Los asistentes de IA pueden redactar, explicar, completar, reorganizar (*refactorizar*), documentar y probar código. Bien usados, aceleran mucho. Las reglas para usarlos bien:

**Pedir bien.** Cuanto más claro el encargo, mejor la respuesta:
- los **requisitos**: qué debe hacer y qué no;
- el **contexto**: versión de Python, qué código ya existe, para quién es;
- **ejemplos** de entradas y salidas esperadas;
- las **restricciones**: «sin librerías externas», «que lo entienda un alumno de bachillerato».

Si la respuesta no convence, se afina la petición o se piden alternativas y se comparan.

**Validar siempre, y de forma independiente.** El código generado puede parecer perfecto y estar mal. Antes de usarlo:
- **léelo y entiéndelo**: la persona revisa y aprueba, y sigue siendo la responsable del resultado;
- **ejecútalo y pruébalo** con tus propios casos, típicos y límite;
- comprueba que los **módulos, funciones y APIs que usa existen de verdad**: a veces los asistentes inventan nombres verosímiles;
- revisa que sea **legible, mantenible y seguro**, y que se pueda usar legalmente.

**Proteger los datos.** No pegues en un asistente contraseñas, claves de API, datos personales de nadie ni código que no puedas compartir. Si hace falta un ejemplo, usa datos inventados.

## Conexiones

- Las trazas del bloque 0, las excepciones y los marcos de función se juntan aquí: depurar es hacer una traza con un propósito.
- Una prueba es una especificación que se ejecuta: es el «qué debe hacer» del capítulo [Especificación](01-especificacion.md), convertido en código.
- Validar lo que propone una IA es lo mismo que validar lo que escribe un compañero: leer, probar y preguntar.

## La grieta

Con esto se cierra el temario del PCAP. El siguiente paso ya no es aprender piezas sueltas, sino construir: un proyecto propio, con sus módulos, sus clases, sus ficheros y sus pruebas, en un repositorio de verdad.

## Ejercicios

1. **Clasifica el error.** Di si es de sintaxis, de ejecución o de lógica:
   a) `if x > 3 print(x)`; b) `lista[10]` con una lista de 3 elementos; c) calcular el área de un círculo con `3.14 * r * 2`.
2. **Lee el traceback.** ¿En qué línea y en qué función se produjo el error? ¿Qué error fue?

   ```text
   Traceback (most recent call last):
     File "tienda.py", line 12, in <module>
       total = precio_final(20, "10")
     File "tienda.py", line 4, in precio_final
       return precio - precio * descuento / 100
   TypeError: unsupported operand type(s) for /: 'str' and 'int'
   ```

3. **Diseña los casos.** Escribe tres `assert` para una función `es_par(n)`: un caso típico, un caso límite y un número negativo.
4. **Una prueba con `unittest`.** Escribe un `TestCase` para la función `es_codigo_postal(s)` del capítulo anterior con un caso válido, uno con letras y uno demasiado corto.
5. **Revisa a la IA.** Un asistente propone `import statistics` y `statistics.average(datos)` para calcular una media. ¿Cómo comprobarías si es correcto antes de usarlo?

El solucionario está al final del capítulo.

## Solucionario

1. a) **Sintaxis**: falta `:` después de la condición. b) **Ejecución**: `IndexError` al llegar a esa línea. c) **Lógica**: el programa funciona, pero la fórmula es la del perímetro mal escrita; el área es `3.14 * r ** 2`.
2. En la **línea 4**, dentro de **`precio_final`**, y fue un **`TypeError`**. La línea 12 llamó a la función con `descuento = "10"`, una cadena: `precio * "10"` no da error, sino que repite la cadena 20 veces, y al dividir esa cadena entre 100 salta el error. El fallo real está en la llamada, que debería pasar el número `10`.
3. Por ejemplo:

   ```python
   assert es_par(8) == True
   assert es_par(0) == True
   assert es_par(-3) == False
   ```

4. Una solución:

   ```python
   import unittest

   def es_codigo_postal(s):
       return len(s) == 5 and s.isdigit()

   class PruebasCodigoPostal(unittest.TestCase):
       def test_valido(self):
           self.assertTrue(es_codigo_postal("08029"))

       def test_con_letras(self):
           self.assertFalse(es_codigo_postal("08A29"))

       def test_corto(self):
           self.assertFalse(es_codigo_postal("0802"))

   unittest.main(argv=["ignorado"], exit=False)
   ```

5. Comprobando que la función existe: en la documentación oficial del módulo `statistics`, o ejecutando `"average" in dir(statistics)`, que da `False`. La función correcta es `statistics.mean`. Y después, probándola con un caso conocido: `statistics.mean([6, 8])` debe dar `7`.
