// Sesión 19 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 19, tema: "Sesión 19 · Atributos de clase, __str__ y herencia")

#portada([Atributos de clase, #raw("__str__") y herencia], subtitulo: [Compartir datos entre todos los objetos de una clase, darles una representación legible y reutilizar una clase con la herencia.], kicker: "Sesión 19 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-ND 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 18.], [0:15], [Situación: un formulario de matrícula general y el de una beca, que es el mismo con dos casillas más.], [0:25], [#strong[Predice]. El #raw("__str__") de #raw("Animal") llama al #raw("habla") de cada hijo: primer contacto con el polimorfismo.], [0:45], [Construcción: atributos de clase, #raw("__str__"), herencia, #raw("super()").], [1:20], [Ejercicios del capítulo (secciones 3 y 4).], [1:45], [Preguntas tipo examen y tarea 19.],))

== Para empezar

#situacion[Un formulario de matrícula general y el de una beca, que es el mismo con dos casillas más.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("class Animal:\n    patas = 4\n\n    def habla(self):\n        return \"...\"\n\n    def __str__(self):\n        return f\"{type(self).__name__} que dice {self.habla()}\"\n\nclass Perro(Animal):\n    def habla(self):\n        return \"guau\"\n\nclass Gallina(Animal):\n    patas = 2\n\nfor a in [Perro(), Gallina()]:\n    print(a, a.patas)", talla: 13.5pt), uncover("2-", respuesta([#raw("Perro que dice guau 4") · #raw("Gallina que dice ... 2")], [Cada objeto usa el #raw("habla") y el #raw("patas") más cercano en su clase.])))

== Atributos de clase y #raw("__str__")

#fuente[Clases y objetos · 3]

#codigo("class Cuenta:\n    banco = \"Banco AC\"                  # atributo de clase: común a todas\n\n    def __init__(self, titular, saldo):\n        self.titular = titular          # atributos de instancia: propios de cada una\n        self.saldo = saldo\n\n    def __str__(self):\n        return f\"{self.titular}: {self.saldo} € ({Cuenta.banco})\"\n\na = Cuenta(\"Ana\", 130)\nprint(a)\nprint(a.__dict__)                       # los atributos de instancia de a\n…", talla: 13pt)

== Herencia

#fuente[Clases y objetos · 4]

#codigo("class Cuenta:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n\n    def ingresar(self, cantidad):\n        self.saldo = self.saldo + cantidad\n\nclass CuentaAhorro(Cuenta):             # hereda de Cuenta\n    def __init__(self, titular, saldo, interes):\n        super().__init__(titular, saldo)    # reutiliza el __init__ de Cuenta\n        self.interes = interes\n\n…", talla: 13pt)

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-19.ipynb", ([Añade un método], [¿Qué imprime?], [Un rectángulo. Escribe una clase Rectangulo con atributos base y…],))

== Tarea 19 · Figuras

#tarea-casa(([Crea la clase #raw("Figura") con un método #raw("area()") que lance #raw("NotImplementedError") y un #raw("__str__") que escriba el nombre de…], [Crea #raw("Rectangulo(base, altura)") y #raw("Circulo(radio)"), hijas de #raw("Figura"), cada una con su #raw("area()") y su #raw("perimetro()").], [Haz una lista con dos rectángulos y dos círculos, ordénala por área con #raw("sort") y #raw("key"), e imprime cada figura.], [¿Por qué no hace falta escribir #raw("__str__") en las hijas?],), [La figura más pequeña de la lista #raw("[Rectangulo(3, 4), Circulo(1), Rectangulo(1, 1), Circulo(2)]") es el rectángulo de 1 × 1.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/clases/#preguntas-tipo-examen", siguiente: [Sesión 20 · Nombres ocultos y polimorfismo])
