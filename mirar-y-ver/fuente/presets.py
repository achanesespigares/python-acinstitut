P = {
'for': '''lista = [3, 8, 2, 5]
total = 0
for x in lista:
    total = total + x
print(total)''',
'indice': '''lista = [3, 8, 2, 5]
total = 0
for i in range(len(lista)):
    total = total + lista[i]
print(total)''',
'while': '''lista = [3, 8, 2, 5]
total = 0
i = 0
while i < len(lista):
    total = total + lista[i]
    i = i + 1
print(total)''',
'contar': '''lista = [3, 8, 2, 5]
pares = 0
for x in lista:
    if x % 2 == 0:
        pares = pares + 1
print(pares)''',
'trampa': '''lista = [3, 8, 2, 5]
for x in lista:
    total = 0
    total = total + x
print(total)''',
}
P.update({
'maximo': '''lista = [3, 8, 2, 9, 5]
mayor = lista[0]
for x in lista:
    if x > mayor:
        mayor = x
print(mayor)''',
'posicion': '''lista = [3, 8, 2, 9, 5]
pos = 0
for i in range(len(lista)):
    if lista[i] > lista[pos]:
        pos = i
print(pos, lista[pos])''',
'empates': '''lista = [3, 9, 2, 9, 5]
pos = 0
for i in range(len(lista)):
    if lista[i] >= lista[pos]:
        pos = i
print(pos, lista[pos])''',
'trampa0': '''lista = [-4, -1, -7, -3]
mayor = 0
for x in lista:
    if x > mayor:
        mayor = x
print(mayor)''',
})
P.update({
'break': '''lista = [3, 7, 8, 5, 6]
encontrado = None
for x in lista:
    if x % 2 == 0:
        encontrado = x
        break
print(encontrado)''',
'mientras': '''lista = [3, 7, 8, 5, 6]
i = 0
while i < len(lista) and lista[i] % 2 != 0:
    i = i + 1
print(i)''',
'ninguno': '''lista = [3, 7, 9, 5]
encontrado = None
for x in lista:
    if x % 2 == 0:
        encontrado = x
        break
print(encontrado)''',
'sinbreak': '''lista = [3, 7, 8, 5, 6]
encontrado = None
for x in lista:
    if x % 2 == 0:
        encontrado = x
print(encontrado)''',
'ordenand': '''lista = [3, 7, 9]
i = 0
while lista[i] % 2 != 0 and i < len(lista):
    i = i + 1
print(i)''',
})
P.update({
'asignar': '''a = 5
b = a
a = a + 1
print(a, b)''',
'texto': '''nombre = "Ana"
saludo = "Hola, " + nombre
nombre = "Luis"
print(saludo)''',
'doblar': '''n = 1
n = n * 2
n = n * 2
n = n * 2
print(n)''',
'ecuacion': '''x = 3
y = x + 1
x = 10
print(y)''',
'aux': '''a = 3
b = 8
aux = a
a = b
b = aux
print(a, b)''',
'tupla': '''a = 3
b = 8
a, b = b, a
print(a, b)''',
'pisar': '''a = 3
b = 8
a = b
b = a
print(a, b)''',
'alias': '''a = [1, 2, 3]
b = a
b.append(4)
print(a)''',
'nueva': '''a = [1, 2, 3]
b = a
b = b + [4]
print(a)''',
'copia': '''a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)''',
'masigual': '''a = [1, 2, 3]
b = a
b += [4]
print(a)''',
})
P.update({
'doble': '''def doble(x):
    y = x * 2
    return y

n = doble(4)
print(n)''',
'area': '''def area(base, altura):
    return base * altura / 2

a1 = area(6, 4)
a2 = area(3, 10)
print(a1 + a2)''',
'componer': '''def cuadrado(x):
    return x * x

def suma_cuadrados(a, b):
    return cuadrado(a) + cuadrado(b)

print(suma_cuadrados(3, 4))''',
'sinreturn': '''def doble(x):
    print(x * 2)

n = doble(4)
print(n + 1)''',
'sombra': '''x = 10

def f(x):
    x = x + 1
    return x

y = f(3)
print(x, y)''',
'mutparam': '''def añadir(l):
    l.append(99)

datos = [1, 2]
añadir(datos)
print(datos)''',
'reasparam': '''def reiniciar(l):
    l = []

datos = [1, 2]
reiniciar(datos)
print(datos)''',
'unbound': '''contador = 0

def sumar():
    contador = contador + 1

sumar()
print(contador)''',
'factorial': '''def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))''',
'cuenta': '''def cuenta(n):
    if n == 0:
        print("¡despegue!")
        return
    print(n)
    cuenta(n - 1)
    print("vuelta", n)

cuenta(3)''',
'sumarec': '''def suma(l):
    if not l:
        return 0
    return l[0] + suma(l[1:])

print(suma([3, 8, 2]))''',
'sinbase': '''def factorial(n):
    return n * factorial(n - 1)

print(factorial(4))''',
})
P.update({
'nota': '''nota = 6.5
if nota >= 9:
    calificacion = "Sobresaliente"
elif nota >= 7:
    calificacion = "Notable"
elif nota >= 5:
    calificacion = "Aprobado"
else:
    calificacion = "Suspenso"
print(calificacion)''',
'paridad': '''n = 7
if n % 2 == 0:
    print(n, "es par")
else:
    print(n, "es impar")''',
'bisiesto': '''año = 1900
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print(año, "es bisiesto")
else:
    print(año, "no es bisiesto")''',
'orden': '''nota = 9.5
if nota >= 5:
    calificacion = "Aprobado"
elif nota >= 7:
    calificacion = "Notable"
elif nota >= 9:
    calificacion = "Sobresaliente"
print(calificacion)''',
'sueltos': '''nota = 9.5
if nota >= 9:
    calificacion = "Sobresaliente"
if nota >= 7:
    calificacion = "Notable"
if nota >= 5:
    calificacion = "Aprobado"
print(calificacion)''',
'duplicar': '''n = 1
pasos = 0
while n < 100:
    n = n * 2
    pasos = pasos + 1
print(pasos, n)''',
'cifras': '''x = 4096
cifras = 0
while x > 0:
    x = x // 10
    cifras = cifras + 1
print(cifras)''',
'collatz': '''n = 6
pasos = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    pasos = pasos + 1
print(pasos)''',
'infinito': '''n = 1
pasos = 0
while n < 100:
    pasos = pasos + 1
print(pasos)''',
'range5': '''for i in range(5):
    print(i)''',
'pares': '''suma = 0
for i in range(2, 11, 2):
    suma = suma + i
print(suma)''',
'tabla': '''n = 7
for i in range(1, 6):
    print(n, "x", i, "=", n * i)''',
'hasta10': '''suma = 0
for i in range(1, 10):
    suma = suma + i
print(suma)''',
'tocari': '''for i in range(5):
    print(i)
    i = i + 10''',
})
P.update({
'indices': '''notas = [7, 4, 9]
notas[1] = 6
notas[-1] = 10
print(notas[0], notas[-1])''',
'metodos': '''pila = [1, 2]
pila.append(3)
pila.insert(0, 0)
ultimo = pila.pop()
print(pila, ultimo)''',
'ordenar': '''datos = [5, 2, 8]
copia = sorted(datos)
datos.sort()
print(datos, copia)''',
'sortnone': '''datos = [5, 2, 8]
datos = datos.sort()
print(datos)''',
'borrar': '''nums = [2, 4, 5, 6]
for x in nums:
    if x % 2 == 0:
        nums.remove(x)
print(nums)''',
'plana': '''a = [1, 2, 3]
b = a.copy()
b[0] = 99
print(a, b)''',
'anidada': '''matriz = [[1, 2], [3, 4]]
copia = matriz.copy()
copia[0][0] = 99
print(matriz)''',
'profunda': '''import copy
matriz = [[1, 2], [3, 4]]
copia = copy.deepcopy(matriz)
copia[0][0] = 99
print(matriz)''',
'tablero': '''tablero = [[0] * 3] * 3
tablero[0][0] = 1
print(tablero)''',
'filas': '''tablero = [[0] * 3 for _ in range(3)]
tablero[0][0] = 1
print(tablero)''',
'agenda': '''edades = {"Ana": 30, "Luis": 25}
edades["Marta"] = 28
edades["Ana"] = 31
print(edades["Ana"], len(edades))''',
'contarletras': '''texto = "banana"
cuenta = {}
for letra in texto:
    cuenta[letra] = cuenta.get(letra, 0) + 1
print(cuenta)''',
'items': '''precios = {"pan": 1.2, "leche": 0.9}
total = 0
for producto, precio in precios.items():
    total = total + precio
print(round(total, 2))''',
'keyerror': '''edades = {"Ana": 30, "Luis": 25}
print(edades["Marta"])''',
})
BIN = '''lista = %s
objetivo = %s
izq, der = 0, len(lista) - 1
pos = -1
while izq <= der:
    medio = (izq + der) // 2
    if lista[medio] == objetivo:
        pos = medio
        break
    elif lista[medio] < objetivo:
        izq = %s
    else:
        der = medio - 1
print(pos)'''
P.update({
'lineal': '''lista = [3, 8, 12, 15, 21, 27, 33, 40]
objetivo = 27
pos = -1
for i in range(len(lista)):
    if lista[i] == objetivo:
        pos = i
        break
print(pos)''',
'binaria': BIN % ('[3, 8, 12, 15, 21, 27, 33, 40]', '27', 'medio + 1'),
'noesta': BIN % ('[3, 8, 12, 15, 21, 27, 33, 40]', '20', 'medio + 1'),
'desordenada': BIN % ('[21, 3, 40, 8, 33, 15, 27, 12]', '21', 'medio + 1'),
'sinmasuno': BIN % ('[3, 8, 12, 15, 21, 27, 33, 40]', '40', 'medio'),
'burbuja': '''lista = [5, 1, 4, 2, 8]
n = len(lista)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)''',
'temprana': '''lista = [1, 2, 3, 5, 4]
n = len(lista)
for i in range(n - 1):
    cambiado = False
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            cambiado = True
    if not cambiado:
        break
print(lista)''',
'pisarb': '''lista = [5, 1, 4, 2, 8]
n = len(lista)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j] = lista[j + 1]
            lista[j + 1] = lista[j]
print(lista)''',
'rangob': '''lista = [5, 1, 4, 2, 8]
n = len(lista)
for i in range(n - 1):
    for j in range(n):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)''',
})
INS = '''lista = %s
for i in range(1, len(lista)):
    clave = lista[i]
    j = i - 1
    while %slista[j] > clave:
        lista[j + 1] = lista[j]
        j = j - 1
    lista[j + 1] = clave
print(lista)'''
P.update({
'insercion': INS % ('[5, 2, 4, 6, 1, 3]', 'j >= 0 and '),
'casi': INS % ('[1, 2, 3, 5, 4, 6]', 'j >= 0 and '),
'alreves': INS % ('[6, 5, 4, 3, 2, 1]', 'j >= 0 and '),
'sinj': INS % ('[3, 1, 2]', ''),
})
CAIDA = '''g = 9.8
dt = %s
t, y, v = 0.0, 20.0, 0.0
while y > 0:
%s
    t = t + dt
print(round(t, 2), round(y, 2))'''
OSC = '''k, m = 4.0, 1.0
dt = %s
t, x, v = 0.0, 1.0, 0.0
while t < 3.2:
    a = -k / m * x
%s
    t = t + dt%s
print(round(%s, 3))'''
TIRO = '''import math
g, dt = 9.8, 0.1
v0, ang = 15.0, %s
vx = v0 * math.cos(%s)
vy = v0 * math.sin(%s)
x, y = 0.0, 0.0
while y >= 0:
    x = x + vx * dt
    vy = vy - g * dt
    y = y + vy * dt
print(round(x, 2))'''
EXP = '    x = x + v * dt\n    v = v + a * dt'
CRO = '    v = v + a * dt\n    x = x + v * dt'
P.update({
'euler': CAIDA % ('0.1', '    y = y + v * dt\n    v = v - g * dt'),
'dtgrande': CAIDA % ('0.4', '    y = y + v * dt\n    v = v - g * dt'),
'cromerc': CAIDA % ('0.1', '    v = v - g * dt\n    y = y + v * dt'),
'signo': CAIDA % ('0.1', '    y = y + v * dt\n    v = v + g * dt'),
'tigual': '''t = 0.0
dt = 0.1
while t != 1.0:
    t = t + dt
print(t)''',
'explicito': OSC % ('0.1', EXP, '', 'x'),
'cromer': OSC % ('0.1', CRO, '', 'x'),
'energia': OSC % ('0.1', EXP, '\n    E = 0.5 * m * v**2 + 0.5 * k * x**2', 'E'),
'explota': OSC % ('0.5', EXP, '', 'x'),
'tiro45': TIRO % ('45', 'math.radians(ang)', 'math.radians(ang)'),
'tiro30': TIRO % ('30', 'math.radians(ang)', 'math.radians(ang)'),
'tiro60': TIRO % ('60', 'math.radians(ang)', 'math.radians(ang)'),
'grados': TIRO % ('45', 'ang', 'ang'),
})
P.update({
'fibo': '''a, b = 0, 1
serie = []
while len(serie) < 8:
    serie.append(a)
    a, b = b, a + b
print(serie)''',
'vocales': '''frase = "mirar y ver"
cuenta = {}
for letra in frase:
    if letra in "aeiou":
        cuenta[letra] = cuenta.get(letra, 0) + 1
print(cuenta)''',
'pareshasta': '''def pares_hasta(n):
    res = []
    for i in range(0, n + 1, 2):
        res.append(i)
    return res

print(pares_hasta(8))''',
'entrada': '''nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
print("Hola,", nombre, "- dentro de 10 años tendrás", edad + 10)''',
'blanco': '''# Escribe o pega aquí tu programa
# y pulsa «Ejecutar y trazar».''',
})
ENTRADAS = {'entrada': ['Ana', '16']}
