"""trazar.py · genera las trazas de los visualizadores de un capítulo.

Uso:   python herramientas/trazar.py capitulos/07-recorrer-listas.md

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
"""
import ast, contextlib, copy, io, json, re, sys
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


def ejecuta(codigo):
    """Ejecuta el código y devuelve, por cada evento de línea, la línea y el estado."""
    eventos, salida = [], io.StringIO()

    def tracer(frame, evento, arg):
        if frame.f_code.co_filename != "<alumno>":
            return tracer
        if evento in ("line", "return"):
            estado = {k: copy.deepcopy(v) for k, v in frame.f_locals.items()
                      if not k.startswith("__") and not callable(v)}
            eventos.append({"linea": frame.f_lineno, "estado": estado, "salida": salida.getvalue()})
        return tracer

    with contextlib.redirect_stdout(salida):
        sys.settrace(tracer)
        try:
            exec(compile(codigo, "<alumno>", "exec"), {})
        finally:
            sys.settrace(None)
    return eventos


def traza(codigo, cfg):
    lineas = codigo.split("\n")
    lista, cab = cfg["lista"], cfg["cabecera"]
    eventos = ejecuta(codigo)
    pasos = [{"linea": None, "estado": {}, "salida": "", "foco": None, "lee": False, "cond": None, "vuelta": 0, "fila": None}]
    filas, vueltas = [], 0

    def foco(estado):
        arr = estado.get(lista)
        if not isinstance(arr, list):
            return None
        if cfg.get("foco", "vuelta") == "vuelta":
            return vueltas - 1 if 0 < vueltas <= len(arr) and cfg["puntero"] in estado else None
        idx = estado.get(cfg["foco"])
        return idx if isinstance(idx, int) and 0 <= idx < len(arr) else None

    for ejec, despues in zip(eventos, eventos[1:]):
        n = ejec["linea"]
        texto = lineas[n - 1].strip()
        if n == cab:
            vueltas += 1
        estado = despues["estado"]
        f = foco(estado)
        if cfg.get("soltar") and n >= cfg["soltar"]:
            f = None
        lee = f is not None and (f"{lista}[" in texto or (n == cab and " in " in texto and lista in texto))

        cond = None
        for clave in ("if ", "elif ", "while "):
            if texto.startswith(clave):
                expr = texto[len(clave):].rstrip(":").strip()
                antes = ejec["estado"]
                cond = {"expr": expr, "sust": sustituye(expr, antes),
                        "valor": bool(eval(expr, dict(ENTORNO), dict(antes)))}

        fila = None
        if n == cab and (cfg["fila_en"] == "comprobacion" or vueltas > 1):
            valores = []
            for c in cfg["columnas"]:
                try:
                    v = eval(c, dict(ENTORNO), dict(ejec["estado"]))
                    valores.append(repr(v) if isinstance(v, str) else str(v))
                except Exception:
                    valores.append("—")
            if cfg["fila_en"] == "comprobacion" and cond:
                valores.append("Sí" if cond["valor"] else "No")
            filas.append(valores)
            fila = len(filas) - 1

        pasos.append({"linea": n, "estado": estado, "salida": despues["salida"], "foco": f,
                      "lee": lee, "cond": cond, "vuelta": vueltas, "fila": fila})
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
        nuevo = json.dumps({"config": cfg, "traza": traza(codigo, cfg)}, ensure_ascii=False, separators=(",", ":"))
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
