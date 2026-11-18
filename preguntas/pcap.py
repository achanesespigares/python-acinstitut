r"""Banco de preguntas tipo examen PCAP (temario PCAP-31-04).

Mismos campos que pcep.py: id, cap, sec, q, ops, ok (índice o lista), exp,
code, v ("salida", "error" o "valor:expr"), err, mono, entradas.
herramientas/preguntas.py ejecuta las preguntas con código y comprueba que la
respuesta marcada es la que da Python. Todas las preguntas son originales.
"""

SECCIONES = {
    "1": "Módulos y paquetes",
    "2": "Excepciones",
    "3": "Cadenas",
    "4": "Programación orientada a objetos",
    "5": "Construcciones avanzadas y E/S",
    "6": "Pruebas, depuración, equipo e IA",
}
REPARTO = {"1": 5, "2": 5, "3": 4, "4": 12, "5": 10, "6": 6}     # 42 preguntas, como el examen

PREGUNTAS = []


def P(id, cap, sec, q, ops, ok, exp, code=None, v=None, err=None, mono=None, entradas=()):
    PREGUNTAS.append(dict(id=id, cap=cap, sec=str(sec), q=q, ops=ops, ok=ok, exp=exp, code=code,
                          v=v, err=err, mono=mono, entradas=list(entradas)))


# ---------------------------------------------------------------- 1 · módulos y paquetes
P("P12-1", "12", 1, "¿Qué imprime este programa?", ["math", "__main__", "math.py", "<module 'math'>"], 0,
  "Cada módulo tiene su variable `__name__` con su nombre. Solo vale `\"__main__\"` en el fichero que se ejecuta directamente.",
  code="import math\nprint(math.__name__)", v="salida", mono=True)
P("P12-2", "12", 1, "Al ejecutar directamente el fichero `geometria.py`, ¿cuánto vale `__name__` dentro de él?",
  ['"__main__"', '"geometria"', '"geometria.py"', "None"], 0,
  "El fichero que se lanza vale `\"__main__\"`. Si otro programa lo importa, valdrá `\"geometria\"`: por eso funciona el truco `if __name__ == \"__main__\":`.", mono=True)
P("P12-3", "12", 1, "¿Qué convierte una carpeta en un **paquete regular** de Python?",
  ["Contener un fichero __init__.py", "Contener un fichero main.py", "Llamarse igual que uno de sus módulos", "Estar dentro de la carpeta de instalación de Python"], 0,
  "El fichero `__init__.py` marca la carpeta como paquete regular y se ejecuta al importarlo.")
P("P12-4", "12", 1, "¿Dónde busca Python un módulo al hacer `import`?",
  ["En las carpetas de la lista sys.path, por orden", "Solo en la carpeta del programa",
   "En Internet, en el repositorio PyPI", "En la carpeta de documentos del usuario"], 0,
  "`sys.path` empieza por la carpeta del programa y sigue con la biblioteca estándar y los paquetes instalados. Python usa el primer módulo que encuentra con ese nombre.")
P("P12-5", "12", 1, "¿Qué imprime este programa?", ["True True", "False True", "True False", "Lanza NameError"], 0,
  "El alias `m` es el módulo `math`. `hasattr` y `dir` permiten examinarlo por dentro: es introspección.",
  code='import math as m\nprint(hasattr(m, "sqrt"), "sqrt" in dir(m))', v="salida")
P("P12-6", "12", 1, "¿Qué imprime este programa?", ["5", "4", "6", "Lanza NameError"], 0,
  "`from math import *` trae todos los nombres públicos del módulo, que se usan sin prefijo: `floor(2.7) = 2` y `ceil(2.2) = 3`.",
  code="from math import *\nprint(floor(2.7) + ceil(2.2))", v="salida")
P("P12-7", "12", 1, "¿Qué orden instala el paquete `requests`?",
  ["pip install requests", "python install requests", "import requests --install", "pip get requests"], 0,
  "Los paquetes externos se instalan desde la terminal con `pip install`, no desde dentro de un programa.", mono=True)
P("P12-8", "12", 1, "¿Para qué sirve un fichero `requirements.txt`?",
  ["Para apuntar las dependencias del proyecto y poder instalarlas con pip install -r requirements.txt",
   "Para guardar las pruebas unitarias del proyecto",
   "Para declarar las variables globales del programa",
   "Para que Python ejecute el programa más rápido"], 0,
  "Documenta qué paquetes (y qué versiones) necesita el proyecto, para que cualquiera pueda reproducir el entorno. Se suele generar con `pip freeze > requirements.txt`.")
P("P12-9", "12", 1, "El paquete `utiles` contiene el módulo `textos.py`, con la función `limpia`. ¿Qué importación permite escribir `limpia(s)` directamente?",
  ["from utiles.textos import limpia", "import utiles.textos", "import limpia from utiles.textos", "from utiles import limpia.textos"], 0,
  "`from paquete.modulo import nombre` trae ese nombre. Con `import utiles.textos` habría que escribir `utiles.textos.limpia(s)`.", mono=True)
