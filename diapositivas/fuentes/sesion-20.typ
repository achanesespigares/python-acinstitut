// Sesión 20 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 20, tema: "Sesión 20 · Nombres ocultos y polimorfismo")

#portada([Nombres ocultos y polimorfismo], subtitulo: [Proteger los datos internos de un objeto y escribir código que funcione con cualquier clase que tenga los métodos adecuados.], kicker: "Sesión 20 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 19.], [0:15], [Situación: la trastienda de una tienda; los clientes pueden entrar, pero hay un cartel de «solo personal».], [0:25], [#strong[Predice] y visualizador: el atributo existe con otro nombre.], [0:45], [Construcción: atributos de clase e instancia, #raw("__dict__"), desfiguración de nombres, sobrescritura,…], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen y tarea 20.],))

== Para empezar

#situacion[La trastienda de una tienda; los clientes pueden entrar, pero hay un cartel de «solo personal».]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("class Caja:\n    def __init__(self):\n        self.__secreto = 42\n        self._interno = 1\n\nc = Caja()\nprint(c._interno)\nprint(hasattr(c, \"__secreto\"), hasattr(c, \"_Caja__secreto\"))", talla: 17pt), uncover("2-", respuesta([#raw("1") · #raw("False True")], [#raw("__secreto") se guarda como #raw("_Caja__secreto").])))

== Atributos de clase y de instancia

#fuente[Clases a fondo · 1]

#codigo("class Alumno:\n    total = 0\n    def __init__(self, nombre):\n        self.nombre = nombre\n        Alumno.total = Alumno.total + 1\n\na = Alumno(\"Ana\")\nb = Alumno(\"Biel\")\nprint(Alumno.total, a.total)")

== Nombres ocultos: la desfiguración de nombres

#fuente[Clases a fondo · 2]

#codigo("try:\n    print(c.__saldo)\nexcept AttributeError as e:\n    print(\"Error:\", e)\nprint(c._Cuenta__saldo)    # posible, pero es saltarse la protección a propósito", talla: 13pt)

== Herencia, sobrescritura y polimorfismo

#fuente[Clases a fondo · 3]

#codigo("class Cachorro(Perro):\n    def habla(self):\n        return super().habla() + \" (flojito)\"\n\nprint(Cachorro(\"Toby\").habla())")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-20.ipynb", ([¿Qué imprime?], [Desfiguración. Para class Caja: con self.\_\_secreto = 7 en su…], [Polimorfismo. Añade una clase Vaca(Animal) que diga «¡Muu!» y métela…], [MRO. Con las clases A, B, C del apartado 4, ¿qué imprime…], [Introspección. Escribe una expresión que diga si un objeto p tiene un…],))

== Tarea 20 · Productos con precio protegido

#tarea-casa(([Crea la clase #raw("Producto") con dos atributos de clase: #raw("creados = 0") e #raw("IVA = 0.21").], [En el constructor guarda el nombre y llama a #raw("set_precio(precio)").], [#raw("set_precio") guarda el precio en #raw("self.__precio") y lanza #raw("ValueError") si no es positivo.], [Añade #raw("get_precio()") y #raw("precio_con_iva()"), redondeado a céntimos.], [Crea dos productos, intenta crear uno con precio 0 y comprueba cuántos se han creado.],), [Una libreta de 2 € cuesta 2,42 € con IVA, y el producto con precio 0 no cuenta.])

== Antes de irte
#cierre(qr: "https://achanesespigares.github.io/python-acinstitut/capitulos/clases-a-fondo/#preguntas-tipo-examen", siguiente: [Sesión 21 · Herencia múltiple, MRO e introspección])
