---
title: Ficheros y flujos
subtitle: Que los datos sobrevivan al programa
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Lo que apuntas en la pizarra desaparece cuando la borras; lo que escribes en tu libreta sigue ahí mañana. La memoria del programa es la pizarra: al terminar, se borra. Un fichero en el disco es la libreta.

## La pregunta

¿Cómo escribe un programa datos en un fichero y cómo los lee otro día? ¿Y qué diferencia hay entre un fichero de texto y uno de bytes?

## La idea

Python habla con los ficheros a través de **flujos** (*streams*): un canal por el que salen o entran datos en orden, como el agua por una tubería. Se abre con `open`:

```python
f = open("notas.txt", "w")      # nombre del fichero y modo
```

| Modo | Para qué | Si el fichero no existe | Si existe |
|---|---|---|---|
| `"r"` | leer (es el modo por defecto) | error `FileNotFoundError` | lo lee |
| `"w"` | escribir | lo crea | **lo vacía** y escribe desde cero |
| `"a"` | añadir al final | lo crea | escribe a continuación |
| `"x"` | crear | lo crea | error `FileExistsError` |
| `"t"` añadido | modo texto: `"rt"`, `"wt"`… (es el de por defecto) | | lee y escribe `str` |
| `"b"` añadido | modo binario: `"rb"`, `"wb"`… | | lee y escribe bytes, no texto |
| `"+"` añadido | leer y escribir: `"r+"`, `"w+"`… | | |

Lo más seguro es abrirlo con **`with`**: al salir del bloque, Python lo cierra solo, aunque haya un error en medio.

```python
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("7\n")
# aquí el fichero ya está cerrado
```

:::{important} Pon siempre `encoding="utf-8"` en los ficheros de texto
Si no lo pones, Python usa la codificación del sistema, que no es la misma en Windows que en Mac o Linux. Con una `ñ` o una tilde, el mismo fichero se leería distinto en cada ordenador.
:::

## Construcción

### 1 · Escribir y volver a leer

:::{tip} Predice
Después de los dos `write`, ¿estará ya el texto en el disco? ¿Qué valor tendrá `linea` en la primera vuelta del segundo bucle?
:::

