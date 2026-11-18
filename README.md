# Programación en Python · AC Institut

Libro de Python de Antonio Chanes Espigares, hecho con **Jupyter Book 2** (motor MyST). Su seña de identidad: los programas se ven ejecutarse paso a paso, con la lista dibujada como casillas, el puntero que avanza, las variables, las condiciones evaluadas y la tabla de traza.

## Estructura

```
myst.yml                    configuración del libro (índice, tema, JupyterLite)
index.md                    portada y hoja de ruta
capitulos/
  00-como-leer.md           cómo usar el libro y los visualizadores
  01-especificacion.md · 02-algoritmo.md · 03-trazas.md                    bloque 0
  04-variables-asignacion.md · 05-tipos-de-datos.md · 06-condicionales.md   bloque 1
  07-bucles.md · 08-recorrer-listas.md                                     bloque 2
  09-funciones.md · 10-cadenas.md · 11-diccionarios.md                     bloque 3
  21-como-funciona-python.md · 22-listas-a-fondo.md · 23-tuplas-y-conjuntos.md
  24-funciones-a-fondo.md · 25-bucles-a-fondo.md · 26-cadenas-y-formato.md
  27-csv-math-random.md                                                    bloque 3+ (todo el PCEP)
  12-modulos.md · 13-excepciones.md · 14-clases.md                         bloque 4
  15-comprensiones.md · 16-funciones-valores.md · 17-ficheros.md
  18-clases-a-fondo.md · 19-cadenas-a-fondo.md · 20-probar-y-depurar.md    bloque 5
  simulacro-pcep.md · simulacro-pcap.md                                    simulacros de examen
  curso-mapa.md · curso-modulo-1.md · curso-modulo-2.md
  curso-proyecto-1.md · curso-proyecto-2.md                                el curso en 30 sesiones
widgets/traza.mjs           el visualizador (anywidget), con sus estilos dentro
herramientas/trazar.py      genera las trazas ejecutando el código con sys.settrace
herramientas/preguntas.py   comprueba el banco de preguntas ejecutándolo y lo coloca en el libro
preguntas/pcep.py           banco de preguntas tipo examen PCEP (original), con su sección y su capítulo
preguntas/pcap.py           banco de preguntas tipo examen PCAP (original)
pdf/                        la guía del curso en PDF: md2typ.py convierte las páginas curso-*.md a Typst (paquete ac-institut)
descargas/                  los PDF ya generados, enlazados desde la portada
estilo/ac-institut.css      piel AC Institut (vino, Montserrat, Arimo, IBM Plex Mono)
.github/workflows/          publicación automática en GitHub Pages
```

## Trabajar con el libro

Requisitos: Node 18 o superior y Python 3.11 o superior.

```bash
npm ci                 # instala MyST en la versión fijada (1.12.0)
npm run trazas         # regenera las trazas de todos los capítulos
npm start              # vista previa en http://localhost:3000
npm run build          # versión estática en _build/html
```

Con la distribución oficial de Jupyter Book 2 funciona igual: `jupyter book start` y `jupyter book build --html`.

## Añadir un programa visualizado

En el capítulo, escribe la celda de código y, justo debajo, el visualizador con su configuración:

````markdown
```{code-cell} python
notas = [7, 4, 9, 6, 8]
total = 0
for nota in notas:
    total = total + nota
print("Suma:", total)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Recorrer una lista y sumar","etiqueta":"for · elemento a elemento",
 "idea":"…","lista":"notas","cabecera":3,"puntero":"nota","foco":"vuelta",
 "columnas":["nota","total"],"fila_en":"fin_iteracion"}}
```
````

Después ejecuta `npm run trazas`: el script ejecuta el código de la celda y escribe la traza dentro del bloque. Las claves de `config` están explicadas al principio de `herramientas/trazar.py`.

## Notas técnicas

- El visualizador usa la directiva `{anywidget}` de MyST (disponible desde mystmd 1.8.2; la documentación la marca como experimental). Por eso la versión de MyST está fijada en `package.json`.
- Los estilos del widget van dentro de `traza.mjs`, no en un `.css` aparte: con mystmd 1.12.0 la opción `:css:` descargaba la hoja pero no la aplicaba.
- Las celdas `{code-cell}` se pueden ejecutar en el navegador (JupyterLite, `jupyter: lite: true` en `myst.yml`).

Licencia: CC BY-NC-SA 4.0.