P("P12-10", "12", 1, "¿Qué guarda Python en la carpeta `__pycache__`?",
  ["Los módulos importados ya compilados a bytecode", "Copias de seguridad de los ficheros .py",
   "Los datos que el programa guarda entre ejecuciones", "Los paquetes instalados con pip"], 0,
  "La primera vez que importa un módulo, Python lo compila a bytecode y lo guarda allí para cargarlo más rápido la siguiente vez.")

# ---------------------------------------------------------------- 2 · excepciones
P("P13-1", "13", 2, "¿Qué imprime este programa?", ["A\nC", "A\nB\nC", "A", "B\nC"], 0,
  "Hay error: se ejecuta el `except` (A), no el `else`, que solo corre si no hubo error. El `finally` se ejecuta siempre (C).",
  code='try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print("A")\nelse:\n    print("B")\nfinally:\n    print("C")', v="salida", mono=True)
P("P13-2", "13", 2, "¿Qué imprime este programa?", ["B\nC", "A\nC", "C", "A\nB\nC"], 0,
  "Sin error, el `except` no se ejecuta, el `else` sí (B) y el `finally` también (C).",
  code='try:\n    x = 1\nexcept ValueError:\n    print("A")\nelse:\n    print("B")\nfinally:\n    print("C")', v="salida", mono=True)
P("P13-3", "13", 2, "¿Qué imprime este programa?", ["ValueError ('malo',)", "Exception ('malo',)", "ValueError malo", "ValueError ['malo']"], 0,
  "`as e` guarda el objeto excepción, que sigue siendo un `ValueError` aunque lo atrape `except Exception`. `e.args` es la tupla de argumentos.",
  code='try:\n    raise ValueError("malo")\nexcept Exception as e:\n    print(type(e).__name__, e.args)', v="salida", mono=True)
P("P13-4", "13", 2, "¿Qué imprime este programa?", ["L", "I", "L\nI", "Lanza IndexError"], 0,
  "`IndexError` es una subclase de `LookupError`, así que el primer `except` ya lo atrapa y el segundo no llega a mirarse.",
  code='try:\n    [1, 2][3]\nexcept LookupError:\n    print("L")\nexcept IndexError:\n    print("I")', v="salida", mono=True)
P("P13-5", "13", 2, "¿Qué imprime este programa?", ["True False", "True True", "False False", "False True"], 0,
  "`ZeroDivisionError` cuelga de `ArithmeticError`; `ValueError` no, cuelga directamente de `Exception`.",
  code="print(issubclass(ZeroDivisionError, ArithmeticError), issubclass(ValueError, ArithmeticError))", v="salida")
P("P13-6", "13", 2, "¿Qué imprime este programa?", ["g", "Lanza ZeroDivisionError", "None", "1"], 0,
  "El error nace en `f`, que no lo atiende: se propaga a `g`, que lo atrapa y devuelve `\"g\"`.",
  code='def f():\n    return 1 / 0\n\ndef g():\n    try:\n        return f()\n    except ZeroDivisionError:\n        return "g"\n\nprint(g())', v="salida")
P("P13-7", "13", 2, "¿Qué imprime este programa?", ["dentro\nfuera", "dentro", "fuera", "Lanza ValueError"], 0,
  "Un `raise` sin nada dentro de un `except` vuelve a lanzar la misma excepción, que atrapa el `try` de fuera.",
  code='try:\n    try:\n        int("x")\n    except ValueError:\n        print("dentro")\n        raise\nexcept ValueError:\n    print("fuera")', v="salida", mono=True)
P("P13-8", "13", 2, "¿Qué imprime este programa?", ["finally\ntry", "try\nfinally", "try", "finally"], 0,
  "El `finally` se ejecuta **antes** de que la función devuelva su valor, incluso aunque haya un `return` dentro del `try`.",
  code='def f():\n    try:\n        return "try"\n    finally:\n        print("finally")\n\nprint(f())', v="salida", mono=True)
P("P13-9", "13", 2, "¿De qué clase conviene heredar al crear tus propias excepciones?",
  ["Exception", "BaseException", "Error", "object"], 0,
  "`BaseException` es la raíz, pero de ella cuelgan también `KeyboardInterrupt` y `SystemExit`, que no son errores del programa. Las excepciones propias heredan de `Exception` o de una de sus subclases.", mono=True)
P("P13-10", "13", 2, "¿Qué imprime este programa?", ["V 12", "Lanza NotaInvalida", "12", "V NotaInvalida"], 0,
  "`NotaInvalida` hereda de `ValueError`, así que `except ValueError` también la atrapa. Imprimir `e` muestra su mensaje.",
  code='class NotaInvalida(ValueError):\n    pass\n\ntry:\n    raise NotaInvalida("12")\nexcept ValueError as e:\n    print("V", e)', v="salida")

# ---------------------------------------------------------------- 3 · cadenas
P("P19-1", "19", 3, "¿Qué imprime este programa?", ["32 d", "-32 d", "32 c", "1 d"], 0,
  "Las minúsculas están 32 puntos de código por detrás de las mayúsculas (`a` = 97, `A` = 65). `chr(ord(\"c\") + 1)` es la letra siguiente.",
  code='print(ord("a") - ord("A"), chr(ord("c") + 1))', v="salida")
