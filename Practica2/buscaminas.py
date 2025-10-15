import random

def generar_tablero():
    tablero = [[0 for _ in range(8)] for _ in range(8)]

    minas_colocadas = 0
    while minas_colocadas < 10:
        fila = random.randint(0, 7)
        columna = random.randint(0, 7)

        if tablero[fila][columna] != -1:
            tablero[fila][columna] = -1
            minas_colocadas += 1

    return tablero

tablero = generar_tablero()

for fila in tablero:
    print(fila)

def minas_vecinas(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])

    for x in range(filas):
        for y in range(columnas):
            if tablero[x][y] == -1:
                continue  # si ya es mina, no contamos

            contador = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue  # saltar la celda actual

                    nx, ny = x + dx, y + dy
                    if 0 <= nx < filas and 0 <= ny < columnas:
                        if tablero[nx][ny] == -1:
                            contador += 1

            tablero[x][y] = contador









