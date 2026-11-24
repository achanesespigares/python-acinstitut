---
title: Diccionarios
subtitle: Buscar por nombre, no por posición
kernelspec:
  name: python3
  display_name: Python 3
description: "Diccionarios: buscar por nombre, no por posición. Python paso a paso, con visualizadores y diagrama de flujo."
---

## Punto de partida

En la agenda del móvil no buscas «el contacto número 47»: buscas «Marta» y aparece su teléfono. Y en un diccionario de papel buscas una palabra para leer su definición. En los dos casos, lo que tienes es un **nombre**, y lo que quieres es **lo que va asociado** a ese nombre.

## La pregunta

Las listas encuentran las cosas por su posición: 0, 1, 2… ¿Cómo guardamos datos que se buscan por un nombre?

## La idea

Un **diccionario** (`dict`) guarda parejas **clave → valor**. Se busca por la clave y se obtiene el valor:

```python
telefonos = {"Marta": "600111222", "Joan": "611333444"}
telefonos["Marta"]            # '600111222'
telefonos["Biel"] = "622555666"   # si la clave no existe, se añade
```

:::{important} Las reglas de los diccionarios
- Cada **clave** aparece una sola vez. Si asignas a una clave que ya existe, su valor se **sustituye**.
- Pedir una clave que no existe da un error (`KeyError`). Antes de pedirla, se puede preguntar con `in`: `"Biel" in telefonos`.
- `for clave in diccionario:` recorre las claves.
:::

## Construcción

### 1 · Contar cada letra

Es la pregunta con la que terminaba el capítulo de cadenas: ¿cuántas veces aparece cada letra?

:::{tip} Predice
En «abracadabra», ¿qué letra saldrá más veces? ¿Cuántas claves tendrá el diccionario al final?
:::

