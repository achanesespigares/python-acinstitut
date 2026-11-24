"""Diagrama de flujo de un programa de Python.

Lo usan el libro (trazar.py, laboratorio.py) y el laboratorio «Mirar y ver»
(mirar-y-ver/fuente/construir.py lo añade a su trazador). Lee la estructura con
ast y la devuelve como bloques anidados; el dibujo lo hace diagrama.js.
"""
import json


# ── Diagrama de flujo ─────────────────────────────────────────────────────────────────────────
# Lee la estructura del programa con ast y la devuelve como bloques anidados. La página dibuja
# los bloques y, en cada paso de la traza, ilumina el que contiene la línea que se ejecuta.
#   p   proceso (filas seguidas de sentencias simples)    io  entrada/salida (print, input)
#   if  rombo con ramas si/no        wh  while             for  bucle for
#   fin return / break / continue / raise (terminan el camino)
#   try bloque try con sus except     funciones aparte, en 'fn'
def diagrama(codigo):
    import ast
    try:
        arbol = ast.parse(codigo)
    except SyntaxError as e:
        return json.dumps({'error': 'SyntaxError en la línea %s: %s' % (e.lineno, e.msg)})
    funcs = []

    def txt(nodo, maxc=44):
        # el texto tal como lo escribió el alumno; si no se puede, el que reconstruye ast
        s = ast.get_source_segment(codigo, nodo) if hasattr(nodo, 'lineno') else None
        if not s:
            try:
                s = ast.unparse(nodo)
            except Exception:
                s = type(nodo).__name__
        s = ' '.join(s.split())
        return s if len(s) <= maxc else s[:maxc - 1] + '…'

    def lin(nodo):
        return [nodo.lineno, getattr(nodo, 'end_lineno', None) or nodo.lineno]

    def es_io(nodo):
        for x in ast.walk(nodo):
            if isinstance(x, ast.Call) and isinstance(x.func, ast.Name) and x.func.id in ('print', 'input'):
                return True
        return False

    def firma(f):
        return '%s(%s)' % (f.name, txt(f.args, 36))

    def cabecera(nodo):
        # líneas de la cabecera de un bloque compuesto: desde la palabra clave hasta el «:»
        fin = nodo.lineno
        for campo in ('test', 'iter', 'target'):
            x = getattr(nodo, campo, None)
            if x is not None and getattr(x, 'end_lineno', None): fin = max(fin, x.end_lineno)
        return [nodo.lineno, fin]

    def secuencia(cuerpo, prefijo=''):
        out = []
        def fila(tipo, l, t):
            if out and out[-1]['t'] == tipo: out[-1]['r'].append(l + [t])
            else: out.append({'t': tipo, 'r': [l + [t]]})
        for s in cuerpo:
            if isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant) and isinstance(s.value.value, str):
                continue                                    # docstring o texto suelto
            if isinstance(s, ast.If):
                out.append({'t': 'if', 'l': cabecera(s), 'c': txt(s.test), 'si': secuencia(s.body, prefijo), 'no': secuencia(s.orelse, prefijo)})
            elif isinstance(s, ast.While):
                out.append({'t': 'wh', 'l': cabecera(s), 'c': txt(s.test), 'b': secuencia(s.body, prefijo), 'els': secuencia(s.orelse, prefijo)})
            elif isinstance(s, (ast.For, ast.AsyncFor)):
                out.append({'t': 'for', 'l': cabecera(s), 'c': '%s in %s' % (txt(s.target, 16), txt(s.iter, 26)), 'b': secuencia(s.body, prefijo), 'els': secuencia(s.orelse, prefijo)})
            elif isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef)):
                fila('p', [s.lineno, s.lineno], 'def ' + firma(s))
                funcs.append({'n': prefijo + s.name, 'sig': prefijo + firma(s), 'l': [s.lineno, s.lineno], 'b': secuencia(s.body, prefijo + s.name + '.')})
            elif isinstance(s, ast.ClassDef):
                fila('p', [s.lineno, s.lineno], 'class ' + s.name)
                for m in s.body:
                    if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        funcs.append({'n': s.name + '.' + m.name, 'sig': s.name + '.' + firma(m), 'l': [m.lineno, m.lineno], 'b': secuencia(m.body, s.name + '.' + m.name + '.')})
            elif isinstance(s, ast.Return):
                out.append({'t': 'fin', 'k': 'ret', 'l': lin(s), 'x': txt(s)})
            elif isinstance(s, ast.Break):
                out.append({'t': 'fin', 'k': 'brk', 'l': lin(s), 'x': 'break'})
            elif isinstance(s, ast.Continue):
                out.append({'t': 'fin', 'k': 'cont', 'l': lin(s), 'x': 'continue'})
            elif isinstance(s, ast.Raise):
                out.append({'t': 'fin', 'k': 'raise', 'l': lin(s), 'x': txt(s)})
            elif isinstance(s, ast.Try) or type(s).__name__ == 'TryStar':
                out.append({'t': 'try', 'l': [s.lineno, s.lineno], 'b': secuencia(s.body, prefijo),
                            'h': [{'l': [h.lineno, h.lineno], 'x': 'except' + (' ' + txt(h.type, 30) if h.type is not None else '') + (' as ' + h.name if h.name else ''),
                                   'b': secuencia(h.body, prefijo)} for h in s.handlers],
                            'els': secuencia(s.orelse, prefijo), 'fin': secuencia(s.finalbody, prefijo)})
            elif isinstance(s, (ast.With, ast.AsyncWith)):
                fila('p', [s.lineno, s.lineno], 'with ' + ', '.join(txt(i.context_expr, 30) + (' as ' + txt(i.optional_vars, 12) if i.optional_vars is not None else '') for i in s.items))
                out.extend(secuencia(s.body, prefijo))
            elif isinstance(s, ast.Match):
                out.append({'t': 'p', 'r': [lin(s) + ['match ' + txt(s.subject)]]})
            else:
                fila('io' if es_io(s) else 'p', lin(s), txt(s))
        return out

    principal = secuencia(arbol.body)
    return json.dumps({'main': principal, 'fn': funcs})
