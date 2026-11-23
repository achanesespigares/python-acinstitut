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
hace falta Pyodide 314.0.7 en `mirar-y-ver/py/` (`pyodide.js`,
`pyodide.asm.mjs`, `pyodide.asm.wasm`, `python_stdlib.zip`,
`pyodide-lock.json`); la publicación los descarga de jsDelivr. Si no están,
la página intenta cargarlos desde la CDN.

En la versión dentro de claude.ai (artefacto), el marco no permite leer datos
de la CDN, así que Pyodide va dentro del propio artefacto y la biblioteca
estándar viaja como `py/stdlib.b64.txt`; la página la detecta y la usa.
