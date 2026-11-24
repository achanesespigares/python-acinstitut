// Piezas propias de la guía del curso, sobre ac-institut 0.3.1 (sin tocar el paquete)
#import "@local/ac-institut:0.3.1": *

#let mono = ("IBM Plex Mono", "DejaVu Sans Mono")
#let _clave(loc) = loc.page() * 100000 + loc.position().y.pt()

// Código: fondo gris superficie, filete de acento a la izquierda, IBM Plex Mono
#let _en-prediccion = state("guia-en-prediccion", false)
#let estilo-codigo(doc) = {
  show raw: set text(font: mono)
  show raw.where(block: false): set text(size: 1.12em)
  show raw.where(block: false): it => box(fill: gris.superficie, inset: (x: 0.22em, y: 0em),
    outset: (y: 0.22em), radius: 0.8mm, it)
  show raw.where(block: true): set text(size: 8.6pt)
  show raw.where(block: true): it => context {
    let pal = estado-paleta.get()
    let dentro = _en-prediccion.get()
    block(width: 100%, fill: gris.superficie, stroke: if dentro { none } else { (left: 0.8mm + pal.acento) },
      inset: (left: 0.9em, right: 0.7em, y: 0.65em), spacing: 1em, breakable: true, {
        set par(justify: false, leading: 0.5em)
        it
      })
  }
  doc
}

// Enlace al libro en la web, con el color de la paleta
#let web(url, cuerpo) = context link(url, text(fill: estado-paleta.get().oscuro, cuerpo))

// Unidad del libro (sesión, capítulo de la guía o proyecto): deja la misma marca que capitulo()
// para que el índice y las portadillas de parte la listen, con su propio rótulo pequeño.
#let unidad(n, titulo, rotulo: none, entradilla: none) = {
  pagebreak(weak: true)
  [#metadata((tipo: "capitulo", n: n, titulo: titulo)) <ac-capitulo>]
  place(hide(heading(level: 2, bookmarked: true)[#if n != "" [#n · ]#titulo]))
  if rotulo != none {
    context micro(rotulo, color: estado-paleta.get().rotulo, talla: 0.85em)
    v(2.5mm, weak: true)
  }
  block(spacing: 0pt, text(font: fuentes.titulos, weight: "bold", size: 21pt, hyphenate: false, titulo))
  if entradilla != none { v(3mm, weak: true); block(text(size: 10.5pt, fill: gris.subtitulo, entradilla)) }
  v(2.5mm, weak: true)
  line(length: 100%, stroke: 0.35mm + gris.filete)
  v(4mm)
}

// Apartado dentro de una unidad (el \apartado de estilo-axiom: cuadrado de color + título)
#let apartado-guia(t) = context {
  let pal = estado-paleta.get()
  block(above: 1.6em, below: 0.8em, sticky: true, {
    box(width: 2mm, height: 2mm, fill: pal.acento, baseline: -0.5mm)
    h(2.2mm)
    text(font: fuentes.titulos, weight: "bold", size: 12.5pt, hyphenate: false, t)
  })
}
#let subapartado-guia(t) = block(above: 1.3em, below: 0.6em, sticky: true,
  text(font: fuentes.titulos, weight: "semibold", size: 10.5pt, hyphenate: false, t))

// Tarea semiguiada: caja «hoja» con cabecera de acento; se puede partir entre páginas
#let tarea(titulo, cuerpo) = context {
  let pal = estado-paleta.get()
  block(width: 100%, stroke: 0.45mm + black, breakable: true, above: 1.6em, below: 1.2em, {
    block(width: 100%, fill: pal.acento, inset: (x: 0.85em, y: 0.5em), below: 0pt, sticky: true,
      micro(titulo, color: white))
    block(width: 100%, inset: (x: 0.85em, y: 0.75em), above: 0pt, cuerpo)
  })
}

// Línea de comprobación al pie de una tarea
#let comprobacion(cuerpo) = context {
  let pal = estado-paleta.get()
  block(above: 0.9em, width: 100%, fill: pal.suave, inset: (x: 0.7em, y: 0.55em),
    [#micro("Comprobación", color: pal.rotulo, talla: 0.72em)#h(0.6em)#cuerpo])
}

// Ficha de cabecera de una sesión (Objetivo · En el libro)
#let ficha-sesion(filas) = block(below: 1.2em, filas-ficha(filas, ancho-rotulo: 24mm, talla: 9.8pt))

// Tabla Axiom: cabecera en rótulo pequeño, filas separadas por raya fina
#let tabla(anchos, cabecera, filas) = context {
  let pal = estado-paleta.get()
  set par(justify: false, leading: 0.5em)
  block(above: 1em, below: 1.2em, table(
    columns: anchos,
    stroke: (x, y) => (bottom: if y == 0 { 0.45mm + gris.tinta } else { 0.25mm + gris.filas }),
    inset: (x: 0.45em, y: 0.5em),
    align: left + top,
    table.header(..cabecera.map(c => micro(c, color: pal.rotulo, talla: 0.72em))),
    ..filas.flatten().map(c => text(size: 9.2pt, c)),
  ))
}

