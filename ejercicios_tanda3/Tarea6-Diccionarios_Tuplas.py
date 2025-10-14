#Ejercicio 1
num = int(input("Ingresa un numero: "))
for i in range(1, num+1):
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

"""

