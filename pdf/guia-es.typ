// Programación en Python · El curso en 30 sesiones · guía del profesor (castellano)
// Se genera con: python3 md2typ.py es  →  typst compile guia-es.typ
#import "comun.typ": *

#show: hoja.with(piel: "ac-institut", asignatura: "Programación en Python", paleta: "matematicas",
  pie-parte: true, titulo: "El curso en 30 sesiones · Programación en Python")
#show: estilo-codigo
#set par(justify: false)
#set list(indent: 0.4em)
#set enum(indent: 0.2em)

#portada-hoja(piel: "ac-institut", kicker: [AC Institut · Programación en Python],
  [El curso en 30 sesiones], linea: [De cero al PCEP, y del PCEP al PCAP],
  subtitulo: [La guía del profesor: el guion de cada sesión de dos horas, el programa para predecir,
    la tarea semiguiada y los dos proyectos de cierre de módulo. Las soluciones, al final.],
  caja: (izq: "Contenido", der: "30 sesiones · 2 h", cuerpo: [
    #set text(size: 9.5pt)
    #filas-ficha((
      ("Módulo 1", [Sesiones 1 a 15. De cero al temario completo del PCEP.]),
      ("Módulo 2", [Sesiones 16 a 30. Del PCEP al PCAP.]),
      ("Proyectos", [Un gestor de notas y una biblioteca orientada a objetos, con hitos y rúbrica.]),
      ("Soluciones", [Lo que sale en cada «Predice», las 26 tareas y las soluciones de referencia.]),
    ))
  ]),
  firma: "Antonio Chanes Espigares · 2026 · Barcelona")

#creditos(titulo: [El curso en 30 sesiones], obra: "El curso en 30 sesiones",
  filas: (
    ("Autor", [Antonio Chanes Espigares]),
    ("Obra", [Guía del curso del libro _Programación en Python · Ver el código pensar_]),
    ("En la web", [#link("https://achanesespigares.github.io/python-acinstitut/")[achanesespigares.github.io/python-acinstitut]: el libro, con los visualizadores, las preguntas tipo examen y los simulacros]),
    ("Edición", [Primera edición · noviembre de 2026]),
    ("Código", [Todos los programas, tareas y soluciones de referencia se han ejecutado con Python 3 y dan exactamente lo que dice el texto.]),
  ))

#indice()

#parte("I", "El curso", linea: [El mapa de las 30 sesiones, cómo es una sesión y cómo se evalúa])
#include "build/es/parte-curso.typ"

#parte("II", "Módulo 1", linea: [De cero al PCEP · sesiones 1 a 15])
#include "build/es/modulo-1.typ"

#parte("III", "Módulo 2", linea: [Del PCEP al PCAP · sesiones 16 a 30])
#include "build/es/modulo-2.typ"

#parte("IV", "Proyectos", linea: [Los proyectos de cierre de cada módulo, con hitos y rúbrica])
#include "build/es/proyectos.typ"

#parte("V", "Soluciones", linea: [Los «Predice», las tareas y las soluciones de referencia de los proyectos])
#include "build/es/soluciones.typ"
