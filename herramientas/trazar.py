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

La "lista" también puede ser una cadena: cada carácter es una casilla.
Si el programa define funciones, cada llamada aparece como un marco con sus
variables locales, y el paso del return muestra el valor devuelto.
Los objetos de las clases del alumno se dibujan con un número (Cuenta nº1):
si dos variables muestran el mismo número, son el mismo objeto.
Si una línea lanza una excepción, el paso la muestra y el siguiente es el except.

Para programas sin lista ni bucle: omite "lista" y "cabecera", y usa
  fila_en: "cada_linea"       una fila de la tabla por cada línea ejecutada
  columnas: ["a", "b"]        variables que aparecen en la tabla
"""
import ast, contextlib, copy, io, json, re, sys, types
from pathlib import Path

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
            if n.id in estado and not isinstance(estado[n.id], (list, dict)):
                return ast.Constant(estado[n.id])
            return n

    return ast.unparse(Sustituto().visit(ast.parse(expr, mode="eval")))


def visible(k, v):
    return not k.startswith("__") and not callable(v) and not isinstance(v, types.ModuleType)


def foto(d):
    """Copia real de las variables visibles (para evaluar expresiones después)."""
    return {k: copy.deepcopy(v) for k, v in d.items() if visible(k, v)}


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
        return [marca(x, numeros) for x in v]
    if isinstance(v, dict):
        return {str(k): marca(x, numeros) for k, x in v.items()}
    if isinstance(v, BaseException):
        return {"__exc__": repr(v)}
    return copy.deepcopy(v)


def muestra(v):
    """Cómo se escribe un valor marcado: los objetos como «Cuenta nº1»."""
    if isinstance(v, dict) and "__obj__" in v:
        return f"{v['__clase__']} nº{v['__obj__']}"
    if isinstance(v, dict) and "__exc__" in v:
        return v["__exc__"]
    if isinstance(v, list):
        return "[" + ", ".join(muestra(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{" + ", ".join(f"{k!r}: {muestra(x)}" for k, x in v.items()) + "}"
    return repr(v)


def es_cuerpo_de_clase(frame):
    nombres = frame.f_code.co_names
    return "__module__" in nombres and "__qualname__" in nombres and frame.f_code.co_name != "<module>"


def ejecuta(codigo):
    """Ejecuta el código y devuelve un evento por cada línea (y por cada return de función),
    con las variables globales, la pila de marcos de función, lo impreso y los errores."""
    eventos, salida, numeros = [], io.StringIO(), {}
    estado_error = {"propagando": False}

    def tracer(frame, evento, arg):
        if frame.f_code.co_filename != "<alumno>" or es_cuerpo_de_clase(frame):
            return tracer
        if evento == "exception":
            if not estado_error["propagando"] and eventos:
                tipo, valor, _ = arg
                eventos[-1]["excepcion"] = f"{tipo.__name__}: {valor}" if str(valor) else tipo.__name__
                estado_error["propagando"] = True
            return tracer
        if evento in ("line", "return"):
            por_error = evento == "return" and estado_error["propagando"]
            if evento == "line":
                estado_error["propagando"] = False
            cadena, f = [], frame
            while f is not None and f.f_code.co_filename == "<alumno>":
                if not es_cuerpo_de_clase(f):
                    cadena.append(f)
                f = f.f_back
            cadena.reverse()                       # de fuera hacia dentro: módulo, función, función…
            modulo = cadena[0]
            pila = [{"nombre": getattr(fr.f_code, "co_qualname", fr.f_code.co_name),
                     "args": list(fr.f_code.co_varnames[:fr.f_code.co_argcount]),
                     "vars": {k: marca(v, numeros) for k, v in fr.f_locals.items() if visible(k, v)},
                     "real": foto(fr.f_locals)} for fr in cadena[1:]]
            es_funcion = frame is not modulo
            eventos.append({"ev": evento, "linea": frame.f_lineno,
                            "glob": foto(modulo.f_locals),
                            "glob_m": {k: marca(v, numeros) for k, v in modulo.f_locals.items() if visible(k, v)},
                            "local": foto(frame.f_locals) if es_funcion else {}, "pila": pila,
                            "marco": getattr(frame.f_code, "co_qualname", frame.f_code.co_name), "funcion": es_funcion,
                            "retorno": marca(arg, numeros) if (evento == "return" and es_funcion and not por_error) else None,
                            "por_error": por_error, "salida": salida.getvalue()})
        return tracer

    with contextlib.redirect_stdout(salida):
        sys.settrace(tracer)
        try:
            exec(compile(codigo, "<alumno>", "exec"), {"__name__": "__main__"})
        finally:
            sys.settrace(None)
    return eventos


def contexto(ev):
    """Variables que ve la línea que se ejecuta: globales más las locales de su función."""
    return {**ev["glob"], **ev["local"]}


def traza(codigo, cfg):
    lineas = codigo.split("\n")
    lista, cab = cfg.get("lista"), cfg.get("cabecera")
    eventos = ejecuta(codigo)
    pasos = [{"linea": None, "estado": {}, "salida": "", "foco": None, "lee": False, "cond": None, "vuelta": 0,
              "fila": None, "repr": {}, "tipos": {}, "pila": [], "devuelve": None, "excepcion": None}]
    filas, vueltas = [], 0

    def foco(estado):
        if not lista:
            return None
        arr = estado.get(lista)
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
                 "repr": {k: muestra(v) for k, v in m["vars"].items()}} for m in tras["pila"]]
        pasos.append({"linea": n, "estado": estado, "salida": despues["salida"], "foco": f,
                      "lee": lee, "cond": cond, "vuelta": vueltas, "fila": fila,
                      "repr": {k: muestra(v) for k, v in estado.items()},
                      "tipos": {k: type(v).__name__ for k, v in tras["glob"].items()},
                      "pila": pila, "devuelve": devuelve, "excepcion": ejec.get("excepcion")})
    return {"codigo": codigo, "pasos": pasos, "filas": filas}


CELDA = re.compile(r"^```\{code-cell\}[^\n]*\n(.*?)^```", re.S | re.M)
WIDGET = re.compile(r"^(```\{anywidget\}[^\n]*traza\.mjs[^\n]*\n(?::[^\n]*\n)*)(.*?)^```", re.S | re.M)


def procesa(ruta):
    texto = Path(ruta).read_text(encoding="utf-8")
    trozos, pos, hechos = [], 0, 0
    for w in WIDGET.finditer(texto):
        celdas = list(CELDA.finditer(texto, 0, w.start()))
        if not celdas:
            raise SystemExit(f"{ruta}: hay un visualizador sin celda de código antes.")
        codigo = "\n".join(l for l in celdas[-1].group(1).rstrip("\n").split("\n") if not l.startswith(":"))
        cuerpo = json.loads(w.group(2))
        cfg = cuerpo["config"]
        nuevo = json.dumps({"config": cfg, "traza": traza(codigo, cfg)}, ensure_ascii=False, separators=(",", ":"), default=repr)
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
