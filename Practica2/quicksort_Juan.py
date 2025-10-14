array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def quicksort(a):
    menores= []
    igual= []
    mayores = []

    if len(array) > 1:
        numCentral = array[0]
        for num in array:
            if num < numCentral:
                menores.append(numCentral)
            elif num > numCentral:
                mayores.append(numCentral)
            else:
                igual.append(numCentral)
        return quicksort(menores)+numCentral+quicksort(mayores)
    else:
        raise ValueError("No se puede ordenar")

