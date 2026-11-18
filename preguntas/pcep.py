"""Banco de preguntas tipo examen PCEP (temario PCEP-30-03).

Cada pregunta es un P(...). Campos:
  id      identificador único
  cap     capítulo del libro donde aparece (prefijo del fichero: "22", "05"…)
  sec     sección del temario PCEP (1 a 5)
  q       enunciado (admite `código` y **negrita**)
  ops     opciones de respuesta
  ok      índice de la correcta (o lista de índices si hay varias)
  exp     explicación que se muestra al corregir
  code    (opcional) programa de la pregunta
  v       (opcional) cómo se comprueba al ejecutar el código:
            "salida"       lo impreso coincide con la opción correcta
            "error"        el programa lanza la excepción `err`
            "valor:expr"   repr(expr) al terminar coincide con la opción correcta
  mono    (opcional) opciones en letra de código
  entradas (opcional) lo que se teclea en cada input()

herramientas/preguntas.py ejecuta cada pregunta con código, comprueba que la
respuesta marcada como correcta es la que da Python y que ninguna otra opción
lo es, genera la ejecución paso a paso y coloca las preguntas en el libro.
Todas las preguntas son originales.
"""

SECCIONES = {
    "1": "Fundamentos de programación y de Python",
    "2": "Control de flujo: condicionales y bucles",
    "3": "Colecciones de datos",
    "4": "Funciones y excepciones",
    "5": "Ficheros y módulos",
}
REPARTO = {"1": 6, "2": 8, "3": 9, "4": 7, "5": 5}     # 35 preguntas, como el examen

PREGUNTAS = []


def P(id, cap, sec, q, ops, ok, exp, code=None, v=None, err=None, mono=None, entradas=()):
    PREGUNTAS.append(dict(id=id, cap=cap, sec=str(sec), q=q, ops=ops, ok=ok, exp=exp, code=code,
                          v=v, err=err, mono=mono, entradas=list(entradas)))


# ---------------------------------------------------------------- sección 1
P("21-1", "21", 1, "¿Qué hace un **intérprete**?",
  ["Traduce y ejecuta el programa instrucción a instrucción",
   "Traduce todo el programa a un ejecutable antes de ponerlo en marcha",
   "Revisa la ortografía de los comentarios",
   "Convierte el código Python en código C para que sea más rápido"], 0,
  "El intérprete traduce y ejecuta cada instrucción en el momento. El que traduce todo antes es el compilador.")
P("21-2", "21", 1, "La línea `print(\"hola\"` (sin cerrar el paréntesis) contiene un error…",
  ["léxico", "sintáctico", "semántico", "de lógica"], 1,
  "Todas las «palabras» existen, pero la frase está mal construida: es un error de **sintaxis**. Python lo detecta antes de ejecutar nada.")
P("21-3", "21", 1, "¿Qué imprime este programa?", ["64", "512", "36", "9"], 1,
  "La potencia se agrupa por la derecha: `2 ** 3 ** 2` es `2 ** (3 ** 2)`, es decir, `2 ** 9 = 512`.",
  code="print(2 ** 3 ** 2)", v="salida", mono=True)
P("21-4", "21", 1, "¿Qué imprime este programa?", ["4", "-4", "0.25", "Lanza un error"], 1,
  "El `-` unario tiene menos prioridad que `**`: `-2 ** 2` es `-(2 ** 2)`, que da `-4`.",
  code="print(-2 ** 2)", v="salida")
P("21-5", "21", 1, "¿Qué imprime este programa?", ["9", "12.25", "12", "6"], 0,
  "`x //= 2` deja `x = 7 // 2 = 3`, y `x **= 2` lo eleva al cuadrado: 9.",
  code="x = 7\nx //= 2\nx **= 2\nprint(x)", v="salida")
P("21-6", "21", 1, "¿Cuál **no** es un nombre de variable válido?", ["_total", "nota2", "2nota", "Nota"], 2,
  "Un nombre no puede empezar por un dígito. `_total`, `nota2` y `Nota` son válidos (y `Nota` es distinta de `nota`).", mono=True)
P("21-7", "21", 1, "El usuario teclea `4`. ¿Qué imprime el programa?", ["8", "44", "4 4", "Lanza un error"], 1,
  "`input()` siempre devuelve texto: `a` vale `'4'`, y multiplicar una cadena por 2 la repite: `'44'`.",
  code="a = input()\nprint(a * 2)", v="salida", entradas=["4"])
P("21-8", "21", 1, "¿Qué imprime este programa?", ["abcd", "a b c\nd", "ab\ncd", "a bc d"], 0,
  "Con `sep=\"\"` no se pone nada entre `a` y `b`, y con `end=\"c\"` se escribe `c` en lugar del salto de línea. El segundo `print` sigue en la misma línea.",
  code='print("a", "b", sep="", end="c")\nprint("d")', v="salida", mono=True)

