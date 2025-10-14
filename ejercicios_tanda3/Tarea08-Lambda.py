#Ejercicio 1
mult = lambda a: (a-1) * a * (a+1)
print(mult(3))

#Ejercicio 3
def mas_vocales_que_consonantes(palabra):
    vocales = "aeiou"
    num_vocales = 0
    num_consonantes = 0

    for letra in palabra:
        if letra.lower() in vocales:
            num_vocales += 1
        else:
            num_consonantes += 1

    return num_vocales > num_consonantes

# Usamos lambda para aplicar la función
lista = ["aurelio", "ramirez", "sol", "aeiou", "luz", "idea", "casa"]
resultado = list(filter(lambda x: mas_vocales_que_consonantes(x), lista))
print(resultado)


#Ejercicio 5
def palabra_mas_larga(p1, p2):
    return p1 if len(p1) > len(p2) else p2

from functools import reduce
lista = ["sol", "estrella", "luz", "universo", "galaxia"]

resultado = reduce(palabra_mas_larga, lista)
print(resultado)


