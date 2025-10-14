#Ejercicio 1
def divisores(numero):
    lista = []
    for i in range(1, numero +1):
        if numero % i == 0:
            lista.append(i)
    return lista
print(divisores(10))


#Ejercicio 4
def vocal(a):
    if a.lower() in "aeiou":
        return True
    else:
        return False
print(vocal('A'))


#Ejercicio 7
def palindromo(palabra):
    if palabra == palabra[::-1]:
        print(palabra + " es palindromo")
    else:
        print(palabra + " no es palindromo")
print(palindromo('reconocer'))
