"""
#Ejercicio 1
num1=45
num2=6

division=(num1/num2)
print("45 / 6 = ", division)


#Ejercicio 2
num1=45
num2=6

division=(num1%num2)
print("El resto de 45/6 es igual a ", division)

#Ejercicio 3
print("10+20/7-2", 10+20/7-2)

#Ejercicio 4
print (9-(25+5-2)/(7*4))


###  TAREA 3 ###

# Ejercicio 1
num = int(input("Introduce un número: "))

if num > 0:
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")

# Ejercicio 2
nombre = input("Introduce tu nombre: ")

if len(nombre) > 10:
    print("El nombre es largo")
else:
    print("El nombre es corto")

# Ejercicio 3
nombre = input("Introduce tu nombre: ")

texto_largo = "El nombre es largo"
texto_corto = "El nombre es corto"

print(texto_largo) if len(nombre) > 10 else print(texto_corto)

# Ejercicio 4
num1 = int(input("Introduce un numero positivo: "))
num2 = int(input("Introduce otro numero positivo: "))

if num1 > num2:
    print("El primer número es mayor que el segundo")
elif num1 < num2:
    print("El segundo número es mayor que el primero")
else:
    print("Los números son iguales")
"""
# Ejercicio 5
num1 = int(input("Introduce un numero positivo: "))
num2 = int(input("Introduce otro numero positivo: "))

if num1 >= num2:
    if num1 % num2 == 0:
        print("La división es exacta")
        print("Cociente:",num1//num2)
    else:
        print("La división no es exacta")
        print("Cociente:", num1 // num2, "Resto:", num1 % num2)

else:
    print("El segundo número es mayor que el primero")

# Ejercicio 6
num1 = int(input("Introduce un numero positivo: "))
num2 = int(input("Introduce otro numero positivo: "))

if num1 > num2:
    print("El primer número es mayor que el segundo")
    print("División:",num1/num2)
    if num1 % num2 == 0:
        print("La división es exacta")
        print("Cociente:",num1//num2)
    else:
        print("La división no es exacta")
        print("Cociente:", num1 // num2, "Resto:", num1 % num2)
elif num1 < num2:
    print("El segundo número es mayor que el primero")
    print("División:", num1 / num2)
else:
    print("Los números son iguales")
    print("División:", num1 / num2)

# Ejercicio 7
num1 = int(input("Introduce un numero positivo: "))
num2 = int(input("Introduce otro numero positivo: "))

if num1 > num2:
    if num1 % num2 == 0:
        print(num1,"es multiplo de",num2)
    else:
        print(num1,"no es multiplo de",num2)
elif num2 > num1:
    if num2 % num1 == 0:
        print(num2,"es multiplo de",num1)
    else:
        print(num2,"no es multiplo de",num1)
else:
    print("Los numeros son iguales")

# Ejercicio 8
palabra = input("Introduce una palabra: ")

if palabra[0].isupper():
    print("La palabra empieza con mayúscula")
else:
    print("La palabra no empieza con minuscula")

# Ejercicio 9
letra = input("Introduce una letra: ")

if len(letra) != 1:
    print("Por favor, introduce solo una letra")
else:
    letra = letra.lower()  # Convertir a minúscula
    if letra in "aeiou":
        print("La letra es una vocal")
    else:
        print("La letra no es una vocal")

# Ejercicio 10
import math

a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

# Comprobar que a != 0
if a == 0:
    print("El coeficiente 'a' no puede ser 0 en una ecuación de segundo grado.")
else:
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        # Dos soluciones reales diferentes
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("La ecuación tiene dos soluciones reales diferentes:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif discriminante == 0:
        # Dos soluciones reales iguales
        x = -b / (2*a)
        print("La ecuación tiene dos soluciones reales iguales:")
        print("x =", x)
    else:
        # No hay soluciones reales
        print("La ecuación no tiene soluciones reales.")
