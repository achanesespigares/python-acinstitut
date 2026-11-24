"""sesiones.py · los cuadernos de Colab y las diapositivas de las 30 sesiones del curso.

Uso (desde la raíz del libro):
    python3 herramientas/sesiones.py            → cuadernos/sesion-NN.ipynb y diapositivas/fuentes/sesion-NN.typ
    python3 herramientas/sesiones.py --pdf      → además compila los PDF (hacen falta paquetes/ y fuentes/ en pdf/)

Todo sale de las páginas de la guía (capitulos/curso-modulo-*.md) y de los capítulos del libro:
el «Predice», el guion de clase y la tarea de cada sesión; los ejemplos y los ejercicios de sus capítulos.
Si cambia la guía o un capítulo, se vuelve a ejecutar y cuadernos y diapositivas se ponen al día.
"""
import ast
import builtins
import contextlib
import io
import json
import os
import re
import signal
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "pdf"))
from md2typ import cadena, celdas, inline, plano, secciones, sin_frontmatter, url_de  # noqa: E402

CAP = RAIZ / "capitulos"
REPO = "achanesespigares/python-acinstitut"
WEB = "https://python.antonychanes.com/"
COLAB = f"https://colab.research.google.com/github/{REPO}/blob/main/cuadernos/"
INSIGNIA = "https://colab.research.google.com/assets/colab-badge.svg"


def llano(t):
    """Texto sin marcas de markdown (negritas, código, enlaces), conservando los * de las fórmulas."""
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return t.replace("**", "").replace("`", "")


def url_cuaderno(n):
    return f"{COLAB}sesion-{n:02d}.ipynb"


# ── Lectura de la guía ─────────────────────────────────────────────────
ENLACE_LIBRO = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)(?:\s*§\s*(\d+)(?:–(\d+))?)?")


def bloques_codigo(texto):
    return re.findall(r"```(?:python|text)?\n(.*?)```", texto, re.S)


def lee_sesiones():
    res = []
    for k in (1, 2):
        fm, md = sin_frontmatter((CAP / f"curso-modulo-{k}.md").read_text(encoding="utf-8"))
        partes = re.split(r"^\(soluciones-[^)]*\)=\s*$", md, flags=re.M)
        respuestas = {}
        tabla_pred = re.search(r"^### .*Predice.*?\n(.*?)(?=^### )", partes[1], re.S | re.M)
        for l in (tabla_pred.group(1) if tabla_pred else "").splitlines():
            if re.match(r"^\| \d+ \|", l):
                c = celdas(l)
                respuestas[int(c[0])] = (c[1], c[2])
        for tit, txt in secciones(partes[0]):
            m = re.match(r"\S+ (\d+) · (.*)", tit or "")
            if not m:
                continue
            n = int(m.group(1))
            s = {"n": n, "titulo": m.group(2), "modulo": k, "libro": [], "predice": None, "clase": [],
                 "tarea": None, "hito": None, "consejo": None, "respuesta": respuestas.get(n)}
            s["objetivo"] = re.search(r"\*\*Objetivo\.\*\* (.*)", txt).group(1).strip()
            libro = re.search(r"\*\*En el libro\.\*\* (.*)", txt)
            s["libro_md"] = libro.group(1).strip() if libro else ""
            for txt_l, fich, a, b in ENLACE_LIBRO.findall(s["libro_md"]):
                if re.match(r"\d\d-", fich):
                    s["libro"].append((fich, int(a) if a else None, int(b) if b else (int(a) if a else None)))
            subs = dict((t, x) for t, x in secciones(txt, 3) if t)
            pre = dict(secciones(txt, 3)).get(None, "")
            if "Predice" in subs:
                p = subs["Predice"]
                codigo = bloques_codigo(p)
                cita = [l[1:].strip() for l in p.splitlines() if l.startswith(">")]
                intro = [x.strip() for x in re.split(r"\n\s*\n", re.sub(r"```.*?```", "", p, flags=re.S))
                         if x.strip() and not x.strip().startswith(">")]
                s["predice"] = {"codigo": codigo[0] if codigo else None, "cita": cita, "intro": " ".join(intro)}
            tabla_txt = subs.get("En clase", pre)
            for l in tabla_txt.splitlines():
                if re.match(r"^\| \d:\d\d", l):
                    s["clase"].append(tuple(celdas(l)))
            consejo = re.search(r":::\{tip\} (.*?)\n(.*?)\n:::", txt, re.S)
            if consejo:
                s["consejo"] = (consejo.group(1), consejo.group(2).strip())
            for t, x in subs.items():
                if t.startswith("Tarea "):
                    cuerpo, _, hito = x.partition("**Hito ")
                    comp = re.search(r"\*\*Comprobación\.\*\* (.*)", cuerpo)
                    pasos = re.findall(r"^\d+\. (.*)$", cuerpo, re.M)
                    intro = [p.strip() for p in re.split(r"\n\s*\n", re.sub(r"```.*?```", "", cuerpo, flags=re.S))
                             if p.strip() and not re.match(r"^\d+\. |\*\*Comprobación", p.strip())]
                    s["tarea"] = {"titulo": t, "intro": intro, "codigo": bloques_codigo(cuerpo), "pasos": pasos,
                                  "comprobacion": comp.group(1).strip() if comp else None}
                    if hito:
                        s["hito"] = "**Hito " + hito.strip().rstrip("-").strip()
            res.append(s)
    return sorted(res, key=lambda s: s["n"])