```{code-cell} python
texto = "abracadabra"
cuenta = {}
for letra in texto:
    if letra in cuenta:
        cuenta[letra] = cuenta[letra] + 1
    else:
        cuenta[letra] = 1
print(cuenta)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Contar cada letra","etiqueta":"dict · frecuencias","idea":"Si la letra ya es una clave, se suma 1 a su cuenta. Si no lo es, se añade con valor 1. El diccionario va creciendo con las letras que van apareciendo.","lista":"texto","diccionario":"cuenta","cabecera":3,"puntero":"letra","foco":"vuelta","columnas":["letra","cuenta[letra]"],"fila_en":"fin_iteracion"},"traza":{"codigo":"texto = \"abracadabra\"\ncuenta = {}\nfor letra in texto:\n    if letra in cuenta:\n        cuenta[letra] = cuenta[letra] + 1\n    else:\n        cuenta[letra] = 1\nprint(cuenta)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"texto":"abracadabra"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"texto":"'abracadabra'"},"tipos":{"texto":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"texto":"abracadabra","cuenta":{}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{}"},"tipos":{"texto":"str","cuenta":"dict"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{},"letra":"a"},"salida":"","foco":0,"lee":true,"cond":null,"vuelta":1,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{},"letra":"a"},"salida":"","foco":0,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'a' in cuenta","valor":false},"vuelta":1,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"texto":"abracadabra","cuenta":{"a":1},"letra":"a"},"salida":"","foco":0,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":1},"letra":"b"},"salida":"","foco":1,"lee":true,"cond":null,"vuelta":2,"fila":0,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 1}","letra":"'b'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":1},"letra":"b"},"salida":"","foco":1,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'b' in cuenta","valor":false},"vuelta":2,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 1}","letra":"'b'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"texto":"abracadabra","cuenta":{"a":1,"b":1},"letra":"b"},"salida":"","foco":1,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 1, 'b': 1}","letra":"'b'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":1,"b":1},"letra":"r"},"salida":"","foco":2,"lee":true,"cond":null,"vuelta":3,"fila":1,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 1, 'b': 1}","letra":"'r'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":1,"b":1},"letra":"r"},"salida":"","foco":2,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'r' in cuenta","valor":false},"vuelta":3,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 1, 'b': 1}","letra":"'r'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"texto":"abracadabra","cuenta":{"a":1,"b":1,"r":1},"letra":"r"},"salida":"","foco":2,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 1, 'b': 1, 'r': 1}","letra":"'r'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":1,"b":1,"r":1},"letra":"a"},"salida":"","foco":3,"lee":true,"cond":null,"vuelta":4,"fila":2,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 1, 'b': 1, 'r': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":1,"b":1,"r":1},"letra":"a"},"salida":"","foco":3,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'a' in cuenta","valor":true},"vuelta":4,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 1, 'b': 1, 'r': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"texto":"abracadabra","cuenta":{"a":2,"b":1,"r":1},"letra":"a"},"salida":"","foco":3,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 2, 'b': 1, 'r': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":2,"b":1,"r":1},"letra":"c"},"salida":"","foco":4,"lee":true,"cond":null,"vuelta":5,"fila":3,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 2, 'b': 1, 'r': 1}","letra":"'c'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":2,"b":1,"r":1},"letra":"c"},"salida":"","foco":4,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'c' in cuenta","valor":false},"vuelta":5,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 2, 'b': 1, 'r': 1}","letra":"'c'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"texto":"abracadabra","cuenta":{"a":2,"b":1,"r":1,"c":1},"letra":"c"},"salida":"","foco":4,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 2, 'b': 1, 'r': 1, 'c': 1}","letra":"'c'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":2,"b":1,"r":1,"c":1},"letra":"a"},"salida":"","foco":5,"lee":true,"cond":null,"vuelta":6,"fila":4,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 2, 'b': 1, 'r': 1, 'c': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":2,"b":1,"r":1,"c":1},"letra":"a"},"salida":"","foco":5,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'a' in cuenta","valor":true},"vuelta":6,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 2, 'b': 1, 'r': 1, 'c': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"texto":"abracadabra","cuenta":{"a":3,"b":1,"r":1,"c":1},"letra":"a"},"salida":"","foco":5,"lee":false,"cond":null,"vuelta":6,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 3, 'b': 1, 'r': 1, 'c': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":3,"b":1,"r":1,"c":1},"letra":"d"},"salida":"","foco":6,"lee":true,"cond":null,"vuelta":7,"fila":5,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 3, 'b': 1, 'r': 1, 'c': 1}","letra":"'d'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":3,"b":1,"r":1,"c":1},"letra":"d"},"salida":"","foco":6,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'d' in cuenta","valor":false},"vuelta":7,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 3, 'b': 1, 'r': 1, 'c': 1}","letra":"'d'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"texto":"abracadabra","cuenta":{"a":3,"b":1,"r":1,"c":1,"d":1},"letra":"d"},"salida":"","foco":6,"lee":false,"cond":null,"vuelta":7,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 3, 'b': 1, 'r': 1, 'c': 1, 'd': 1}","letra":"'d'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":3,"b":1,"r":1,"c":1,"d":1},"letra":"a"},"salida":"","foco":7,"lee":true,"cond":null,"vuelta":8,"fila":6,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 3, 'b': 1, 'r': 1, 'c': 1, 'd': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":3,"b":1,"r":1,"c":1,"d":1},"letra":"a"},"salida":"","foco":7,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'a' in cuenta","valor":true},"vuelta":8,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 3, 'b': 1, 'r': 1, 'c': 1, 'd': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"texto":"abracadabra","cuenta":{"a":4,"b":1,"r":1,"c":1,"d":1},"letra":"a"},"salida":"","foco":7,"lee":false,"cond":null,"vuelta":8,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 4, 'b': 1, 'r': 1, 'c': 1, 'd': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":4,"b":1,"r":1,"c":1,"d":1},"letra":"b"},"salida":"","foco":8,"lee":true,"cond":null,"vuelta":9,"fila":7,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 4, 'b': 1, 'r': 1, 'c': 1, 'd': 1}","letra":"'b'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":4,"b":1,"r":1,"c":1,"d":1},"letra":"b"},"salida":"","foco":8,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'b' in cuenta","valor":true},"vuelta":9,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 4, 'b': 1, 'r': 1, 'c': 1, 'd': 1}","letra":"'b'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"texto":"abracadabra","cuenta":{"a":4,"b":2,"r":1,"c":1,"d":1},"letra":"b"},"salida":"","foco":8,"lee":false,"cond":null,"vuelta":9,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 4, 'b': 2, 'r': 1, 'c': 1, 'd': 1}","letra":"'b'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":4,"b":2,"r":1,"c":1,"d":1},"letra":"r"},"salida":"","foco":9,"lee":true,"cond":null,"vuelta":10,"fila":8,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 4, 'b': 2, 'r': 1, 'c': 1, 'd': 1}","letra":"'r'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":4,"b":2,"r":1,"c":1,"d":1},"letra":"r"},"salida":"","foco":9,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'r' in cuenta","valor":true},"vuelta":10,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 4, 'b': 2, 'r': 1, 'c': 1, 'd': 1}","letra":"'r'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"texto":"abracadabra","cuenta":{"a":4,"b":2,"r":2,"c":1,"d":1},"letra":"r"},"salida":"","foco":9,"lee":false,"cond":null,"vuelta":10,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 4, 'b': 2, 'r': 2, 'c': 1, 'd': 1}","letra":"'r'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":4,"b":2,"r":2,"c":1,"d":1},"letra":"a"},"salida":"","foco":10,"lee":true,"cond":null,"vuelta":11,"fila":9,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 4, 'b': 2, 'r': 2, 'c': 1, 'd': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"texto":"abracadabra","cuenta":{"a":4,"b":2,"r":2,"c":1,"d":1},"letra":"a"},"salida":"","foco":10,"lee":false,"cond":{"expr":"letra in cuenta","sust":"'a' in cuenta","valor":true},"vuelta":11,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 4, 'b': 2, 'r': 2, 'c': 1, 'd': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"texto":"abracadabra","cuenta":{"a":5,"b":2,"r":2,"c":1,"d":1},"letra":"a"},"salida":"","foco":10,"lee":false,"cond":null,"vuelta":11,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"texto":"abracadabra","cuenta":{"a":5,"b":2,"r":2,"c":1,"d":1},"letra":"a"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":12,"fila":10,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{"texto":"abracadabra","cuenta":{"a":5,"b":2,"r":2,"c":1,"d":1},"letra":"a"},"salida":"{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}\n","foco":null,"lee":false,"cond":null,"vuelta":12,"fila":null,"repr":{"texto":"'abracadabra'","cuenta":"{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}","letra":"'a'"},"tipos":{"texto":"str","cuenta":"dict","letra":"str"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["'a'","1"],["'b'","1"],["'r'","1"],["'a'","2"],["'c'","1"],["'a'","3"],["'d'","1"],["'a'","4"],["'b'","2"],["'r'","2"],["'a'","5"]]}}
```

