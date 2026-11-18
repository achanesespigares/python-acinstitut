---
title: Cadenas a fondo
subtitle: Lo que hay debajo de cada carácter
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

Un ordenador no sabe lo que es una letra: solo guarda números. Para guardar texto hace falta un acuerdo que diga qué número es cada letra, como el alfabeto morse dice qué pitidos son cada letra.

## La pregunta

¿Qué número es cada carácter? ¿Por qué `"Zorro" < "abeja"` es verdad? ¿Y por qué no se puede cambiar una letra de una cadena?

## La idea

- **ASCII** (1963) es el primer acuerdo famoso: 128 caracteres, del 0 al 127. La `A` es el 65, la `a` el 97, el `0` el 48 y el espacio el 32. No tiene `ñ` ni tildes.
- **Unicode** es el acuerdo actual: asigna un número, su **punto de código** (*code point*), a casi cada carácter de cada idioma, emojis incluidos. Los 128 primeros coinciden con ASCII. La `ñ` es el 241 y el `€` el 8364.
- **UTF-8** es la forma más usada de guardar esos números en bytes: los de ASCII ocupan 1 byte, la `ñ` ocupa 2, el `€` 3 y un emoji 4.

En Python, `ord` da el punto de código de un carácter, y `chr` hace lo contrario:

```{code-cell} python
print(ord("A"), ord("a"), ord("ñ"), ord("€"))
print(chr(65), chr(241), chr(8364))
print("ñ".encode("utf-8"), len("ñ"), len("ñ".encode("utf-8")))
```

`len("ñ")` es 1 porque cuenta caracteres. En UTF-8 ese carácter ocupa 2 bytes.

Por eso Python distingue dos tipos: `str` es **texto** (una sucesión de caracteres Unicode) y `bytes` es **datos en bruto** (una sucesión de números de 0 a 255). Se pasa de uno a otro con `encode` y `decode`, y siempre hay que decir con qué codificación:

```{code-cell} python
datos = "año".encode("utf-8")
print(type(datos).__name__, datos, list(datos))
print(datos.decode("utf-8"))
```

## Construcción

### 1 · Desplazar letras: el cifrado César

Julio César escribía sus mensajes moviendo cada letra unas posiciones en el alfabeto. Con `ord` y `chr` es sumar un número.

:::{tip} Predice
¿En qué se convierte la `h`? ¿Cuántas cadenas distintas llega a valer `cifrado`?
:::

```{code-cell} python
mensaje = "hola"
cifrado = ""
for letra in mensaje:
    codigo = ord(letra) + 3
    cifrado = cifrado + chr(codigo)
print(cifrado)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"El cifrado César","etiqueta":"ord · chr","idea":"Cada letra se convierte en su número, se le suma 3 y se vuelve a convertir en letra: h (104) pasa a k (107). cifrado no se modifica: en cada vuelta se fabrica una cadena nueva, más larga.","lista":"mensaje","cabecera":3,"puntero":"letra","columnas":["letra","codigo","cifrado"],"fila_en":"fin_iteracion"},"traza":{"codigo":"mensaje = \"hola\"\ncifrado = \"\"\nfor letra in mensaje:\n    codigo = ord(letra) + 3\n    cifrado = cifrado + chr(codigo)\nprint(cifrado)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"mensaje":"hola"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"mensaje":"'hola'"},"tipos":{"mensaje":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"mensaje":"hola","cifrado":""},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"''"},"tipos":{"mensaje":"str","cifrado":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"mensaje":"hola","cifrado":"","letra":"h"},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"''","letra":"'h'"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"mensaje":"hola","cifrado":"","letra":"h","codigo":107},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"''","letra":"'h'","codigo":"107"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"mensaje":"hola","cifrado":"k","letra":"h","codigo":107},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"'k'","letra":"'h'","codigo":"107"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"mensaje":"hola","cifrado":"k","letra":"o","codigo":107},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"mensaje":"'hola'","cifrado":"'k'","letra":"'o'","codigo":"107"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"mensaje":"hola","cifrado":"k","letra":"o","codigo":114},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"'k'","letra":"'o'","codigo":"114"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"mensaje":"hola","cifrado":"kr","letra":"o","codigo":114},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"'kr'","letra":"'o'","codigo":"114"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"mensaje":"hola","cifrado":"kr","letra":"l","codigo":114},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"mensaje":"'hola'","cifrado":"'kr'","letra":"'l'","codigo":"114"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"mensaje":"hola","cifrado":"kr","letra":"l","codigo":111},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"'kr'","letra":"'l'","codigo":"111"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"mensaje":"hola","cifrado":"kro","letra":"l","codigo":111},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"'kro'","letra":"'l'","codigo":"111"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"mensaje":"hola","cifrado":"kro","letra":"a","codigo":111},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"mensaje":"'hola'","cifrado":"'kro'","letra":"'a'","codigo":"111"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"mensaje":"hola","cifrado":"kro","letra":"a","codigo":100},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"'kro'","letra":"'a'","codigo":"100"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"mensaje":"hola","cifrado":"krod","letra":"a","codigo":100},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"'krod'","letra":"'a'","codigo":"100"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"mensaje":"hola","cifrado":"krod","letra":"a","codigo":100},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":3,"repr":{"mensaje":"'hola'","cifrado":"'krod'","letra":"'a'","codigo":"100"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"mensaje":"hola","cifrado":"krod","letra":"a","codigo":100},"salida":"krod\n","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"mensaje":"'hola'","cifrado":"'krod'","letra":"'a'","codigo":"100"},"tipos":{"mensaje":"str","cifrado":"str","letra":"str","codigo":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["'h'","107","'k'"],["'o'","114","'kr'"],["'l'","111","'kro'"],["'a'","100","'krod'"]]}}
```

