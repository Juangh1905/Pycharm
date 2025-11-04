import numpy as np

#ejercicio 1
def carga(nombre_fichero):
    """
    Parameters
    ----------
    nombre_fichero : str
        Nombre del fichero que contiene el tablero de Sudoku.

    Returns
    -------
    np.ndarray
        Matriz de Sudoku como array de enteros, donde los huecos están representados por ceros.
    """
    tablero = []
    with open(nombre_fichero, 'r') as f:
        for linea in f:
            fila = [int(num) for num in linea.strip().split(';')]
            tablero.append(fila)
    return np.array(tablero)


#Ejercicio 2
def esValidoFila(matriz, fila):
    numeros_en_fila = [num for num in matriz[fila] if num != 0]

    # Comprobar duplicados
    # Si la longitud de la lista de números filtrados es igual a la
    # longitud del 'set' (conjunto) de esos números, no hay duplicados.
    return len(numeros_en_fila) == len(set(numeros_en_fila))

#Ejercicio 3
def esValidoFila(matriz, columna):
    numeros_en_col = [num for num in matriz[columna] if num != 0]
    return len(numeros_en_col) == len(set(numeros_en_col))

#Ejercicio 4
def esValidoCuadro(matriz,fila,columna):
    coordenada = matriz[fila][columna]



matriz = carga("sudoku.txt")
esValidoFila(matriz,0)
print(matriz)
