---
title: "Proyecto 1 · Gestor de notas de clase"
subtitle: El proyecto de cierre del módulo 1, de la sesión 12 a la 15
---

## El encargo

Un profesor guarda las notas de su grupo en un fichero `notas.csv` y quiere dejar de hacer las cuentas a mano. Necesita un programa de consola que:

- **cargue** el fichero al arrancar, y si no existe empiece con la lista vacía;
- muestre un **menú** que se repite hasta elegir salir;
- **liste** a todo el grupo con sus notas, la nota final y la calificación;
- **añada** alumnos nuevos, pidiendo sus notas sin romperse si se escribe algo raro;
- **busque** a un alumno por su nombre, sin distinguir mayúsculas;
- dé un **resumen** del grupo: media, mejor nota y cuántos aprueban;
- **guarde** los cambios en el mismo fichero al salir.

La nota final pondera los dos parciales al 30 % y las prácticas al 40 %. Una nota que falta (casilla vacía) cuenta como 0.

## Los datos de partida

Cada alumno copia este fichero en su Colab con `%%writefile notas.csv`:

```text
nombre,parcial1,parcial2,practicas
Ana,7.5,8.0,9.0
Bruno,4.0,5.5,6.0
Carla,9.0,9.5,10.0
David,3.0,4.0,
Elena,6.0,5.0,7.5
Fran,8.0,7.0,
```

## Lo que se practica

| Del curso | Dónde aparece en el proyecto |
|---|---|
| Especificación y algoritmo | El hito 1, antes de escribir código |
| Variables, tipos y operadores | La media ponderada |
| Condicionales | La calificación y las opciones del menú |
| Bucles, `break`, `continue` | El menú y la petición de notas |
| Listas y diccionarios | Cada alumno es un diccionario; el grupo, una lista |
| Cadenas y formato | La tabla alineada con f-strings |
| Funciones | Una función por tarea, sin `input` dentro de los cálculos |
| Excepciones | Notas no numéricas y fichero que no existe |
| Ficheros CSV | Cargar y guardar |

## Los hitos

| Sesión | Hito | Qué se entrega |
|---|---|---|
| 12 | **1 · Diseño** | La especificación de cada opción del menú (entradas, salida, casos raros) y el algoritmo de la nota final y del resumen, en lenguaje natural. Cómo se va a guardar un alumno en memoria. |
| 13 | **2 · Funciones** | `nota_final`, `calificacion`, `buscar` y `resumen`, probadas con una lista de alumnos escrita a mano en el código. |
| 14 | **3 · Programa completo** | Cargar y guardar el CSV, el menú, y la petición de notas que no se rompe. |
| 15 | **4 · Exposición** | 5 minutos: demostración en directo, una función explicada por dentro y un error que costó encontrar. |

## La versión mínima y las ampliaciones

Para aprobar el proyecto basta con la **versión mínima**: las cinco opciones del menú funcionando con el fichero de partida.

Ampliaciones, para quien vaya sobrado (cada una suma en la rúbrica):

- modificar las notas de un alumno ya existente;
- borrar un alumno, pidiendo confirmación;
- listar ordenado por nota final;
- exportar un segundo CSV con solo los suspensos;
- elegir el fichero al arrancar.

## La rúbrica

| Criterio | 0 | 1 | 2 |
|---|---|---|---|
| **Funciona** | Falla alguna opción mínima | Todo funciona con datos buenos | Todo funciona también con datos malos |
| **Diseño** | Sin especificación | Especificación incompleta | Especificación y algoritmo claros, entregados a tiempo |
| **Funciones** | Todo en un bloque | Hay funciones, pero mezclan cálculo e `input` | Cada función hace una cosa y devuelve su resultado |
| **Errores** | Se rompe con un dato raro | Controla algunos casos | Controla notas no válidas y fichero ausente |
| **Legibilidad** | Nombres sin sentido | Nombres claros | Nombres claros, comentarios útiles, tabla bien alineada |
| **Exposición** | No se entiende | Se entiende el uso | Se entiende el uso y una función por dentro |
| **Ampliaciones** | Ninguna | Una | Dos o más |

Nota del proyecto: la suma de los siete criterios, sobre 14, pasada a 10.

:::{tip} Cómo acompañar el proyecto
Lo que más ayuda es que el hito 1 se entregue de verdad antes de programar. Quien escribe la especificación del menú ya tiene la mitad del programa: cada fila de su tabla será un `elif`.
:::

---

## Solución de referencia

Una posible solución, solo para el profesor. Tiene unas 160 líneas y usa únicamente lo visto en el módulo 1. Se ha probado con el fichero de partida, con notas no numéricas, con nombres repetidos y con un fichero que no existe.

