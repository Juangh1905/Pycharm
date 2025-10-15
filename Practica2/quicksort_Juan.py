
# quicksort_juan.py

def quicksort(a):
    menores = []
    igual = []
    mayores = []

    if len(a) > 1:
        pivote = a[0]
        for num in a:
            if num < pivote:
                menores.append(num)
            elif num > pivote:
                mayores.append(num)
            else:
                igual.append(num)
        return quicksort(menores) + igual + quicksort(mayores)
    else:
        return a

# Prueba 1
lista1 = [5, 2, 9, 1, 7]
print("Lista original 1:", lista1)
print("Lista ordenada 1:", quicksort(lista1))

# Prueba 2
lista2 = [10, 3, 8, 4, 6, 2]
print("\nLista original 2:", lista2)
print("Lista ordenada 2:", quicksort(lista2))


