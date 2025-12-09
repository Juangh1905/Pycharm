def es_valido(laberinto, x, y, visitado):
    # dentro de límites y no es pared ni visitado
    return (0 <= x < len(laberinto) and
            0 <= y < len(laberinto[0]) and
            laberinto[x][y] == 0 and
            (x,y) not in visitado)

def busca_camino(laberinto, x, y, camino, visitado):
    # caso base: llegada a la meta
    if (x, y) == (len(laberinto)-1, len(laberinto[0])-1):
        camino.append((x,y))
        return True

    if es_valido(laberinto, x, y, visitado):
        camino.append((x,y))   # anotar
        visitado.add((x,y))

        # explorar en las 4 direcciones
        if (busca_camino(laberinto, x+1, y, camino, visitado) or
            busca_camino(laberinto, x, y+1, camino, visitado) or
            busca_camino(laberinto, x-1, y, camino, visitado) or
            busca_camino(laberinto, x, y-1, camino, visitado)):
            return True

        camino.pop()           # desanotar
        visitado.remove((x,y))

    return False

# Ejemplo de laberinto
laberinto = [
    [0,1,0,0],
    [0,0,1,0],
    [1,0,0,0],
    [0,0,1,0]
]

camino = []
visitado = set()

if busca_camino(laberinto, 0, 0, camino, visitado):
    print("Camino encontrado:", camino)
else:
    print("No hay salida")
