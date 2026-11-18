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

La "lista" también puede ser una cadena: cada carácter es una casilla.
Si el programa define funciones, cada llamada aparece como un marco con sus
variables locales, y el paso del return muestra el valor devuelto.

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


def foto(d):
    """Copia de las variables visibles: sin funciones, módulos ni nombres internos."""
    return {k: copy.deepcopy(v) for k, v in d.items()
            if not k.startswith("__") and not callable(v) and not isinstance(v, types.ModuleType)}


def ejecuta(codigo):
    """Ejecuta el código y devuelve un evento por cada línea (y por cada return de función),
    con las variables globales, la pila de marcos de función y lo impreso hasta entonces."""
    eventos, salida = [], io.StringIO()

    def tracer(frame, evento, arg):
        if frame.f_code.co_filename != "<alumno>":
            return tracer
        if evento in ("line", "return"):
            cadena, f = [], frame
            while f is not None and f.f_code.co_filename == "<alumno>":
                cadena.append(f)
                f = f.f_back
            cadena.reverse()                       # de fuera hacia dentro: módulo, función, función…
            modulo = cadena[0]
            pila = [{"nombre": fr.f_code.co_name,
                     "args": list(fr.f_code.co_varnames[:fr.f_code.co_argcount]),
                     "vars": foto(fr.f_locals)} for fr in cadena[1:]]
            es_funcion = frame is not modulo
            eventos.append({"ev": evento, "linea": frame.f_lineno, "glob": foto(modulo.f_locals),
                            "local": foto(frame.f_locals) if es_funcion else {}, "pila": pila,
                            "marco": frame.f_code.co_name, "funcion": es_funcion,
                            "retorno": arg if (evento == "return" and es_funcion) else None,
                            "salida": salida.getvalue()})
        return tracer

    with contextlib.redirect_stdout(salida):
        sys.settrace(tracer)
        try:
            exec(compile(codigo, "<alumno>", "exec"), {})
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
              "fila": None, "repr": {}, "tipos": {}, "pila": [], "devuelve": None}]
    filas, vueltas = [], 0

    def foco(estado):
        if not lista:
            return None
        arr = estado.get(lista)
        if not isinstance(arr, (list, str)):
            return None
        if cfg.get("foco", "vuelta") == "vuelta":
            return vueltas - 1 if 0 < vueltas <= len(arr) and cfg["puntero"] in estado else None
        idx = estado.get(cfg["foco"])
        return idx if isinstance(idx, int) and 0 <= idx < len(arr) else None

    def evalua(expr, ctx):
        try:
            return repr(eval(expr, dict(ENTORNO), dict(ctx)))
        except Exception:
            return "—"

    for ejec, despues in zip(eventos, eventos[1:]):
        n = ejec["linea"]
        texto = lineas[n - 1].strip()
        devuelve = None
        if ejec["ev"] == "return":
            if not ejec["funcion"]:
                continue
            devuelve = {"funcion": ejec["marco"], "valor": repr(ejec["retorno"])}
        elif n == cab:
            vueltas += 1
        # Tras un return, si lo siguiente es otra llamada (no la vuelta al que llamó),
        # se enseña el instante justo después de devolver: la pila sin el marco que acaba.
        tras = despues
        if devuelve and len(despues["pila"]) >= len(ejec["pila"]):
            tras = {**ejec, "pila": ejec["pila"][:-1], "salida": despues["salida"]}
        estado = tras["glob"]
        ctx_despues = {**tras["glob"], **(tras["pila"][-1]["vars"] if tras["pila"] else {})}
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
            if any(v != "—" for v in valores[1:]) or despues["salida"] != ejec["salida"]:
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
                 "repr": {k: repr(v) for k, v in m["vars"].items()}} for m in tras["pila"]]
        pasos.append({"linea": n, "estado": estado, "salida": despues["salida"], "foco": f,
                      "lee": lee, "cond": cond, "vuelta": vueltas, "fila": fila,
                      "repr": {k: repr(v) for k, v in estado.items()},
                      "tipos": {k: type(v).__name__ for k, v in estado.items()},
                      "pila": pila, "devuelve": devuelve})
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
