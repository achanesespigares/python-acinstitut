// Sesión 21 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 21, tema: "Sesión 21 · Herencia múltiple, MRO e introspección")

#portada([Herencia múltiple, MRO e introspección], subtitulo: [Saber qué método se ejecuta cuando hay varias clases madre, y preguntar a un objeto por sus atributos y su clase.], kicker: "Sesión 21 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 20.], [0:15], [Situación: preguntar una duda: primero al compañero de mesa, luego al profesor de la materia, luego al tutor.], [0:25], [#strong[Predice]. El MRO se dibuja como un rombo.], [0:45], [Construcción: herencia múltiple, #raw("__mro__"), #raw("isinstance"), #raw("issubclass"), #raw("hasattr"), #raw("getattr"), #raw("is") frente a…], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen y tarea 21.],))

== Para empezar

#situacion[Preguntar una duda: primero al compañero de mesa, luego al profesor de la materia, luego al tutor. Siempre en el mismo orden.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("class A:\n    def quien(self):\n        return \"A\"\n\nclass B(A):\n    def quien(self):\n        return \"B\"\n\nclass C(A):\n    def quien(self):\n        return \"C\"\n\nclass D(B, C):\n    pass\n\nprint(D().quien())\nprint([k.__name__ for k in D.__mro__])\nprint(isinstance(D(), C), issubclass(C, B))", talla: 13.5pt), uncover("2-", respuesta([#raw("B") · #raw("['D', 'B', 'C', 'A', 'object']") · #raw("True False")], [El MRO recorre de izquierda a derecha y deja #raw("A") para el final.])))

== Herencia múltiple y MRO

#fuente[Clases a fondo · 4]

#codigo("class A:\n    def quien(self):\n        return \"A\"\n\nclass B(A):\n    def quien(self):\n        return \"B\"\n\nclass C(A):\n    def quien(self):\n        return \"C\"\n\nclass D(B, C):\n…")

== Introspección: el objeto se describe a sí mismo

#fuente[Clases a fondo · 5]

#codigo("p = Perro(\"Rex\")\nprint(type(p).__name__, Perro.__bases__, Perro.__module__)\nprint(isinstance(p, Animal), issubclass(Perro, Animal), issubclass(Perro, Gato))\nsetattr(p, \"edad\", 3)\nprint(p.__dict__, getattr(p, \"edad\"))", talla: 13pt)

== Construir objetos con cuidado

#fuente[Clases a fondo · 6]

#codigo("class Cuenta:\n    def __init__(self, titular, saldo=0, movimientos=None):\n        if saldo < 0:\n            raise ValueError(\"el saldo inicial no puede ser negativo\")\n        self.titular = titular\n        self.saldo = saldo\n        self.movimientos = [] if movimientos is None else movimientos\n\nc = Cuenta(\"Ana\", saldo=50)        # argumento por nombre: se lee solo\nprint(c.titular, c.saldo, c.movimientos)\ntry:\n    Cuenta(\"Biel\", -10)\nexcept ValueError as e:\n…", talla: 15pt)

== Identidad e igualdad: #raw("is") y #raw("==")

#fuente[Clases a fondo · 7]

#codigo("x = [1, 2]\ny = [1, 2]\nz = x\nprint(x == y, x is y, x is z)\nprint(x is not y)")

== #raw("__str__"), #raw("__repr__") y propiedades

#fuente[Clases a fondo · 8]

#codigo("class Punto:\n    def __init__(self, x, y):\n        self.__x, self.__y = x, y\n\n    @property\n    def x(self):\n        return self.__x\n\n    def __str__(self):\n        return f\"({self.__x}, {self.__y})\"\n\n    def __repr__(self):\n        return f\"Punto({self.__x}, {self.__y})\"\n…")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-21.ipynb", ([¿Qué imprime?], [Desfiguración. Para class Caja: con self.\_\_secreto = 7 en su…], [Polimorfismo. Añade una clase Vaca(Animal) que diga «¡Muu!» y métela…], [MRO. Con las clases A, B, C del apartado 4, ¿qué imprime…], [Introspección. Escribe una expresión que diga si un objeto p tiene un…],))

== Tarea 21 · El rombo y las órdenes por nombre

#tarea-casa(([Crea cuatro clases en rombo: #raw("Base"), #raw("Izq(Base)"), #raw("Der(Base)") y #raw("Abajo(Izq, Der)").], [#strong[Predice] en qué orden salen los cuatro nombres al crear un #raw("Abajo()"), y después compruébalo con #raw("Abajo.__mro__").], [Crea una clase #raw("Robot") con los métodos #raw("saluda()") y #raw("avanza()").], [Con una lista de órdenes en texto, #raw("[\"saluda\", \"baila\", \"avanza\"]"), ejecuta cada una con #raw("getattr") si el robot la tiene…],), [#raw("Base") se imprime una sola vez, la última.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/clases-a-fondo/#preguntas-tipo-examen", siguiente: [Sesión 22 · Comprensiones y el #raw("else") de los bucles])
