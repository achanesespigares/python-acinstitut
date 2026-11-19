"""Convierte las páginas del curso (MyST/Markdown del libro) en el PDF de la guía, con ac-institut.

Uso (desde pdf/): python3 md2typ.py [idioma]   y después
  typst compile --package-path paquetes --font-path fuentes guia-es.typ ../descargas/el-curso-en-30-sesiones.pdf
Lee capitulos/curso-*.md del libro y escribe build/<idioma>/*.typ, que incluye guia-<idioma>.typ.
El paquete ac-institut 0.3.1 (paquetes/) y las fuentes (fuentes/) vienen de Dropbox, /Recursos Claude/typst.
"""
import json
import re
import sys
from pathlib import Path

LIBRO = Path(__file__).resolve().parent.parent
WEB = "https://achanesespigares.github.io/python-acinstitut/"
AQUI = Path(__file__).parent

# Palabras que el conversor reconoce, por idioma
LEX = {
    "es": dict(objetivo="Objetivo.", libro="En el libro.", comprobacion="Comprobación.",
               predice="Predice", en_clase="En clase", tarea="Tarea", sesion="Sesión",
               r_objetivo="Objetivo", r_libro="En el libro", consejo="Consejo",
               material="Material.", r_material="Material"),
}


# ── Texto en línea ─────────────────────────────────────────────────────
ESCAPAR = set('\\#$*_`@<>[]~/"\'')


def esc(t):
    out = []
    for c in t:
        if c in ESCAPAR:
            out.append("\\" + c if c not in '"\'' else c)
        else:
            out.append(c)
    s = "".join(out)
    # comillas rectas: que no las convierta en tipográficas dentro de texto normal
    s = s.replace('"', '\\"').replace("'", "\\'")
    return s


def cadena(t):
    return json.dumps(t, ensure_ascii=False)


def url_de(destino):
    if destino.startswith("http"):
        return destino
    if destino.startswith("#"):
        return None
    nombre = Path(destino).stem
    if nombre.startswith("curso-"):
        return None                     # está en este mismo PDF
    nombre = re.sub(r"^\d+-", "", nombre)
    return WEB + "capitulos/" + nombre + "/"


TOKEN = re.compile(r"`([^`]+)`|\*\*(.+?)\*\*|\*(.+?)\*|\[([^\]]+)\]\(([^)]+)\)")


def inline(s):
    s = s.replace("\\|", "|")
    out, pos = [], 0
    for m in TOKEN.finditer(s):
        out.append(esc(s[pos:m.start()]))
        code, bold, it, ltxt, lurl = m.groups()
        if code is not None:
            out.append(f"#raw({cadena(code)})")
        elif bold is not None:
            out.append(f"#strong[{inline(bold)}]")
        elif it is not None:
            out.append(f"#emph[{inline(it)}]")
        else:
            u = url_de(lurl)
            out.append(f"#web({cadena(u)})[{inline(ltxt)}]" if u else inline(ltxt))
        pos = m.end()
    out.append(esc(s[pos:]))
    r = "".join(out)
    if re.match(r"^(\d+\.|[-+=])\s", r):
        r = "\\" + r
    return r


def plano(s):
    """Texto sin marcas (para la panorámica)."""
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return re.sub(r"[`*]", "", s).replace("\\|", "|")


# ── Bloques ────────────────────────────────────────────────────────────
def celdas(linea):
    partes = re.split(r"(?<!\\)\|", linea.strip())
    return [c.strip() for c in partes[1:-1]]


def anchos(filas):
    ncol = len(filas[0])
    largos = [max(len(plano(f[i])) for f in filas) for i in range(ncol)]
    res = []
    for L in largos:
        res.append("auto" if L <= 14 else f"{max(1, round(L / 30, 1))}fr")
    if all(a == "auto" for a in res):
        res[-1] = "1fr"
    return "(" + ", ".join(res) + ",)"