P("04-1", "04", 1, "¿Qué imprime este programa?", ["5 3", "5 5", "3 3", "3 5"], 0,
  "`b = a` hace que `b` valga 3. Después `a` pasa a valer 5, pero eso no cambia `b`: un número no se modifica, se sustituye.",
  code="a = 3\nb = a\na = 5\nprint(a, b)", v="salida")
P("04-2", "04", 1, "¿Qué imprime este programa?", ["2 1", "2 2", "1 1", "1 2"], 1,
  "Es el intercambio que falla: `a = b` pierde el 1, y `b = a` copia el 2 que ya tiene `a`.",
  code="a, b = 1, 2\na = b\nb = a\nprint(a, b)", v="salida")
P("04-3", "04", 1, "¿Qué imprime este programa?", ["22", "21", "20", "11"], 0,
  "Primero `x` pasa de 10 a 11, y después se duplica: 22. Cada asignación usa el valor que tenía `x` en ese momento.",
  code="x = 10\nx = x + 1\nx = x * 2\nprint(x)", v="salida")
P("04-4", "04", 1, "Después de `x = 5`, ¿qué describe mejor a `x`?",
  ["Un nombre (una etiqueta) que apunta al valor 5",
   "Una caja con una copia del 5 que nadie más puede usar",
   "Una constante que ya no puede cambiar",
   "Una función que devuelve 5"], 0,
  "Una variable es un nombre que apunta a un valor. Se puede cambiar a qué apunta con otra asignación.")

P("05-1", "05", 1, "¿Qué imprime este programa?", ["<class 'int'>", "<class 'float'>", "<class 'str'>", "1"], 1,
  "La división `/` siempre da un `float`, aunque sea exacta: `7 / 7` es `1.0`.",
  code="print(type(7 / 7))", v="salida", mono=True)
P("05-2", "05", 1, "¿Qué imprime este programa?", ["3 1 3.5", "3.5 1 3", "3 1 3", "4 1 3.5"], 0,
  "`//` da el cociente entero (3), `%` el resto (1) y `/` la división con decimales (3.5).",
  code="print(7 // 2, 7 % 2, 7 / 2)", v="salida")
P("05-3", "05", 1, "¿Qué imprime este programa?", ["8", "53", "'53'", "Lanza un error"], 1,
  "Las dos son cadenas: `+` las **junta**. `print` escribe el texto sin comillas.",
  code='print("5" + "3")', v="salida")
P("05-4", "05", 1, "¿Qué ocurre al ejecutar este programa?", ["Imprime 53", "Imprime 8", "Lanza TypeError", "Lanza ValueError"], 2,
  "No se puede sumar una cadena y un número: Python no adivina si quieres juntar o sumar, y lanza `TypeError`.",
  code='print("5" + 3)', v="error", err="TypeError")
P("05-5", "05", 1, "¿Qué imprime este programa?", ["15", "15.9", "16", "Lanza un error"], 0,
  "`int(\"12\")` convierte el texto en 12, e `int(3.9)` **quita** los decimales (no redondea): 3. Total, 15.",
  code='print(int("12") + int(3.9))', v="salida")
P("05-6", "05", 1, "¿Qué imprime este programa?", ["True", "False", "Lanza un error", "None"], 0,
  "`10 > 3` es `True`; `2 > 5` es `False`, y `not False` es `True`. `True and True` da `True`.",
  code="print(10 > 3 and not 2 > 5)", v="salida")

# ---------------------------------------------------------------- sección 2
P("06-1", "06", 2, "¿Qué imprime este programa?", ["A", "A\nB", "B", "C"], 0,
  "La primera condición que se cumple gana: `7 > 5` es `True`, se imprime `A` y las demás ramas ya no se miran.",
  code='n = 7\nif n > 5:\n    print("A")\nelif n > 3:\n    print("B")\nelse:\n    print("C")', v="salida", mono=True)
P("06-2", "06", 2, "¿Qué imprime este programa?", ["B", "C", "B\nC", "A\nB"], 0,
  "Son dos `if` **independientes**. El primero no se cumple y no tiene `else`; el segundo se cumple e imprime `B`.",
  code='n = 4\nif n > 5:\n    print("A")\nif n > 3:\n    print("B")\nelse:\n    print("C")', v="salida", mono=True)
P("06-3", "06", 2, "¿Qué imprime este programa?", ["aprobado", "sobresaliente", "aprobado\nsobresaliente", "No imprime nada"], 0,
  "Las ramas están mal ordenadas: `9 >= 5` ya se cumple, así que la rama de sobresaliente es **inalcanzable** para cualquier nota.",
  code='nota = 9\nif nota >= 5:\n    print("aprobado")\nelif nota >= 9:\n    print("sobresaliente")', v="salida", mono=True)
