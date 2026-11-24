// Sesión 18 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 18, tema: "Sesión 18 · Clases y objetos")

#portada([Clases y objetos], subtitulo: [Definir una clase con su constructor y sus métodos, crear objetos y distinguir dos objetos iguales de dos nombres para el mismo objeto.], kicker: "Sesión 18 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 17.], [0:15], [Situación: el plano de una casa y las casas construidas con él.], [0:25], [#strong[Predice] y visualizador: solo hay un objeto con dos nombres.], [0:45], [Construcción: #raw("class"), #raw("__init__"), #raw("self"), atributos, métodos, identidad.], [1:20], [Ejercicios del capítulo (los de las secciones 1 y 2).], [1:45], [Tarea 18.],))

== Para empezar

#situacion[El plano de una casa y las casas construidas con él. Pintar una no pinta las demás.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("class Contador:\n    def __init__(self):\n        self.n = 0\n\n    def suma(self):\n        self.n += 1\n        return self\n\na = Contador()\nb = a\na.suma().suma()\nb.suma()\nprint(a.n, b.n, a is b)", talla: 16pt), uncover("2-", respuesta([#raw("3 3 True")], [#raw("a") y #raw("b") son el mismo objeto; #raw("suma") devuelve #raw("self") y se puede encadenar.])))

== Una cuenta bancaria

#fuente[Clases y objetos · 1]

#codigo("class Cuenta:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n\n    def ingresar(self, cantidad):\n        self.saldo = self.saldo + cantidad\n\nc = Cuenta(\"Ana\", 100)\nc.ingresar(50)\nprint(c.titular, c.saldo)")

== Dos cuentas y un alias

#fuente[Clases y objetos · 2]

#codigo("class Cuenta:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n\n    def ingresar(self, cantidad):\n        self.saldo = self.saldo + cantidad\n\na = Cuenta(\"Ana\", 100)\nb = Cuenta(\"Biel\", 20)\nc = a\nc.ingresar(30)\nprint(a.saldo, b.saldo)")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-18.ipynb", ([Añade un método], [¿Qué imprime?], [Un rectángulo. Escribe una clase Rectangulo con atributos base y…],))

== Tarea 18 · Un termómetro

#tarea-casa(([Crea la clase #raw("Termometro") con un constructor que reciba los grados Celsius, 0 por defecto.], [Guarda también la temperatura máxima registrada, que al principio es la inicial.], [Añade #raw("a_fahrenheit()"), que devuelve la temperatura en °F (por 9\/5, más 32).], [Añade #raw("cambiar(grados)"), que sube o baja la temperatura y actualiza la máxima si hace falta.], [Crea un termómetro a 20 °C, súbelo 5 y bájalo 8.],), [Queda a 17 °C, con máxima de 25 °C, que son 62,6 °F.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/clases/#preguntas-tipo-examen", siguiente: [Sesión 19 · Atributos de clase, #raw("__str__") y herencia])
