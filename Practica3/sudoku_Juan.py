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
    elementos = []
    for i in matriz[fila]:
        if i != 0 and i in elementos:
            return False
        elementos.append(i)
    return True



#Ejercicio 3
def esValidoColumna(matriz, columna):
    elementos = []
    for i in matriz[:, columna]:
        if i != 0 and i in elementos:
            return False
        elementos.append(i)
    return True

#Ejercicio 4
def esValidoCuadro(matriz,fila,col):
    elementos = []
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3

    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            num = matriz[i][j]
            if num != 0 and num in elementos:
                return False
            elementos.append(num)
    return True

def resolver_Sudoku(matriz, paso=0):
    if paso >= 81:
        return True  # tablero completo

    x = paso // 9  # fila
    y = paso % 9   # columna

    if matriz[x][y] != 0:
        return resolver_Sudoku(matriz, paso + 1)

    for num in range(1, 10):
        matriz[x][y] = num
        if esValidoFila(matriz, x) and esValidoColumna(matriz, y) and esValidoCuadro(matriz, x, y):
            if resolver_Sudoku(matriz, paso + 1):
                return True
        matriz[x][y] = 0  # backtrack

    return False  # no se pudo colocar ningún número válido



matriz = carga("sudoku.txt")
if resolver_Sudoku(matriz):
    print("¡Sudoku resuelto!")
    print(matriz)
else:
    print("No se pudo resolver el Sudoku.")