P("06-4", "06", 2, "¿Qué imprime este programa?", ["sí", "no", "Lanza un error", "No imprime nada"], 1,
  "Como condición, el número 0 cuenta como falso (y cualquier otro número, como verdadero).",
  code='x = 0\nif x:\n    print("sí")\nelse:\n    print("no")', v="salida")
P("06-5", "06", 2, "¿Qué imprime este programa?", ["X", "Y", "XY", "Lanza un error"], 0,
  "`and` va antes que `or`: primero `b < 5 and a > 7`, que es `False`. Después `a > 3 or False`, que es `True`.",
  code='a = 5\nb = 10\nif a > 3 or b < 5 and a > 7:\n    print("X")\nelse:\n    print("Y")', v="salida")

P("07-1", "07", 2, "¿Qué imprime este programa?", ["[2, 5, 8]", "[2, 5, 8, 11]", "[2, 3, 4, 5, 6, 7, 8, 9]", "[3, 6, 9]"], 0,
  "`range(2, 10, 3)` empieza en 2 y suma 3 mientras no llegue a 10: 2, 5, 8.",
  code="print(list(range(2, 10, 3)))", v="salida", mono=True)
P("07-2", "07", 2, "¿Qué imprime este programa?", ["12", "9", "10", "3"], 0,
  "`n` vale 0, 3, 6, 9 y 12. Con 9 la condición aún se cumple y suma otra vez: el bucle sale con 12.",
  code="n = 0\nwhile n < 10:\n    n += 3\nprint(n)", v="salida")
P("07-3", "07", 2, "¿Qué imprime este programa?", ["10", "15", "4", "9"], 0,
  "`range(1, 5)` da 1, 2, 3 y 4 (el 5 no entra). 1 + 2 + 3 + 4 = 10.",
  code="total = 0\nfor i in range(1, 5):\n    total += i\nprint(total)", v="salida")
P("07-4", "07", 2, "¿Cuál de estos bucles **no termina nunca**?",
  ["i = 0\nwhile i < 3:\n    i += 1", "i = 0\nwhile i < 3:\n    print(i)",
   "for i in range(3):\n    print(i)", "i = 3\nwhile i > 0:\n    i -= 1"], 1,
  "En el segundo, nada cambia `i` dentro del bucle: la condición `i < 3` es verdadera para siempre.", mono=True)
P("07-5", "07", 2, "¿Qué imprime este programa?", ["[5, 3, 1]", "[5, 3, 1, -1]", "[]", "[4, 2, 0]"], 0,
  "Con paso negativo, `range` cuenta hacia atrás desde 5 y se para antes de llegar a 0.",
  code="print(list(range(5, 0, -2)))", v="salida", mono=True)

P("25-1", "25", 2, "¿Qué imprime este programa?", ["13", "024", "01234", "1"], 0,
  "Con los pares, `continue` se salta el `print`. Solo se imprimen 1 y 3, sin separación porque `end=\"\"`.",
  code='for i in range(5):\n    if i % 2 == 0:\n        continue\n    print(i, end="")', v="salida")
P("25-2", "25", 2, "¿Qué imprime este programa?", ["12", "7", "3", "16"], 0,
  "El bucle de dentro da 4 vueltas **por cada una** de las 3 del de fuera: 3 × 4 = 12.",
  code="c = 0\nfor i in range(3):\n    for j in range(4):\n        c += 1\nprint(c)", v="salida")
P("25-3", "25", 2, "¿Qué imprime este programa?", ["0 0\n1 0\n2 0", "0 0", "0 0\n0 1", "0 0\n0 1\n0 2"], 0,
  "`break` solo sale del bucle **de dentro**. El de fuera sigue: en cada vuelta se imprime `j = 0` y se corta en `j = 1`.",
  code="for i in range(3):\n    for j in range(3):\n        if j == 1:\n            break\n        print(i, j)", v="salida", mono=True)
P("25-4", "25", 2, "¿Para qué sirve `pass`?",
  ["Para ocupar el sitio de un bloque que de momento está vacío",
   "Para saltar a la siguiente vuelta del bucle",
   "Para salir del bucle",
   "Para pasar un argumento a una función"], 0,
  "`pass` no hace nada. Existe porque Python no admite un bloque vacío. Saltar una vuelta es `continue`, y salir, `break`.")
P("25-5", "25", 2, "¿Qué imprime este programa?", ["6", "True", "3", "Lanza un error"], 0,
  "El operador morsa `:=` guarda `len(datos)` en `n` (3) y a la vez lo compara con 2. Como se cumple, imprime `3 * 2`.",
  code="datos = [4, 7, 1]\nif (n := len(datos)) > 2:\n    print(n * 2)", v="salida")

P("08-1", "08", 2, "¿Qué imprime este programa?", ["8", "4", "6", "[4, 8, 6]"], 0,
  "Es el campeón provisional: `mayor` empieza con la primera nota y se cambia cada vez que aparece una mayor.",
  code="notas = [4, 8, 6]\nmayor = notas[0]\nfor n in notas:\n    if n > mayor:\n        mayor = n\nprint(mayor)", v="salida")