P("P19-2", "19", 3, "¿Qué imprime este programa?", ["True True", "False False", "True False", "False True"], 0,
  "Se comparan puntos de código: `Z` (90) va antes que `a` (97), y en `\"10\" < \"9\"` decide `\"1\" < \"9\"`. Son textos, no números.",
  code='print("Zorro" < "abeja", "10" < "9")', v="salida")
P("P19-3", "19", 3, "¿Qué imprime este programa?", [r"b'a\xc3\xb1o' 4", "b'año' 3", r"b'a\xf1o' 3", "'año' 4"], 0,
  "En UTF-8, la `ñ` ocupa dos bytes (`c3 b1`). Por eso la cadena tiene 3 caracteres pero 4 bytes.",
  code='print("año".encode("utf-8"), len("año".encode("utf-8")))', v="salida", mono=True)
P("P19-4", "19", 3, "¿Qué imprime este programa?", ["hola", "hola!", "!", "Lanza TypeError"], 0,
  "Las cadenas son inmutables: `s += \"!\"` fabrica una cadena nueva y le pega la etiqueta `s`. `t` sigue apuntando a la vieja.",
  code='s = "hola"\nt = s\ns += "!"\nprint(t)', v="salida")
P("P19-5", "19", 3, "¿Qué imprime este programa?", ["True False True", "True True True", "False False True", "True False False"], 0,
  "El superíndice `²` es un dígito, pero no un dígito decimal (0-9). `\"12a\"` tiene solo letras y dígitos.",
  code='print("²".isdigit(), "²".isdecimal(), "12a".isalnum())', v="salida")
P("P19-6", "19", 3, "¿Qué imprime este programa?", ["11 15 3", "0 15 3", "11 11 3", "11 15 2"], 0,
  "`find(\"la\", 1)` empieza a buscar en la posición 1, así que se salta el `la` del principio y encuentra el de `de la` (11). `rfind` da el último (15) y `count` cuenta los tres.",
  code='s = "la casa de la playa"\nprint(s.find("la", 1), s.rfind("la"), s.count("la"))', v="salida")
P("P19-7", "19", 3, "¿Qué ocurre al ejecutar este programa?", ["Imprime -1", "Lanza ValueError", "Imprime None", "Lanza IndexError"], 1,
  "`index` lanza `ValueError` si no encuentra la subcadena. `find` devolvería `-1`.",
  code='print("python".index("z"))', v="error", err="ValueError")
P("P19-8", "19", 3, "¿Qué imprime este programa?", ["['A', 'b', 'c']", "['b', 'A', 'c']", "['A', 'c', 'b']", "Abc"], 0,
  "`sorted` aplicado a una cadena da la lista de sus caracteres ordenados por punto de código: la mayúscula `A` (65) va primero.",
  code='print(sorted("bAc"))', v="salida", mono=True)
P("P19-9", "19", 3, "¿Qué imprime este programa?", ["abcabccba", "abccba", "abcabcabc", "cbacbaabc"], 0,
  "`s * 2` repite la cadena y `s[::-1]` le da la vuelta. Cada operación fabrica una cadena nueva.",
  code='s = "abc"\nprint(s * 2 + s[::-1])', v="salida")
P("P19-10", "19", 3, "¿Cuáles de estas expresiones valen `True`?",
  ["'abc'.isalpha()", "'abc1'.isalpha()", "' '.isspace()", "''.isdigit()"], [0, 2],
  "`'abc1'` tiene un dígito, así que no es solo letras. Los métodos `is…()` devuelven `False` con la cadena vacía.", mono=True)

# ---------------------------------------------------------------- 4 · orientación a objetos
P("P14-1", "14", 4, "¿Qué imprime este programa?", ["True False", "True True", "False False", "False True"], 0,
  "Los dos objetos tienen el mismo valor en `x`, pero son dos objetos distintos: `==` compara valores e `is`, identidad.",
  code="class A:\n    def __init__(self, x):\n        self.x = x\n\na = A(3)\nb = A(3)\nprint(a.x == b.x, a is b)", v="salida")
P("P14-2", "14", 4, "¿Qué imprime este programa?", ["2", "1", "0", "Lanza AttributeError"], 0,
  "`sube` devuelve `self`, el propio objeto, así que se puede encadenar otra llamada sobre él.",
  code="class C:\n    def __init__(self):\n        self.n = 0\n    def sube(self):\n        self.n += 1\n        return self\n\nc = C()\nc.sube().sube()\nprint(c.n)", v="salida")
P("P14-3", "14", 4, "¿Qué imprime este programa?", ["{'edad': 5}", "{}", "{'P': {'edad': 5}}", "Lanza AttributeError"], 0,
  "A un objeto se le pueden añadir atributos desde fuera; `__dict__` muestra los atributos de instancia.",
  code="class P:\n    pass\n\np = P()\np.edad = 5\nprint(p.__dict__)", v="salida", mono=True)
