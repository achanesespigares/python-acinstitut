// Sesión 17 · generado por herramientas/sesiones.py a partir de la guía del curso: no se edita a mano
#import "../comun-diapos.typ": *
#show: diapos.with(sesion: 17, tema: "Sesión 17 · Excepciones a fondo")

#portada([Excepciones a fondo], subtitulo: [Lanzar excepciones, crear las propias y controlar exactamente qué parte de un #raw("try") se ejecuta.], kicker: "Sesión 17 · Módulo 2", firma: [Antonio Chanes Espigares · CC BY-NC-SA 4.0])

== Hoy

#tabla-hoy(([0:00], [Corrección de la tarea 16.], [0:15], [Situación: un parte de incidencias; cada tipo de avería va a un técnico distinto.], [0:25], [#strong[Predice]. El #raw("finally") imprime antes que el #raw("print") de fuera, aunque haya un #raw("return").], [0:45], [Construcción: #raw("raise"), #raw("else"), #raw("finally"), orden de los #raw("except"), varios tipos en un #raw("except"), jerarquía hasta…], [1:20], [Ejercicios del capítulo.], [1:45], [Preguntas tipo examen y tarea 17.],))

== Para empezar

#situacion[Un parte de incidencias; cada tipo de avería va a un técnico distinto.]

== Predice

#text(size: 0.8em, fill: gris.banda)[Escribe en papel qué crees que pasará. Después, lo ejecutamos.]

#grid(columns: (1.4fr, 1fr), column-gutter: 1em, align: top, codigo("def f(x):\n    try:\n        return 10 / x\n    except ZeroDivisionError:\n        return \"div0\"\n    finally:\n        print(\"f\", x)\n\nprint(f(2))\nprint(f(0))", talla: 17pt), uncover("2-", respuesta([#raw("f 2") · #raw("5.0") · #raw("f 0") · #raw("div0")], [#raw("finally") se ejecuta antes de que el valor devuelto llegue al #raw("print").])))

== Lanzar tus propias excepciones

#fuente[Excepciones · 3]

#codigo("def raiz(x):\n    if x < 0:\n        raise ValueError(\"número negativo\")\n    return x ** 0.5\n\ntry:\n    r = raiz(-4)\nexcept ValueError as e:\n    r = None\n    print(\"Error:\", e)\nprint(r)")

== #raw("else"), #raw("finally") y el orden de los #raw("except")

#fuente[Excepciones · 4]

#codigo("def dividir(a, b):\n    try:\n        resultado = a / b\n    except ZeroDivisionError:\n        print(\"No se puede dividir entre 0\")\n    else:\n        print(\"Resultado:\", resultado)    # solo si NO hubo error\n    finally:\n        print(\"Fin del intento\")          # SIEMPRE, haya error o no\n\ndividir(10, 2)\ndividir(10, 0)", talla: 15pt)

== Tus propias clases de excepción

#fuente[Excepciones · 5]

#codigo("class NotaInvalida(Exception):\n    pass\n\ndef comprobar(nota):\n    if not 0 <= nota <= 10:\n        raise NotaInvalida(f\"{nota} no está entre 0 y 10\")\n    return nota\n\ntry:\n    comprobar(12)\nexcept NotaInvalida as e:\n    print(\"Error:\", e)", talla: 17pt)

== Varios tipos a la vez, la jerarquía entera y volver a lanzar

#fuente[Excepciones · 6]

#codigo("def convierte(texto, divisor):\n    try:\n        return int(texto) / divisor\n    except (ValueError, ZeroDivisionError) as e:\n        print(\"No se puede:\", type(e).__name__)\n        return None\n\nprint(convierte(\"8\", 2))\nprint(convierte(\"ocho\", 2))\nprint(convierte(\"8\", 0))")

== Manos a la obra

#colab("https://colab.research.google.com/github/achanesespigares/python-acinstitut/blob/main/cuadernos/sesion-17.ipynb", ([¿Qué imprime?], [Pedir un número], [El orden. ¿Qué imprime este programa? ¿Cómo lo arreglarías?],))

== Tarea 17 · Un entero en su rango

#tarea-casa(([Crea la clase #raw("FueraDeRango"), hija de #raw("ValueError"), cuyo constructor reciba el valor, el mínimo y el máximo, y prepare…], [Escribe #raw("a_entero(texto, minimo, maximo)"): convierte con #raw("int") y, si el número no está en el rango, lanza…], [Escribe #raw("pedir_entero(pregunta, minimo, maximo)"), que pregunta con #raw("input") hasta recibir un dato válido.], [Usa la rama #raw("else") del #raw("try") para devolver el número.], [¿Qué pasaría si capturaras #raw("ValueError") antes que #raw("FueraDeRango")?],), [Si se escribe #raw("doce"), luego #raw("150") y luego #raw("15"), con el rango 0–120, salen dos avisos distintos y se devuelve 15.])

== Antes de irte
#cierre(qr: "https://python.antonychanes.com/capitulos/excepciones/#preguntas-tipo-examen", siguiente: [Sesión 18 · Clases y objetos])
