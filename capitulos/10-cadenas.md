---
title: Cadenas
subtitle: El texto también es una fila de casillas
kernelspec:
  name: python3
  display_name: Python 3
---

## Punto de partida

En un crucigrama, cada palabra ocupa una fila de casillas, una letra en cada una. Si te dicen «la tercera letra es una R», sabes exactamente dónde mirar.

## La pregunta

Una lista es una fila de casillas con números. ¿Funciona igual el texto? ¿Podemos recorrer una palabra letra a letra, o preguntar por la tercera?

## La idea

Una **cadena** (`str`) es una secuencia de caracteres, y se comporta en casi todo como una lista:

- Cada carácter tiene su **posición**, empezando en 0: si `palabra = "radar"`, entonces `palabra[0]` es `"r"`.
- `len(palabra)` da el número de caracteres.
- `for letra in palabra:` la recorre carácter a carácter.

:::{important} Una diferencia importante: las cadenas no se pueden modificar
Las cadenas son **inmutables**. `palabra[0] = "R"` da un error. Para «cambiar» un texto, se construye uno nuevo, por ejemplo con `+` o con métodos como `upper()` o `replace()`, que devuelven una cadena nueva y dejan la original como estaba.
:::

## Construcción

### 1 · Contar vocales

:::{tip} Predice
«Murciélago» tiene una curiosidad con las vocales. ¿Cuántas cuenta el programa?
:::

```{code-cell} python
palabra = "murciélago"
vocales = 0
for letra in palabra:
    if letra in "aeiouáéíóú":
        vocales = vocales + 1
print(vocales)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Contar vocales","etiqueta":"for · in · contador","idea":"El for recorre la cadena carácter a carácter, igual que recorría una lista. El operador in pregunta si la letra está dentro de la cadena de vocales.","lista":"palabra","cabecera":3,"puntero":"letra","foco":"vuelta","columnas":["letra","vocales"],"fila_en":"fin_iteracion"},"traza":{"codigo":"palabra = \"murciélago\"\nvocales = 0\nfor letra in palabra:\n    if letra in \"aeiouáéíóú\":\n        vocales = vocales + 1\nprint(vocales)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null},{"linea":1,"estado":{"palabra":"murciélago"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"palabra":"'murciélago'"},"tipos":{"palabra":"str"},"pila":[],"devuelve":null},{"linea":2,"estado":{"palabra":"murciélago","vocales":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"0"},"tipos":{"palabra":"str","vocales":"int"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":0,"letra":"m"},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"0","letra":"'m'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":0,"letra":"m"},"salida":"","foco":0,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'m' in 'aeiouáéíóú'","valor":false},"vuelta":1,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"0","letra":"'m'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":0,"letra":"u"},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"palabra":"'murciélago'","vocales":"0","letra":"'u'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":0,"letra":"u"},"salida":"","foco":1,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'u' in 'aeiouáéíóú'","valor":true},"vuelta":2,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"0","letra":"'u'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":5,"estado":{"palabra":"murciélago","vocales":1,"letra":"u"},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"1","letra":"'u'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":1,"letra":"r"},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"palabra":"'murciélago'","vocales":"1","letra":"'r'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":1,"letra":"r"},"salida":"","foco":2,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'r' in 'aeiouáéíóú'","valor":false},"vuelta":3,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"1","letra":"'r'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":1,"letra":"c"},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"palabra":"'murciélago'","vocales":"1","letra":"'c'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":1,"letra":"c"},"salida":"","foco":3,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'c' in 'aeiouáéíóú'","valor":false},"vuelta":4,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"1","letra":"'c'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":1,"letra":"i"},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":5,"fila":3,"repr":{"palabra":"'murciélago'","vocales":"1","letra":"'i'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":1,"letra":"i"},"salida":"","foco":4,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'i' in 'aeiouáéíóú'","valor":true},"vuelta":5,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"1","letra":"'i'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":5,"estado":{"palabra":"murciélago","vocales":2,"letra":"i"},"salida":"","foco":4,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"2","letra":"'i'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":2,"letra":"é"},"salida":"","foco":5,"lee":true,"cond":null,"vuelta":6,"fila":4,"repr":{"palabra":"'murciélago'","vocales":"2","letra":"'é'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":2,"letra":"é"},"salida":"","foco":5,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'é' in 'aeiouáéíóú'","valor":true},"vuelta":6,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"2","letra":"'é'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":5,"estado":{"palabra":"murciélago","vocales":3,"letra":"é"},"salida":"","foco":5,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"3","letra":"'é'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":3,"letra":"l"},"salida":"","foco":6,"lee":true,"cond":null,"vuelta":7,"fila":5,"repr":{"palabra":"'murciélago'","vocales":"3","letra":"'l'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":3,"letra":"l"},"salida":"","foco":6,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'l' in 'aeiouáéíóú'","valor":false},"vuelta":7,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"3","letra":"'l'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":3,"letra":"a"},"salida":"","foco":7,"lee":true,"cond":null,"vuelta":8,"fila":6,"repr":{"palabra":"'murciélago'","vocales":"3","letra":"'a'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":3,"letra":"a"},"salida":"","foco":7,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'a' in 'aeiouáéíóú'","valor":true},"vuelta":8,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"3","letra":"'a'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":5,"estado":{"palabra":"murciélago","vocales":4,"letra":"a"},"salida":"","foco":7,"lee":false,"cond":null,"vuelta":8,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"4","letra":"'a'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":4,"letra":"g"},"salida":"","foco":8,"lee":true,"cond":null,"vuelta":9,"fila":7,"repr":{"palabra":"'murciélago'","vocales":"4","letra":"'g'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":4,"letra":"g"},"salida":"","foco":8,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'g' in 'aeiouáéíóú'","valor":false},"vuelta":9,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"4","letra":"'g'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":4,"letra":"o"},"salida":"","foco":9,"lee":true,"cond":null,"vuelta":10,"fila":8,"repr":{"palabra":"'murciélago'","vocales":"4","letra":"'o'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"murciélago","vocales":4,"letra":"o"},"salida":"","foco":9,"lee":false,"cond":{"expr":"letra in \"aeiouáéíóú\"","sust":"'o' in 'aeiouáéíóú'","valor":true},"vuelta":10,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"4","letra":"'o'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":5,"estado":{"palabra":"murciélago","vocales":5,"letra":"o"},"salida":"","foco":9,"lee":false,"cond":null,"vuelta":10,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"5","letra":"'o'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"murciélago","vocales":5,"letra":"o"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":11,"fila":9,"repr":{"palabra":"'murciélago'","vocales":"5","letra":"'o'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null},{"linea":6,"estado":{"palabra":"murciélago","vocales":5,"letra":"o"},"salida":"5\n","foco":null,"lee":false,"cond":null,"vuelta":11,"fila":null,"repr":{"palabra":"'murciélago'","vocales":"5","letra":"'o'"},"tipos":{"palabra":"str","vocales":"int","letra":"str"},"pila":[],"devuelve":null}],"filas":[["'m'","0"],["'u'","1"],["'r'","1"],["'c'","1"],["'i'","2"],["'é'","3"],["'l'","3"],["'a'","4"],["'g'","4"],["'o'","5"]]}}
```