```python
import csv

RUTA = "notas.csv"
CAMPOS = ["parcial1", "parcial2", "practicas"]
PESOS = [0.3, 0.3, 0.4]


# ---------- datos ----------
def a_nota(texto):
    """Convierte un texto en nota, o devuelve None si está vacío o no es válido."""
    try:
        nota = float(texto)
    except ValueError:
        return None
    if 0 <= nota <= 10:
        return nota
    return None


def cargar(ruta):
    alumnos = []
    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector)                      # la cabecera no es un alumno
            for fila in lector:
                if not fila:
                    continue                  # línea vacía
                alumno = {"nombre": fila[0].strip()}
                for i in range(len(CAMPOS)):
                    texto = fila[i + 1] if i + 1 < len(fila) else ""
                    alumno[CAMPOS[i]] = a_nota(texto)
                alumnos.append(alumno)
    except FileNotFoundError:
        print(f"No encuentro {ruta}; empiezo con la lista vacía.")
    return alumnos


def guardar(ruta, alumnos):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["nombre"] + CAMPOS)
        for a in alumnos:
            fila = [a["nombre"]]
            for campo in CAMPOS:
                fila.append("" if a[campo] is None else a[campo])
            escritor.writerow(fila)


# ---------- cálculos ----------
def nota_final(alumno):
    """Media ponderada; una nota que falta cuenta como 0."""
    total = 0
    for i in range(len(CAMPOS)):
        nota = alumno[CAMPOS[i]]
        if nota is not None:
            total += nota * PESOS[i]
    return round(total, 2)


def calificacion(nota):
    if nota < 5:
        return "Suspenso"
    elif nota < 6:
        return "Suficiente"
    elif nota < 7:
        return "Bien"
    elif nota < 9:
        return "Notable"
    return "Sobresaliente"


def buscar(alumnos, nombre):
    for a in alumnos:
        if a["nombre"].lower() == nombre.lower():
            return a
    return None


def resumen(alumnos):
    if not alumnos:
        return None
    finales = []
    mejor = alumnos[0]
    aprobados = 0
    for a in alumnos:
        nf = nota_final(a)
        finales.append(nf)
        if nf > nota_final(mejor):
            mejor = a
        if nf >= 5:
            aprobados += 1
    return {
        "media": round(sum(finales) / len(finales), 2),
        "mejor": mejor["nombre"],
        "aprobados": aprobados,
        "total": len(alumnos),
    }


# ---------- pantalla ----------
def listar(alumnos):
    print(f"{'Alumno':<10}{'P1':>6}{'P2':>6}{'Pr':>6}{'Final':>7}  Calificación")
    for a in alumnos:
        notas = ""
        for campo in CAMPOS:
            notas += f"{'—' if a[campo] is None else a[campo]:>6}"
        nf = nota_final(a)
        print(f"{a['nombre']:<10}{notas}{nf:>7.2f}  {calificacion(nf)}")


def pedir_nota(pregunta):
    while True:
        texto = input(pregunta)
        if texto == "":
            return None
        nota = a_nota(texto)
        if nota is not None:
            return nota
        print("  Escribe un número entre 0 y 10, o deja en blanco.")


def menu():
    alumnos = cargar(RUTA)
    while True:
        print("\n1 Listar  2 Añadir  3 Buscar  4 Resumen  5 Guardar y salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            listar(alumnos)
        elif opcion == "2":
            nombre = input("Nombre: ").strip()
            if nombre == "" or buscar(alumnos, nombre):
                print("  Nombre vacío o repetido.")
                continue
            alumno = {"nombre": nombre}
            for campo in CAMPOS:
                alumno[campo] = pedir_nota(f"  {campo}: ")
            alumnos.append(alumno)
        elif opcion == "3":
            a = buscar(alumnos, input("Nombre: "))
            if a is None:
                print("  No está.")
            else:
                nf = nota_final(a)
                print(f"  {a['nombre']}: {nf:.2f} ({calificacion(nf)})")
        elif opcion == "4":
            r = resumen(alumnos)
            if r is None:
                print("  No hay alumnos.")
            else:
                print(f"  Media del grupo {r['media']} · mejor {r['mejor']} · "
                      f"aprobados {r['aprobados']} de {r['total']}")
        elif opcion == "5":
            guardar(RUTA, alumnos)
            print("Guardado. ¡Hasta pronto!")
            break
        else:
            print("  Opción no válida.")


if __name__ == "__main__":
    menu()
```

### Una sesión de prueba

Con el fichero de partida, la opción 1 muestra:

```text
Alumno        P1    P2    Pr  Final  Calificación
Ana          7.5   8.0   9.0   8.25  Notable
Bruno        4.0   5.5   6.0   5.25  Suficiente
Carla        9.0   9.5  10.0   9.55  Sobresaliente
David        3.0   4.0     —   2.10  Suspenso
Elena        6.0   5.0   7.5   6.30  Bien
```

Si después se añade a Fran con 8, `siete` (rechazado), 7 y prácticas en blanco, el resumen es: media del grupo 5.99, mejor Carla, 4 aprobados de 6. Al guardar, la línea de Fran queda `Fran,8.0,7.0,` con la casilla de prácticas vacía.

### Decisiones que conviene comentar en clase

- **`a_nota` devuelve `None` en vez de lanzar una excepción**: así la carga del fichero y la petición por teclado comparten la misma regla.
- **El menú es el único sitio con `input`**: las funciones de cálculo se pueden probar sin teclear nada, que es justo lo que pide el hito 2.
- **`next(lector)` salta la cabecera**: sin esa línea, «nombre» se cargaría como un alumno.
- **`if __name__ == "__main__":`** permite importar el fichero para probar sus funciones sin que arranque el menú. Se entiende del todo en la sesión 16, pero se puede usar desde ya.