# ── Lectura de los capítulos ───────────────────────────────────────────
def lee_capitulo(fich):
    texto = (CAP / fich).read_text(encoding="utf-8")
    fm, md = sin_frontmatter(texto)
    partes = {}
    construccion = re.search(r"^## Construcción\n(.*?)(?=^## )", md, re.S | re.M)
    if construccion:
        for tit, txt in secciones(construccion.group(1), 3):
            m = re.match(r"(\d+) · (.*)", tit or "")
            if m:
                trazas = []                       # el código de las visualizaciones paso a paso
                for l in txt.split("\n"):
                    if l.startswith("{"):
                        try:
                            trazas.append(json.loads(l)["traza"]["codigo"].rstrip("\n") + "\n")
                        except (ValueError, KeyError, TypeError):
                            pass
                txt = "\n".join(l for l in txt.split("\n") if not l.startswith("{"))
                txt = re.sub(r"```\{anywidget\}.*?```", "", txt, flags=re.S)
                celdas_codigo = re.findall(r"```\{code-cell\} python\n(.*?)```", txt, re.S)
                prosa = re.sub(r"```.*?```", "", txt, flags=re.S)
                primera = next((p.strip() for p in re.split(r"\n\s*\n", prosa) if p.strip()
                                and not p.strip().startswith(("|", ":::", "#"))), "")
                partes[int(m.group(1))] = {"titulo": m.group(2), "codigo": celdas_codigo, "texto": primera,
                                           "trazas": trazas}
    md = "\n".join(l for l in md.split("\n") if not l.startswith("{"))
    md = re.sub(r"```\{anywidget\}.*?```", "", md, flags=re.S)
    ejercicios = []
    ej = re.search(r"^## Ejercicios\n(.*?)(?=^## )", md, re.S | re.M)
    if ej:
        actual = None
        for l in ej.group(1).splitlines():
            m = re.match(r"^(\d+)\. (.*)", l)
            if m:
                actual = [m.group(2)]
                ejercicios.append(actual)
            elif actual is not None and (l.startswith("   ") or not l.strip()):
                actual.append(l[3:] if l.startswith("   ") else "")
            elif l.strip():
                actual = None
    ejercicios = ["\n".join(e).strip() for e in ejercicios]
    return {"fichero": fich, "titulo": fm["title"], "secciones": partes, "ejercicios": ejercicios}


def secciones_de(cap, a, b):
    nums = sorted(cap["secciones"])
    if a is not None:
        nums = [x for x in nums if a <= x <= b]
    return [(x, cap["secciones"][x]) for x in nums]


def md_enlaces(texto):
    """Markdown de la guía → markdown de cuaderno: los enlaces a capítulos apuntan a la web."""
    def cambia(m):
        u = url_de(m.group(2))
        return f"[{m.group(1)}]({u})" if u else m.group(1)
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", cambia, texto)


# ── Cuadernos ──────────────────────────────────────────────────────────
def _python(cod):
    """El código sin las líneas mágicas de Colab (%%writefile, !pip…), para analizarlo."""
    if cod.startswith("%%writefile"):
        return ""
    return "\n".join(l for l in cod.split("\n") if not l.lstrip().startswith(("!", "%")))