```{code-cell} python
with open("notas.txt", "w") as f:
    f.write("7\n")
    f.write("9\n")
total = 0
with open("notas.txt") as f:
    for linea in f:
        total = total + int(linea)
print(total)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Escribir y volver a leer","etiqueta":"open · with · búfer","idea":"Mira la caja Disco. Lo escrito no llega al disco en cada write: espera en un búfer y se vuelca al cerrar el fichero, al final del with. Al leer, el for entrega el fichero línea a línea, cada una con su salto de línea.","cabecera":6,"puntero":"linea","columnas":["total"],"fila_en":"cada_linea"},"traza":{"codigo":"with open(\"notas.txt\", \"w\") as f:\n    f.write(\"7\\n\")\n    f.write(\"9\\n\")\ntotal = 0\nwith open(\"notas.txt\") as f:\n    for linea in f:\n        total = total + int(linea)\nprint(total)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"f":{"__txt__":"fichero 'notas.txt' abierto en modo 'w'"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.txt' abierto en modo 'w'"},"tipos":{"f":"TextIOWrapper"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":0,"contenido":"","binario":false}]},{"linea":2,"estado":{"f":{"__txt__":"fichero 'notas.txt' abierto en modo 'w'"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.txt' abierto en modo 'w'"},"tipos":{"f":"TextIOWrapper"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":0,"contenido":"","binario":false}]},{"linea":3,"estado":{"f":{"__txt__":"fichero 'notas.txt' abierto en modo 'w'"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.txt' abierto en modo 'w'"},"tipos":{"f":"TextIOWrapper"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":0,"contenido":"","binario":false}]},{"linea":1,"estado":{"f":{"__txt__":"fichero 'notas.txt' (cerrado)"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"f":"fichero 'notas.txt' (cerrado)"},"tipos":{"f":"TextIOWrapper"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]},{"linea":4,"estado":{"f":{"__txt__":"fichero 'notas.txt' (cerrado)"},"total":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":0,"repr":{"f":"fichero 'notas.txt' (cerrado)","total":"0"},"tipos":{"f":"TextIOWrapper","total":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]},{"linea":5,"estado":{"f":{"__txt__":"fichero 'notas.txt' abierto en modo 'r'"},"total":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":1,"repr":{"f":"fichero 'notas.txt' abierto en modo 'r'","total":"0"},"tipos":{"f":"TextIOWrapper","total":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]},{"linea":6,"estado":{"f":{"__txt__":"fichero 'notas.txt' abierto en modo 'r'"},"total":0,"linea":"7\n"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":2,"repr":{"f":"fichero 'notas.txt' abierto en modo 'r'","total":"0","linea":"'7\\n'"},"tipos":{"f":"TextIOWrapper","total":"int","linea":"str"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]},{"linea":7,"estado":{"f":{"__txt__":"fichero 'notas.txt' abierto en modo 'r'"},"total":7,"linea":"7\n"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":3,"repr":{"f":"fichero 'notas.txt' abierto en modo 'r'","total":"7","linea":"'7\\n'"},"tipos":{"f":"TextIOWrapper","total":"int","linea":"str"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]},{"linea":6,"estado":{"f":{"__txt__":"fichero 'notas.txt' abierto en modo 'r'"},"total":7,"linea":"9\n"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":4,"repr":{"f":"fichero 'notas.txt' abierto en modo 'r'","total":"7","linea":"'9\\n'"},"tipos":{"f":"TextIOWrapper","total":"int","linea":"str"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]},{"linea":7,"estado":{"f":{"__txt__":"fichero 'notas.txt' abierto en modo 'r'"},"total":16,"linea":"9\n"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":5,"repr":{"f":"fichero 'notas.txt' abierto en modo 'r'","total":"16","linea":"'9\\n'"},"tipos":{"f":"TextIOWrapper","total":"int","linea":"str"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]},{"linea":6,"estado":{"f":{"__txt__":"fichero 'notas.txt' abierto en modo 'r'"},"total":16,"linea":"9\n"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":6,"repr":{"f":"fichero 'notas.txt' abierto en modo 'r'","total":"16","linea":"'9\\n'"},"tipos":{"f":"TextIOWrapper","total":"int","linea":"str"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]},{"linea":5,"estado":{"f":{"__txt__":"fichero 'notas.txt' (cerrado)"},"total":16,"linea":"9\n"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":7,"repr":{"f":"fichero 'notas.txt' (cerrado)","total":"16","linea":"'9\\n'"},"tipos":{"f":"TextIOWrapper","total":"int","linea":"str"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]},{"linea":8,"estado":{"f":{"__txt__":"fichero 'notas.txt' (cerrado)"},"total":16,"linea":"9\n"},"salida":"16\n","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":8,"repr":{"f":"fichero 'notas.txt' (cerrado)","total":"16","linea":"'9\\n'"},"tipos":{"f":"TextIOWrapper","total":"int","linea":"str"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"notas.txt","tam":4,"contenido":"7\n9\n","binario":false}]}],"filas":[["4","0"],["5","0"],["6","0"],["7","7"],["6","7"],["7","16"],["6","16"],["5","16"],["8","16"]]}}
```

Dos detalles que el visualizador deja a la vista:

- **El búfer.** Escribir en el disco es lento, así que Python acumula lo escrito y lo vuelca de golpe al cerrar (o con `f.flush()`). Si un programa termina sin cerrar el fichero, puede perder lo último que escribió. Con `with`, no pasa.
- **El salto de línea.** Cada línea leída termina en `"\n"`. `int("7\n")` funciona porque `int` ignora los espacios y saltos de los extremos, pero para comparar texto conviene limpiarlo con `linea.strip()`.

En el libro, los ejemplos con ficheros se ejecutan en una carpeta temporal: los ficheros se ven en la caja Disco, pero no se guardan en tu ordenador.

### 2 · Las formas de leer