def bloques(md, lex, nivel_base=2):
    """md → lista de cadenas Typst. Los títulos ## pasan a apartado y ### a subapartado."""
    lineas = md.split("\n")
    out, i = [], 0
    while i < len(lineas):
        l = lineas[i]
        if not l.strip() or l.strip() == "---" or re.match(r"^\(.+\)=$", l.strip()):
            i += 1
            continue
        if l.startswith("```"):
            lang = l[3:].strip()
            j = i + 1
            while not lineas[j].startswith("```"):
                j += 1
            codigo = "\n".join(lineas[i + 1:j])
            lang = "python" if lang.startswith("python") else ("text" if not lang else lang)
            out.append(f"#raw(block: true, lang: {cadena(lang)}, {cadena(codigo)})")
            i = j + 1
            continue
        if l.startswith(":::{"):
            m = re.match(r":::\{(\w+)\}\s*(.*)", l)
            j = i + 1
            while lineas[j].strip() != ":::":
                j += 1
            cuerpo = "\n".join(bloques("\n".join(lineas[i + 1:j]), lex))
            titulo = m.group(2) or lex["consejo"]
            out.append(f"#atencion(titulo: [{inline(titulo)}])[\n{cuerpo}\n]")
            i = j + 1
            continue
        m = re.match(r"^(#{2,4}) (.*)", l)
        if m:
            nivel = len(m.group(1))
            f = "apartado-guia" if nivel == nivel_base else "subapartado-guia"
            out.append(f"#{f}[{inline(m.group(2))}]")
            i += 1
            continue
        if l.startswith("|"):
            j = i
            while j < len(lineas) and lineas[j].startswith("|"):
                j += 1
            filas = [celdas(x) for x in lineas[i:j] if not re.match(r"^\|[\s:|-]+\|$", x)]
            cab, cuerpo = filas[0], filas[1:]
            if not cuerpo:                       # tabla para rellenar: dos filas en blanco
                cuerpo = [["\u00a0"] * len(cab)] * 3
            cab_t = ", ".join(cadena(plano(c)) for c in cab)
            fil_t = ",\n  ".join("(" + ", ".join(f"[{inline(c)}]" for c in f) + ",)" for f in cuerpo)
            out.append(f"#tabla({anchos(filas)}, ({cab_t},), (\n  {fil_t},\n))")
            i = j
            continue
        if l.startswith(">"):
            j = i
            texto = []
            while j < len(lineas) and lineas[j].startswith(">"):
                texto.append(lineas[j][1:].lstrip())
                j += 1
            interior = "\n".join(bloques("\n".join(texto), lex))
            out.append(f"#block(inset: (left: 1.2em), stroke: (left: 0.3mm + gris.filete))[\n{interior}\n]")
            i = j
            continue
        if re.match(r"^(\d+\.|-) ", l):
            ordenada = l[0].isdigit()
            j, items = i, []
            while j < len(lineas) and (re.match(r"^(\d+\.|-) ", lineas[j]) or
                                       (lineas[j].startswith("  ") and lineas[j].strip())):
                if re.match(r"^(\d+\.|-) ", lineas[j]):
                    items.append(re.sub(r"^(\d+\.|-) ", "", lineas[j]))
                else:
                    items[-1] += " " + lineas[j].strip()
                j += 1
            f = "enum" if ordenada else "list"
            out.append(f"#{f}(" + ", ".join(f"[{inline(t)}]" for t in items) + ")")
            i = j
            continue
        # párrafo
        j = i
        texto = []
        while j < len(lineas) and lineas[j].strip() and not re.match(r"^(```|#|\||>|:::|(\d+\.|-) )", lineas[j]):
            texto.append(lineas[j].strip())
            j += 1
        p = " ".join(texto)
        if p.startswith("**" + lex["comprobacion"] + "**"):
            out.append(f"#comprobacion[{inline(p[len(lex['comprobacion']) + 4:].strip())}]")
        else:
            out.append(inline(p))
        i = j
    return out