P("P14-4", "14", 4, "¿Qué ocurre al ejecutar este programa?", ["Imprime 1", "Lanza TypeError", "Lanza NameError", "Imprime None"], 1,
  "Al llamar a un método, Python pasa el objeto como primer argumento. Como `f` no tiene `self`, recibe un argumento que no esperaba.",
  code="class A:\n    def f():\n        return 1\n\nprint(A().f())", v="error", err="TypeError")
P("P14-5", "14", 4, "¿Qué imprime este programa?", ["Saldo: 5", "<__main__.Cuenta object>", "5", "Cuenta(5)"], 0,
  "`print` usa el método `__str__` del objeto para saber qué escribir.",
  code='class Cuenta:\n    def __init__(self, s):\n        self.s = s\n    def __str__(self):\n        return f"Saldo: {self.s}"\n\nprint(Cuenta(5))', v="salida")
P("P14-6", "14", 4, "¿Qué imprime este programa?", ["A True", "A False", "Lanza AttributeError", "B True"], 0,
  "`B` hereda el método `hola` de `A`, y un objeto de `B` también es un `A`.",
  code='class A:\n    def hola(self):\n        return "A"\n\nclass B(A):\n    pass\n\nprint(B().hola(), isinstance(B(), A))', v="salida")
P("P14-7", "14", 4, "¿Qué imprime este programa?", ["11", "10", "1", "Lanza AttributeError"], 0,
  "`super().__init__()` ejecuta el `__init__` de `A` (que pone `v = 1`) y después `B` le suma 10.",
  code="class A:\n    def __init__(self):\n        self.v = 1\n\nclass B(A):\n    def __init__(self):\n        super().__init__()\n        self.v += 10\n\nprint(B().v)", v="salida")
P("P14-8", "14", 4, "¿Qué principio consiste en reunir en un objeto sus datos y los métodos que los manejan, protegiendo los detalles internos?",
  ["Encapsulación", "Herencia", "Polimorfismo", "Recursividad"], 0,
  "Eso es la encapsulación. La herencia reutiliza una clase en otra, y el polimorfismo permite que objetos distintos respondan al mismo método.")

P("P18-1", "18", 4, "¿Qué imprime este programa?", ["5 0 0", "5 5 5", "5 5 0", "0 0 0"], 0,
  "`a.n = 5` crea un atributo de instancia en `a` que **tapa** al de la clase solo para `a`. `b` y la clase siguen con 0.",
  code="class X:\n    n = 0\n\na = X()\nb = X()\na.n = 5\nprint(a.n, b.n, X.n)", v="salida")
P("P18-2", "18", 4, "¿Qué imprime este programa?", ["2", "1", "0", "Lanza AttributeError"], 0,
  "`X.n` es un atributo de clase, uno solo para todos. Cada objeto nuevo lo incrementa.",
  code="class X:\n    n = 0\n    def __init__(self):\n        X.n += 1\n\nX()\nX()\nprint(X.n)", v="salida")
P("P18-3", "18", 4, "¿Qué imprime este programa?", ["[1, 2]", "[1]", "[2]", "[]"], 0,
  "`lista` es un atributo **de clase** y es mutable: `self.lista.append` modifica la lista compartida por todos los objetos.",
  code="class X:\n    lista = []\n    def __init__(self, v):\n        self.lista.append(v)\n\na = X(1)\nb = X(2)\nprint(a.lista)", v="salida", mono=True)
P("P18-4", "18", 4, "¿Qué imprime este programa?", ["{'_C__s': 1}", "{'__s': 1}", "{'s': 1}", "{}"], 0,
  "Un atributo que empieza por dos guiones bajos se guarda con el nombre de la clase delante: es la desfiguración de nombres.",
  code="class C:\n    def __init__(self):\n        self.__s = 1\n\nprint(C().__dict__)", v="salida", mono=True)
P("P18-5", "18", 4, "¿Qué ocurre al ejecutar este programa?", ["Imprime 1", "Lanza AttributeError", "Imprime None", "Lanza NameError"], 1,
  "Fuera de la clase, `__s` no existe con ese nombre: se llama `_C__s`.",
  code="class C:\n    def __init__(self):\n        self.__s = 1\n\nprint(C().__s)", v="error", err="AttributeError")
P("P18-6", "18", 4, "¿Qué imprime este programa?", ["BA", "B", "A", "AB"], 0,
  "`B.f` sobrescribe `A.f`, pero llama al de la madre con `super().f()` y le añade su parte delante.",
  code='class A:\n    def f(self):\n        return "A"\n\nclass B(A):\n    def f(self):\n        return "B" + super().f()\n\nprint(B().f())', v="salida")
P("P18-7", "18", 4, "¿Qué imprime este programa?", ["C", "A", "B", "Lanza AttributeError"], 0,
  "El MRO de `D` es `D, B, C, A`. `B` no tiene `f`, así que Python sigue buscando y lo encuentra en `C` antes de llegar a `A`.",
  code='class A:\n    def f(self):\n        return "A"\n\nclass B(A):\n    pass\n\nclass C(A):\n    def f(self):\n        return "C"\n\nclass D(B, C):\n    pass\n\nprint(D().f())', v="salida")
