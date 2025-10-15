# binaria_juan.py
def busqueda_binaria(lista, num, desplazamiento=0):
    if not lista:
        return -1

    mitad = int(len(lista) // 2)
    numCentral = lista[mitad]
    posicion_real = desplazamiento + mitad

    if num < numCentral:
        return busqueda_binaria(lista[:mitad], num, desplazamiento)
    elif num > numCentral:
        return busqueda_binaria(lista[mitad+1:], num, posicion_real + 1)
    else:
        return f"Encontrado el {num} en la posición {posicion_real}"




# Prueba 1
lista1 = [1, 3, 5, 7, 9, 11, 13]
print(busqueda_binaria(lista1, 13))


# Prueba 2
lista2 = [20, 35, 42, 1, 3, 5, 7, 9, 11, 13, 15]
print(busqueda_binaria(lista2, 15))


