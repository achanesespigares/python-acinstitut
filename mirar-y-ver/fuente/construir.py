"""Construye el laboratorio «Mirar y ver · cómo piensa tu código».

Ejecuta con Python de verdad cada programa de presets.py usando el mismo
trazador que usa la página en el navegador (tracer.py), guarda las trazas
codificadas por diferencias e inyecta trazas y trazador en plantilla.html.

    python3 mirar-y-ver/fuente/construir.py [salida.html]

Por defecto escribe mirar-y-ver/index.html.
"""
import json, os, sys

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from tracer import trazar
HERR = os.path.join(D, '..', '..', 'herramientas')   # el diagrama de flujo es común con el libro
sys.path.insert(0, HERR)
from diagrama import diagrama
from presets import P, ENTRADAS

# Puestos con vista de cajas y flechas: conservan pila de marcos y montón
FLECHAS = {'asignar', 'texto', 'doblar', 'ecuacion', 'aux', 'tupla', 'pisar', 'alias', 'nueva', 'copia', 'masigual',
           'doble', 'area', 'componer', 'sinreturn', 'sombra', 'mutparam', 'reasparam', 'unbound', 'factorial', 'cuenta',
           'sumarec', 'sinbase', 'indices', 'metodos', 'ordenar', 'sortnone', 'borrar', 'plana', 'anidada', 'profunda',
           'tablero', 'filas', 'agenda', 'contarletras', 'items', 'keyerror', 'fibo', 'vocales', 'pareshasta', 'entrada', 'blanco'}


def codificar(tr):
    """Cada paso guarda solo lo que cambia respecto al anterior."""
    out, pv, po = [], {}, ''
    for e in tr:
        v = e['v']
        n = {'l': e['l']}
        d = {k: x for k, x in v.items() if pv.get(k) != x}
        rm = [k for k in pv if k not in v]
        if d: n['d'] = d
        if rm: n['x'] = rm
        if e['o'] != po: n['o'] = e['o']
        for k in ('f', 'h', 'r', 'e'):
            if k in e: n[k] = e[k]
        out.append(n)
        pv, po = v, e['o']
    return out


def main():
    salida = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, '..', 'index.html')
    trazas = {}
    for k, codigo in P.items():
        tr = json.loads(trazar(codigo, 400, json.dumps(ENTRADAS[k]) if k in ENTRADAS else None))
        if k not in FLECHAS:
            for e in tr:
                e.pop('f', None); e.pop('h', None)
        trazas[k] = codificar(tr)
    diagramas = {k: json.loads(diagrama(codigo)) for k, codigo in P.items()}
    datos = {'ent': {k: '\n'.join(v) for k, v in ENTRADAS.items()}, 'code': P, 'trace': trazas, 'dg': diagramas}
    html = open(os.path.join(D, 'plantilla.html'), encoding='utf-8').read()
    html = html.replace('__PRE__', json.dumps(datos, separators=(',', ':')))
    sitio = os.environ.get('SITIO', 'https://achanesespigares.github.io/python-acinstitut').rstrip('/')
    html = html.replace('__SITIO__', sitio)
    html = html.replace('/*__DG__*/', open(os.path.join(HERR, '..', 'widgets', 'diagrama.js'), encoding='utf-8').read())
    trz = open(os.path.join(D, 'tracer.py'), encoding='utf-8').read() + '\n\n' + open(os.path.join(HERR, 'diagrama.py'), encoding='utf-8').read()
    html = html.replace('__TRZ__', json.dumps(trz))
    open(salida, 'w', encoding='utf-8').write(html)
    print(f'{len(P)} programas trazados → {os.path.normpath(salida)} ({len(html) // 1024} KB)')


if __name__ == '__main__':
    main()
