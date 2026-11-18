"""preguntas.py · comprueba el banco de preguntas y lo coloca en el libro.

Uso:   python herramientas/preguntas.py            (todos los bancos)
       python herramientas/preguntas.py --solo-comprobar

1. Carga los bancos de preguntas/ (pcep.py…).
2. Ejecuta cada pregunta que tiene código y comprueba que la opción marcada como
   correcta es exactamente lo que hace Python (lo que imprime, el error que lanza
   o el valor que queda), y que ninguna otra opción lo es. Si algo no cuadra, se
   detiene y lo dice: así ninguna respuesta del libro puede estar mal.
3. Genera la ejecución paso a paso de cada pregunta de código (con trazar.py).
4. Escribe el banco listo para el libro en datos/<banco>.json. Los capítulos solo
   llevan un visualizador con su configuración, y el widget carga ese fichero al
   abrir la página (así el libro no engorda y se construye igual de rápido):
     {"config": {"tipo": "preguntas", "banco": "pcep", "capitulo": "22", ...}}
     {"config": {"tipo": "preguntas", "banco": "pcep", "modo": "simulacro", ...}}
   La publicación copia datos/ dentro de la web (ver .github/workflows/publicar.yml).
"""
import ast, builtins, contextlib, io, json, os, shutil, sys, tempfile, textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import trazar                                    # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
BANCOS = {"pcep": RAIZ / "preguntas" / "pcep.py", "pcap": RAIZ / "preguntas" / "pcap.py"}


def carga(nombre):
    ns = {}
    exec(compile(BANCOS[nombre].read_text(encoding="utf-8"), str(BANCOS[nombre]), "exec"), ns)
    return ns["SECCIONES"], ns["REPARTO"], ns["PREGUNTAS"]


def ejecuta(codigo, entradas=()):
    """Ejecuta el código en una carpeta temporal: (lo impreso, nombre del error o None, variables)."""
    salida, pendientes = io.StringIO(), list(entradas)

    def entrada(mensaje=""):
        salida.write(mensaje)
        return pendientes.pop(0) if pendientes else ""

    g = {"__name__": "__main__", "__builtins__": {**vars(builtins), "input": entrada}}
    carpeta, antes = tempfile.mkdtemp(prefix="pregunta-"), os.getcwd()
    os.chdir(carpeta)
    error = None
    try:
        with contextlib.redirect_stdout(salida):
            exec(compile(codigo, "programa.py", "exec"), g)
    except Exception as e:                       # noqa: BLE001 (queremos cualquier error)
        error = type(e).__name__
    finally:
        os.chdir(antes)
        shutil.rmtree(carpeta, ignore_errors=True)
    return salida.getvalue(), error, g


def comprueba(q):
    """Lista de problemas de una pregunta (vacía si todo está bien)."""
    p = []
    ops, ok = q["ops"], q["ok"]
    buenas = ok if isinstance(ok, list) else [ok]
    if len(ops) < 3:
        p.append("tiene menos de 3 opciones")
    if len(set(ops)) != len(ops):
        p.append("tiene opciones repetidas")
    if any(not (0 <= i < len(ops)) for i in buenas):
        p.append("la respuesta correcta no es una opción")
    if not q["exp"].strip():
        p.append("no tiene explicación")
    v = q.get("v")
    if v and not q.get("code"):
        p.append("se pide comprobarla, pero no tiene código")
    if not v or not q.get("code") or p:
        return p
    salida, error, g = ejecuta(q["code"], q.get("entradas", ()))
    if v == "salida":
        real = salida.rstrip("\n")
        if error:
            p.append(f"debería imprimir, pero lanza {error}")
        elif real != ops[buenas[0]]:
            p.append(f"imprime {real!r}, no {ops[buenas[0]]!r}")
        otras = [o for i, o in enumerate(ops) if i not in buenas and o == real]
        if otras:
            p.append(f"otra opción también es correcta: {otras[0]!r}")
    elif v == "error":
        if error != q.get("err"):
            p.append(f"debería lanzar {q.get('err')}, pero lanza {error or 'nada'}")
    elif v.startswith("valor:"):
        if error:
            p.append(f"lanza {error}")
        else:
            real = repr(eval(v[6:], g))
            if real != ops[buenas[0]]:
                p.append(f"{v[6:]} vale {real}, no {ops[buenas[0]]!r}")
    else:
        p.append(f"forma de comprobar desconocida: {v}")
    return p


