"""trazar.py · genera las trazas de los visualizadores de un capítulo.

Uso:   python herramientas/trazar.py capitulos/08-recorrer-listas.md

Busca en el capítulo cada directiva {anywidget} que carga traza.mjs, toma la
celda {code-cell} que la precede, ejecuta ese código con sys.settrace y escribe
en el cuerpo JSON de la directiva la traza resultante. La parte "config" de cada
directiva (qué lista dibujar, qué línea es la cabecera del bucle, columnas de la
tabla…) la escribes tú y se conserva tal cual. Si cambias el código de una
celda, vuelve a ejecutar este script.

Claves de "config":
  titulo, etiqueta, idea      textos del visualizador
  lista                       nombre de la lista que se dibuja como casillas
  cabecera                    número de línea del for / while
  puntero                     variable que señala la casilla actual (i, nota…)
  foco                        "vuelta" (for por elementos) o el nombre del índice ("i")
  columnas                    expresiones de la tabla de traza, p. ej. ["i", "notas[i]", "total"]
  fila_en                     "fin_iteracion" (for) o "comprobacion" (while)
  soltar                      (opcional) línea a partir de la cual se deja de señalar casilla
  mostrar_tipos               (opcional) true para enseñar el tipo de cada variable (int, str…)
  diccionario                 (opcional) nombre de un diccionario que se dibuja como tabla clave → valor
  foco: "ninguno"             (opcional) dibuja la lista sin señalar ninguna casilla
  entradas                    (opcional) lo que se «teclea» en cada input(), p. ej. ["7", "3"]
  matriz, fila, col           (opcional) una lista de listas que se dibuja como tabla, con la
                              casilla [fila][col] señalada

La "lista" también puede ser una cadena: cada carácter es una casilla.
Si el programa define funciones, cada llamada aparece como un marco con sus
variables locales, y el paso del return muestra el valor devuelto.
Los objetos de las clases del alumno se dibujan con un número (Cuenta nº1):
si dos variables muestran el mismo número, son el mismo objeto.
Si una línea lanza una excepción, el paso la muestra y el siguiente es el except.
Las lambdas y los cierres guardados en variables se ven como valores; los generadores
se pausan en cada yield y se reanudan; las comprensiones de listas muestran, vuelta a
vuelta, el elemento que calculan; y si el programa escribe ficheros, se dibuja el disco
(el código se ejecuta en una carpeta temporal).

Para programas sin lista ni bucle: omite "lista" y "cabecera", y usa
  fila_en: "cada_linea"       una fila de la tabla por cada línea ejecutada
  columnas: ["a", "b"]        variables que aparecen en la tabla
"""
import ast, builtins, contextlib, copy, dis, inspect, io, json, linecache, os, re, shutil, sys, tempfile, traceback, types
from pathlib import Path, PurePath

ENTORNO = {"len": len, "range": range, "sum": sum, "max": max, "min": min, "abs": abs}


def sustituye(expr, estado):
    """'notas[i] > maximo' -> '4 > 7': cambia nombres y consultas por sus valores."""
    def valor(nodo):
        return eval(compile(ast.Expression(nodo), "", "eval"), dict(ENTORNO), dict(estado))

    class Sustituto(ast.NodeTransformer):
        def visit_Subscript(self, n):
            try: return ast.Constant(valor(n))
            except Exception: return n

        def visit_Call(self, n):
            try: return ast.Constant(valor(n))
            except Exception: return n

        def visit_Name(self, n):
            if n.id in estado and isinstance(estado[n.id], (int, float, str, bool, type(None), tuple)):
                return ast.Constant(estado[n.id])
            return n

    try:
        return ast.unparse(Sustituto().visit(ast.parse(expr, mode="eval")))
    except Exception:
        return expr


ARCHIVO = "programa.py"          # nombre con el que el código del alumno sale en los tracebacks
CODIGO = {"texto": ""}          # el programa que se está trazando (para escribir las lambdas)
LIMITE = None                   # máximo de pasos; el laboratorio del navegador lo fija para cortar bucles sin fin


class DemasiadosPasos(Exception):
    """El programa ha dado más pasos que LIMITE (casi siempre, un bucle que no termina)."""