El diccionario empieza vacío (`{}`) y termina con **5 claves**: `a` aparece 5 veces, `b` y `r` 2 veces cada una, y `c` y `d` una. Fíjate en la tabla de diccionario del visualizador: la fila que cambia en cada vuelta se marca.

Este patrón, «si ya está, súmale uno; si no, empieza en uno», aparece en muchísimos programas: contar votos, palabras, visitas…

### 2 · Las notas de la clase

:::{tip} Predice
Después de los cambios de las líneas 2 y 3, ¿cuántos alumnos aprueban?
:::

```{code-cell} python
notas = {"Ana": 7, "Biel": 4, "Carla": 9}
notas["Biel"] = 5
notas["Dani"] = 6
aprobados = 0
for nombre in notas:
    if notas[nombre] >= 5:
        aprobados = aprobados + 1
print(aprobados)
```

```{anywidget} ../widgets/traza.mjs
{"config":{"titulo":"Las notas de la clase","etiqueta":"dict · modificar y recorrer","idea":"notas['Biel'] = 5 sustituye un valor que ya existía; notas['Dani'] = 6 añade una clave nueva. Después, el for recorre las claves y consulta la nota de cada una.","diccionario":"notas","cabecera":5,"puntero":"nombre","columnas":["nombre","notas[nombre]","aprobados"],"fila_en":"fin_iteracion"},"traza":{"codigo":"notas = {\"Ana\": 7, \"Biel\": 4, \"Carla\": 9}\nnotas[\"Biel\"] = 5\nnotas[\"Dani\"] = 6\naprobados = 0\nfor nombre in notas:\n    if notas[nombre] >= 5:\n        aprobados = aprobados + 1\nprint(aprobados)","pasos":[{"linea":null,"estado":{},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{},"tipos":{},"pila":[],"devuelve":null,"excepcion":null},{"linea":1,"estado":{"notas":{"Ana":7,"Biel":4,"Carla":9}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 4, 'Carla': 9}"},"tipos":{"notas":"dict"},"pila":[],"devuelve":null,"excepcion":null},{"linea":2,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9}"},"tipos":{"notas":"dict"},"pila":[],"devuelve":null,"excepcion":null},{"linea":3,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6}},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}"},"tipos":{"notas":"dict"},"pila":[],"devuelve":null,"excepcion":null},{"linea":4,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":0},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":0,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"0"},"tipos":{"notas":"dict","aprobados":"int"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":0,"nombre":"Ana"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"0","nombre":"'Ana'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":0,"nombre":"Ana"},"salida":"","foco":null,"lee":false,"cond":{"expr":"notas[nombre] >= 5","sust":"7 >= 5","valor":true},"vuelta":1,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"0","nombre":"'Ana'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":1,"nombre":"Ana"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":1,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"1","nombre":"'Ana'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":1,"nombre":"Biel"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":0,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"1","nombre":"'Biel'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":1,"nombre":"Biel"},"salida":"","foco":null,"lee":false,"cond":{"expr":"notas[nombre] >= 5","sust":"5 >= 5","valor":true},"vuelta":2,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"1","nombre":"'Biel'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":2,"nombre":"Biel"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":2,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"2","nombre":"'Biel'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":2,"nombre":"Carla"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":1,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"2","nombre":"'Carla'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":2,"nombre":"Carla"},"salida":"","foco":null,"lee":false,"cond":{"expr":"notas[nombre] >= 5","sust":"9 >= 5","valor":true},"vuelta":3,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"2","nombre":"'Carla'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":3,"nombre":"Carla"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":3,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"3","nombre":"'Carla'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":3,"nombre":"Dani"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":2,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"3","nombre":"'Dani'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":6,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":3,"nombre":"Dani"},"salida":"","foco":null,"lee":false,"cond":{"expr":"notas[nombre] >= 5","sust":"6 >= 5","valor":true},"vuelta":4,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"3","nombre":"'Dani'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":7,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":4,"nombre":"Dani"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":4,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"4","nombre":"'Dani'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":5,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":4,"nombre":"Dani"},"salida":"","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":3,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"4","nombre":"'Dani'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null},{"linea":8,"estado":{"notas":{"Ana":7,"Biel":5,"Carla":9,"Dani":6},"aprobados":4,"nombre":"Dani"},"salida":"4\n","foco":null,"lee":false,"cond":null,"vuelta":5,"fila":null,"repr":{"notas":"{'Ana': 7, 'Biel': 5, 'Carla': 9, 'Dani': 6}","aprobados":"4","nombre":"'Dani'"},"tipos":{"notas":"dict","aprobados":"int","nombre":"str"},"pila":[],"devuelve":null,"excepcion":null}],"filas":[["'Ana'","7","1"],["'Biel'","5","2"],["'Carla'","9","3"],["'Dani'","6","4"]]}}
```

