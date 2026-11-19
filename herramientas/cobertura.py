"""cobertura.py · escribe capitulos/cobertura.md: qué capítulo cubre cada objetivo oficial del PCEP y del PCAP.

Uso:   python herramientas/cobertura.py

Los objetivos son los de los temarios oficiales del Python Institute (PCEP-30-03 y PCAP-31-04,
versión 1.5 del 2 de noviembre de 2026), resumidos en castellano. Para cada objetivo se indica en
qué capítulos se trabaja y una lista de pruebas: términos que tienen que aparecer en esos capítulos.
Si falta alguno, el objetivo sale como parcial y la página dice cuál. Así, si un capítulo cambia y
pierde algo del temario, basta con volver a ejecutar este script para verlo.
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CAP = RAIZ / "capitulos"

# objetivo: (código, qué pide, [capítulos], [pruebas: expresiones regulares que deben aparecer])
PCEP = {
    "codigo": "PCEP-30-03", "nivel": "Entry", "preguntas": 35, "minutos": 50, "aprobado": 70,
    "url": "https://pythoninstitute.org/pcep-exam-syllabus", "banco": "pcep", "simulacro": "simulacro-pcep.md",
    "secciones": [
        ("1", "Fundamentos de programación y de Python", 6, 17, [
            ("1.1.1", "Cómo es un lenguaje y cómo se ejecuta: léxico, sintaxis, semántica, errores, intérprete y compilador",
             ["21"], ["léxico", "sintaxis", "semántica", "intérprete", "compilador"]),
            ("1.2.1", "Reglas de estructura: palabras reservadas, expresiones e instrucciones, sangría, comentarios",
             ["21", "06"], ["palabras reservadas", "instrucción", "sangría", "comentario"]),
            ("1.3.1", "Literales int, float, str y bool, y los límites de la coma flotante",
             ["05", "21"], [r"0b|0x", r"\b1e", "True", r"0\.1 \+ 0\.2"]),
            ("1.3.2", "Variables e identificadores, con las reglas de nombres y la guía PEP 8",
             ["04", "21"], ["identificador", "PEP 8"]),
            ("1.4.1", "Operadores numéricos, de cadenas, de asignación, lógicos y de comparación, y su prioridad",
             ["05", "21"], ["//", r"\*\*", "prioridad", r"\band\b", "=="]),
            ("1.4.2", "Entrada y salida por consola con print() e input(), y conversión de tipos",
             ["04", "05", "21"], [r"input\(", r"int\(", r"float\(", "sep=", "end="]),
        ]),
        ("2", "Control del flujo: condicionales y bucles", 8, 23, [
            ("2.1.1", "if e if-else", ["06"], [r"\bif\b", "else:"]),
            ("2.1.2", "Cadenas if-elif-else y el orden de las ramas", ["06"], ["elif", "orden"]),
            ("2.1.3", "Condiciones compuestas y anidadas", ["06"], [r"\band\b", r"\bor\b", "anidad"]),
            ("2.2.1", "while, valores centinela, bucles infinitos y el operador morsa",
             ["07", "25"], [r"\bwhile\b", "centinela", "infinit", ":="]),
            ("2.2.2", "for y el recorrido de iterables con in", ["07", "08"], [r"for \w+ in "]),
            ("2.2.3", "range() con inicio, fin y paso", ["07"], [r"range\(\d+, \d+, -?\d+\)|range\(\w+, \w+, \w+\)"]),
            ("2.2.4", "Bucles anidados y estructuras combinadas", ["25"], ["anidad"]),
            ("2.2.5", "break, continue y pass", ["25"], [r"\bbreak\b", r"\bcontinue\b", r"\bpass\b"]),
        ]),
        ("3", "Colecciones: listas, tuplas, conjuntos, diccionarios y cadenas", 9, 26, [
            ("3.1.1", "Crear listas, índices positivos y negativos, rebanadas y copias",
             ["08", "22"], [r"\[-1\]", "rebanad", "copia"]),
            ("3.1.2", "Modificar, buscar, ordenar y recorrer listas; in y len()",
             ["08", "22"], [r"append\(", r"insert\(", r"remove\(", r"index\(", r"sort\(", r"len\("]),
            ("3.1.3", "Listas multidimensionales", ["22"], [r"\]\["]),
            ("3.2.1", "Tuplas: inmutabilidad, anidamiento y diferencias con las listas", ["23"], ["tupla", "TypeError"]),
            ("3.3.1", "Conjuntos: crear, añadir, quitar y pertenencia", ["23"], [r"set\(", r"add\(", r"discard\(|remove\("]),
            ("3.4.1", "Diccionarios: acceso, cambios, borrado y recorrido con keys(), values() e items()",
             ["11"], [r"keys\(\)", r"values\(\)", r"items\(\)", r"del |pop\("]),
            ("3.5.1", "Construir cadenas: comillas, escapes, multilínea, índices, rebanadas e inmutabilidad",
             ["10", "26"], ["escape", r"'''|\"\"\"", "inmutab", r"\[::-1\]"]),
            ("3.5.2", "Transformar cadenas: mayúsculas, find(), split(), join(), strip(), replace()",
             ["10", "19", "26"], [r"upper\(", r"find\(", r"split\(", r"join\(", r"strip\(", r"replace\("]),
            ("3.5.3", "Dar formato: f-strings, format() y el operador %", ["26"], [r'f"', r"format\(", "%s|%d"]),
        ]),
        ("4", "Funciones y excepciones", 7, 20, [
            ("4.1.1", "Definir y llamar funciones propias", ["09"], [r"\bdef "]),
            ("4.1.2", "Valores devueltos, None y devolver varios valores", ["09", "24"], ["return", "None", r"return \w+, \w+"]),
            ("4.1.3", "Parámetros, argumentos, valores por defecto y argumentos con nombre",
             ["09", "24"], ["por defecto", "con nombre"]),
            ("4.1.4", "*args y **kwargs", ["24"], [r"\*args", r"\*\*kwargs"]),
            ("4.1.5", "Ámbito local y global, nombres que se tapan y la instrucción `global`", ["09", "24"], [r"\bglobal\b", "local", "sombre"]),
            ("4.2.1", "Excepciones básicas de Python y cuándo saltan",
             ["13"], ["ValueError", "ZeroDivisionError", "IndexError", "KeyError", "TypeError", "NameError"]),
            ("4.2.2", "Atender excepciones con try y except", ["13"], ["try:", "except"]),
        ]),
        ("5", "Ficheros e importación de módulos", 5, 14, [
            ("5.1.1", "Ficheros de texto: modos `r`, `w` y `a`, y la instrucción with",
             ["17", "27"], [r"\"r\"|'r'", r"\"w\"|'w'", r"\"a\"|'a'", "with open"]),
            ("5.1.2", "Ficheros CSV con el módulo csv: reader() y writer()", ["27"], [r"csv\.reader", r"csv\.writer"]),
            ("5.2.1", "Importar y usar módulos", ["12", "27"], [r"\bimport ", r"from \w+ import"]),
            ("5.2.2", "El módulo math: ceil(), floor(), trunc(), sqrt()", ["27"], ["ceil", "floor", "trunc", "sqrt"]),
            ("5.2.3", "El módulo random: random(), seed(), choice(), sample()", ["27"], [r"random\(\)", "seed", "choice", "sample"]),
        ]),
    ],
}

PCAP = {
    "codigo": "PCAP-31-04", "nivel": "Associate", "preguntas": 42, "minutos": 65, "aprobado": 72,
    "url": "https://pythoninstitute.org/pcap-exam-syllabus", "banco": "pcap", "simulacro": "simulacro-pcap.md",
    "secciones": [
        ("1", "Módulos y paquetes", 5, 12, [
            ("1.1.1", "Formas de import, alias, import *, nombres cualificados y nombres que chocan",
             ["12"], [r"import \w+ as ", r"import \*", "tapa"]),
            ("1.1.2", "dir(), la ruta de búsqueda sys.path y los fallos al importar",
             ["12"], [r"dir\(", r"sys\.path", "ModuleNotFoundError"]),
            ("1.2.1", "Módulos propios, if __name__ == \"__main__\", __pycache__ e importaciones circulares",
             ["12"], ["__name__", "__pycache__", "circular"]),
            ("1.2.2", "Paquetes y subpaquetes, el papel de __init__.py y los errores al importarlos",
             ["12"], [r"__init__\.py", "subpaquete"]),
            ("1.3.1", "PyPI, pip y requirements.txt", ["12"], ["PyPI", "pip install", r"requirements\.txt"]),
        ]),
        ("2", "Excepciones", 5, 12, [
            ("2.1.1", "Orden de los except, varios tipos a la vez, el objeto excepción y qué rama atiende",
             ["13"], [r"except \(", "as e", "orden"]),
            ("2.1.2", "else y finally con try y except", ["13"], ["else:", "finally"]),
            ("2.1.3", "La jerarquía de excepciones, BaseException frente a Exception, y args",
             ["13"], ["jerarqu", "BaseException", r"\.args"]),
            ("2.1.4", "Lanzar excepciones, volver a lanzarlas y cómo se propagan entre funciones",
             ["13"], [r"\braise\b", "vuelve a lanzar", "propaga|sube"]),
            ("2.2.1", "Definir, lanzar y organizar excepciones propias", ["13"], [r"class \w+\(Exception\)"]),
        ]),
        ("3", "Cadenas", 4, 9.5, [
            ("3.1.1", "ASCII, Unicode, UTF-8, str frente a bytes, ord() y chr()",
             ["19"], ["ASCII", "Unicode", "UTF-8", "bytes", r"ord\(", r"chr\("]),
            ("3.2.1", "Inmutabilidad, cadenas nuevas, igualdad y orden entre cadenas", ["19"], ["inmutab", "compar"]),
            ("3.2.2", "Los métodos is…() y cómo combinarlos", ["19"], ["isdigit", "isalpha", "isspace"]),
            ("3.2.3", "Buscar: index, find, rindex, rfind, count, startswith, endswith y sorted()",
             ["19"], ["rindex", "rfind", r"count\(", "startswith", "endswith", "sorted"]),
        ]),
        ("4", "Programación orientada a objetos", 12, 28.5, [
            ("4.1.1", "Los cuatro pilares: abstracción, encapsulación, herencia y polimorfismo",
             ["14", "18"], ["bstracci", "ncapsula", "herencia", "polimorf"]),
            ("4.1.2", "Clases, objetos, atributos, métodos y cómo se relacionan", ["14"], [r"\bclass ", r"\bself\b", "atributo", "método"]),
            ("4.2.1", "Variables de clase y de instancia, y atributos que se tapan", ["14", "18"], ["atributos? de clase", "instancia"]),
            ("4.2.2", "__dict__ y la desfiguración de nombres", ["18"], ["__dict__", "mangling"]),
            ("4.3.1", "Métodos de instancia, self, argumentos y __str__()", ["14", "18"], [r"\bself\b", "__str__"]),
            ("4.4.1", "hasattr(), getattr() y la búsqueda de atributos por la jerarquía", ["18"], ["hasattr", "getattr"]),
            ("4.4.2", "Los metadatos de una clase: __name__, __module__ y __bases__", ["18"], ["__name__", "__module__", "__bases__"]),
            ("4.5.1", "Herencia simple, sobrescribir métodos y super()", ["14", "18"], [r"super\(\)", "sobrescri"]),
            ("4.5.2", "Herencia múltiple, el MRO, el rombo y super() cooperativo", ["18"], ["MRO|__mro__", "rombo|diamante"]),
            ("4.5.3", "isinstance(), is frente a ==, y polimorfismo", ["18"], ["isinstance", r"\bis\b", "polimorf"]),
            ("4.6.1", "__init__(), atributos, valores por defecto y super().__init__()", ["14", "18"], ["__init__", r"super\(\)\.__init__"]),
            ("4.6.2", "Argumentos con nombre, validar con excepciones y valores por defecto mutables",
             ["18"], [r"\braise\b", r"=\[\]"]),
        ]),
        ("5", "Construcciones avanzadas y entrada y salida", 10, 24, [
            ("5.1.1", "Comprensiones de lista, conjunto y diccionario, con filtros y expresiones condicionales",
             ["15"], [r"\[[^\]]* for \w+ in ", r"\{[^}]* for \w+ in ", r" if [^\]]* else "]),
            ("5.1.2", "Comprensiones anidadas, orden de los for y aplanar listas", ["15"], ["anidad", "aplan"]),
            ("5.2.1", "match-case y sus diferencias con if-elif-else", ["15"], [r"\bmatch\b", r"\bcase\b"]),
            ("5.2.2", "El else de while y de for, y cuándo se ejecuta", ["15"], ["else", r"\bbreak\b", r"\bwhile\b"]),
            ("5.3.1", "Funciones lambda y cuándo es mejor una función con nombre", ["16"], ["lambda"]),
            ("5.3.2", "map() y filter() como iteradores, y convertir su resultado", ["16"], [r"map\(", r"filter\(", r"list\("]),
            ("5.3.3", "Cierres, funciones que devuelven funciones y fábricas", ["16"], ["cierre", "f[áa]brica"]),
            ("5.4.1", "Flujos estándar (sys.stdin, sys.stdout, sys.stderr), modo texto y binario, modos de apertura",
             ["17"], [r"sys\.stdin", r"sys\.stdout", r"sys\.stderr", "binari"]),
            ("5.4.2", "Ficheros con with, leer y escribir, bytearray y excepciones de ficheros",
             ["17"], ["with open", "bytearray", "FileNotFoundError|OSError"]),
            ("5.4.3", "pathlib: rutas, recorrer carpetas y leer y escribir texto y bytes",
             ["17"], ["pathlib", "iterdir", "read_text", "write_bytes"]),
        ]),
        ("6", "Pruebas, depuración, trabajo en equipo e IA", 6, 14, [
            ("6.1.1", "Pruebas unitarias, casos de prueba, assert, aislamiento y regresiones",
             ["20"], ["unittest", "TestCase", r"\bassert\b", "aislad", "regres"]),
            ("6.1.2", "Errores de sintaxis, de ejecución y de lógica; leer tracebacks y comprobar arreglos",
             ["20"], ["sintaxis", "ejecución", "lógica", "traceback"]),
            ("6.2.1", "Repositorios compartidos, ramas, commits, pull requests y conflictos",
             ["20"], ["rama", "commit", "pull request", "conflicto"]),
            ("6.2.2", "Issues, documentación, revisiones de código, pruebas automáticas e integración continua",
             ["20"], ["issue", "revisi", "integración continua"]),
            ("6.3.1", "Pedir a la IA con contexto y restricciones, y evaluar y afinar lo que devuelve",
             ["20"], ["requisitos", "contexto", "restricciones"]),
            ("6.3.2", "Revisión humana, probar el código de la IA, verificar referencias, proteger datos y responsabilidad",
             ["20"], ["responsable", "pruébalo", "existen de verdad", "contraseñas|datos personales"]),
        ]),
    ],
}


def capitulos():
    """{"06": (fichero, título, texto sin las trazas JSON)}"""
    r = {}
    for ruta in sorted(CAP.glob("[0-9][0-9]-*.md")):
        texto = ruta.read_text(encoding="utf-8")
        titulo = re.search(r"^title:\s*(.+)$", texto, re.M).group(1).strip().strip('"')
        prosa = "\n".join(l for l in texto.split("\n") if not l.startswith("{"))
        r[ruta.name[:2]] = (ruta.name, titulo, prosa)
    return r


def banco_por_seccion(nombre):
    datos = json.loads((RAIZ / "datos" / f"{nombre}.json").read_text(encoding="utf-8"))
    cuenta = {}
    for q in datos["preguntas"]:
        cuenta[q["sec"]] = cuenta.get(q["sec"], 0) + 1
    return cuenta


FIJOS = ['if __name__ == "__main__"', "super().__init__()", "__init__.py", "__init__()", "__str__()", "__name__",
         "__pycache__", "__dict__", "__module__", "__bases__", "import *", "sys.path", "sys.stdin", "sys.stdout",
         "sys.stderr", "requirements.txt", "**kwargs", "*args", "if-elif-else", "if-else", "match-case", "is…()"]
PALABRAS = ["import", "try", "except", "else", "finally", "with", "while", "for", "in", "is", "if", "None", "break",
            "continue", "pass", "lambda", "BaseException", "Exception", "bytes", "str", "bytearray", "pathlib", "csv",
            "math", "random", "int", "float", "bool", "pip", "args", "index", "find", "rindex", "rfind", "count",
            "startswith", "endswith", "assert", "self", "==", "%"]


def codifica(texto):
    """Pone entre comillas invertidas lo que es código (si no, «__name__» saldría en negrita)."""
    trozos = [re.escape(f) for f in sorted(FIJOS, key=len, reverse=True)]
    trozos += [r"\b\w+\(\)", r"(?<![\w`])(?:" + "|".join(re.escape(w) for w in PALABRAS) + r")(?![\w`(])"]
    return re.sub("|".join(trozos), lambda m: f"`{m.group(0)}`", texto)


def evalua(objetivo, caps):
    codigo, pide, nums, pruebas = objetivo
    texto = "\n".join(caps[n][2] for n in nums)
    faltan = [p for p in pruebas if not re.search(p, texto, re.I)]
    estado = "✓" if not faltan else ("◐" if len(faltan) < len(pruebas) else "✗")
    return estado, faltan


def enlaces(nums, caps):
    return " · ".join(f"[{caps[n][1]}]({caps[n][0]})" for n in nums)


def pagina():
    caps = capitulos()
    lineas = ['---', 'title: El temario oficial, objetivo a objetivo',
              'subtitle: Dónde cubre este libro cada punto del PCEP y del PCAP', '---', '',
              'El Python Institute publica el temario de cada examen como una lista de **objetivos** numerados. '
              'Esta página los recorre todos, resumidos en castellano, y dice en qué capítulos del libro se trabaja cada uno.', '',
              'Los temarios son los de la **versión 1.5**, revisada por el Python Institute el **2 de noviembre de 2026**. '
              'El texto oficial completo, en inglés, está en '
              f'[el temario del PCEP]({PCEP["url"]}) y [el temario del PCAP]({PCAP["url"]}).', '',
              ':::{note} Cómo se comprueba', 'La página la escribe el script `herramientas/cobertura.py`. Para cada objetivo, '
              'busca en los capítulos indicados los términos que ese objetivo exige: ✓ si están todos, ◐ si falta alguno '
              '(y dice cuál) y ✗ si no hay ninguno. Si un capítulo cambia, se vuelve a ejecutar y la página se pone al día sola.',
              ':::', '']
    resumen, cuerpos = [], []
    for ex in (PCEP, PCAP):
        banco = banco_por_seccion(ex["banco"])
        filas_res, total_ok, total = [], 0, 0
        cuerpo = [f'## {ex["codigo"]}', '',
                  f'{ex["preguntas"]} preguntas en {ex["minutos"]} minutos; se aprueba con el {ex["aprobado"]} %. '
                  f'Puedes practicarlo entero en el [simulacro]({ex["simulacro"]}).', '']
        for num, nombre, items, peso, objetivos in ex["secciones"]:
            evals = [evalua(o, caps) for o in objetivos]
            ok = sum(e[0] == "✓" for e in evals)
            total_ok += ok
            total += len(objetivos)
            peso_txt = f"{peso:g}".replace(".", ",")
            filas_res.append(f'| {num} · {nombre} | {items} | {peso_txt} % | {ok} de {len(objetivos)} | {banco.get(num, 0)} |')
            cuerpo += [f'### Sección {num} · {nombre}', '',
                       f'{items} preguntas del examen ({peso_txt} %) · {banco.get(num, 0)} preguntas en el banco del libro', '',
                       '| Objetivo | Qué pide | Dónde está en el libro | |', '|---|---|---|---|']
            for o, (estado, faltan) in zip(objetivos, evals):
                nota = estado if not faltan else f'{estado} falta: {", ".join(f"`{f}`" for f in faltan)}'
                cuerpo.append(f'| **{o[0]}** | {codifica(o[1])} | {enlaces(o[2], caps)} | {nota} |')
            cuerpo.append('')
        resumen += [f'**{ex["codigo"]}** · {total_ok} de {total} objetivos cubiertos', '',
                    '| Sección | Preguntas del examen | Peso | Objetivos cubiertos | Preguntas en el banco |',
                    '|---|---|---|---|---|'] + filas_res + ['']
        cuerpos += cuerpo
    lineas += ['## De un vistazo', ''] + resumen + cuerpos
    lineas += ['## Lo que no entra en el libro', '',
               'Nada del temario oficial se queda fuera: todos los objetivos tienen al menos un capítulo. '
               'Lo que el libro **añade** por su cuenta, porque ayuda a entender, es la parte de pensar antes de programar '
               '(especificación, algoritmo y trazas), los generadores y el laboratorio.', '']
    (CAP / "cobertura.md").write_text("\n".join(lineas), encoding="utf-8")
    return caps


if __name__ == "__main__":
    caps = pagina()
    for ex in (PCEP, PCAP):
        for _, _, _, _, objetivos in ex["secciones"]:
            for o in objetivos:
                estado, faltan = evalua(o, caps)
                if faltan:
                    print(ex["codigo"], o[0], estado, "falta:", faltan)
    print("escrito capitulos/cobertura.md")