def secciones(md, nivel=2):
    """Parte el texto por títulos de un nivel: [(título, cuerpo)], con el preámbulo como título None."""
    patron = re.compile(r"^" + "#" * nivel + r" (.*)$", re.M)
    trozos, ult, tit = [], 0, None
    for m in patron.finditer(md):
        trozos.append((tit, md[ult:m.start()]))
        tit, ult = m.group(1), m.end()
    trozos.append((tit, md[ult:]))
    return trozos


def sin_frontmatter(md):
    fm = re.match(r"^---\n(.*?)\n---\n", md, re.S)
    datos = {}
    if fm:
        for l in fm.group(1).splitlines():
            k, _, v = l.partition(":")
            datos[k.strip()] = v.strip().strip('"')
        md = md[fm.end():]
    return datos, md


# ── Piezas del libro ───────────────────────────────────────────────────
def sesion(titulo, cuerpo, lex, modulo):
    m = re.match(r"(\S+) (\d+) · (.*)", titulo)
    n, nombre = m.group(2), m.group(3)
    filas, resto = [], []
    for parr in re.split(r"\n\s*\n", cuerpo.strip()):
        p = parr.strip().replace("\n", " ")
        for clave, rot in (("objetivo", "r_objetivo"), ("libro", "r_libro"), ("material", "r_material")):
            pref = "**" + lex[clave] + "**"
            if p.startswith(pref):
                filas.append(f"({cadena(lex[rot])}, [{inline(p[len(pref):].strip())}])")
                break
        else:
            resto.append(parr)
    t = [f"#unidad({cadena(n)}, [{inline(nombre)}], rotulo: {cadena(lex['sesion'] + ' ' + n + ' · ' + modulo)})"]
    if filas:
        t.append("#ficha-sesion((" + ", ".join(filas) + ",))")
    for tit, txt in secciones("\n\n".join(resto), 3):
        if tit is None:
            t += bloques(txt, lex)
        elif tit == lex["predice"]:
            t.append("#prediccion-sesion[\n" + "\n\n".join(bloques(txt, lex)) + "\n]")
        elif tit.startswith(lex["tarea"] + " "):
            # la comprobación queda dentro de la caja; lo que va después (hitos) fuera
            partes = re.split(r"\n(?=\*\*Hito )", txt, maxsplit=1)
            t.append(f"#tarea({cadena(plano(tit))})[\n" + "\n\n".join(bloques(partes[0], lex)) + "\n]")
            if len(partes) > 1:
                t += bloques(partes[1], lex)
        else:
            t.append(f"#apartado-guia[{inline(tit)}]")
            t += bloques(txt, lex)
    return "\n\n".join(t)


def capitulo_libre(n, titulo, md, lex, rotulo=None, entradilla=None):
    cab = f"#unidad({cadena(n)}, [{inline(titulo)}]"
    if rotulo:
        cab += f", rotulo: {cadena(rotulo)}"
    if entradilla:
        cab += f", entradilla: [{inline(entradilla)}]"
    cab += ")"
    return cab + "\n\n" + "\n\n".join(bloques(md, lex))


def panoramica(md_mapa):
    filas = [celdas(l) for l in md_mapa.splitlines() if re.match(r"^\| \*\*\d+", l) or re.match(r"^\| \d+", l)]
    ses = []
    for f in filas:
        n = int(plano(f[0]))
        tema = plano(f[1])
        fuerte = n in (15, 29, 30)
        ses.append(f"(n: {n}, tema: {cadena(tema)}, sale: {cadena(plano(f[3]))}, "
                   f"tipo: {cadena('fuerte' if fuerte else 'normal')})")
    return "#panoramica((\n  " + ",\n  ".join(ses) + ",\n))"