def nombres_asignados(codigo):
    """Variables globales que asigna el programa, en orden (para las columnas de la traza)."""
    vistos = []
    for nodo in ast.parse(codigo).body:
        for n in ast.walk(nodo):
            if isinstance(nodo, (ast.FunctionDef, ast.ClassDef)):
                break
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store) and n.id not in vistos:
                vistos.append(n.id)
    return vistos[:4]


def con_traza(q):
    if not q.get("code") or not q.get("v"):
        return None
    try:
        ast.parse(q["code"])
    except SyntaxError:
        return None                              # un programa que no compila no se puede ejecutar
    cfg = {"titulo": "Así se ejecuta", "etiqueta": "paso a paso",
           "idea": "Avanza paso a paso y comprueba en qué momento se decide la respuesta.",
           "columnas": nombres_asignados(q["code"]), "fila_en": "cada_linea"}
    if q.get("entradas"):
        cfg["entradas"] = q["entradas"]
    return {"config": cfg, "traza": trazar.traza(q["code"], cfg)}


def para_el_libro(q, traza):
    r = {"id": q["id"], "cap": q["cap"], "sec": q["sec"], "q": q["q"], "ops": q["ops"], "ok": q["ok"], "exp": q["exp"]}
    if q.get("code"):
        r["code"] = q["code"]
    if q.get("mono") or q.get("v") in ("salida",) or (q.get("v") or "").startswith("valor:"):
        r["mono"] = True
    if traza:
        r["traza"] = traza
    return r


def guarda(nombre, secciones, reparto, listas):
    destino = RAIZ / "datos" / f"{nombre}.json"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text(json.dumps({"secciones": secciones, "reparto": reparto, "preguntas": listas},
                                  ensure_ascii=False, separators=(",", ":"), allow_nan=False), encoding="utf-8")
    usados = set()
    for ruta in sorted((RAIZ / "capitulos").glob("*.md")):
        for w in trazar.WIDGET.finditer(ruta.read_text(encoding="utf-8")):
            cfg = json.loads(w.group(2))["config"]
            if cfg.get("tipo") == "preguntas" and cfg.get("banco") == nombre:
                if cfg.get("modo") == "simulacro":
                    print(f"  · {ruta.name}: simulacro con el banco entero")
                else:
                    usados.add(cfg["capitulo"])
                    print(f"  · {ruta.name}: {sum(q['cap'] == cfg['capitulo'] for q in listas)} preguntas")
    sin_sitio = sorted({q["cap"] for q in listas} - usados)
    if sin_sitio:
        print(f"  ¡Ojo! hay preguntas de capítulos sin visualizador de preguntas: {sin_sitio}")
    return destino


def main():
    solo = "--solo-comprobar" in sys.argv
    fallos = 0
    for nombre in BANCOS:
        secciones, reparto, preguntas = carga(nombre)
        ids = [q["id"] for q in preguntas]
        repetidos = {i for i in ids if ids.count(i) > 1}
        if repetidos:
            print(f"{nombre}: identificadores repetidos: {sorted(repetidos)}")
            fallos += 1
        for q in preguntas:
            q["code"] = textwrap.dedent(q["code"]).strip("\n") if q.get("code") else None
            for problema in comprueba(q):
                print(f"{nombre} {q['id']}: {problema}")
                fallos += 1
        por_sec = {s: sum(q["sec"] == s for q in preguntas) for s in secciones}
        print(f"{nombre}: {len(preguntas)} preguntas · por sección {por_sec}")
        for s, n in reparto.items():
            if por_sec.get(s, 0) < n:
                print(f"{nombre}: la sección {s} tiene {por_sec.get(s, 0)} preguntas y el simulacro pide {n}")
                fallos += 1
        if fallos or solo:
            continue
        listas = [para_el_libro(q, con_traza(q)) for q in preguntas]
        destino = guarda(nombre, secciones, reparto, listas)
        print(f"{nombre}: banco escrito en {destino.relative_to(RAIZ)} ({destino.stat().st_size // 1024} KB)")
    if fallos:
        raise SystemExit(f"{fallos} problema(s): no se ha tocado el libro.")


if __name__ == "__main__":
    main()