P("08-4", "08", 2, "¿Qué imprime este programa?", ["slm", "sol", "solluzmar", "s"], 0,
  "En cada vuelta se añade a `res` la primera letra de la palabra, `p[0]`.",
  code='res = ""\nfor p in ["sol", "luz", "mar"]:\n    res += p[0]\nprint(res)', v="salida")

# ---------------------------------------------------------------- sección 3
P("08-2", "08", 3, "¿Qué imprime este programa?", ["5 5", "5 1", "4 5", "Lanza IndexError"], 0,
  "La lista tiene 5 elementos, y el último está en la posición `len(datos) - 1 = 4`, que vale 5.",
  code="datos = [3, 1, 4, 1, 5]\nprint(len(datos), datos[len(datos) - 1])", v="salida")
P("08-3", "08", 3, "¿Qué ocurre al ejecutar este programa?", ["Imprime 3", "Imprime None", "Lanza IndexError", "Lanza KeyError"], 2,
  "Con 3 elementos, las posiciones van de 0 a 2. La posición 3 no existe: `IndexError`.",
  code="datos = [1, 2, 3]\nprint(datos[3])", v="error", err="IndexError")
P("22-1", "22", 3, "¿Qué imprime este programa?", ["3", "4", "1", "Lanza un error"], 1,
  "`b = a` no copia: `a` y `b` son la **misma** lista. Lo que se añade por `b` se ve por `a`.",
  code="a = [1, 2, 3]\nb = a\nb.append(4)\nprint(len(a))", v="salida")
P("22-2", "22", 3, "¿Qué imprime este programa?", ["[1, 2, 3]", "[9, 2, 3]", "[9]", "None"], 0,
  "`a[:]` fabrica una copia: cambiar `b` no toca `a`.",
  code="a = [1, 2, 3]\nb = a[:]\nb[0] = 9\nprint(a)", v="salida", mono=True)
P("22-3", "22", 3, "¿Qué imprime este programa?", ["d ['b', 'd']", "d ['b', 'c', 'd']", "e ['b', 'd']", "c ['b', 'd']"], 0,
  "`x[-2]` es el penúltimo, `'d'`. `x[1:4:2]` va de la posición 1 a la 3, de 2 en 2: `'b'` y `'d'`.",
  code='x = ["a", "b", "c", "d", "e"]\nprint(x[-2], x[1:4:2])', v="salida", mono=True)
P("22-4", "22", 3, "¿Qué imprime este programa?", ["[7, 3, 8]", "[5, 7, 3, 8]", "[7, 5, 3, 8]", "[3, 8]"], 0,
  "`insert(1, 7)` deja `[5, 7, 3, 8]` y `del x[0]` quita el 5.",
  code="x = [5, 3, 8]\nx.insert(1, 7)\ndel x[0]\nprint(x)", v="salida", mono=True)
P("22-5", "22", 3, "¿Qué imprime este programa?", ["[1, 2, 3]", "None", "[3, 1, 2]", "Lanza un error"], 1,
  "`sort()` ordena la lista en su sitio y devuelve `None`. Para obtener una lista ordenada nueva se usa `sorted(x)`.",
  code="x = [3, 1, 2]\ny = x.sort()\nprint(y)", v="salida")
P("22-6", "22", 3, "¿Qué imprime este programa?", ["7", "5", "3", "8"], 0,
  "`m[2][0]` es la fila 2, columna 0: 5. `m[0][1]` es la fila 0, columna 1: 2. Suman 7.",
  code="m = [[1, 2], [3, 4], [5, 6]]\nprint(m[2][0] + m[0][1])", v="salida")
P("22-7", "22", 3, "¿Qué imprime este programa?", ["[[1, 0], [1, 0]]", "[[1, 0], [0, 0]]", "[[1, 1], [0, 0]]", "Lanza un error"], 0,
  "`[[0] * 2] * 2` repite **la misma fila** dos veces: son dos etiquetas de una sola lista. Al cambiar una, cambian las dos.",
  code="t = [[0] * 2] * 2\nt[0][0] = 1\nprint(t)", v="salida", mono=True)

P("23-1", "23", 3, "¿Qué imprime este programa?", ["int", "tuple", "list", "Lanza un error"], 0,
  "`(5)` es solo el número 5 entre paréntesis. Una tupla de un elemento necesita la coma: `(5,)`.",
  code="t = (5)\nprint(type(t).__name__)", v="salida")
P("23-2", "23", 3, "¿Qué ocurre al ejecutar este programa?", ["t pasa a ser (9, 2, 3)", "Lanza TypeError", "Lanza IndexError", "No pasa nada: t sigue igual"], 1,
  "Las tuplas son inmutables: no se puede cambiar ninguna posición.",
  code="t = (1, 2, 3)\nt[0] = 9", v="error", err="TypeError")
