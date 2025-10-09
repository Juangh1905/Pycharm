"""
#Ejercicio 1
s = "abcdefg"
lista1= [i for i in s]
lista1.reverse()
print(lista1)
"""

#Ejercicio 2
s1 = "hola caracola"
s2 = "adios marieta"

lista = []

for i in range(len(s1)):
    lista.append(s1[i])
    lista.append(s2[i])

print("".join(lista))

#Ejercicio 3
s3 = "esto es un string"
lista3 = []
for i in range(0,len(s3)):
    cons=lista[i]
    if cons not in lista3:
        print("La consonante")

"""
#Ejercicio 5
suma = 0
contador = 0


while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero       # Sumamos el número
    contador += 1        # Contamos cuántos números se han introducido

if contador > 0:
    media = suma / contador
    print("La media es:", media)
else:
    print("No se introdujeron números.")

#Ejercicio 6
inicio = int(input("Introduce el extremo izquierdo: "))
fin = int(input("Introduce el extremo derecho: "))

num = inicio

while num <= fin:
    print(num)
    num += 1

#Ejercicio 6 (con for)
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
for i in range(num1, num2 + 1):
    print(i)

#Ejercicio 7
num1 = int(input("Introduce el extremo izquierdo: "))
num2 = int(input("Introduce el extremo derecho: "))

suma = 0

for j in range(num1, num2 + 1):
    if j % 3 == 0:
        suma += j
print("La suma de los múltiplos de 3 es:", suma)

#Ejercicio 7 (con while)
inicio = int(input("Introduce el extremo izquierdo: "))
fin = int(input("Introduce el extremo derecho: "))

# Inicializamos variables
num = inicio
suma = 0

# Bucle while para sumar los múltiplos de 3
while num <= fin:
    if num % 3 == 0:
        suma += num
    num += 1

# Mostramos el resultado
print("La suma de los múltiplos de 3 es:", suma)

"""
#Ejercicio 8
num = int(input("Introduce un número entero: "))
"""
# Triángulo rectángulo
for i in range(1, num + 1):
    print("*" * i)

"""
# Cuadrado
for i in range(num):
    print("* " * num)