def funcion_como_valor(k, v):
    """Una función que vale la pena ver como valor: una lambda, un cierre o un alias."""
    return isinstance(v, types.FunctionType) and (
        v.__name__ == "<lambda>" or "<locals>" in v.__qualname__ or v.__name__ != k)


def visible(k, v):
    if k.startswith("__") or isinstance(v, (types.ModuleType, type)):
        return False
    return funcion_como_valor(k, v) if callable(v) else True


def copia(v):
    try:
        return copy.deepcopy(v)
    except Exception:            # generadores, ficheros…: se guarda la referencia
        return v


def foto(d):
    """Copia real de las variables visibles (para evaluar expresiones después)."""
    return {k: copia(v) for k, v in d.items() if visible(k, v)}


def describe_funcion(f):
    params = ", ".join(f.__code__.co_varnames[:f.__code__.co_argcount])
    if f.__name__ == "<lambda>":
        texto = f"lambda {params}: …"
        try:
            linea = CODIGO["texto"].split("\n")[f.__code__.co_firstlineno - 1]
            lambdas = [n for n in ast.walk(ast.parse(linea.strip())) if isinstance(n, ast.Lambda)]
            if len(lambdas) == 1:
                texto = ast.unparse(lambdas[0])
        except Exception:
            pass
    else:
        texto = f"función {f.__name__}({params})"
    if f.__closure__:
        recuerda = ", ".join(f"{n} = {c.cell_contents!r}" for n, c in zip(f.__code__.co_freevars, f.__closure__))
        texto += f" · recuerda {recuerda}"
    return texto


def cuerpo_lambda(code):
    """El cuerpo de una lambda, 'a[1]', leído del código del alumno."""
    try:
        linea = CODIGO["texto"].split("\n")[code.co_firstlineno - 1]
        lambdas = [n for n in ast.walk(ast.parse(linea.strip())) if isinstance(n, ast.Lambda)]
        return ast.unparse(lambdas[0].body) if len(lambdas) == 1 else None
    except Exception:
        return None


def nombre_de(code):
    q = getattr(code, "co_qualname", code.co_name)
    return code.co_name if "<locals>" in q else q


def es_objeto(v):
    """Objeto de una clase definida por el alumno."""
    return hasattr(v, "__dict__") and not isinstance(v, (type, types.ModuleType, BaseException)) \
        and type(v).__module__ == "__main__"


def marca(v, numeros):
    """Versión para el visualizador: cada objeto se convierte en {nº, clase, atributos}.
    El número es el mismo mientras sea el mismo objeto, así se ven los alias."""
    if es_objeto(v):
        n = numeros.setdefault(id(v), len(numeros) + 1)
        return {"__obj__": n, "__clase__": type(v).__name__,
                "attrs": {k: marca(x, numeros) for k, x in vars(v).items()}}
    if isinstance(v, list):
        return [marca(x, numeros) for x in v]
    if isinstance(v, tuple):
        return {"__tupla__": [marca(x, numeros) for x in v]}
    if isinstance(v, dict):
        return {str(k): marca(x, numeros) for k, x in v.items()}
    if isinstance(v, BaseException):
        return {"__exc__": repr(v)}
    if isinstance(v, float) and v != v or v in (float("inf"), float("-inf")) and isinstance(v, float):
        return {"__txt__": repr(v)}               # inf y nan no existen en JSON
    if isinstance(v, (bool, int, float, str, type(None))):
        return v
    if isinstance(v, types.FunctionType):
        return {"__txt__": describe_funcion(v)}
    if isinstance(v, types.GeneratorType):
        return {"__txt__": f"generador {v.__name__}" + (" (agotado)" if v.gi_frame is None else "")}
    if isinstance(v, io.IOBase):
        nombre = getattr(v, "name", "?")
        return {"__txt__": f"fichero '{nombre}' " + ("(cerrado)" if v.closed else f"abierto en modo '{getattr(v, 'mode', '?')}'")}
    if isinstance(v, PurePath):
        return {"__txt__": f"Path('{v.as_posix()}')"}
    if isinstance(v, (bytes, bytearray)):
        return {"__bytes__": list(v), "repr": repr(v)}
    if isinstance(v, (set, frozenset)):
        return {"__txt__": ("{" + ", ".join(sorted(repr(x) for x in v)) + "}") if v else "set()"}
    return {"__txt__": re.sub(r" at 0x[0-9a-fA-F]+", "", repr(v))}