def construir(idioma="es"):
    lex = LEX[idioma]
    src = LIBRO / "capitulos" if idioma == "es" else LIBRO / idioma / "capitulos"
    dst = AQUI / "build" / idioma
    dst.mkdir(parents=True, exist_ok=True)
    leer = lambda n: sin_frontmatter((src / f"curso-{n}.md").read_text())

    # Parte I · El curso: mapa (con panorámica) y cómo leer cada sesión
    fm, md = leer("mapa")
    trozos = secciones(md)
    piezas = []
    for tit, txt in trozos:
        if tit is None:
            continue
        piezas.append(f"#apartado-guia[{inline(tit)}]")
        if re.search(r"\| Sesión|\| Session|\| Sessió", txt):
            piezas.append("#block(breakable: false)[" + panoramica(txt) + "]")
            piezas.append("#pagebreak()")
        piezas += bloques(txt, lex)
    curso = f"#unidad(\"\", [{inline(fm['title'])}], entradilla: [{inline(fm['subtitle'])}])\n\n" + "\n\n".join(piezas)

    m1fm, m1 = leer("modulo-1")
    m2fm, m2 = leer("modulo-2")
    lectura = []
    for k, md_mod in enumerate((m1, m2)):
        tit, txt = [x for x in secciones(md_mod) if x[0] is not None][0]   # «Cómo leer esta página»
        parrafos = re.split(r"\n\s*\n", txt.strip())
        lectura.append("\n\n".join(parrafos[1:] if k == 1 else parrafos))
    como = capitulo_libre("", "Cómo leer cada sesión", "\n\n".join(lectura), lex)
    (dst / "parte-curso.typ").write_text(
        '#import "../../comun.typ": *\n\n' + curso + "\n\n" + como + "\n")

    # Partes II y III · Las sesiones; soluciones aparte
    soluciones = []
    for k, (fmx, mdx) in enumerate(((m1fm, m1), (m2fm, m2)), start=1):
        partes = re.split(r"^\(soluciones-[^)]*\)=\s*$", mdx, flags=re.M)
        ses = []
        for tit, txt in secciones(partes[0]):
            if tit and re.match(r"\S+ \d+ · ", tit):
                ses.append(sesion(tit, txt, lex, fmx["title"].split(" · ")[0]))
        (dst / f"modulo-{k}.typ").write_text('#import "../../comun.typ": *\n\n' + "\n\n".join(ses) + "\n")
        sol = re.sub(r"^## .*\n", "", partes[1].strip(), count=1)
        soluciones.append(capitulo_libre("", fmx["title"].split(" · ")[0], sol, lex,
                                         entradilla=None) .replace("#apartado-guia", "#apartado-guia"))

    # Parte IV · Proyectos; la solución de referencia, a las soluciones
    proyectos = []
    for k in (1, 2):
        fmp, mdp = leer(f"proyecto-{k}")
        corte = mdp.rfind("\n---\n")
        enunciado, solucion = mdp[:corte], mdp[corte + 5:]
        titulo = fmp["title"].split(" · ", 1)[1]
        proyectos.append(capitulo_libre(f"P{k}", titulo, enunciado, lex,
                                        rotulo=fmp["title"].split(" · ")[0], entradilla=fmp["subtitle"]))
        sol = re.sub(r"^## .*\n", "", solucion.strip(), count=1)
        soluciones.append(capitulo_libre(f"P{k}", titulo, sol, lex,
                                         rotulo=fmp["title"].split(" · ")[0] + " · solución de referencia"))
    (dst / "proyectos.typ").write_text('#import "../../comun.typ": *\n\n' + "\n\n".join(proyectos) + "\n")
    (dst / "soluciones.typ").write_text('#import "../../comun.typ": *\n\n' + "\n\n".join(soluciones) + "\n")
    print("escrito", dst)


if __name__ == "__main__":
    construir(sys.argv[1] if len(sys.argv) > 1 else "es")