P("P18-8", "18", 4, "¿Qué imprime este programa?", ["['C', 'B', 'A', 'object']", "['C', 'B', 'A']", "['object', 'A', 'B', 'C']", "['C']"], 0,
  "El MRO va de la clase a sus madres y termina siempre en `object`, la madre de todas las clases.",
  code="class A:\n    pass\n\nclass B(A):\n    pass\n\nclass C(B):\n    pass\n\nprint([k.__name__ for k in C.__mro__])", v="salida", mono=True)
P("P18-9", "18", 4, "¿Qué imprime este programa?", ["True False A", "True True A", "False False B", "True False object"], 0,
  "`B` es subclase de `A`, pero un objeto de `A` no es un `B`. `__bases__` da las madres directas: `(A,)`.",
  code="class A:\n    pass\n\nclass B(A):\n    pass\n\nprint(issubclass(B, A), isinstance(A(), B), B.__bases__[0].__name__)", v="salida")
P("P18-10", "18", 4, "¿Qué imprime este programa?", ["1 0 False", "1 None False", "1 0 True", "Lanza AttributeError"], 0,
  "`getattr(objeto, nombre, por_defecto)` devuelve el valor por defecto si el atributo no existe, sin lanzar error.",
  code='class P:\n    def __init__(self):\n        self.x = 1\n\np = P()\nprint(getattr(p, "x"), getattr(p, "y", 0), hasattr(p, "y"))', v="salida")
P("P18-11", "18", 4, "¿Qué imprime este programa?", ["guau miau", "miau guau", "guau", "Lanza AttributeError"], 0,
  "Es polimorfismo: objetos de clases distintas responden al mismo método `voz`, cada uno a su manera.",
  code='class Gato:\n    def voz(self):\n        return "miau"\n\nclass Perro:\n    def voz(self):\n        return "guau"\n\nprint(*[a.voz() for a in [Perro(), Gato()]])', v="salida")
P("P18-12", "18", 4, "¿Qué imprime este programa?", ["True False", "True True", "False False", "False True"], 0,
  "Las dos listas valen lo mismo (`==`), pero son dos objetos distintos (`is`).",
  code="x = [1]\ny = [1]\nprint(x == y, x is y)", v="salida")
P("P18-13", "18", 4, "¿Qué imprime este programa?", ["[1]", "[]", "None", "Lanza AttributeError"], 0,
  "El valor por defecto `[]` se crea una sola vez, al definir la función, y lo comparten todos los objetos creados sin argumento.",
  code="class Caja:\n    def __init__(self, cosas=[]):\n        self.cosas = cosas\n\na = Caja()\nb = Caja()\na.cosas.append(1)\nprint(b.cosas)", v="salida", mono=True)
P("P18-14", "18", 4, "¿Qué imprime este programa?", ["negativa", "ValueError", "-1", "Lanza ValueError"], 0,
  "`__init__` valida el dato y lanza `ValueError` si es imposible; el `except` lo atrapa e imprime su mensaje.",
  code='class Edad:\n    def __init__(self, n):\n        if n < 0:\n            raise ValueError("negativa")\n        self.n = n\n\ntry:\n    Edad(-1)\nexcept ValueError as e:\n    print(e)', v="salida")
P("P18-15", "18", 4, "¿Qué ocurre al ejecutar este programa?", ["Imprime 5", "Lanza TypeError", "Imprime <__main__.A object>", "Imprime None"], 1,
  "`__str__` tiene que devolver una cadena. Si devuelve un número, `print` lanza `TypeError: __str__ returned non-string`.",
  code="class A:\n    def __str__(self):\n        return 5\n\nprint(A())", v="error", err="TypeError")
P("P18-16", "18", 4, "¿Qué imprime este programa?", ["Perro __main__", "Perro Perro", "__main__ Perro", "<class 'Perro'> __main__"], 0,
  "`__name__` es el nombre de la clase y `__module__`, el del módulo donde se definió: el programa principal.",
  code="class Perro:\n    pass\n\nprint(Perro.__name__, Perro.__module__)", v="salida")
P("P18-17", "18", 4, "¿Cuáles de estas afirmaciones sobre la desfiguración de nombres son ciertas?",
  ["self.__x se guarda como _Clase__x", "Hace imposible leer el atributo desde fuera",
   "Sirve para evitar choques de nombres con las subclases", "También cambia el nombre de métodos como __init__"], [0, 2],
  "Desde fuera se puede seguir leyendo como `_Clase__x`: no es privacidad de verdad. Los nombres con dos guiones bajos también al **final**, como `__init__`, no se desfiguran.")

# ---------------------------------------------------------------- 5 · construcciones avanzadas y E/S
P("P15-1", "15", 5, "¿Qué imprime este programa?", ["[2, 6]", "[0, 4, 8]", "[1, 3]", "[2, 4, 6, 8]"], 0,
  "`x % 2` vale 1 (verdadero) con los impares, 1 y 3, que se duplican.",
  code="print([x * 2 for x in range(5) if x % 2])", v="salida", mono=True)
