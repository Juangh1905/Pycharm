### Tarea 4 ###
"""
#Ejercicio 1
num = 1
while num != 0:
    num = int(input("Introduce un numero positivo, y 0 para detener el bucle: "))
    if num % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

#Ejercicio 2
palabra = input("Introduce una palabra: ")
letra = input("Introduce una letra: ")

if palabra.__contains__(letra):
    print("La letra esta dentro de la palabra")
else:
    print("La letra no esta dentro de la palabra")


#Ejercicio 3
presupuesto = 200
total = 0

while total < presupuesto:
    precio = float(input("Introduce un precio (0 para terminar): "))
    if precio == 0:
        break  # El usuario ha terminado
    total += precio
    if total > presupuesto:
        print("Te has pasado del presupuesto.")
        break

print("Total de tus compras:", total, "€")



#Ejercicio 4
num = 1
while num != 0:
    num = int(input("Introduce un numero, y 0 para detener el bucle: "))
    if num >= 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")


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

num = inicio
suma = 0

while num <= fin:
    if num % 3 == 0:
        suma += num
    num += 1

# Mostramos el resultado
print("La suma de los múltiplos de 3 es:", suma)


#Ejercicio 8
nums = int(input("Cuántos números vas a introducir: "))
producto = 1

for i in range(nums):
    numero = float(input("Introduce un número: "))
    producto *= numero

print("El producto de los números introducidos es:", producto)

#Ejercicio 9
edad = int(input("Introduce tu edad: "))
ano = int(input("Introduce el año actual: "))
ano_nacimiento = ano - edad

for i in range(ano_nacimiento ,ano+1):
    print(i)



#Ejercicio 10
num = int(input("Introduce un número entero: "))

# Triángulo rectángulo
for i in range(1, num + 1):
    print("*" * i)

# Cuadrado
for i in range(num):
    print("* " * num)
    
"""

