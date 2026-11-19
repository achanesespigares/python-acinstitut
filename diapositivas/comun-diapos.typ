// Piezas de las diapositivas de las sesiones, sobre ac-institut 0.3.1 (sin tocar el paquete)
// La piel se elige al compilar: --input piel=rocafort (para clase) o piel=ac-institut (la del libro).
#import "@local/ac-institut:0.3.1": *
#import "@preview/tiaoma:0.3.0": qrcode

#let PIEL = sys.inputs.at("piel", default: "ac-institut")
#let mono = ("IBM Plex Mono", "DejaVu Sans Mono")
#let web(url, cuerpo) = link(url, cuerpo)

#let diapos(sesion: none, tema: none, cuerpo) = {
  let kicker = if PIEL == "rocafort" { "Institut Rocafort · Programación en Python" }
               else { "AC Institut · Programación en Python" }
  show: presentacion.with(piel: PIEL, asignatura: "Programación en Python", tema: tema, kicker: kicker,
    paleta: "matematicas", titulo: tema)
  show raw: set text(font: mono)
  show raw.where(block: false): it => box(fill: gris.superficie, inset: (x: 0.2em), outset: (y: 0.2em), radius: 1pt, it)
  set par(justify: false)
  cuerpo
}

// Código grande y legible desde el fondo del aula
#let codigo(texto, talla: 19pt) = context {
  let pal = estado-paleta.get()
  block(width: 100%, fill: gris.superficie, stroke: (left: 1.2mm + pal.acento), inset: (x: 0.9em, y: 0.6em),
    text(size: talla, raw(texto, lang: "python", block: true)))
}

#let fuente(cuerpo) = block(below: 0.5em, text(size: 0.65em, fill: gris.banda, cuerpo))

#let cita(cuerpo) = block(inset: (left: 1em), stroke: (left: 0.5mm + gris.filete), text(size: 0.95em, cuerpo))

#let situacion(cuerpo) = context {
  let pal = estado-paleta.get()
  v(1fr)
  block(width: 100%, fill: pal.suave, inset: 1.1em, text(size: 1.05em, cuerpo))
  v(1.4fr)
}

#let respuesta(salida, clave) = context {
  let pal = estado-paleta.get()
  block(above: 0.8em, width: 100%, stroke: 0.45mm + black, inset: 0pt, {
    block(width: 100%, fill: pal.acento, inset: (x: 0.7em, y: 0.35em), below: 0pt,
      micro("Lo que sale", color: white, talla: 0.6em))
    block(width: 100%, inset: (x: 0.7em, y: 0.5em), above: 0pt,
      [#text(size: 0.9em, salida) \ #text(size: 0.75em, fill: gris.subtitulo, clave)])
  })
}

#let tabla-hoy(celdas) = context {
  let pal = estado-paleta.get()
  set text(size: 0.72em)
  table(columns: (auto, 1fr), inset: (x: 0.5em, y: 0.42em), align: left + top,
    stroke: (x, y) => (bottom: 0.3mm + gris.filas),
    ..celdas.enumerate().map(((i, c)) => if calc.even(i) { text(font: fuentes.titulos, weight: "bold", fill: pal.acento, c) } else { c }))
}

#let colab(url, ejercicios) = context {
  let pal = estado-paleta.get()
  grid(columns: (1fr, auto), column-gutter: 1.2em, align: top,
    {
      text(size: 0.8em)[Abre el cuaderno de la sesión en Colab, con los ejemplos de hoy y estos ejercicios:]
      v(0.4em)
      set text(size: 0.78em)
      enum(..ejercicios)
    },
    align(center, {
      qrcode(url, width: 5.2cm)
      v(0.2em)
      text(size: 0.55em, fill: gris.banda)[Cuaderno en Colab]
    }))
}

#let tarea-casa(pasos, comprobacion) = context {
  let pal = estado-paleta.get()
  set text(size: 0.7em)
  enum(..pasos)
  if comprobacion != none {
    block(above: 0.8em, width: 100%, fill: pal.suave, inset: (x: 0.7em, y: 0.5em),
      [#micro("Comprobación", color: pal.rotulo, talla: 0.75em)#h(0.6em)#comprobacion])
  }
}

#let cierre(qr: none, siguiente: none) = context {
  let pal = estado-paleta.get()
  grid(columns: (1fr, auto), column-gutter: 1.2em, align: top,
    {
      if qr != none { text(size: 0.9em)[Las *preguntas tipo examen* del capítulo, en directo: se corrigen al momento.] }
      v(1fr)
      if siguiente != none {
        micro("La próxima sesión", color: pal.rotulo, talla: 0.65em)
        v(0.2em)
        text(font: fuentes.titulos, weight: "bold", size: 1em, siguiente)
      }
    },
    if qr != none { align(center, { qrcode(qr, width: 5.2cm); v(0.2em); text(size: 0.55em, fill: gris.banda)[Preguntas del capítulo] }) })
}

// Un contenido con un QR a la derecha (el cuaderno del proyecto, el simulacro…)
#let con-qr(url, pie, cuerpo) = grid(columns: (1fr, auto), column-gutter: 1.2em, align: top,
  cuerpo,
  align(center, {
    qrcode(url, width: 4.6cm)
    v(0.2em)
    text(size: 0.55em, fill: gris.banda, pie)
  }))