P("23-3", "23", 3, "¿Qué imprime este programa?", ["3 2 1", "1 2 3", "3 2 3", "1 2 1"], 0,
  "La tupla se desempaqueta en `a`, `b`, `c`, y `a, c = c, a` intercambia los dos valores en un solo paso.",
  code="a, b, c = (1, 2, 3)\na, c = c, a\nprint(a, b, c)", v="salida")
P("23-4", "23", 3, "¿Qué imprime este programa?", ["3", "5", "2", "Lanza un error"], 0,
  "Un conjunto no guarda repetidos: quedan 1, 2 y 3.",
  code="s = {3, 1, 3, 2, 1}\nprint(len(s))", v="salida")
P("23-5", "23", 3, "¿Qué crea `{}`?", ["Un diccionario vacío", "Un conjunto vacío", "Una tupla vacía", "Una lista vacía"], 0,
  "`{}` es un diccionario vacío. El conjunto vacío se escribe `set()`.")
P("23-6", "23", 3, "¿Qué imprime este programa?", ["[1, 2, 3]", "[1, 2, 2, 3]", "Lanza KeyError", "[1, 2]"], 0,
  "Añadir un 2 que ya está no cambia nada. `discard(5)` no da error aunque el 5 no esté (`remove(5)` sí lo daría).",
  code="s = {1, 2}\ns.add(2)\ns.add(3)\ns.discard(5)\nprint(sorted(s))", v="salida", mono=True)

P("11-1", "11", 3, "¿Qué imprime este programa?", ["3 5", "3 1", "2 5", "4 5"], 0,
  "`d[\"a\"] = 5` cambia el valor de una clave que ya existe, y `d[\"c\"] = 3` añade una nueva: quedan 3 parejas.",
  code='d = {"a": 1, "b": 2}\nd["a"] = 5\nd["c"] = 3\nprint(len(d), d["a"])', v="salida")
P("11-2", "11", 3, "¿Qué ocurre al ejecutar este programa?", ["Imprime None", "Lanza KeyError", "Lanza IndexError", "Imprime 0"], 1,
  "Leer una clave que no existe con corchetes lanza `KeyError`. Con `d.get(\"b\")` se obtendría `None`.",
  code='d = {"a": 1}\nprint(d["b"])', v="error", err="KeyError")
P("11-3", "11", 3, "¿Qué imprime este programa?", ["True False", "True True", "False True", "False False"], 0,
  "`in` con un diccionario mira las **claves**, no los valores: `\"x\"` es una clave, pero `1` es un valor.",
  code='d = {"x": 1, "y": 2}\nprint("x" in d, 1 in d)', v="salida")
P("11-4", "11", 3, "¿Qué imprime este programa?", ["3", "ab", "[1, 2]", "Lanza un error"], 0,
  "`items()` da las parejas clave-valor; el bucle suma los valores, 1 + 2.",
  code='d = {"a": 1, "b": 2}\ntotal = 0\nfor k, v in d.items():\n    total += v\nprint(total)', v="salida")
P("11-5", "11", 3, "¿Qué imprime este programa?", ["1", "0", "None", "Lanza KeyError"], 0,
  "`get(clave, por_defecto)` devuelve el valor por defecto si la clave no está: 0 + 1.",
  code='d = {"a": 1}\nprint(d.get("b", 0) + d.get("a", 0))', v="salida")
P("11-6", "11", 3, "¿Qué imprime este programa?", ["['b']", "['a']", "['a', 'b']", "[2]"], 0,
  "`del d[\"a\"]` quita la pareja con clave `\"a\"`, y `keys()` da las claves que quedan.",
  code='d = {"a": 1, "b": 2}\ndel d["a"]\nprint(list(d.keys()))', v="salida", mono=True)

P("10-1", "10", 3, "¿Qué imprime este programa?", ["a ogr", "a ogra", "r ogr", "a rog"], 0,
  "`s[-1]` es la última letra. `s[2:5]` va de la posición 2 a la 4: `o`, `g`, `r`.",
  code='s = "programa"\nprint(s[-1], s[2:5])', v="salida", mono=True)
P("10-2", "10", 3, "¿Qué imprime este programa?", ["ALOH", "HOLA", "aloh", "Aloh"], 0,
  "`[::-1]` le da la vuelta a la cadena y `upper()` la pasa a mayúsculas.",
  code='print("hola"[::-1].upper())', v="salida")
P("10-3", "10", 3, "¿Qué imprime este programa?", ["3 2", "3 3", "2 2", "3 1"], 0,
  "Hay tres `a` en `banana`. `find` da la **primera** posición de `n`, que es la 2.",
  code='s = "banana"\nprint(s.count("a"), s.find("n"))', v="salida")