Salen **5**: «murciélago» tiene las cinco vocales, una de cada. La `é` cuenta porque la hemos incluido con tilde en la cadena de vocales. Prueba a quitar `"áéíóú"` y vuelve a ejecutar la celda.

### 2 · Darle la vuelta a una palabra

:::{tip} Predice
¿Cómo irá creciendo `al_reves`? Escribe sus valores antes de mirar.
:::

```{code-cell} python
palabra = "radar"
al_reves = ""
for letra in palabra:
    al_reves = letra + al_reves
print(al_reves, al_reves == palabra)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Darle la vuelta a una palabra","etiqueta":"concatenación · palíndromo","idea":"Cada letra nueva se pega delante de lo que ya había, así que la cadena se construye al revés. Si al revés sale la misma palabra, es un palíndromo.","lista":"palabra","cabecera":3,"puntero":"letra","foco":"vuelta","columnas":["letra","al_reves"],"fila_en":"fin_iteracion"},"traza":{"codigo":"palabra = \"radar\"\nal_reves = \"\"\nfor letra in palabra:\n    al_reves = letra + al_reves\nprint(al_reves, al_reves == palabra)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null},{"linea":1,"estado":{"palabra":"radar"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"palabra":"'radar'"},"tipos":{"palabra":"str"},"pila":[],"devuelve":null},{"linea":2,"estado":{"palabra":"radar","al_reves":""},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"palabra":"'radar'","al_reves":"''"},"tipos":{"palabra":"str","al_reves":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"radar","al_reves":"","letra":"r"},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"palabra":"'radar'","al_reves":"''","letra":"'r'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"radar","al_reves":"r","letra":"r"},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"palabra":"'radar'","al_reves":"'r'","letra":"'r'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"radar","al_reves":"r","letra":"a"},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"palabra":"'radar'","al_reves":"'r'","letra":"'a'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"radar","al_reves":"ar","letra":"a"},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"palabra":"'radar'","al_reves":"'ar'","letra":"'a'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"radar","al_reves":"ar","letra":"d"},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"palabra":"'radar'","al_reves":"'ar'","letra":"'d'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"radar","al_reves":"dar","letra":"d"},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"palabra":"'radar'","al_reves":"'dar'","letra":"'d'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"radar","al_reves":"dar","letra":"a"},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"palabra":"'radar'","al_reves":"'dar'","letra":"'a'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"radar","al_reves":"adar","letra":"a"},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"palabra":"'radar'","al_reves":"'adar'","letra":"'a'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"radar","al_reves":"adar","letra":"r"},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":5,"fila":3,"repr":{"palabra":"'radar'","al_reves":"'adar'","letra":"'r'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":4,"estado":{"palabra":"radar","al_reves":"radar","letra":"r"},"salida":"","foco":4,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"palabra":"'radar'","al_reves":"'radar'","letra":"'r'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":3,"estado":{"palabra":"radar","al_reves":"radar","letra":"r"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":4,"repr":{"palabra":"'radar'","al_reves":"'radar'","letra":"'r'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null},{"linea":5,"estado":{"palabra":"radar","al_reves":"radar","letra":"r"},"salida":"radar True\n","foco":null,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"palabra":"'radar'","al_reves":"'radar'","letra":"'r'"},"tipos":{"palabra":"str","al_reves":"str","letra":"str"},"pila":[],"devuelve":null}],"filas":[["'r'","'r'"],["'a'","'ar'"],["'d'","'dar'"],["'a'","'adar'"],["'r'","'radar'"]]}}
```