P("P15-2", "15", 5, "¿Qué imprime este programa?", ["[[0, 0, 0], [0, 1, 2]]", "[[0, 0], [0, 1], [0, 2]]", "[0, 0, 0, 0, 1, 2]", "[[0, 1, 2], [0, 0, 0]]"], 0,
  "La comprensión de fuera fabrica una fila por cada `i`; la de dentro, los valores `i * j` de esa fila.",
  code="print([[i * j for j in range(3)] for i in range(2)])", v="salida", mono=True)
P("P15-3", "15", 5, "¿Qué imprime este programa?", ["[1, 2, 3]", "[[1, 2], [3]]", "[3, 1, 2]", "Lanza NameError"], 0,
  "Con dos `for`, el primero es el de fuera: recorre los grupos, y el segundo, los números de cada grupo. Así se aplana una lista de listas.",
  code="print([n for g in [[1, 2], [3]] for n in g])", v="salida", mono=True)
P("P15-4", "15", 5, "¿Qué imprime este programa?", ["{'sol': 3, 'mar': 3}", "[3, 3]", "{3: 'mar'}", "{'sol', 'mar'}"], 0,
  "Con llaves y `clave: valor`, la comprensión fabrica un diccionario.",
  code='print({p: len(p) for p in ["sol", "mar"]})', v="salida", mono=True)
P("P15-5", "15", 5, "¿Qué imprime este programa?", ["['impar', 'par']", "['par', 'impar']", "['par']", "Lanza SyntaxError"], 0,
  "La expresión condicional va delante del `for` y elige un valor para cada elemento: no filtra.",
  code='print(["par" if n % 2 == 0 else "impar" for n in [1, 2]])', v="salida", mono=True)
P("P15-6", "15", 5, "¿Qué imprime este programa?", ["ninguno", "par", "par\nninguno", "No imprime nada"], 0,
  "El bucle termina sin `break`, porque no hay ningún par, así que se ejecuta su `else`.",
  code='for n in [3, 5, 7]:\n    if n % 2 == 0:\n        print("par")\n        break\nelse:\n    print("ninguno")', v="salida", mono=True)
P("P15-7", "15", 5, "¿Qué imprime este programa?", ["3", "fin\n3", "fin\n5", "5"], 0,
  "El `while` termina con `break` cuando `i` vale 3, así que su `else` no se ejecuta.",
  code='i = 0\nwhile i < 5:\n    i += 1\n    if i == 3:\n        break\nelse:\n    print("fin")\nprint(i)', v="salida", mono=True)
P("P15-8", "15", 5, "¿Qué imprime este programa?", ["diagonal 2", "otro", "origen", "diagonal 2\notro"], 0,
  "`(0, 0)` no encaja. `(x, y)` encaja con cualquier pareja y captura sus valores, y la guarda `if x == y` se cumple.",
  code='punto = (2, 2)\nmatch punto:\n    case (0, 0):\n        print("origen")\n    case (x, y) if x == y:\n        print("diagonal", x)\n    case _:\n        print("otro")', v="salida", mono=True)
P("P15-9", "15", 5, "¿Qué imprime este programa?", ["salir", "?", "salir\n?", "Lanza SyntaxError"], 0,
  "Con `|`, el patrón encaja con cualquiera de las alternativas.",
  code='orden = "q"\nmatch orden:\n    case "s" | "q":\n        print("salir")\n    case _:\n        print("?")', v="salida")

P("P16-1", "16", 5, "¿Qué imprime este programa?", ["9 8", "9 9", "6 8", "Lanza TypeError"], 0,
  "Una lambda puede tener valores por defecto: `f(3)` es `3 ** 2` y `f(2, 3)` es `2 ** 3`.",
  code="f = lambda x, y=2: x ** y\nprint(f(3), f(2, 3))", v="salida")
P("P16-2", "16", 5, "¿Qué imprime este programa?", ["['A', 'B']", "<map object>", "['a', 'b']", "AB"], 0,
  "`map` aplica la función a cada elemento; `list` recoge los resultados.",
  code='print(list(map(lambda s: s.upper(), ["a", "b"])))', v="salida", mono=True)
P("P16-3", "16", 5, "¿Qué imprime este programa?", ["[5, 8]", "[True, False, True, False]", "[1, 2]", "[5, 2, 8]"], 0,
  "`filter` se queda con los elementos para los que la función devuelve `True`.",
  code="print(list(filter(lambda n: n > 2, [1, 5, 2, 8])))", v="salida", mono=True)
P("P16-4", "16", 5, "¿Qué imprime este programa?", ["[1, 2] []", "[1, 2] [1, 2]", "[1, 2]", "Lanza StopIteration"], 0,
  "`map` devuelve un iterador, que se gasta al recorrerlo: la segunda vez ya no entrega nada.",
  code="m = map(abs, [-1, 2])\nprint(list(m), list(m))", v="salida", mono=True)