P("10-4", "10", 3, "¿Qué ocurre al ejecutar este programa?", ["s pasa a valer 'Hola'", "Lanza TypeError", "Lanza IndexError", "Lanza ValueError"], 1,
  "Las cadenas son inmutables: no se puede cambiar un carácter. Habría que fabricar otra: `s = \"H\" + s[1:]`.",
  code="s = 'hola'\ns[0] = 'H'", v="error", err="TypeError")

P("26-1", "26", 3, "¿Qué imprime este programa?", ["4", "5", "6", "3"], 0,
  "`\\n` y `\\\\` son secuencias de escape: cada una es **un solo** carácter. La cadena tiene `a`, salto de línea, `b` y una barra.",
  code='print(len("a\\nb\\\\"))', v="salida")
P("26-2", "26", 3, "¿Qué imprime este programa?", ["hOLA mUNDO", "HOLA MUNDO", "  hOLA mUNDO ", "Hola mundo"], 0,
  "`strip()` quita los espacios de los extremos y `swapcase()` cambia mayúsculas por minúsculas y al revés.",
  code='print("  Hola Mundo ".strip().swapcase())', v="salida", mono=True)
P("26-3", "26", 3, "¿Qué imprime este programa?", ["3.14|007", "3.1|7", "3.14|7", "3.14|700"], 0,
  "`:.2f` deja dos decimales y `:03` rellena con ceros hasta 3 cifras.",
  code='x = 3.14159\nprint(f"{x:.2f}|{7:03}")', v="salida", mono=True)
P("26-4", "26", 3, "¿Qué imprime este programa?", ["a-b-c", "-abc-", "abc", "['a', 'b', 'c']"], 0,
  "`join` recorre la cadena carácter a carácter y pone el separador entre cada dos.",
  code='print("-".join("abc"))', v="salida", mono=True)
P("26-5", "26", 3, "¿Qué imprime este programa?", ["Ana tiene 16 años", "%s tiene %d años", "Ana tiene 16.0 años", "Lanza TypeError"], 0,
  "En el formato antiguo con `%`, `%s` se sustituye por una cadena y `%d` por un entero.",
  code='print("%s tiene %d años" % ("Ana", 16))', v="salida")
P("26-6", "26", 3, "¿Qué imprime este programa?", ["Es", "es", "Python", "['Es']"], 0,
  "`title()` pone en mayúscula la primera letra de cada palabra, y `split()[1]` toma la segunda palabra.",
  code='print("python es fácil".title().split()[1])', v="salida")

# ---------------------------------------------------------------- sección 4
P("09-1", "09", 4, "¿Qué imprime este programa?", ["8", "6", "62", "Lanza un error"], 0,
  "`f(3)` devuelve 6 y `f(1)` devuelve 2: 6 + 2 = 8.",
  code="def f(x):\n    return x * 2\n\nprint(f(3) + f(1))", v="salida")
P("09-2", "09", 4, "¿Qué imprime este programa?", ["hola\nNone", "hola", "None", "hola\nhola"], 0,
  "La función **imprime** `hola`, pero no tiene `return`: devuelve `None`, que es lo que se guarda en `r`.",
  code='def f():\n    print("hola")\n\nr = f()\nprint(r)', v="salida", mono=True)
P("09-3", "09", 4, "¿Qué imprime este programa?", ["pos no", "pos pos", "no no", "pos\nno"], 0,
  "`return` termina la función al momento. Con 5 devuelve `\"pos\"`; con 0 no entra en el `if` y llega al segundo `return`.",
  code='def f(n):\n    if n > 0:\n        return "pos"\n    return "no"\n\nprint(f(5), f(0))', v="salida", mono=True)
P("09-4", "09", 4, "En `def area(base, altura):` y la llamada `area(3, 4)`, ¿qué son `3` y `4`?",
  ["Argumentos", "Parámetros", "Variables globales", "Palabras reservadas"], 0,
  "Los **parámetros** son los nombres de la definición (`base`, `altura`); los **argumentos**, los valores de la llamada.")

P("24-1", "24", 4, "¿Qué imprime este programa?", ["21", "13", "30", "Lanza un error"], 0,
  "`a = 1`, `b` se queda con su valor por defecto (2) y `c = 10` por nombre: `1 + 2 * 10 = 21`.",
  code="def f(a, b=2, c=3):\n    return a + b * c\n\nprint(f(1, c=10))", v="salida")
P("24-2", "24", 4, "¿Qué ocurre al ejecutar este programa?", ["Imprime 4", "Imprime -4", "Lanza SyntaxError", "Lanza TypeError"], 2,
  "Un argumento por posición no puede ir **después** de uno por nombre. Es un error de sintaxis: el programa ni siquiera empieza.",
  code="def f(a, b):\n    return a - b\n\nprint(f(b=1, 5))", v="error", err="SyntaxError")
