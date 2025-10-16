"""
#Ejercicio 1
num = int(input("Ingresa un número: "))
diccionario = {}

for i in range(1, num + 1):
    diccionario[i] = i**3  #

print(diccionario)


#Ejercicio 2
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
telefono = int(input("Ingresa tu telefono: "))

print(nombre,"tiene",edad,"años y su número de teléfono es", telefono)

#Ejercicio 3
cesta_compra = {}
while True:
    articulo = input("Ingresa un artículo: ")
    precio = float(input("Ingresa su precio: "))
    cesta_compra[articulo] = precio
    verificar = input("¿Quieres añadir un nuevo producto? (y/n): ")
    if verificar.lower() in ("n", "no"):
        break

print("\nLista de la compra:")
total = 0
for articulo, precio in cesta_compra.items():
    print(f"{articulo} {precio}€")
    total += precio

print(f"{'Total'} {total}€")



#Ejercicio 4
numeros = {}
numeros["positivos"] = 0
numeros["negativos"] = 0
while True:
    num = int(input("Ingresa un numero entero (0 para terminar): "))
    if num == 0:
        break
    elif num > 0:
        numeros["positivos"]+= 1
    else:
        numeros["negativos"] += 1

print(numeros)


# Ejercicio 5
clase = {}

while True:
    alumno = input("Ingresa el nombre del alumno: ")
    if alumno == "":
        break

    notas = []
    while True:
        nota = int(input(f"Introduce una nota para {alumno} (1-10, 0 para terminar): "))
        if nota == 0:
            break
        elif 1 <= nota <= 10:
            notas.append(nota)
        else:
            print("️La nota debe estar entre 1 y 10.")

    clase[alumno] = notas

for alumno, notas in clase.items():
    if notas:
        media = sum(notas) / len(notas)
        print(f"{alumno}: notas = {notas}, media = {media:.2f}")
    else:
        print(f"{alumno}: sin notas registradas")


#Ejercicio 6
num = int(input("Ingresa un número: "))
diccionario = {}

for i in range(1, num + 1):
    diccionario[i] =   "*"*i

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")


#Ejercicio 9
frase = input("Introduce una frase: ")

palabras = frase.split()

# lista de tuplas
resultado = []

for posicion, palabra in enumerate(palabras):
    tupla = (palabra, len(palabra), palabra[0], posicion)
    resultado.append(tupla)

# Mostramos el resultado
for item in resultado:
    print(item)



#Ejercicio 10
lista1 =[]
while True:
    palabra = input("Ingresa una palabra: ")
    if len(palabra) > 0:
        lista1.append(palabra)
    else:
        break
tupla = tuple(lista1)
palabra1, *_, ultimaPalabra = lista1
print(palabra1, ultimaPalabra)



#Ejercicio 11
lista_palabras = ["hola", "adios", "buenas", "hello"]
lista_longitud = []
for palabra in lista_palabras:
    longitud = len(palabra)
    lista_longitud.append(longitud)

for palabra, longitud in zip(lista_palabras, lista_longitud):
    print(palabra, 'su longitud es:', longitud)

"""

#Ejercicio 12






