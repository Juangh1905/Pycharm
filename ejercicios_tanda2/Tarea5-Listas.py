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

"""
#Ejercicio 5




#Ejercicio 6






#Ejercicio 7 