P("24-3", "24", 4, "¿Qué imprime este programa?", ["(3, 9)", "[3, 9]", "3 9", "9"], 0,
  "`*args` recoge los tres argumentos en una tupla. La función devuelve dos valores, que viajan juntos en otra tupla.",
  code="def f(*args):\n    return len(args), sum(args)\n\nprint(f(2, 3, 4))", v="salida", mono=True)
P("24-4", "24", 4, "¿Qué imprime este programa?", ["['a', 'b']", "[1, 2]", "['b', 'a']", "{'a': 2, 'b': 1}"], 0,
  "`**k` recoge los argumentos con nombre en un diccionario. `sorted` de un diccionario ordena sus **claves**.",
  code="def f(**k):\n    return sorted(k)\n\nprint(f(b=1, a=2))", v="salida", mono=True)
P("24-5", "24", 4, "¿Qué imprime este programa?", ["5 1", "5 5", "1 1", "1 5"], 0,
  "El `x = 5` de dentro crea una variable **local** que tapa a la global. La global sigue valiendo 1.",
  code="x = 1\n\ndef f():\n    x = 5\n    return x\n\nprint(f(), x)", v="salida")
P("24-6", "24", 4, "¿Qué imprime este programa?", ["4", "2", "0", "Lanza UnboundLocalError"], 0,
  "Con `global c`, la función cambia la variable de fuera. Dos llamadas suman 2 cada una.",
  code="c = 0\n\ndef sube():\n    global c\n    c += 2\n\nsube()\nsube()\nprint(c)", v="salida")
P("24-7", "24", 4, "¿Qué ocurre al ejecutar este programa?",
  ["t pasa a valer 1", "Lanza UnboundLocalError", "Lanza NameError", "No pasa nada: t sigue a 0"], 1,
  "Como la función **asigna** `t`, Python la considera local en toda la función. Al leerla en `t + 1`, todavía no tiene valor.",
  code="t = 0\n\ndef f():\n    t = t + 1\n\nf()", v="error", err="UnboundLocalError")

P("13-1", "13", 4, "¿Qué imprime este programa?", ["B", "A\nB", "A", "Lanza ValueError"], 0,
  "`int(\"tres\")` falla: el resto del `try` (el `print(\"A\")`) ya no se ejecuta y se salta al `except`.",
  code='try:\n    x = int("tres")\n    print("A")\nexcept ValueError:\n    print("B")', v="salida", mono=True)
P("13-2", "13", 4, "¿Qué imprime este programa?", ["Z", "V", "V\nZ", "Lanza ZeroDivisionError"], 0,
  "Python prueba los `except` en orden y entra en el primero cuyo tipo encaja: el de `ZeroDivisionError`.",
  code='try:\n    print(1 / 0)\nexcept ValueError:\n    print("V")\nexcept ZeroDivisionError:\n    print("Z")', v="salida", mono=True)
P("13-3", "13", 4, "¿Qué imprime este programa?", ["fuera", "None", "Lanza IndexError", "2"], 0,
  "Un `except` puede atender varios tipos a la vez, escritos en una tupla. `IndexError` está entre ellos.",
  code='datos = [1, 2]\ntry:\n    print(datos[5])\nexcept (IndexError, KeyError):\n    print("fuera")', v="salida")
P("13-4", "13", 4, "¿Qué ocurre al ejecutar este programa?", ["Lanza ValueError", "Lanza TypeError", "Imprime 3", "Imprime 3.5"], 0,
  "`int` acepta el texto de un entero, pero `\"3.5\"` no lo es: `ValueError`. Funcionaría `int(float(\"3.5\"))`, que da 3.",
  code='print(int("3.5"))', v="error", err="ValueError")
P("13-5", "13", 4, "¿Qué excepción salta al usar una variable que no existe?", ["NameError", "KeyError", "ValueError", "IndexError"], 0,
  "Un nombre que Python no conoce produce `NameError`. `KeyError` es para claves de diccionario e `IndexError` para posiciones.", mono=True)

# ---------------------------------------------------------------- sección 5
P("17-1", "17", 5, "¿Qué modo abre un fichero para **añadir al final** sin borrar lo que había?", ['"a"', '"w"', '"r"', '"x"'], 0,
  "`\"a\"` (*append*) escribe a continuación. `\"w\"` vacía el fichero al abrirlo, `\"r\"` es para leer y `\"x\"` falla si el fichero ya existe.", mono=True)
P("17-2", "17", 5, "¿Qué imprime este programa?", ["dos", "uno\ndos", "uno", "Lanza FileExistsError"], 0,
  "Cada vez que se abre en modo `\"w\"`, el fichero se vacía: la segunda escritura borra la primera.",
  code='with open("f.txt", "w") as f:\n    f.write("uno\\n")\nwith open("f.txt", "w") as f:\n    f.write("dos\\n")\nwith open("f.txt") as f:\n    print(f.read().strip())', v="salida", mono=True)
