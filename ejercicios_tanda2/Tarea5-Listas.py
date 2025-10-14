"""
#Ejercicio 1
s = "abcdefg"
lista1= [i for i in s]
lista1.reverse()
print(lista1)


#Ejercicio 2
s1 = "hola caracola"
s2 = "adios marieta"

lista = []

for i in range(len(s1)):
    lista.append(s1[i])
    lista.append(s2[i])

print("".join(lista))

#Ejercicio 3
s3 = input("Introduce un string: ")
lista3 = []
for cons in s3:
    if cons.lower() in ("aeiou"):
        lista3.append(cons)
print("Lista con las consonaste",lista3)



#Ejercicio 4
palabra = input("Introduce una palabra: ")
lista = list(palabra)
lista_invertida = lista[::-1]

if lista == lista_invertida:
    print(f"La palabra {palabra} es un palindromo")
else:
    print(f"La palabra {palabra} no es un palindromo")


#Ejercicio 5
matriz = [[3,2,1],
          [4,10,6],
          [7,1,9]]
for row in matriz:
    maximo = max(row)
    print(f"La fila {row} es {maximo}")



#Ejercicio 6
n = int(input("Introduce el tamaño n de la matriz (n x n): "))

matriz = []

# Llenar la matriz con números del 0 al n² - 1
contador = 0
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(contador)
        contador += 1
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz generada:")
for fila in matriz:
    print(fila)

"""

#Ejercicio 7
n = int(input("Número de filas (n): "))
m = int(input("Número de columnas (m): "))

matriz = []

# Leer los valores manualmente
print(f"\nIntroduce los {n*m} valores de la matriz:")
for i in range(n):
    fila = []
    for j in range(m):
        valor = int(input(f"Elemento [{i+1},{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz introducida:")
for fila in matriz:
    print(fila)

# Calcular la suma de cada columna
suma_columnas = []
for j in range(m):
    suma = 0
    for i in range(n):
        suma += matriz[i][j]
    suma_columnas.append(suma)

# Verificar si todas las sumas son iguales
if all(s == suma_columnas[0] for s in suma_columnas):
    print("\n Todas las columnas tienen la misma suma:", suma_columnas[0])
else:
    print("\n Las columnas tienen sumas diferentes:")
    for idx, s in enumerate(suma_columnas):
        print(f"Columna {idx+1}: suma = {s}")