Las dos asignaciones parecen iguales, pero hacen cosas distintas: la de Biel **cambia** un valor y la de Dani **añade** una pareja. Al final aprueban los **4**.

### 3 · Métodos útiles

```{code-cell} python
notas = {"Ana": 7, "Biel": 5, "Carla": 9}
print(notas.keys())              # las claves
print(notas.values())            # los valores
print(notas.get("Zoe", "sin nota"))   # get no da error si la clave no está
for nombre, nota in notas.items():    # claves y valores a la vez
    print(nombre, "→", nota)
```

| Si quieres… | Usa |
|---|---|
| buscar algo por su posición | una **lista** |
| buscar algo por un nombre | un **diccionario** |
| saber si una clave existe | `clave in diccionario` |
| leer sin riesgo de error | `diccionario.get(clave, por_defecto)` |

## Conexiones

- El contador de letras junta todo lo aprendido: recorrer una cadena, un condicional y un acumulador, ahora uno por clave.
- Las listas y los diccionarios se combinan: una lista de diccionarios es casi una hoja de cálculo, con una fila por alumno y una columna por dato.

## La grieta

¿Y si quisieras guardar varias notas por alumno? El valor de un diccionario puede ser cualquier cosa, también una lista: `{"Ana": [7, 8, 6]}`. ¿Cómo calcularías entonces la media de cada alumno? Ahí se juntan las funciones, los bucles, las listas y los diccionarios: ya tienes todas las piezas.

## Preguntas tipo examen

Preguntas como las del examen PCEP sobre lo que has visto en este capítulo. Se corrigen al momento, y las que tienen código se pueden ver ejecutándose paso a paso. Hay un simulacro completo al final del libro.

```{anywidget} ../widgets/traza.mjs
{"config":{"tipo":"preguntas","banco":"pcep","capitulo":"11","titulo":"Preguntas tipo examen","etiqueta":"PCEP"}}
```

## Ejercicios

1. **¿Qué imprime?**

   ```python
   d = {"a": 1, "b": 2}
   d["a"] = d["b"] + 10
   d["c"] = d["a"]
   print(d)
   ```

2. **Contar palabras.** Adapta el contador de letras para contar cuántas veces aparece cada palabra en `"el gato y el perro y el pez"`. Pista: `texto.split()` parte el texto en una lista de palabras.
3. **La mejor nota.** Con `notas = {"Ana": 7, "Biel": 5, "Carla": 9}`, escribe un programa que imprima el nombre del alumno con la nota más alta. Pista: es el campeón provisional, pero guardando el nombre.

El solucionario está al final del capítulo.

## Solucionario

1. Imprime `{'a': 12, 'b': 2, 'c': 12}`. Primero `d["a"]` pasa a valer 2 + 10 = 12, y después la clave nueva `"c"` copia ese 12.
2. Una solución:

   ```python
   texto = "el gato y el perro y el pez"
   cuenta = {}
   for palabra in texto.split():
       if palabra in cuenta:
           cuenta[palabra] = cuenta[palabra] + 1
       else:
           cuenta[palabra] = 1
   print(cuenta)
   ```

   Imprime `{'el': 3, 'gato': 1, 'y': 2, 'perro': 1, 'pez': 1}`.
3. Una solución:

   ```python
   notas = {"Ana": 7, "Biel": 5, "Carla": 9}
   mejor = None
   for nombre in notas:
       if mejor is None or notas[nombre] > notas[mejor]:
           mejor = nombre
   print(mejor)
   ```

   Imprime `Carla`.
