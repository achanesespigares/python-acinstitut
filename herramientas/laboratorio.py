"""laboratorio.py · el puente entre el laboratorio del libro y trazar.py.

El navegador (Pyodide) carga trazar.py y este fichero y llama a laboratorio(codigo, entradas),
que devuelve en JSON lo mismo que ve un visualizador del libro: {"config": …, "traza": …}.
Decide solo qué dibujar: si el programa recorre una lista con un for, la lista sale como casillas.
"""
import ast
import json

import trazar

PASOS_MAXIMOS = 1000


def nombres_asignados(arbol):
    """Variables globales que asigna el programa, en orden (columnas de la tabla de traza)."""
    vistos = []
    for nodo in arbol.body:
        if isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        for n in ast.walk(nodo):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store) and n.id not in vistos:
                vistos.append(n.id)
    return vistos


def recorrido(arbol, asignados):
    """El primer for del programa que recorre una lista (o una cadena) global, si lo hay."""
    for nodo in arbol.body:
        if not isinstance(nodo, ast.For) or not isinstance(nodo.target, ast.Name):
            continue
        it = nodo.iter
        # for x in lista
        if isinstance(it, ast.Name) and it.id in asignados:
            return {"lista": it.id, "cabecera": nodo.lineno, "puntero": nodo.target.id, "foco": "vuelta"}
        # for i in range(len(lista))
        if (isinstance(it, ast.Call) and isinstance(it.func, ast.Name) and it.func.id == "range"
                and len(it.args) == 1 and isinstance(it.args[0], ast.Call)
                and isinstance(it.args[0].func, ast.Name) and it.args[0].func.id == "len"
                and it.args[0].args and isinstance(it.args[0].args[0], ast.Name)
                and it.args[0].args[0].id in asignados):
            return {"lista": it.args[0].args[0].id, "cabecera": nodo.lineno,
                    "puntero": nodo.target.id, "foco": nodo.target.id}
    return None


def laboratorio(codigo, entradas=()):
    codigo = codigo.replace("\t", "    ").rstrip()
    if not codigo.strip():
        return json.dumps({"error": "Escribe un programa antes de ejecutarlo."})
    try:
        arbol = ast.parse(codigo)
    except SyntaxError as e:
        return json.dumps({"error": f"Python no entiende la línea {e.lineno}: {e.msg}.",
                           "linea": e.lineno}, ensure_ascii=False)
    asignados = nombres_asignados(arbol)
    cfg = {"titulo": "Tu programa", "etiqueta": "paso a paso",
           "idea": "Avanza con «Paso ▶». Antes de cada paso, intenta predecir qué va a pasar.",
           "columnas": asignados[:4], "fila_en": "cada_linea"}
    lista = recorrido(arbol, asignados)
    if lista:
        cfg.update(lista)
        cfg["fila_en"] = "fin_iteracion"
        extra = [f"{lista['lista']}[{lista['puntero']}]"] if lista["foco"] != "vuelta" else []
        resto = [n for n in asignados if n not in (lista["puntero"], lista["lista"])]
        cfg["columnas"] = ([lista["puntero"]] + extra + resto)[:4]
    if entradas:
        cfg["entradas"] = list(entradas)
    trazar.LIMITE = PASOS_MAXIMOS
    traza = trazar.traza(codigo, cfg)
    return json.dumps({"config": cfg, "traza": traza}, ensure_ascii=False, separators=(",", ":"),
                      default=repr, allow_nan=False)