:::{important} Las cadenas son inmutables
Una cadena no se puede modificar: `cifrado[0] = "X"` da `TypeError`. `cifrado = cifrado + chr(codigo)` no cambia la cadena vieja; fabrica una nueva y le pega la etiqueta `cifrado`. Todos los métodos que parecen cambiar una cadena, como `upper()` o `replace()`, **devuelven una cadena nueva** y dejan la original intacta.
:::

```{code-cell} python
s = "hola"
try:
    s[0] = "H"
except TypeError as e:
    print("Error:", e)
t = s.replace("h", "H")
print(s, t)
print(s[1:3], s * 2, s + "!", s)     # rebanar, repetir y concatenar: siempre cadenas nuevas
print(sorted("hola"))                # sorted ordena los caracteres y da una lista
```

### 2 · Comparar cadenas

Python compara dos cadenas carácter a carácter, de izquierda a derecha, como un diccionario: el primer carácter distinto decide, y lo decide su **punto de código**.

:::{tip} Predice
¿En qué posición son distintas `"casa"` y `"cama"`? ¿Cuál es menor?
:::

```{code-cell} python
a = "casa"
b = "cama"
i = 0
while a[i] == b[i]:
    i = i + 1
print(a[i], b[i], ord(a[i]), ord(b[i]))
print(a < b)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Comparar letra a letra","etiqueta":"orden de las cadenas","idea":"El bucle avanza mientras las letras coinciden. En la posición 2 aparece la primera diferencia: s (115) contra m (109). Como 115 > 109, 'casa' va después de 'cama', y a < b es False.","lista":"a","cabecera":4,"puntero":"i","foco":"i","columnas":["i","a[i]","b[i]"],"fila_en":"comprobacion"},"traza":{"codigo":"a = \"casa\"\nb = \"cama\"\ni = 0\nwhile a[i] == b[i]:\n    i = i + 1\nprint(a[i], b[i], ord(a[i]), ord(b[i]))\nprint(a < b)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"a":"casa"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"'casa'"},"tipos":{"a":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"a":"casa","b":"cama"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"'casa'","b":"'cama'"},"tipos":{"a":"str","b":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"a":"casa","b":"cama","i":0},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"a":"'casa'","b":"'cama'","i":"0"},"tipos":{"a":"str","b":"str","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":"casa","b":"cama","i":0},"salida":"","foco":0,"lee":true,"cond":{"expr":"a[i] == b[i]","sust":"'c' == 'c'","valor":true},"vuelta":1,"fila":0,"repr":{"a":"'casa'","b":"'cama'","i":"0"},"tipos":{"a":"str","b":"str","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":"casa","b":"cama","i":1},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"a":"'casa'","b":"'cama'","i":"1"},"tipos":{"a":"str","b":"str","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":"casa","b":"cama","i":1},"salida":"","foco":1,"lee":true,"cond":{"expr":"a[i] == b[i]","sust":"'a' == 'a'","valor":true},"vuelta":2,"fila":1,"repr":{"a":"'casa'","b":"'cama'","i":"1"},"tipos":{"a":"str","b":"str","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"a":"casa","b":"cama","i":2},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"a":"'casa'","b":"'cama'","i":"2"},"tipos":{"a":"str","b":"str","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"a":"casa","b":"cama","i":2},"salida":"","foco":2,"lee":true,"cond":{"expr":"a[i] == b[i]","sust":"'s' == 'm'","valor":false},"vuelta":3,"fila":2,"repr":{"a":"'casa'","b":"'cama'","i":"2"},"tipos":{"a":"str","b":"str","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"a":"casa","b":"cama","i":2},"salida":"s m 115 109\n","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":null,"repr":{"a":"'casa'","b":"'cama'","i":"2"},"tipos":{"a":"str","b":"str","i":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"a":"casa","b":"cama","i":2},"salida":"s m 115 109\nFalse\n","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"a":"'casa'","b":"'cama'","i":"2"},"tipos":{"a":"str","b":"str","i":"int"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["0","'c'","'c'","Sí"],["1","'a'","'a'","Sí"],["2","'s'","'m'","No"]]}}
```

Consecuencias que conviene conocer:

| Comparación | Resultado | Por qué |
|---|---|---|
| `"Zorro" < "abeja"` | `True` | todas las mayúsculas (65–90) van antes que las minúsculas (97–122) |
| `"10" < "9"` | `True` | se compara `"1"` con `"9"`: es texto, no números |
| `"casa" < "casas"` | `True` | si una es el principio de la otra, la corta va antes |
| `"ñu" < "oso"` | `False` | la `ñ` (241) va después de todas las letras sin tilde |

Para ordenar sin que importen las mayúsculas, se compara una versión en minúsculas: `sorted(palabras, key=str.lower)`.

### 3 · Validar, buscar y contar

Los métodos `is…` responden `True` o `False` sobre **todos** los caracteres de la cadena (y dan `False` con la cadena vacía):

| Método | `True` si todos son… | `"123"` | `"abc"` | `"a1"` | `" "` |
|---|---|---|---|---|---|
| `isdecimal()` | dígitos decimales del 0 al 9 | `True` | `False` | `False` | `False` |
| `isdigit()` | dígitos (también `²`, `³`…) | `True` | `False` | `False` | `False` |
| `isnumeric()` | números (también `½`, `Ⅻ`…) | `True` | `False` | `False` | `False` |
| `isalpha()` | letras | `False` | `True` | `False` | `False` |
| `isalnum()` | letras o dígitos | `True` | `True` | `True` | `False` |
| `isspace()` | espacios | `False` | `False` | `False` | `True` |
| `islower()` / `isupper()` | minúsculas / mayúsculas | `False` | `True` / `False` | `True` / `False` | `False` |

Los tres primeros solo se distinguen con caracteres especiales: `"²".isdecimal()` es `False` pero `"²".isdigit()` es `True`, y `"½"` solo es `isnumeric()`. Para validar que un texto se puede pasar a `int`, el más seguro es `isdecimal()`. Y se combinan con `and`, `or` y `not`: `s.isalnum() and not s.isdigit()` pide letras y dígitos, pero no solo dígitos.

Para buscar y contar:

```{code-cell} python
frase = "la casa de la playa"
print(frase.find("la"), frase.rfind("la"), frase.find("zz"))
print(frase.index("casa"), frase.rindex("la"), frase.count("a"), "casa" in frase)
print(frase.find("a", 5), frase.find("a", 5, 9), frase.count("a", 10))
print(frase.startswith("la"), frase.endswith("ya"))
print(frase.split(), "-".join(["a", "b", "c"]))
```

- `find` da la primera posición, o `-1` si no está; `index` hace lo mismo pero lanza `ValueError` si no está. `rfind` y `rindex` son sus versiones desde el final.
- Todos admiten **inicio y fin** opcionales: `frase.find("a", 5, 9)` busca solo entre las posiciones 5 y 8, como en una rebanada.
- `count` cuenta apariciones que no se solapan: `"aaaa".count("aa")` da 2.
- `split` trocea una cadena en una lista; `join` hace lo contrario.

## Conexiones

- `bytearray(b'ABCD')` del capítulo de ficheros eran los puntos de código 65, 66, 67 y 68.
- Ordenar palabras es comparar cadenas: ahora sabes por qué sale primero `"Zorro"` que `"abeja"`.
- La inmutabilidad de las cadenas es lo contrario que en las listas, que sí se cambian en su sitio. Por eso un alias de una lista ve los cambios y uno de una cadena no.

## La grieta

Ya escribes programas largos con clases, ficheros y funciones. ¿Cómo sabes que funcionan? ¿Y qué haces cuando no funcionan? Probar y depurar es la otra mitad de programar.

## Preguntas tipo examen

Preguntas como las del examen PCAP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcap","capitulo":"19","titulo":"Preguntas tipo examen","etiqueta":"PCAP"}}
```

## Ejercicios

1. **Descifrar.** Escribe el programa que deshace el cifrado César del apartado 1 a partir de `cifrado = "krod"`.
2. **¿Qué imprime?** `print(sorted(["pera", "Uva", "manzana"]))`.
3. **Solo dígitos.** Escribe una función `es_codigo_postal(s)` que devuelva `True` si `s` tiene exactamente 5 caracteres y todos son dígitos.
4. **Contar palabras.** ¿Cuántas palabras tiene `"  el  sol   sale "`? Calcúlalo con un método de las cadenas.

El solucionario está al final del capítulo.

## Solucionario

1. Se resta en lugar de sumar:

   ```python
   cifrado = "krod"
   original = ""
   for letra in cifrado:
       original = original + chr(ord(letra) - 3)
   print(original)
   ```

   Imprime `hola`.
2. Imprime **['Uva', 'manzana', 'pera']**: la `U` mayúscula (85) va antes que cualquier minúscula.
3. Una solución:

   ```python
   def es_codigo_postal(s):
       return len(s) == 5 and s.isdigit()
   ```

4. `len("  el  sol   sale ".split())` da **3**: `split()` sin argumentos trocea por cualquier cantidad de espacios y descarta los de los extremos.