P("17-3", "17", 5, "¿Qué ocurre si `no_esta.txt` no existe?", ["Lanza FileNotFoundError", "Crea el fichero vacío", "Imprime una línea vacía", "Lanza PermissionError"], 0,
  "El modo por defecto es `\"r\"`, leer, y no se puede leer un fichero que no existe.",
  code='with open("no_esta.txt") as f:\n    print(f.read())', v="error", err="FileNotFoundError")
P("17-4", "17", 5, "¿Qué imprime este programa?", ["3", "6", "1", "4"], 0,
  "`readlines()` devuelve una lista con una cadena por línea: `['a\\n', 'b\\n', 'c\\n']`.",
  code='with open("n.txt", "w") as f:\n    f.write("a\\nb\\nc\\n")\nwith open("n.txt") as f:\n    print(len(f.readlines()))', v="salida")

P("27-1", "27", 5, "¿Qué imprime este programa?", ["-2 -3 -2", "-3 -2 -2", "-2 -3 -3", "-3 -3 -2"], 0,
  "`ceil` redondea hacia arriba (-2), `floor` hacia abajo (-3) y `trunc` quita los decimales (-2).",
  code="import math\nprint(math.ceil(-2.5), math.floor(-2.5), math.trunc(-2.5))", v="salida")
P("27-2", "27", 5, "¿Qué imprime este programa?", ["6.0", "6", "7.0", "6.9"], 0,
  "`math.sqrt` siempre da un `float` (4.0), y `floor(2.9)` da el entero 2. Un `float` más un `int` da `float`.",
  code="import math\nprint(math.sqrt(16) + math.floor(2.9))", v="salida")
P("27-3", "27", 5, "¿Qué hace `random.seed(5)`?",
  ["Fija el punto de partida: con la misma semilla salen los mismos números",
   "Devuelve un número al azar entre 0 y 5",
   "Baraja una lista 5 veces",
   "Hace que todos los números al azar valgan 5"], 0,
  "Los números de `random` salen de una fórmula a partir de una semilla. Misma semilla, misma secuencia: el programa es reproducible.")
P("27-4", "27", 5, "¿Qué expresión elige **3 elementos distintos** de una lista al azar?",
  ["random.sample(lista, 3)", "random.choice(lista, 3)", "random.shuffle(lista, 3)", "random.randint(lista, 3)"], 0,
  "`sample(secuencia, k)` elige `k` elementos sin repetir. `choice` elige uno solo y `shuffle` baraja la lista en su sitio.", mono=True)
P("27-5", "27", 5, "¿Qué imprime este programa?", ["['Ana', '7']", "['Ana', 7]", "Ana,7", "('Ana', '7')"], 0,
  "`csv.reader` devuelve cada fila como una **lista de cadenas**: el 7 vuelve como `'7'`.",
  code='import csv\nwith open("t.csv", "w", newline="") as f:\n    csv.writer(f).writerow(["Ana", 7])\nwith open("t.csv", newline="") as f:\n    fila = next(csv.reader(f))\nprint(fila)', v="salida", mono=True)
P("27-6", "27", 5, "¿Qué valores puede dar `random.randint(1, 6)`?",
  ["Los enteros del 1 al 6, ambos incluidos", "Los enteros del 1 al 5", "Cualquier decimal entre 1 y 6", "Los enteros del 0 al 6"], 0,
  "`randint(a, b)` incluye los dos extremos, a diferencia de `range` y de `randrange`.")
P("27-7", "27", 5, "¿Qué imprime este programa?", ["True", "False", "Depende de cada ejecución", "Lanza un error"], 0,
  "Con la misma semilla, la secuencia vuelve a empezar desde el mismo punto: los dos números son iguales.",
  code="import random\nrandom.seed(1)\na = random.random()\nrandom.seed(1)\nb = random.random()\nprint(a == b)", v="salida")

P("12-1", "12", 5, "¿Qué ocurre al ejecutar este programa?", ["Imprime 3.0", "Lanza NameError", "Lanza ImportError", "Imprime 3"], 1,
  "Con `import math`, la función se llama `math.sqrt`. El nombre `sqrt` a secas no existe en el programa.",
  code="import math\nprint(sqrt(9))", v="error", err="NameError")
P("12-2", "12", 5, "¿Qué imprime este programa?", ["3.14", "3.1416", "Lanza NameError", "3"], 0,
  "`from math import sqrt, pi` trae esos dos nombres, que se usan sin prefijo. `round(pi, 2)` es 3.14.",
  code="from math import sqrt, pi\nprint(round(pi, 2))", v="salida")
P("12-3", "12", 5, "¿Qué imprime este programa?", ["7", "8", "7.8", "Lanza NameError"], 0,
  "`import math as m` importa el módulo con el alias `m`. `floor` redondea hacia abajo.",
  code="import math as m\nprint(m.floor(7.8))", v="salida")
