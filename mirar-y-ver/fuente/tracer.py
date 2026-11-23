import sys, json, io, types
def trazar(codigo, maxp=400, entradas=None):
    ev = []
    out = io.StringIO()
    ent = [str(x) for x in json.loads(entradas)] if entradas else []
    def entrada(msg=''):
        out.write(str(msg))
        if not ent: raise EOFError('input() se ha quedado sin entradas: escríbelas en la caja «Entradas», una por línea')
        x = ent.pop(0)
        out.write(x + '\n')
        return x
    g = {'__name__': '__main__', 'input': entrada}
    ids, vivos = {}, []
    PRIM = (bool, int, float, complex, str, type(None))
    def foto(d):
        r = {}
        for k, v in d.items():
            if k.startswith('__'): continue
            if v is None or isinstance(v, (bool, int, float, str)): r[k] = ['s', repr(v)]
            elif isinstance(v, (list, tuple)): r[k] = ['l', [repr(e) for e in v[:24]]]
            elif isinstance(v, dict): r[k] = ['d', [[repr(a), repr(b)] for a, b in list(v.items())[:16]]]
        return r
    def ref(o):
        k = id(o)
        if k not in ids:
            ids[k] = len(ids) + 1
            vivos.append(o)
        return ids[k]
    NADA = object()
    fallo = set()
    def memoria(marcos_d, extra=NADA):
        heap = {}
        def ver(o):
            r = ref(o)
            if r in heap: return r
            if isinstance(o, PRIM): heap[r] = ['p', type(o).__name__, repr(o)]
            elif isinstance(o, (list, tuple)):
                heap[r] = None
                heap[r] = ['l' if isinstance(o, list) else 't', [ver(e) for e in o[:24]]]
            elif isinstance(o, dict):
                heap[r] = None
                heap[r] = ['d', [[ver(a), ver(b)] for a, b in list(o.items())[:16]]]
            elif isinstance(o, types.FunctionType): heap[r] = ['f', o.__name__]
            else: heap[r] = ['o', type(o).__name__]
            return r
        marcos = []
        for nombre, d in marcos_d:
            vs = [[k, ver(v)] for k, v in list(d.items()) if not k.startswith('__') and not isinstance(v, types.ModuleType) and v is not entrada]
            marcos.append([nombre, vs])
        rv = ver(extra) if extra is not NADA else None
        return marcos, {str(k): v for k, v in heap.items()}, rv
    def pila_de(frame):
        p = []
        while frame is not None and frame.f_code.co_filename == '<alumno>':
            p.append(frame)
            frame = frame.f_back
        return [('Global', f.f_globals) if f.f_code.co_name == '<module>' else (f.f_code.co_name, f.f_locals) for f in p[::-1]]
    def t(frame, event, arg):
        if frame.f_code.co_filename != '<alumno>': return None
        if event == 'return' and frame.f_code.co_name == '<module>': return t
        if event == 'exception': fallo.add(id(frame)); return t
        if event == 'return' and id(frame) in fallo: return t
        if event == 'line': fallo.discard(id(frame))
        if event == 'line' and not frame.f_lineno: return t
        if event in ('line', 'return'):
            if len(ev) >= maxp: raise RuntimeError('más de %d pasos: ¿bucle infinito?' % maxp)
            pila = pila_de(frame)
            if len(pila) > 51: raise RecursionError('más de 50 llamadas anidadas: ¿falta el caso base?')
            m, h, rv = memoria(pila, arg) if event == 'return' else memoria(pila)
            e = {'l': frame.f_lineno, 'v': foto(frame.f_locals), 'o': out.getvalue(), 'f': m, 'h': h}
            if event == 'return': e['r'] = rv
            ev.append(e)
        return t
    err = None
    viejo = sys.stdout
    try:
        c = compile(codigo, '<alumno>', 'exec')
        sys.stdout = out
        sys.settrace(t)
        try:
            exec(c, g)
        finally:
            sys.settrace(None)
            sys.stdout = viejo
    except SyntaxError as e:
        err = 'SyntaxError en la línea %s: %s' % (e.lineno, e.msg)
    except Exception as e:
        ln = None
        tb = e.__traceback__
        while tb:
            if tb.tb_frame.f_code.co_filename == '<alumno>': ln = tb.tb_lineno
            tb = tb.tb_next
        err = '%s%s: %s' % (type(e).__name__, ' en la línea %s' % ln if ln else '', e)
    m, h, _ = memoria([('Global', g)])
    ev.append({'l': 0, 'v': foto(g), 'o': out.getvalue(), 'e': err, 'f': m, 'h': h})
    return json.dumps(ev)