P("P16-5", "16", 5, "¿Qué imprime este programa?", ["8", "9", "6", "Lanza NameError"], 0,
  "`potencia(3)` devuelve una función que **recuerda** `e = 3` aunque `potencia` ya haya terminado: es un cierre.",
  code="def potencia(e):\n    return lambda b: b ** e\n\ncubo = potencia(3)\nprint(cubo(2))", v="salida")
P("P16-6", "16", 5, "¿Qué imprime este programa?", ["['ccc', 'bb', 'a']", "['a', 'bb', 'ccc']", "['ccc', 'a', 'bb']", "[3, 2, 1]"], 0,
  "`key=len` ordena por longitud y `reverse=True`, de mayor a menor.",
  code='print(sorted(["bb", "a", "ccc"], key=len, reverse=True))', v="salida", mono=True)
P("P16-7", "16", 5, "¿Qué imprime este programa?", ["20 f", "20 g", "f 20", "Lanza TypeError"], 0,
  "`g = f` no copia la función: es otra etiqueta para el mismo objeto función, que sigue llamándose `f`.",
  code="def f(x):\n    return x * 10\n\ng = f\nprint(g(2), g.__name__)", v="salida")
P("P16-8", "16", 5, "¿Cuándo es mejor una función con `def` que una lambda?",
  ["Cuando la lógica no cabe en una expresión o se va a usar en varios sitios", "Siempre que tenga parámetros",
   "Nunca: las lambdas son siempre más claras", "Cuando se pasa como key a sorted"], 0,
  "Una lambda es una sola expresión, pensada para usar y tirar. Si la lógica crece o se reutiliza, una función con nombre se lee y se prueba mejor.")

P("P17-1", "17", 5, "¿Qué modo abre un fichero para **leer bytes**?", ['"rb"', '"rt"', '"w+"', '"a"'], 0,
  "La `b` indica modo binario; la `t` (o nada) es modo texto. `\"w+\"` lee y escribe, pero en texto, y vaciando el fichero.", mono=True)
P("P17-2", "17", 5, "¿Qué imprime este programa?", ["bytearray(b'Abc')", "bytearray(b'abc')", "bytearray(b'65bc')", "Lanza TypeError"], 0,
  "Un `bytearray` se puede modificar casilla a casilla; cada casilla es un número de 0 a 255, y 65 es la `A`.",
  code='datos = bytearray(b"abc")\ndatos[0] = 65\nprint(datos)', v="salida", mono=True)
P("P17-3", "17", 5, "¿Qué imprime este programa?", ["3 255", "3 -1", "6 255", "3 b'\\xff'"], 0,
  "Se escriben tres bytes. Al leer en modo `\"rb\"` se obtienen `bytes`, y una posición de `bytes` es un entero.",
  code='with open("x.bin", "wb") as f:\n    f.write(bytes([1, 2, 255]))\nwith open("x.bin", "rb") as f:\n    b = f.read()\nprint(len(b), b[2])', v="salida", mono=True)
P("P17-4", "17", 5, "¿Qué imprime este programa?", ["notas.txt .txt 2026", "notas .txt datos", "notas.txt txt 2026", "notas.txt .txt datos/2026"], 0,
  "El operador `/` une trozos de ruta. `name` es el nombre con extensión, `suffix` la extensión con su punto y `parent` la carpeta que lo contiene.",
  code='from pathlib import Path\np = Path("datos") / "2026" / "notas.txt"\nprint(p.name, p.suffix, p.parent.name)', v="salida", mono=True)
P("P17-5", "17", 5, "¿Qué ocurre al ejecutar este programa?", ["Lanza FileExistsError", "Vacía el fichero", "No pasa nada", "Lanza PermissionError"], 0,
  "El modo `\"x\"` crea el fichero y falla si ya existe: la segunda apertura lanza `FileExistsError`.",
  code='with open("n.txt", "x") as f:\n    pass\nwith open("n.txt", "x") as f:\n    pass', v="error", err="FileExistsError")
P("P17-6", "17", 5, "¿Por qué flujo salen los mensajes de error y los tracebacks?", ["sys.stderr", "sys.stdout", "sys.stdin", "sys.path"], 0,
  "`sys.stderr` es la salida de errores; `sys.stdout`, la normal, y `sys.stdin`, la entrada. `sys.path` no es un flujo.", mono=True)
P("P17-7", "17", 5, "¿Qué imprime este programa?", ["['hola', 'adiós']", "['hola\\n', 'adiós\\n']", "hola adiós", "['hola', 'adiós', '']"], 0,
  "`write_text` y `read_text` escriben y leen el fichero entero; `splitlines()` lo parte en líneas sin el salto final.",
  code='from pathlib import Path\nPath("s.txt").write_text("hola\\nadiós\\n", encoding="utf-8")\nprint(Path("s.txt").read_text(encoding="utf-8").splitlines())', v="salida", mono=True)

# ---------------------------------------------------------------- 6 · pruebas, depuración, equipo e IA
P("P20-1", "20", 6, "Calcular `media = suma / 2` cuando había 3 notas es un error…", ["de lógica", "de sintaxis", "de ejecución", "léxico"], 0,
  "El programa funciona y no avisa de nada, pero el resultado es incorrecto: es un error de lógica. Solo lo cazan las pruebas.")