```{code-cell} python
with open("lista.txt", "w", encoding="utf-8") as f:
    f.write("pan\nleche\nhuevos\n")

with open("lista.txt", encoding="utf-8") as f:
    print(repr(f.read()))          # todo el texto de golpe

with open("lista.txt", encoding="utf-8") as f:
    print(repr(f.readline()))      # una línea
    print(f.readlines())           # las que quedan, en una lista

with open("lista.txt", encoding="utf-8") as f:
    print([l.strip() for l in f])  # recorriendo: lo más habitual
```

`f.read(5)` lee solo 5 caracteres. Cuando no queda nada, `read()` y `readline()` devuelven la cadena vacía `""`.

### 3 · Cuando abrir falla

Abrir un fichero que no existe lanza `FileNotFoundError`. Todas las excepciones de entrada y salida heredan de `OSError`, y su atributo `errno` dice el código del error del sistema:

```{code-cell} python
import errno

try:
    with open("no_existe.txt") as f:
        print(f.read())
except FileNotFoundError as e:
    print("No está:", e.filename)
    print(e.errno == errno.ENOENT, e.strerror)
```

| Excepción | Código `errno` | Cuándo |
|---|---|---|
| `FileNotFoundError` | `ENOENT` | el fichero no existe |
| `PermissionError` | `EACCES` | no tienes permiso |
| `IsADirectoryError` | `EISDIR` | es una carpeta, no un fichero |
| `FileExistsError` | `EEXIST` | ya existe (modo `"x"`) |

### 4 · Flujos binarios y `bytearray`

Un fichero de texto guarda caracteres; uno binario guarda **bytes**, números de 0 a 255. Para trabajar con bytes que se pueden cambiar existe `bytearray`, una lista de bytes modificable casilla a casilla.

:::{tip} Predice
¿Qué número habrá en cada casilla al terminar el bucle? ¿Cuántos bytes ocupará el fichero?
:::

