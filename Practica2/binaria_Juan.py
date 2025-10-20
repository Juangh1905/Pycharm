# binaria_juan.py
def busqueda_binaria(lista, objetivo):
    if not lista:
        return -1

    mitad = len(lista) // 2
    numCentral = lista[mitad]

    if numCentral == objetivo:
        return mitad
    elif numCentral > objetivo:
        return busqueda_binaria(lista[:mitad], objetivo)
    else:
        resultado = busqueda_binaria(lista[mitad+1:], objetivo)
        return -1 if resultado == -1 else mitad + 1 + resultado



# Prueba 1
lista1 = [1, 3, 5, 7, 9, 11, 13]
print(busqueda_binaria(lista1, 13))


# Prueba 2
lista2 = [7, 9, 13, 15, 20, 35,]
print(busqueda_binaria(lista2, 7))


