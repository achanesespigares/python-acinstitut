# Mirar y ver · cómo piensa tu código

Laboratorio de programación de AC Institut, hermano del libro. Se publica en
<https://achanesespigares.github.io/python-acinstitut/mirar-y-ver/>.

Ocho áreas (Variables, Decisiones, Patrones, Funciones, Colecciones, Algoritmos,
Física y código, Tu código) y 22 puestos. Cada puesto es una construcción de
Python con cuatro lecturas: la memoria paso a paso, la predicción antes de
ejecutar, la lectura operativa («si ves… haz…») y la trampa con su chequeo.

## Archivos

```
fuente/plantilla.html   la página: estilos, vistas (casillas, cajas y flechas, recorrido, gráfica) y textos de cada puesto
fuente/presets.py       los 96 programas de los puestos y los ejemplos de «Tu código»
fuente/tracer.py        el trazador con sys.settrace (el mismo que ejecuta el navegador)
fuente/construir.py     traza cada programa con Python y escribe mirar-y-ver/index.html
```

## Construir y probar

```
python3 mirar-y-ver/fuente/construir.py
```

Escribe `mirar-y-ver/index.html` (no se versiona: lo genera la publicación).
Las variantes de los puestos funcionan sin más. Para ejecutar código propio
hace falta Python en el navegador: Pyodide 314.0.7.

## Un solo Python para los dos laboratorios

El libro y «Mirar y ver» usan el mismo Python, que la publicación descarga una
sola vez en `<web>/pyodide/` (`pyodide.js`, `pyodide.mjs`, `pyodide.asm.mjs`,
`pyodide.asm.wasm`, `python_stdlib.zip`, `pyodide-lock.json`). La página lo
busca en este orden: `../pyodide/` (la web del libro), `py/` (la copia que
viaja con el artefacto de claude.ai, con la biblioteca estándar como
`py/stdlib.b64.txt` porque el artefacto no sirve `.zip`) y, por último, la CDN.

## Puentes con el libro

- Cada visualizador del libro y su laboratorio tienen «Ábrelo en Mirar y ver»:
  abren `mirar-y-ver/#tucodigo?codigo=…&entradas=…`, que carga el programa en
  «Tu código» y lo ejecuta.
- Cada puesto termina su lectura operativa con «En el libro» y los capítulos
  que lo explican (tabla `EN_LIBRO` de la plantilla).
- «Tu código» tiene «Abrir en el laboratorio del libro», que abre
  `capitulos/laboratorio#codigo=…&entradas=…`: allí se ven con más detalle las
  clases, los ficheros, los generadores y las excepciones con su `except`.