```{code-cell} python
datos = bytearray(4)
for i in range(len(datos)):
    datos[i] = 65 + i
with open("datos.bin", "wb") as f:
    f.write(datos)
print(datos)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Bytes a mano","etiqueta":"bytearray · modo wb","idea":"bytearray(4) crea cuatro bytes a 0. El bucle los rellena con 65, 66, 67 y 68. En el disco, el fichero ocupa exactamente 4 bytes, que el visualizador enseña en hexadecimal: 41 42 43 44.","lista":"datos","cabecera":2,"puntero":"i","foco":"i","columnas":["i","datos[i]"],"fila_en":"fin_iteracion"},"traza":{"codigo":"datos = bytearray(4)\nfor i in range(len(datos)):\n    datos[i] = 65 + i\nwith open(\"datos.bin\", \"wb\") as f:\n    f.write(datos)\nprint(datos)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"datos":{"__bytes__":[0,0,0,0],"repr":"bytearray(b'\\x00\\x00\\x00\\x00')"}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"datos":"bytearray(b'\\x00\\x00\\x00\\x00')"},"tipos":{"datos":"bytearray"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":2,"estado":{"datos":{"__bytes__":[0,0,0,0],"repr":"bytearray(b'\\x00\\x00\\x00\\x00')"},"i":0},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"datos":"bytearray(b'\\x00\\x00\\x00\\x00')","i":"0"},"tipos":{"datos":"bytearray","i":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":3,"estado":{"datos":{"__bytes__":[65,0,0,0],"repr":"bytearray(b'A\\x00\\x00\\x00')"},"i":0},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"datos":"bytearray(b'A\\x00\\x00\\x00')","i":"0"},"tipos":{"datos":"bytearray","i":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":2,"estado":{"datos":{"__bytes__":[65,0,0,0],"repr":"bytearray(b'A\\x00\\x00\\x00')"},"i":1},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"datos":"bytearray(b'A\\x00\\x00\\x00')","i":"1"},"tipos":{"datos":"bytearray","i":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":3,"estado":{"datos":{"__bytes__":[65,66,0,0],"repr":"bytearray(b'AB\\x00\\x00')"},"i":1},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":null,"repr":{"datos":"bytearray(b'AB\\x00\\x00')","i":"1"},"tipos":{"datos":"bytearray","i":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":2,"estado":{"datos":{"__bytes__":[65,66,0,0],"repr":"bytearray(b'AB\\x00\\x00')"},"i":2},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"datos":"bytearray(b'AB\\x00\\x00')","i":"2"},"tipos":{"datos":"bytearray","i":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":3,"estado":{"datos":{"__bytes__":[65,66,67,0],"repr":"bytearray(b'ABC\\x00')"},"i":2},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":null,"repr":{"datos":"bytearray(b'ABC\\x00')","i":"2"},"tipos":{"datos":"bytearray","i":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":2,"estado":{"datos":{"__bytes__":[65,66,67,0],"repr":"bytearray(b'ABC\\x00')"},"i":3},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"datos":"bytearray(b'ABC\\x00')","i":"3"},"tipos":{"datos":"bytearray","i":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":3,"estado":{"datos":{"__bytes__":[65,66,67,68],"repr":"bytearray(b'ABCD')"},"i":3},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":null,"repr":{"datos":"bytearray(b'ABCD')","i":"3"},"tipos":{"datos":"bytearray","i":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":2,"estado":{"datos":{"__bytes__":[65,66,67,68],"repr":"bytearray(b'ABCD')"},"i":3},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":5,"fila":3,"repr":{"datos":"bytearray(b'ABCD')","i":"3"},"tipos":{"datos":"bytearray","i":"int"},"pila":[],"devuelve":null,"excepcion":null,"disco":[]},{"linea":4,"estado":{"datos":{"__bytes__":[65,66,67,68],"repr":"bytearray(b'ABCD')"},"i":3,"f":{"__txt__":"fichero 'datos.bin' abierto en modo 'wb'"}},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"datos":"bytearray(b'ABCD')","i":"3","f":"fichero 'datos.bin' abierto en modo 'wb'"},"tipos":{"datos":"bytearray","i":"int","f":"BufferedWriter"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"datos.bin","tam":0,"contenido":"","binario":true}]},{"linea":5,"estado":{"datos":{"__bytes__":[65,66,67,68],"repr":"bytearray(b'ABCD')"},"i":3,"f":{"__txt__":"fichero 'datos.bin' abierto en modo 'wb'"}},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"datos":"bytearray(b'ABCD')","i":"3","f":"fichero 'datos.bin' abierto en modo 'wb'"},"tipos":{"datos":"bytearray","i":"int","f":"BufferedWriter"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"datos.bin","tam":0,"contenido":"","binario":true}]},{"linea":4,"estado":{"datos":{"__bytes__":[65,66,67,68],"repr":"bytearray(b'ABCD')"},"i":3,"f":{"__txt__":"fichero 'datos.bin' (cerrado)"}},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"datos":"bytearray(b'ABCD')","i":"3","f":"fichero 'datos.bin' (cerrado)"},"tipos":{"datos":"bytearray","i":"int","f":"BufferedWriter"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"datos.bin","tam":4,"contenido":"41 42 43 44","binario":true}]},{"linea":6,"estado":{"datos":{"__bytes__":[65,66,67,68],"repr":"bytearray(b'ABCD')"},"i":3,"f":{"__txt__":"fichero 'datos.bin' (cerrado)"}},"salida":"bytearray(b'ABCD')\n","foco":3,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"datos":"bytearray(b'ABCD')","i":"3","f":"fichero 'datos.bin' (cerrado)"},"tipos":{"datos":"bytearray","i":"int","f":"BufferedWriter"},"pila":[],"devuelve":null,"excepcion":null,"disco":[{"nombre":"datos.bin","tam":4,"contenido":"41 42 43 44","binario":true}]}],"filas":[["0","65"],["1","66"],["2","67"],["3","68"]]}}
```

Python escribe `bytearray(b'ABCD')` porque 65, 66, 67 y 68 son los códigos de las letras A, B, C y D: lo verás a fondo en el capítulo de cadenas. Para leer un fichero binario se abre en `"rb"`, y `f.read()` devuelve `bytes`; `f.readinto(datos)` lo vuelca directamente en un `bytearray` que ya tengas.