def muestra(v):
    """Cómo se escribe un valor marcado: los objetos como «Cuenta nº1»."""
    if isinstance(v, dict) and "__obj__" in v:
        return f"{v['__clase__']} nº{v['__obj__']}"
    if isinstance(v, dict) and "__exc__" in v:
        return v["__exc__"]
    if isinstance(v, dict) and "__txt__" in v:
        return v["__txt__"]
    if isinstance(v, dict) and "__bytes__" in v:
        return v["repr"]
    if isinstance(v, dict) and "__tupla__" in v:
        t = v["__tupla__"]
        return "(" + ", ".join(muestra(x) for x in t) + ("," if len(t) == 1 else "") + ")"
    if isinstance(v, list):
        return "[" + ", ".join(muestra(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{" + ", ".join(f"{k!r}: {muestra(x)}" for k, x in v.items()) + "}"
    return repr(v)


def es_cuerpo_de_clase(frame):
    nombres = frame.f_code.co_names
    return "__module__" in nombres and "__qualname__" in nombres and frame.f_code.co_name != "<module>"


def disco():
    """Los ficheros de la carpeta de trabajo, con su contenido (texto o bytes)."""
    r = []
    for p in sorted(Path(".").iterdir()):
        if not p.is_file():
            continue
        b = p.read_bytes()
        try:
            t = b.decode("utf-8")
            binario = p.suffix in (".bin", ".dat") or any(ord(c) < 32 and c not in "\n\t\r" for c in t)
        except UnicodeDecodeError:
            binario = True
        r.append({"nombre": p.name, "tam": len(b),
                  "contenido": " ".join(f"{x:02X}" for x in b) if binario else t, "binario": binario})
    return r


CO_GENERATOR = inspect.CO_GENERATOR


def estrellas(code):
    """Los parámetros *args y **kwargs de una función: {"notas": "*", "datos": "**"}."""
    r, i = {}, code.co_argcount + code.co_kwonlyargcount
    if code.co_flags & inspect.CO_VARARGS:
        r[code.co_varnames[i]] = "*"
        i += 1
    if code.co_flags & inspect.CO_VARKEYWORDS:
        r[code.co_varnames[i]] = "**"
    return r


def clases_de(g, numeros):
    """Atributos de clase (datos, no métodos) de las clases que define el alumno."""
    r = {}
    for k, v in g.items():
        if isinstance(v, type) and v.__module__ == "__main__" and not issubclass(v, BaseException):
            datos = {a: marca(x, numeros) for a, x in vars(v).items()
                     if not a.startswith("__") and not callable(x) and not isinstance(x, (staticmethod, classmethod, property))}
            if datos:
                r[k] = datos
    return r


def ejecuta(codigo, entradas=()):
    """Ejecuta el código y devuelve un evento por cada línea (y por cada return de función),
    con las variables globales, la pila de marcos de función, lo impreso y los errores."""
    CODIGO["texto"] = codigo
    eventos, salida, numeros = [], io.StringIO(), {}
    pendientes = list(entradas)

    def entrada_simulada(mensaje=""):
        """input() de mentira: escribe el mensaje y «teclea» la siguiente entrada de la lista."""
        valor = pendientes.pop(0) if pendientes else ""
        salida.write(f"{mensaje}{valor}\n")
        return valor
    estado_error = {"propagando": False}

    def tracer(frame, evento, arg):
        if frame.f_code.co_filename != ARCHIVO or es_cuerpo_de_clase(frame):
            return tracer
        if evento == "exception":
            if not estado_error["propagando"] and eventos:
                tipo, valor, _ = arg
                eventos[-1]["excepcion"] = f"{tipo.__name__}: {valor}" if str(valor) else tipo.__name__
                estado_error["propagando"] = True
            return tracer
        if evento in ("line", "return"):
            if LIMITE and len(eventos) >= LIMITE:
                raise DemasiadosPasos(f"El programa se ha detenido al llegar a {LIMITE} pasos. "
                                      "¿Hay un bucle que no termina nunca?")
            por_error = evento == "return" and estado_error["propagando"]
            if evento == "line":
                estado_error["propagando"] = False
            cadena, f = [], frame
            while f is not None and f.f_code.co_filename == ARCHIVO:
                if not es_cuerpo_de_clase(f):
                    cadena.append(f)
                f = f.f_back
            cadena.reverse()                       # de fuera hacia dentro: módulo, función, función…
            modulo = cadena[0]
            pila = [{"nombre": nombre_de(fr.f_code),
                     "args": list(fr.f_code.co_varnames[:fr.f_code.co_argcount]),
                     "estrella": estrellas(fr.f_code),
                     "vars": {k: marca(v, numeros) for k, v in fr.f_locals.items() if visible(k, v)},
                     "real": foto(fr.f_locals), "gen": bool(fr.f_code.co_flags & CO_GENERATOR),
                     "expr": cuerpo_lambda(fr.f_code) if fr.f_code.co_name == "<lambda>" else None} for fr in cadena[1:]]
            es_funcion = frame is not modulo
            pausa = (evento == "return" and es_funcion and not por_error and bool(frame.f_code.co_flags & CO_GENERATOR)
                     and dis.opname[frame.f_code.co_code[frame.f_lasti]] not in ("RETURN_VALUE", "RETURN_CONST"))
            # en una comprensión (que Python 3.12+ ejecuta dentro del propio módulo) f_locals
            # solo trae la variable de la comprensión: las globales salen de f_globals
            loc = modulo.f_locals
            compr = {} if loc is modulo.f_globals else {k: v for k, v in loc.items() if not k.startswith("__")}
            eventos.append({"ev": evento, "linea": frame.f_lineno,
                            "glob": foto(modulo.f_globals),
                            "glob_m": {k: marca(v, numeros) for k, v in modulo.f_globals.items() if visible(k, v)},
                            "local": foto(frame.f_locals) if es_funcion else {}, "pila": pila, "compr": foto(compr),
                            "marco": nombre_de(frame.f_code), "funcion": es_funcion,
                            "retorno": marca(arg, numeros) if (evento == "return" and es_funcion and not por_error) else None,
                            "por_error": por_error, "pausa": pausa, "salida": salida.getvalue(), "disco": disco(),
                            "clases": clases_de(modulo.f_globals, numeros)})
        return tracer

    carpeta, antes = tempfile.mkdtemp(prefix="traza-"), os.getcwd()
    os.chdir(carpeta)
    lineas = codigo.split("\n")
    linecache.cache[ARCHIVO] = (len(codigo), None, [l + "\n" for l in lineas], ARCHIVO)
    try:
        with contextlib.redirect_stdout(salida), contextlib.redirect_stderr(salida):
            sys.settrace(tracer)
            try:
                mios = {**vars(builtins), "input": entrada_simulada}
                exec(compile(codigo, ARCHIVO, "exec"), {"__name__": "__main__", "__builtins__": mios})
            except BaseException as e:          # error que nadie atiende: el programa se detiene
                sys.settrace(None)
                tb = e.__traceback__.tb_next     # sin el marco de este script
                if isinstance(e, DemasiadosPasos):
                    salida.write(str(e) + "\n")
                else:
                    salida.write("".join(traceback.format_exception(type(e), e, tb)))
                while eventos and eventos[-1]["ev"] == "return" and not eventos[-1]["funcion"]:
                    eventos.pop()                # el «return» del módulo que se interrumpe
                ultimo = eventos[-1]
                eventos.append({**ultimo, "ev": "fin", "pila": [], "local": {}, "funcion": False,
                                "salida": salida.getvalue(), "disco": disco()})
            finally:
                sys.settrace(None)
    finally:
        os.chdir(antes)
        shutil.rmtree(carpeta, ignore_errors=True)
    return eventos


def comprension(texto):
    """Si la línea contiene una comprensión de lista o de diccionario con un solo for,
    devuelve (nodo, variable); si no, None."""
    try:
        arbol = ast.parse(texto)
    except SyntaxError:
        return None
    for n in ast.walk(arbol):
        if isinstance(n, (ast.ListComp, ast.DictComp)) and len(n.generators) == 1 \
                and isinstance(n.generators[0].target, ast.Name):
            return n, n.generators[0].target.id
    return None


def contexto(ev):
    """Variables que ve la línea que se ejecuta: globales más las locales de su función."""
    return {**ev["glob"], **ev["local"]}


def traza(codigo, cfg):
    lineas = codigo.split("\n")
    lista, cab = cfg.get("lista"), cfg.get("cabecera")
    eventos = ejecuta(codigo, cfg.get("entradas", ()))
    pasos = [{"linea": None, "estado": {}, "salida": "", "foco": None, "lee": False, "cond": None, "vuelta": 0,
              "fila": None, "repr": {}, "tipos": {}, "pila": [], "devuelve": None, "excepcion": None}]
    filas, vueltas = [], 0
    parcial, linea_compr = None, None
    hay_disco = any(e["disco"] for e in eventos)
    hay_clases = any(e["clases"] for e in eventos)

    def foco(estado):
        if not lista:
            return None
        arr = estado.get(lista)
        if isinstance(arr, dict) and "__bytes__" in arr:
            arr = arr["__bytes__"]
        if not isinstance(arr, (list, str)):
            return None
        if cfg.get("foco") == "ninguno":
            return None
        if cfg.get("foco", "vuelta") == "vuelta":
            return vueltas - 1 if 0 < vueltas <= len(arr) and cfg["puntero"] in estado else None
        idx = estado.get(cfg["foco"])
        return idx if isinstance(idx, int) and 0 <= idx < len(arr) else None

    def evalua(expr, ctx):
        try:
            return muestra(marca(eval(expr, dict(ENTORNO), dict(ctx)), {}))
        except Exception:
            return "—"

    for ejec, despues in zip(eventos, eventos[1:]):
        n = ejec["linea"]
        texto = lineas[n - 1].strip()
        devuelve = None
        if ejec["ev"] == "return":
            if not ejec["funcion"]:
                continue
            devuelve = {"funcion": ejec["marco"], "valor": muestra(ejec["retorno"]), "error": ejec["por_error"]}
        elif n == cab:
            vueltas += 1
        # Tras un return, si lo siguiente es otra llamada (no la vuelta al que llamó),
        # se enseña el instante justo después de devolver: la pila sin el marco que acaba.
        tras = despues
        if devuelve and len(despues["pila"]) >= len(ejec["pila"]):
            tras = {**ejec, "pila": ejec["pila"][:-1], "salida": despues["salida"]}
        estado = tras["glob_m"]
        ctx_despues = {**tras["glob"], **(tras["pila"][-1]["real"] if tras["pila"] else {})}
        f = foco(estado)
        if cfg.get("soltar") and n >= cfg["soltar"]:
            f = None
        lee = bool(lista) and devuelve is None and f is not None and (
            f"{lista}[" in texto or (n == cab and " in " in texto and lista in texto))

        cond = None
        if devuelve is None:
            for clave in ("if ", "elif ", "while "):
                if texto.startswith(clave):
                    expr = texto[len(clave):].rstrip(":").strip()
                    antes = contexto(ejec)
                    cond = {"expr": expr, "sust": sustituye(expr, antes),
                            "valor": bool(eval(expr, dict(ENTORNO), dict(antes)))}

        compr = None
        nodo = comprension(texto) if devuelve is None else None
        if nodo and despues["linea"] == n and nodo[1] in despues["compr"]:
            c, var = nodo
            if linea_compr != n or nodo[1] not in ejec["compr"]:
                parcial = {} if isinstance(c, ast.DictComp) else []
            linea_compr = n
            ctx = {**despues["glob"], **despues["local"], **despues["compr"]}
            ev = lambda e: eval(compile(ast.Expression(e), "", "eval"), dict(ENTORNO), dict(ctx))
            try:
                pasa = all(ev(i) for i in c.generators[0].ifs)
                if isinstance(c, ast.DictComp):
                    expr = ast.unparse(c.key) + ": " + ast.unparse(c.value)
                    res = None
                    if pasa:
                        kk, vv = ev(c.key), ev(c.value)
                        parcial[kk] = vv
                        res = f"{kk!r}: {muestra(marca(vv, {}))}"
                else:
                    expr = ast.unparse(c.elt)
                    res = None
                    if pasa:
                        x = ev(c.elt)
                        parcial.append(x)
                        res = muestra(marca(x, {}))
                compr = {"var": var, "valor": muestra(marca(ctx[var], {})), "expr": expr, "res": res,
                         "cond": " and ".join(ast.unparse(i) for i in c.generators[0].ifs) or None,
                         "pasa": pasa, "parcial": muestra(marca(parcial, {}))}
            except Exception:
                compr = None
        elif devuelve is None and not (nodo and n == linea_compr):
            linea_compr = None

        fila = None
        if cfg["fila_en"] == "cada_linea":
            valores = [f"{n} ↩" if devuelve else str(n)] + [evalua(c, ctx_despues) for c in cfg["columnas"]]
            if (any(v != "—" for v in valores[1:]) or despues["salida"] != ejec["salida"]
                    or ejec.get("excepcion") or (devuelve and devuelve["error"])):
                filas.append(valores)
                fila = len(filas) - 1
        elif devuelve is None and n == cab and (cfg["fila_en"] == "comprobacion" or vueltas > 1):
            valores = []
            for c in cfg["columnas"]:
                try:
                    v = eval(c, dict(ENTORNO), dict(contexto(ejec)))
                    valores.append(repr(v) if isinstance(v, str) else str(v))
                except Exception:
                    valores.append("—")
            if cfg["fila_en"] == "comprobacion" and cond:
                valores.append("Sí" if cond["valor"] else "No")
            filas.append(valores)
            fila = len(filas) - 1

        pila = [{"nombre": m["nombre"], "args": m["args"], "vars": m["vars"],
                 "repr": {k: muestra(v) for k, v in m["vars"].items()}, **({"gen": True} if m["gen"] else {}),
                **({"expr": m["expr"]} if m["expr"] else {}), **({"estrella": m["estrella"]} if m["estrella"] else {})}
                for m in tras["pila"]]
        if devuelve and ejec["pausa"]:
            devuelve["pausa"] = True
        if devuelve and ejec["pila"] and ejec["pila"][-1]["gen"]:
            devuelve["gen"] = True
        paso = {"linea": n, "estado": estado, "salida": despues["salida"], "foco": f,
                "lee": lee, "cond": cond, "vuelta": vueltas, "fila": fila,
                "repr": {k: muestra(v) for k, v in estado.items()},
                "tipos": {k: type(v).__name__ for k, v in tras["glob"].items()},
                "pila": pila, "devuelve": devuelve, "excepcion": ejec.get("excepcion")}
        if compr:
            paso["compr"] = compr
        if hay_disco:
            paso["disco"] = tras["disco"]
        if hay_clases:
            paso["clases"] = tras["clases"]
        pasos.append(paso)
    return {"codigo": codigo, "pasos": pasos, "filas": filas}


CELDA = re.compile(r"^```\{code-cell\}[^\n]*\n(.*?)^```", re.S | re.M)
WIDGET = re.compile(r"^(```\{anywidget\}[^\n]*traza\.mjs[^\n]*\n(?::[^\n]*\n)*)(.*?)^```", re.S | re.M)


def procesa(ruta):
    texto = Path(ruta).read_text(encoding="utf-8")
    trozos, pos, hechos = [], 0, 0
    for w in WIDGET.finditer(texto):
        cuerpo = json.loads(w.group(2))
        cfg = cuerpo["config"]
        if cfg.get("tipo") in ("preguntas", "laboratorio"):   # sin traza fija: preguntas.py o el navegador
            continue
        celdas = list(CELDA.finditer(texto, 0, w.start()))
        if not celdas:
            raise SystemExit(f"{ruta}: hay un visualizador sin celda de código antes.")
        codigo = "\n".join(l for l in celdas[-1].group(1).rstrip("\n").split("\n") if not l.startswith(":"))
        nuevo = json.dumps({"config": cfg, "traza": traza(codigo, cfg)}, ensure_ascii=False, separators=(",", ":"), default=repr, allow_nan=False)
        trozos += [texto[pos:w.start()], w.group(1), nuevo, "\n"]
        pos = w.end() - 3
        hechos += 1
        print(f"  · {cfg.get('titulo', '(sin título)')}: {len(nuevo):,} caracteres de traza")
    trozos.append(texto[pos:])
    Path(ruta).write_text("".join(trozos), encoding="utf-8")
    print(f"{ruta}: {hechos} visualizador(es) actualizados")


if __name__ == "__main__":
    for r in sys.argv[1:]:
        procesa(r)