// Panorámica de las 30 sesiones: una ficha por sesión, por módulos
#let panoramica(sesiones) = context {
  let pal = estado-paleta.get()
  let ficha(s) = {
    let fuerte = s.tipo != "normal"
    block(width: 100%, height: 23mm, breakable: false,
      fill: if fuerte { pal.acento } else { pal.suave },
      stroke: if fuerte { none } else { 0.25mm + pal.acento.lighten(40%) },
      inset: (x: 2.2mm, y: 2mm), {
        set par(justify: false, leading: 0.38em)
        text(font: fuentes.titulos, weight: "bold", size: 15pt,
          fill: if fuerte { white } else { pal.acento }, str(s.n))
        v(1mm)
        text(size: 7.2pt, fill: if fuerte { white } else { gris.tinta }, hyphenate: true, s.tema)
        place(bottom + left, text(font: fuentes.titulos, weight: "semibold", size: 5.8pt, tracking: 0.06em,
          fill: if fuerte { white } else { gris.banda }, upper(s.sale)))
      })
  }
  for (titulo, grupo) in (("Módulo 1 · De cero al PCEP", sesiones.slice(0, 15)),
                          ("Módulo 2 · Del PCEP al PCAP", sesiones.slice(15))) {
    block(above: 1em, below: 0.6em, sticky: true, micro(titulo, color: pal.rotulo, talla: 0.8em))
    grid(columns: (1fr,) * 5, gutter: 2mm, ..grupo.map(ficha))
  }
  v(2mm)
  grid(columns: (auto, auto, auto, auto), column-gutter: 2.5mm, align: horizon,
    box(width: 4mm, height: 3mm, fill: pal.suave, stroke: 0.25mm + pal.acento.lighten(40%)),
    text(size: 8pt)[sesión con tarea semiguiada],
    box(width: 4mm, height: 3mm, fill: pal.acento),
    text(size: 8pt)[proyecto, simulacro o exposición])
}

// Créditos con licencia CC BY-NC-ND 4.0 (la del libro en la web), más el permiso para los programas
#let creditos(titulo: none, filas: (), obra: none, autor: "Antonio Chanes Espigares", anio: "2026") = {
  let deed = "https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es"
  pagebreak(weak: true)
  context {
    let pal = estado-paleta.get()
    set par(justify: false)
    micro("Créditos", color: gris.banda, talla: 0.8em)
    v(4mm)
    block(spacing: 0pt, text(font: fuentes.titulos, weight: "bold", size: 21pt, hyphenate: false, titulo))
    v(3mm)
    line(length: 100%, stroke: 0.35mm + gris.filete)
    v(5mm)
    filas-ficha(filas)
    v(12mm)
    caja-hoja("Licencia", "CC BY-NC-ND 4.0", pal: pal, {
      set par(justify: false, leading: 0.55em)
      grid(columns: (auto, 1fr), column-gutter: 5mm, align: horizon,
        link(deed, stack(dir: ltr, spacing: 1.1mm,
          ..("cc", "by", "nc", "nd").map(i => image("marcas/cc-" + i + ".svg", height: 7.5mm)))),
        text(size: 9.5pt)[«#obra» © #anio de #autor está bajo una licencia Creative Commons
          Atribución-NoComercial-SinDerivadas 4.0 Internacional. Para ver una copia de esta licencia,
          visita #link(deed)[creativecommons.org/licenses/by-nc-nd/4.0/deed.es].])
      v(3.5mm)
      filas-ficha((
        ("Puedes", [*Compartir* el material: copiarlo y redistribuirlo en cualquier medio o formato.]),
        ("Atribución", [Dar crédito de manera adecuada, enlazar la licencia e indicar si se han hecho
          cambios, sin sugerir que el autor respalda tu uso.]),
        ("No comercial", [No usar el material con propósitos comerciales.]),
        ("Sin derivadas", [Si lo remezclas, transformas o creas a partir de él, no puedes difundir
          el material modificado.]),
        ("Además", [Los programas de ejemplo del libro y del laboratorio pueden copiarse, modificarse
          y compartirse libremente para aprender o enseñar.]),
      ), talla: 9pt)
      v(3mm)
      text(size: 8pt, fill: gris.banda)[Resumen orientativo: prevalece el texto legal de la licencia.]
    })
  }
}

// Predicción de una sesión: el código va sin su propio filete (ya lo pone la caja)
#let prediccion-sesion(cuerpo) = prediccion({ _en-prediccion.update(true); cuerpo; _en-prediccion.update(false) })