P("P20-2", "20", 6, "¿Qué imprime este programa?", ["ok", "Lanza AssertionError", "negativo", "True"], 0,
  "La condición del `assert` se cumple, así que no hace nada y el programa sigue.",
  code='x = 5\nassert x > 0, "negativo"\nprint("ok")', v="salida")
P("P20-3", "20", 6, "¿Qué ocurre al ejecutar este programa?", ["Lanza AssertionError", "Imprime 6", "No pasa nada", "Lanza ValueError"], 0,
  "`doble(2)` devuelve 6, no 4: la comprobación falla y el `assert` lanza `AssertionError` con el mensaje.",
  code='def doble(x):\n    return x * 3\n\nassert doble(2) == 4, "doble falla"', v="error", err="AssertionError")
P("P20-4", "20", 6, "En un traceback, ¿dónde aparecen el tipo de error y su mensaje?",
  ["En la última línea", "En la primera línea", "En la línea del medio", "En ninguna: hay que deducirlo del código"], 0,
  "Un traceback se lee de abajo arriba: la última línea dice qué error ha sido, y las de encima, por dónde ha pasado el programa.")
P("P20-5", "20", 6, "En `unittest`, ¿qué métodos de un `TestCase` se ejecutan como pruebas?",
  ["Los que empiezan por test", "Todos los métodos de la clase", "Los que terminan en _prueba", "Solo el método main"], 0,
  "`unittest` busca los métodos cuyo nombre empieza por `test` y ejecuta cada uno como una prueba independiente.")
P("P20-6", "20", 6, "¿Qué comprueba `with self.assertRaises(ValueError):` en una prueba?",
  ["Que el bloque lance ValueError", "Que el bloque no lance ningún error",
   "Que el resultado del bloque sea igual a ValueError", "Que ValueError exista en Python"], 0,
  "La prueba pasa si el código del bloque lanza esa excepción, y falla si no la lanza. Sirve para probar las entradas no válidas.")
P("P20-7", "20", 6, "Para una función que calcula la media de una lista, ¿cuál de estos es un **caso límite**?",
  ["Una lista con un solo elemento", "Una lista de cinco notas normales", "Una lista ya ordenada", "Una lista de números enteros"], 0,
  "Los casos límite están en el borde de lo permitido: un solo elemento, la lista vacía, el valor más grande… Las otras opciones son casos típicos.")
P("P20-8", "20", 6, "¿Qué es una **regresión**?",
  ["Algo que funcionaba y deja de funcionar después de un cambio", "Un error de sintaxis",
   "Una prueba que tarda mucho en ejecutarse", "Volver a una versión anterior del código"], 0,
  "Por eso las pruebas se vuelven a ejecutar después de cada cambio: para cazar lo que se ha roto sin querer.")
P("P20-9", "20", 6, "¿Para qué sirve una **rama** en Git?",
  ["Para trabajar en un cambio en paralelo sin tocar la línea principal", "Para borrar el historial del proyecto",
   "Para copiar el repositorio a otro ordenador", "Para ejecutar las pruebas automáticamente"], 0,
  "Cada mejora se hace en su rama y se une a la principal, normalmente con un pull request revisado, cuando está lista.")
P("P20-10", "20", 6, "¿Cuándo aparece un **conflicto** al unir dos ramas?",
  ["Cuando las dos han cambiado las mismas líneas de un fichero", "Cuando las dos ramas tienen commits",
   "Cuando una rama tiene más ficheros que la otra", "Cuando se usa un pull request"], 0,
  "Git no sabe cuál de los dos cambios vale y lo tiene que decidir una persona. Se previenen con ramas cortas, uniendo a menudo y hablando con el equipo.")
P("P20-11", "20", 6, "¿Qué hace la **integración continua** (CI)?",
  ["Ejecuta automáticamente las pruebas cada vez que se sube un cambio", "Escribe las pruebas por ti",
   "Une las ramas sin necesidad de revisión", "Publica el código sin probarlo"], 0,
  "Su resultado ayuda a decidir si un cambio se puede unir: si las pruebas fallan, no se une.")
P("P20-12", "20", 6, "Un asistente de IA te propone un código. ¿Qué debes hacer antes de usarlo?",
  ["Ejecutarlo y probarlo con tus propios casos", "Comprobar que los módulos y funciones que usa existen de verdad",
   "Usarlo tal cual si el asistente asegura que está probado", "Darle tus contraseñas para que lo configure"], [0, 1],
  "La persona revisa, prueba y sigue siendo responsable del código. Los asistentes pueden inventar funciones verosímiles, y nunca se les dan credenciales.")
P("P20-13", "20", 6, "¿Qué no debes pegar nunca en un asistente de IA?",
  ["Claves de API y datos personales de otras personas", "El enunciado de un ejercicio",
   "Un mensaje de error de Python", "Un ejemplo de código con datos inventados"], 0,
  "Las credenciales, los datos personales y el código que no puedas compartir se protegen. Si hace falta un ejemplo, se usan datos inventados.")