### 5 · `pathlib`: las rutas como objetos

El módulo `pathlib` trata las rutas de ficheros como objetos con métodos útiles, y funciona igual en Windows, Mac y Linux:

```{code-cell} python
from pathlib import Path

p = Path("saludo.txt")
p.write_text("hola\n", encoding="utf-8")
print(p.exists(), p.name, p.suffix, p.stem)
print(p.read_text(encoding="utf-8"))
print(Path("datos") / "2026" / "notas.txt")   # / une trozos de ruta

Path("bytes.bin").write_bytes(bytes([1, 2, 255]))
print(Path("bytes.bin").read_bytes())
```

Una ruta puede ser:

- **relativa**, como `Path("saludo.txt")`: se entiende a partir de la carpeta desde la que se ejecuta el programa;
- **absoluta**, como `/Users/tony/saludo.txt` o `C:\Users\tony\saludo.txt`: empieza en la raíz del disco y no depende de dónde estés.

`p.is_absolute()` lo dice, `p.resolve()` convierte una relativa en absoluta, y `Path(".").iterdir()` recorre lo que hay en una carpeta:

```{code-cell} python
print(Path("saludo.txt").is_absolute(), Path("saludo.txt").resolve().is_absolute())
print(sorted(f.name for f in Path(".").iterdir() if f.suffix in (".txt", ".bin")))
```

### 6 · Los tres flujos estándar

Todo programa nace con tres flujos abiertos, en el módulo `sys`:

| Flujo | Qué es | Ejemplo |
|---|---|---|
| `sys.stdin` | la entrada, normalmente el teclado | lo usa `input()` |
| `sys.stdout` | la salida normal, la pantalla | lo usa `print()` |
| `sys.stderr` | la salida de errores | los tracebacks salen por aquí |

```{code-cell} python
import sys

sys.stdout.write("Esto es como print, sin salto de línea automático\n")
print("Y esto sale por el canal de errores", file=sys.stderr)
```

## Conexiones

- Un fichero abierto se recorre con `for` igual que una lista: es otra cosa que entrega valores de uno en uno.
- `with` es un `try … finally` empaquetado: pase lo que pase dentro, al salir se cierra.
- Leer un fichero de notas y guardar el resultado en otro es el esqueleto de muchísimos programas reales.

## La grieta

Ya sabemos fabricar clases sencillas. Pero, ¿cómo protege una clase sus datos? ¿Qué pasa cuando una clase hereda de dos a la vez? Toca entrar en las clases a fondo.

## Ejercicios

1. **El diario.** Escribe un programa que añada la línea `"hoy he aprendido ficheros"` al final de `diario.txt` cada vez que se ejecute, sin borrar lo anterior.
2. **Contar líneas.** Escribe un programa que cuente cuántas líneas no vacías tiene un fichero `lista.txt`.
3. **¿Qué hay en el fichero?**

   ```python
   with open("a.txt", "w") as f:
       f.write("uno")
   with open("a.txt", "w") as f:
       f.write("dos")
   ```

4. **A prueba de errores.** Modifica el ejercicio 2 para que, si el fichero no existe, imprima «No encuentro lista.txt» en lugar de detenerse.

El solucionario está al final del capítulo.

## Solucionario

1. Con el modo `"a"`:

   ```python
   with open("diario.txt", "a", encoding="utf-8") as f:
       f.write("hoy he aprendido ficheros\n")
   ```

2. Una solución:

   ```python
   contador = 0
   with open("lista.txt", encoding="utf-8") as f:
       for linea in f:
           if linea.strip() != "":
               contador = contador + 1
   print(contador)
   ```

3. Solo **dos**. El modo `"w"` vacía el fichero al abrirlo, así que la segunda apertura borra el `uno`. Para conservarlo habría que usar `"a"`.
4. Se envuelve en `try`:

   ```python
   try:
       contador = 0
       with open("lista.txt", encoding="utf-8") as f:
           for linea in f:
               if linea.strip() != "":
                   contador = contador + 1
       print(contador)
   except FileNotFoundError:
       print("No encuentro lista.txt")
   ```