`al_reves` empieza siendo la **cadena vacía** `""`, el equivalente de empezar un acumulador en 0. Y como las cadenas no se modifican, en cada vuelta se crea una cadena nueva y más larga.

### 3 · Trozos de una cadena: las rebanadas

Con corchetes y dos puntos se saca un trozo de una cadena (o de una lista). Es la **rebanada** (*slice*): `cadena[inicio:fin]` va desde `inicio` hasta antes de `fin`, como `range`.

```{code-cell} python
palabra = "programar"
print(palabra[0:3])    # pro
print(palabra[3:])     # gramar: desde la 3 hasta el final
print(palabra[-1])     # r: las posiciones negativas cuentan desde el final
print(palabra[::-1])   # ramargorp: toda la cadena, al revés
```

| Expresión | Resultado | Lectura |
|---|---|---|
| `palabra[0:3]` | `'pro'` | posiciones 0, 1 y 2 |
| `palabra[3:]` | `'gramar'` | de la 3 al final |
| `palabra[-1]` | `'r'` | la última |
| `palabra[::-1]` | `'ramargorp'` | toda, de atrás adelante |

### 4 · Métodos que ya vienen hechos

Las cadenas traen funciones propias, los **métodos**, que se llaman con un punto:

```{code-cell} python
frase = "Hola, mundo"
print(frase.upper())             # HOLA, MUNDO
print(frase.count("o"))          # 2
print(frase.replace("mundo", "clase"))
print(frase.split(", "))         # ['Hola', 'mundo']
print(frase)                     # la original no ha cambiado
```

## Conexiones

- Todo lo aprendido en [Recorrer listas](08-recorrer-listas.md) vale para las cadenas: el `for`, los índices, el contador y el acumulador.
- `input()` devuelve una cadena: ahora sabes recorrerla, trocearla y convertirla.
- Contar caracteres es el primer paso para contar **frecuencias**, que es justo lo que resuelven los diccionarios del capítulo siguiente.

## La grieta

Hemos contado vocales. ¿Y si quisiéramos saber cuántas veces aparece **cada** letra? Necesitaríamos un contador por letra, y no sabemos de antemano cuáles van a salir. Hace falta una estructura que asocie cada letra con su cuenta: un **diccionario**.

## Ejercicios

1. **Predice** el resultado: `"python"[1:4]`, `"python"[-2]` y `len("hola mundo")`.
2. **Mayúsculas a mano.** Escribe un programa que cuente cuántas letras mayúsculas tiene `"Hola Mundo Python"`. Pista: `letra.isupper()` dice si una letra es mayúscula.
3. **¿Palíndromo?** ¿Es palíndromo `"Anita lava la tina"`? ¿Qué tendrías que hacer con la frase antes de comparar?

El solucionario está al final del capítulo.

## Solucionario

1. `"python"[1:4]` → `'yth'` (posiciones 1, 2 y 3). `"python"[-2]` → `'o'` (la penúltima). `len("hola mundo")` → `10`, porque el espacio también es un carácter.
2. Una solución:

   ```python
   frase = "Hola Mundo Python"
   mayusculas = 0
   for letra in frase:
       if letra.isupper():
           mayusculas = mayusculas + 1
   print(mayusculas)
   ```

   Imprime `3`.
3. Tal cual, no: las mayúsculas y los espacios lo estropean. Hay que pasarla a minúsculas y quitar los espacios antes de comparar:

   ```python
   frase = "Anita lava la tina"
   limpia = frase.lower().replace(" ", "")
   print(limpia == limpia[::-1])    # True
   ```
