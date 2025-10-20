#buscaminas_juan.py
import random

# a.
def generar_tablero():
    tablero = [[0]*8 for _ in range(8)]
    minas = 0
    while minas < 10:
        f = random.randint(0,7)
        c = random.randint(0,7)
        if tablero[f][c] != -1:
            tablero[f][c] = -1
            minas += 1
    return tablero

# b.
def calcular_vecinos(tablero):
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == -1:
                continue
            contador = 0
            for x in range(max(0,i-1), min(8,i+2)):
                for y in range(max(0,j-1), min(8,j+2)):
                    if tablero[x][y] == -1:
                        contador += 1
            tablero[i][j] = contador
    return tablero

# c.
def descubre(tablero, fila, col):
    if fila < 0 or fila >= 8 or col < 0 or col >= 8:
        return
    if tablero[fila][col] == -1 or tablero[fila][col] == -2:
        return
    if tablero[fila][col] > 0:
        tablero[fila][col] = -2
        return
    tablero[fila][col] = -2
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue
            descubre(tablero, fila+dx, col+dy)

# Imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)
    print()

# ---- Ejemplo de uso ----
tablero = generar_tablero()
tablero = calcular_vecinos(tablero)

print("Tablero inicial:")
imprimir_tablero(tablero)

# Descubrir una casilla
descubre(tablero, 0, 0)

print("Tablero después de descubrir (0,0):")
imprimir_tablero(tablero)
