def define(cod):
    """Nombres que un programa deja definidos al nivel de arriba."""
    try:
        arbol = ast.parse(_python(cod))
    except SyntaxError:
        return set()
    nombres = set()
    for n in ast.walk(arbol):
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            nombres.add(n.name)
        elif isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
            nombres.add(n.id)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            nombres |= {(a.asname or a.name).split(".")[0] for a in n.names}
    return nombres


def usa(cod):
    """Nombres que un programa lee sin haberlos definido él mismo."""
    try:
        arbol = ast.parse(_python(cod))
    except SyntaxError:
        return set()
    leidos = {n.id for n in ast.walk(arbol) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    locales = {n.arg for n in ast.walk(arbol) if isinstance(n, ast.arg)} \
        | {n.name for n in ast.walk(arbol) if isinstance(n, ast.ExceptHandler) and n.name}
    return leidos - locales - define(cod) - set(dir(builtins))


def celda(tipo, texto, i):
    lineas = texto.strip("\n").split("\n")
    fuente = [l + "\n" for l in lineas[:-1]] + [lineas[-1]]
    c = {"cell_type": tipo, "id": f"c{i:03d}", "metadata": {}, "source": fuente}
    if tipo == "code":
        c.update(execution_count=None, outputs=[])
    return c


def cuaderno(s, caps):
    c = []
    md = lambda t: c.append(celda("markdown", t, len(c)))
    code = lambda t: c.append(celda("code", t, len(c)))
    md(f"<small>AC INSTITUT · PROGRAMACIÓN EN PYTHON · MÓDULO {s['modulo']}</small>\n\n"
       f"# Sesión {s['n']} · {s['titulo']}\n\n**Objetivo.** {s['objetivo']}\n\n"
       + (f"**En el libro.** {md_enlaces(s['libro_md'])}\n\n" if s["libro_md"] else "")
       + "Para ejecutar una celda: haz clic en ella y pulsa **Mayús + Intro**. "
         "Las celdas que dicen *Tu respuesta* o `# Tu código` son para ti.")
    paso = 1
    if s["predice"]:
        p = s["predice"]
        md(f"## {paso} · Predice\n\n" + (p["intro"] + "\n\n" if p["intro"] else "")
           + ("\n".join("> " + l for l in p["cita"]) + "\n\n" if p["cita"] else "")
           + "**Antes de ejecutar nada**, escribe en la celda de abajo qué crees que va a pasar.")
        md("*Tu respuesta:* ")
        if p["codigo"]:
            md("Ahora ejecuta el programa y compara. Si no coincide, ¿en qué te equivocaste?")
            code(p["codigo"])
        paso += 1
    ejemplos = []
    for fich, a, b in s["libro"]:
        cap = caps[fich]
        for num, sec in secciones_de(cap, a, b):
            if sec["codigo"]:
                ejemplos.append((cap, num, sec))
    if ejemplos:
        md(f"## {paso} · Construcción\n\nLos ejemplos de los capítulos de hoy, en orden. Ejecútalos y **cambia algo** "
           "en cada uno: un número, una condición, un nombre. Predice antes qué cambiará.")
        actual = None
        conocidos = define(s["predice"]["codigo"]) if s["predice"] and s["predice"]["codigo"] else set()
        for cap, num, sec in ejemplos:
            if cap["fichero"] != actual:
                actual = cap["fichero"]
                md(f"### {cap['titulo']}\n\n[Abrir el capítulo en el libro]({url_de(actual)})")
            md(f"#### {num} · {sec['titulo']}" + (f"\n\n{md_enlaces(sec['texto'])}" if sec["texto"] else ""))
            # Lo que el capítulo ya definió antes (en una visualización o en un apartado que hoy no toca),
            # del más cercano al más lejano.
            antes = list(sec["trazas"])
            for k in sorted((k for k in cap["secciones"] if k < num), reverse=True):
                antes += cap["secciones"][k]["trazas"] + cap["secciones"][k]["codigo"]
            for cod in sec["codigo"]:
                falta = usa(cod) - conocidos
                previo = next((p for p in antes if falta and falta <= define(p)), None) \
                    or next((p for p in antes if falta & define(p)), None)
                if previo and previo not in sec["codigo"]:
                    md("*Primero, el programa que en el libro se ve paso a paso: el ejemplo de abajo lo usa.*")
                    code(previo)
                    conocidos |= define(previo)
                code(cod)
                conocidos |= define(cod)
        paso += 1
    ejercicios = [(caps[f], e) for f, _, _ in s["libro"] for e in caps[f]["ejercicios"]]
    if ejercicios:
        md(f"## {paso} · Práctica\n\nLos ejercicios de los capítulos de hoy. Las soluciones están al final de cada "
           "capítulo en el libro: míralas **después** de intentarlo.")
        actual = None
        for k, (cap, e) in enumerate(ejercicios, 1):
            if cap["fichero"] != actual:
                actual = cap["fichero"]
                md(f"### Ejercicios de «{cap['titulo']}»")
            md(md_enlaces(e))
            code("# Tu código\n")
        paso += 1
    if s["tarea"]:
        t = s["tarea"]
        texto = f"## {paso} · {t['titulo']}\n\nPara la próxima sesión.\n\n"
        texto += "".join(md_enlaces(x) + "\n\n" for x in t["intro"])
        texto += "".join(f"```python\n{x}```\n\n" for x in t["codigo"])
        texto += "".join(f"{i}. {md_enlaces(p)}\n" for i, p in enumerate(t["pasos"], 1))
        if t["comprobacion"]:
            texto += f"\n**Comprobación.** {md_enlaces(t['comprobacion'])}"
        md(texto)
        if s["n"] in (1, 2):
            md("*Tu respuesta:* ")
        else:
            if s["n"] == 3:
                md("*Tu tabla de traza:*\n\n| x | y | ¿x > y? |\n|---|---|---|\n|   |   |   |")
            code("# Tu código\n")
    if not ejemplos and not ejercicios and s["clase"]:
        taller(s, md)
    if s["hito"]:
        md(md_enlaces(s["hito"]) + f"\n\n[![Abrir en Colab]({INSIGNIA})]({url_proyecto(s['modulo'])}) "
           "El cuaderno del proyecto: la primera vez, guárdalo en tu Drive; después, trabaja siempre en tu copia.")
    if s["consejo"]:
        md(f"> **{s['consejo'][0]}.** {md_enlaces(s['consejo'][1])}")
    md("---\n*" + ("Las tareas se corrigen al principio de la próxima sesión. " if s["tarea"] else "")
       + f"Material del curso: [{WEB}capitulos/curso-mapa/]({WEB}capitulos/curso-mapa/)*")
    return metadatos_nb(c)


def url_proyecto(k):
    return f"{COLAB}proyecto-{k}.ipynb"


def metadatos_nb(celdas_nb):
    return {"cells": celdas_nb, "metadata": {"colab": {"provenance": []},
                                             "kernelspec": {"display_name": "Python 3", "name": "python3"},
                                             "language_info": {"name": "python"}},
            "nbformat": 4, "nbformat_minor": 5}


def cuaderno_proyecto(k):
    """El cuaderno de trabajo de un proyecto: encargo, hitos con su espacio, ampliaciones y rúbrica.
    La solución de referencia de la página del proyecto no entra: es para el profesor."""
    fich = f"curso-proyecto-{k}.md"
    fm, texto = sin_frontmatter((CAP / fich).read_text(encoding="utf-8"))
    texto = texto.split("## Solución de referencia")[0]
    texto = re.sub(r":::\{tip\}.*?:::", "", texto, flags=re.S)
    sec = {t: x.strip().rstrip("-").strip() for t, x in secciones(texto) if t}
    c = []
    md = lambda t: c.append(celda("markdown", t, len(c)))
    code = lambda t: c.append(celda("code", t, len(c)))
    md(f"<small>AC INSTITUT · PROGRAMACIÓN EN PYTHON · MÓDULO {k}</small>\n\n# {fm['title']}\n\n"
       f"*{fm.get('subtitle', '')}.* Este cuaderno es tu espacio de trabajo durante todo el proyecto: "
       f"guárdalo en tu Drive (**Archivo → Guardar una copia en Drive**) y vuelve a él en cada sesión.\n\n"
       f"[La página del proyecto en el libro]({url_de(fich)})")
    md("## El encargo\n\n" + md_enlaces(sec["El encargo"]))
    if "Los datos de partida" in sec:
        datos = sec["Los datos de partida"]
        md("## Los datos de partida\n\nEjecuta la celda de abajo: crea el fichero en tu Colab.")
        for b in re.findall(r"```text\n(.*?)```", datos, re.S):
            code("%%writefile notas.csv\n" + b)
    if "Lo que se practica" in sec:
        md("## Lo que se practica\n\n" + md_enlaces(sec["Lo que se practica"]))
    if "Cómo se trabaja en Colab" in sec:
        md("## Cómo se trabaja en Colab\n\n" + md_enlaces(sec["Cómo se trabaja en Colab"]))
    hitos = [celdas(l) for l in sec.get("Los hitos", "").splitlines() if re.match(r"^\| \d+ \|", l)]
    md("## Los hitos\n\n" + md_enlaces(sec["Los hitos"]))
    for ses, hito, entrega in hitos:
        nombre = llano(hito)
        md(f"### {nombre} · sesión {ses}\n\n{md_enlaces(entrega)}")
        if "Diseño" in nombre or "Exposición" in nombre:
            md("*Tu trabajo:*\n\n- \n- \n- ")
        elif k == 2 and "Clases" in nombre:
            code("!mkdir -p biblioteca")
            code('%%writefile biblioteca/errores.py\n"""Las excepciones del catálogo."""\n')
            code('%%writefile biblioteca/modelos.py\n"""Los recursos: la clase madre y sus hijas."""\n')
            code('%%writefile test_biblioteca.py\n"""Las pruebas del paquete."""\nimport unittest\n')
            code("!python -m unittest test_biblioteca -v")
        elif k == 2 and "Catálogo" in nombre:
            code('%%writefile biblioteca/catalogo.py\n"""El catálogo: guardar, buscar, prestar, devolver."""\n')
            code('%%writefile biblioteca/__init__.py\n"""Paquete biblioteca: recursos, catálogo y errores."""\n')
        elif k == 2:
            code("!python -m unittest test_biblioteca -v")
        else:
            code("# Tu código\n")
    if "El registro de la IA" in sec:
        md("## El registro de la IA\n\n" + md_enlaces(sec["El registro de la IA"]))
        md("*Tu registro:*\n\n| Fecha | Qué se pidió | Qué devolvió (resumen) | Qué se comprobó | Qué se corrigió |\n"
           "|---|---|---|---|---|\n|  |  |  |  |  |")
    if "La versión mínima y las ampliaciones" in sec:
        md("## La versión mínima y las ampliaciones\n\n"
           + re.sub(r"^- ", "- [ ] ", md_enlaces(sec["La versión mínima y las ampliaciones"]), flags=re.M))
    if "La rúbrica" in sec:
        md("## La rúbrica\n\nAntes de entregar, puntúate tú: si te sale menos de 2 en algo, ya sabes qué mejorar.\n\n"
           + md_enlaces(sec["La rúbrica"]))
    return metadatos_nb(c)


def secciones_simulacro(cual):
    fm, texto = sin_frontmatter((CAP / f"simulacro-{cual}.md").read_text(encoding="utf-8"))
    return [celdas(l) for l in texto.splitlines() if re.match(r"^\| \d \|", l)]


def taller(s, md):
    """Sesiones sin capítulos nuevos (proyecto, simulacro, exposiciones): el guion de la sesión como cuaderno."""
    k = s["modulo"]
    md("## Hoy\n\n" + "\n".join(f"- **{t}** · {md_enlaces(q)}" for t, q in s["clase"]))
    texto = " ".join(q for _, q in s["clase"])
    if "Exposiciones" in texto or "Taller del proyecto" in texto:
        md(f"## El proyecto\n\n[![Abrir en Colab]({INSIGNIA})]({url_proyecto(k)}) "
           "Abre tu cuaderno del proyecto: el que guardaste en tu Drive.")
    for cual in ("pcep", "pcap"):
        if f"Simulacro {cual.upper()}" in texto:
            filas = secciones_simulacro(cual)
            md(f"## El simulacro {cual.upper()}\n\n[Abrir el simulacro en el libro]({WEB}capitulos/simulacro-{cual}/). "
               "Pon el temporizador y no lo pares. Al acabar, apunta tus aciertos por secciones: es tu diagnóstico.\n\n"
               "| Sección | Qué entra | Preguntas | Mis aciertos |\n|---|---|---|---|\n"
               + "\n".join(f"| {f[0]} | {f[1]} | {f[3]} |  |" for f in filas))
            if "tres preguntas" in texto:
                md("*Las tres preguntas que más me enseñaron, y por qué:*\n\n1. \n2. \n3. ")
            else:
                md("*Mis secciones más flojas, y qué capítulos voy a repasar:*\n\n- \n- ")
    expo = next((q for _, q in s["clase"] if "Exposiciones" in q or "exposiciones" in q), None)
    if expo:
        md("## Tu exposición\n\n" + md_enlaces(expo) + "\n\n*Tu guion, una línea por punto:*\n\n1. \n2. \n3. \n4. ")


def marca_errores(nb):
    """Ejecuta el cuaderno de arriba abajo y avisa en las celdas que acaban en error a propósito
    (las de los capítulos de excepciones y depuración). Devuelve cuántas ha marcado."""
    class Tiempo(Exception):
        pass

    def alarma(*_):
        raise Tiempo

    viejo = signal.signal(signal.SIGALRM, alarma)
    entrada, cwd, ruta = builtins.input, os.getcwd(), list(sys.path)
    d = tempfile.mkdtemp()
    os.chdir(d)
    sys.path.insert(0, d)
    ns, marcadas, modulos = {"__name__": "__main__"}, 0, set(sys.modules)
    builtins.input = lambda *_: (_ for _ in ()).throw(EOFError)
    try:
        for c in nb["cells"]:
            if c["cell_type"] != "code":
                continue
            src = "".join(c["source"])
            if src.startswith("%%writefile"):
                nombre, _, cuerpo = src.partition("\n")
                destino = Path(d) / nombre.split()[1]
                destino.parent.mkdir(parents=True, exist_ok=True)
                destino.write_text(cuerpo, encoding="utf-8")
                continue
            signal.alarm(3)
            try:
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    exec(compile(_python(src), "<celda>", "exec"), ns)
            except (Tiempo, EOFError, SystemExit):
                pass
            except Exception:
                if "input(" not in src and "# Tu código" not in src:
                    aviso = "# Esta celda acaba en error a propósito: lee el mensaje de abajo arriba.\n"
                    c["source"] = [aviso] + c["source"]
                    marcadas += 1
            finally:
                signal.alarm(0)
    finally:
        builtins.input = entrada
        os.chdir(cwd)
        sys.path[:] = ruta
        for m in set(sys.modules) - modulos:          # los módulos del cuaderno no pasan al siguiente
            if getattr(sys.modules[m], "__file__", "") and str(sys.modules[m].__file__).startswith(d):
                del sys.modules[m]
        signal.signal(signal.SIGALRM, viejo)
    return marcadas


# ── Diapositivas ───────────────────────────────────────────────────────
def corta_codigo(cod, max_lineas=13):
    lineas = cod.rstrip("\n").split("\n")
    return "\n".join(lineas[:max_lineas]) + ("\n…" if len(lineas) > max_lineas else "")


def frase(texto, n=150):
    """Primera frase de un texto de la guía, para que quepa en una diapositiva."""
    t = re.sub(r"^\*\*([^*]+)\*\*:\s*", r"\1: ", texto).strip()
    corte = re.match(r"(.+?[.!?])(\s|$)", t)
    t = corte.group(1) if corte and len(corte.group(1)) > 40 else t
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"


def diapositivas(s, caps, siguiente):
    T = []
    add = T.append
    add(f'#portada([{inline(s["titulo"])}], subtitulo: [{inline(s["objetivo"])}], '
        f'kicker: "Sesión {s["n"]} · Módulo {s["modulo"]}", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])')
    if s["clase"]:
        add("== Hoy")
        filas = ", ".join(f'[{inline(t)}], [{inline(frase(q, 110))}]' for t, q in s["clase"])
        add(f"#tabla-hoy(({filas},))")
    sit = next((q for _, q in s["clase"] if "**Situación**" in q), None)
    if sit:
        add("== Para empezar")
        texto = re.sub(r"^\*\*Situación\*\*:\s*", "", sit)
        add(f'#situacion[{inline(texto[:1].upper() + texto[1:])}]')
    if s["predice"]:
        p = s["predice"]
        add("== Predice")
        add("#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]")
        resp = f'respuesta([{inline(s["respuesta"][0])}], [{inline(s["respuesta"][1])}])' if s["respuesta"] else None
        cod = corta_codigo(p["codigo"], 18) if p["codigo"] else None
        if cod and resp and len(cod.splitlines()) > 7:
            # Código largo: la respuesta va al lado para que todo quepa en la diapositiva
            nl = len(cod.splitlines())
            talla = "17pt" if nl <= 11 else "16pt" if nl <= 13 else "15pt" if nl <= 15 else "13.5pt"
            add(f'#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, '
                f'codigo({cadena(cod)}, talla: {talla}), uncover("2-", {resp}))')
        else:
            if cod:
                add(f'#codigo({cadena(cod)})')
            else:
                add("#cita[" + " \\\n".join(inline(l) for l in p["cita"]) + "]")
            if resp:
                add("#pause")
                add("#" + resp)
    ejemplos = []
    for fich, a, b in s["libro"]:
        for num, sec in secciones_de(caps[fich], a, b):
            if sec["codigo"]:
                ejemplos.append((caps[fich], num, sec))
    for cap, num, sec in ejemplos[:5]:
        cod = min(sec["codigo"], key=lambda x: len(x.splitlines()))
        add(f"== {inline(sec['titulo'])}")
        add(f'#fuente[{inline(cap["titulo"])} · {num}]')
        ancho = max(len(l) for l in corta_codigo(cod).splitlines())
        talla = "" if ancho <= 52 else ", talla: 17pt" if ancho <= 60 else ", talla: 15pt" if ancho <= 70 else ", talla: 13pt"
        add(f'#codigo({cadena(corta_codigo(cod))}{talla})')
    if s["predice"] or ejemplos:
        add("== Manos a la obra")
        ej = [e for f, _, _ in s["libro"] for e in caps[f]["ejercicios"]]
        titulos = []
        for e in ej[:6]:
            m = re.match(r"\*\*(.+?)\*\*", e)
            corto = plano(m.group(1)).rstrip(".") if m else ""
            titulos.append(corto if len(corto) >= 14 else frase(llano(e.split("\n")[0]), 70))
        lista = ", ".join(f"[{inline(x)}]" for x in titulos)
        add(f'#colab({cadena(url_cuaderno(s["n"]))}, ({lista},))')
    if s["tarea"]:
        t = s["tarea"]
        add(f"== {inline(t['titulo'])}")
        pasos = ", ".join(f"[{inline(frase(p, 120))}]" for p in t["pasos"][:6])
        comp = f"[{inline(t['comprobacion'])}]" if t["comprobacion"] else "none"
        add(f"#tarea-casa(({pasos},), {comp})")
    if s["hito"]:
        add("== El proyecto")
        add(f"#con-qr({cadena(url_proyecto(s['modulo']))}, [Cuaderno del proyecto], situacion[{inline(s['hito'])}])")
    if not ejemplos and not s["predice"]:
        for _, q in s["clase"]:
            for cual in ("PCEP", "PCAP"):
                if f"Simulacro {cual}" in q:
                    add(f"== El simulacro {cual}")
                    add(f"#con-qr({cadena(WEB + 'capitulos/simulacro-' + cual.lower() + '/')}, [Simulacro en el libro], "
                        f"situacion[{inline(q)}])")
            if "xposiciones" in q:
                add("== Las exposiciones")
                add(f"#con-qr({cadena(url_proyecto(s['modulo']))}, [Cuaderno del proyecto], situacion[{inline(q)}])")
    if s["consejo"]:
        add(f"== {inline(s['consejo'][0])}")
        add(f"#situacion[{inline(s['consejo'][1])}]")
    cierre = []
    capitulo_quiz = next((f for f, _, _ in reversed(s["libro"])), None)
    if capitulo_quiz:
        cierre.append(f'qr: {cadena(url_de(capitulo_quiz) + "#preguntas-tipo-examen")}')
    if siguiente:
        cierre.append(f'siguiente: [Sesión {siguiente["n"]} · {inline(siguiente["titulo"])}]')
    if cierre:
        add(f"== Antes de irte\n#cierre({', '.join(cierre)})")
    else:                                   # la última sesión del curso
        add("== Y ahora, la certificación")
        add(f"#con-qr({cadena(WEB + 'capitulos/cobertura/')}, [El temario oficial en el libro], "
            "situacion[Para presentarte al *PCEP* y al *PCAP*: repite los simulacros del libro hasta superar "
            "el aprobado con margen y repasa, objetivo a objetivo, lo que aún falle.])")
    return "\n\n".join(T)


CABECERA_DIAPOS = '''// Sesión {n} · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: {n}, tema: {tema})

'''


def url_diapos(n):
    return f"{WEB}diapositivas/sesion-{n:02d}.pdf"


def pon_material(sesiones):
    """Escribe (o pone al día) la línea «Material.» de cada sesión en la guía: cuaderno, diapositivas y,
    si toca, el cuaderno del proyecto. Es idempotente: ejecutarlo dos veces deja la guía igual."""
    por_n = {s["n"]: s for s in sesiones}
    for k in (1, 2):
        ruta = CAP / f"curso-modulo-{k}.md"
        lineas = ruta.read_text(encoding="utf-8").split("\n")
        limpias = []
        for l in lineas:
            if l.startswith("**Material.**"):
                if limpias and not limpias[-1].strip():
                    limpias.pop()                     # y la línea en blanco que la separaba
                continue
            limpias.append(l)
        lineas = limpias
        res, n = [], None
        for i, l in enumerate(lineas):
            m = re.match(r"^## Sesión (\d+) · ", l)
            if m:
                n = int(m.group(1))
            res.append(l)
            sig = lineas[i + 2] if i + 2 < len(lineas) else ""
            ancla = l.startswith("**En el libro.**") or (l.startswith("**Objetivo.**") and not sig.startswith("**En el libro.**"))
            if n in por_n and ancla:
                s = por_n[n]
                partes = [f"[Cuaderno en Colab]({url_cuaderno(n)})", f"[Diapositivas en PDF]({url_diapos(n)})"]
                if s["hito"] or not s["libro"]:
                    partes.append(f"[Cuaderno del proyecto]({url_proyecto(k)})")
                res += ["", "**Material.** " + " · ".join(partes)]
                n = None
        ruta.write_text("\n".join(res), encoding="utf-8")


def main(pdf=False):
    sesiones = lee_sesiones()
    pon_material(sesiones)
    fichs = sorted({f for s in sesiones for f, _, _ in s["libro"]})
    caps = {f: lee_capitulo(f) for f in fichs}
    (RAIZ / "cuadernos").mkdir(exist_ok=True)
    fuentes = RAIZ / "diapositivas" / "fuentes"
    fuentes.mkdir(parents=True, exist_ok=True)
    for k in (1, 2):
        (RAIZ / "cuadernos" / f"proyecto-{k}.ipynb").write_text(
            json.dumps(cuaderno_proyecto(k), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    avisos = 0
    for i, s in enumerate(sesiones):
        nb = cuaderno(s, caps)
        avisos += marca_errores(nb)
        (RAIZ / "cuadernos" / f"sesion-{s['n']:02d}.ipynb").write_text(
            json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        sig = sesiones[i + 1] if i + 1 < len(sesiones) else None
        (fuentes / f"sesion-{s['n']:02d}.typ").write_text(
            CABECERA_DIAPOS.format(n=s["n"], tema=cadena(f"Sesión {s['n']} · {plano(s['titulo'])}"))
            + diapositivas(s, caps, sig) + "\n", encoding="utf-8")
    print(f"{len(sesiones)} cuadernos de sesión y 2 de proyecto en cuadernos/ ({avisos} celdas con error a propósito),"
          f" y {len(sesiones)} presentaciones en diapositivas/fuentes/")
    if pdf:
        import typst
        salida = RAIZ / "diapositivas" / "pdf"
        for piel in ("ac-institut", "rocafort"):
            (salida / piel).mkdir(parents=True, exist_ok=True)
            for s in sesiones:
                typst.compile(str(fuentes / f"sesion-{s['n']:02d}.typ"),
                              output=str(salida / piel / f"sesion-{s['n']:02d}.pdf"), root=str(RAIZ),
                              package_path=str(RAIZ / "pdf" / "paquetes"), font_paths=[str(RAIZ / "pdf" / "fuentes")],
                              sys_inputs={"piel": piel})
        print("PDF en diapositivas/pdf/ (ac-institut y rocafort)")
    return sesiones, caps


if __name__ == "__main__":
    main(pdf="--pdf" in sys.argv)
