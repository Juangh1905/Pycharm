from graph import Node, Graph
import matplotlib.pyplot as plt
from a_star import AStar
from math import inf


def crear_grafo():
    grafo = Graph()

    # Añadir nodos con coordenadas
    grafo.add_node(Node('A', (0, 1)))
    grafo.add_node(Node('B', (2, 2)))
    grafo.add_node(Node('C', (1, 0)))
    grafo.add_node(Node('D', (3, 0)))
    grafo.add_node(Node('E', (4, 1)))
    grafo.add_node(Node('F', (5, 0)))
    grafo.add_node(Node('G', (6, 2)))
    grafo.add_node(Node('H', (7, 1)))

    # Añadir aristas con pesos
    grafo.add_edge('A', 'B', 5)
    grafo.add_edge('A', 'C', 2)
    grafo.add_edge('B', 'C', 1)
    grafo.add_edge('B', 'E', 4)
    grafo.add_edge('B', 'D', 2)
    grafo.add_edge('C', 'D', 7)
    grafo.add_edge('D', 'E', 1)
    grafo.add_edge('E', 'F', 15)
    grafo.add_edge('E', 'G', 12)
    grafo.add_edge('F', 'G', 1)

    return grafo

def dibujar_grafo_matplotlib(grafo):
    plt.title("Grafo con matplotlib")
    x = []
    y = []

    for nodo in grafo.nodes:
        x.append(nodo.x)
        y.append(nodo.y)
        plt.scatter(nodo.x, nodo.y, s=200, color = 'white', edgecolors='black')
        plt.text(nodo.x + 0.1, nodo.y + 0.1, nodo.value, fontsize=12)

        for vecino, peso in nodo.neighbors:
            plt.plot([nodo.x, vecino.x], [nodo.y, vecino.y], color='gray')
            mid_x = (nodo.x + vecino.x) / 2
            mid_y = (nodo.y + vecino.y) / 2
            plt.text(mid_x, mid_y, str(peso), fontsize=9)

    plt.axis('equal')
    plt.grid(True)
    plt.show()




grafo = crear_grafo()

""" 
#Ejercicio3.a
#dibujar_grafo_matplotlib(grafo)

#Ejercicio 3.b
#1
nodo_B = grafo.find_node('B')
if nodo_B.has_neighbors():
    vecinos = [vecino.value for vecino, _ in nodo_B.neighbors]
    print(f"Vecinos del nodo B: {vecinos}")
else:
    print("El nodo B no tiene vecinos.")

#2
print("¿Estan conectados G y H?", grafo.are_connected('G', 'H'))

#3
print("¿Estan conectados D y E?", grafo.are_connected('A', 'B'))

#4
print(grafo.number_of_nodes())

#5
print("Lista de nodos: ", [n.value for n in grafo.nodes])


# Ejercicio 4
def reset_graph(grafo):
    for nodo in grafo.nodes:
        nodo.parent = None
        nodo.heuristic_value = -1
        nodo.distance_from_start = inf


# Ejercicio 5
def ruta(origen, destino, grafo):
    algoritmo = AStar(grafo, origen, destino)   # crear objeto
    resultado = algoritmo.search()              # ejecutar búsqueda
    if resultado:
        path, cost = resultado
        print("Ruta:", " → ".join(path))
        print("Coste total:", cost)
    else:
        print("No se encontró ruta entre", origen, "y", destino)

grafo = crear_grafo()

ruta('A', 'G', grafo)


# Ejercicio 6
def ejecutar_busquedas(grafo):
    casos = [
        ('A', 'B'),
        ('A', 'G'),
        ('A', 'H'),
        ('G', 'C')
    ]

    for origen, destino in casos:
        algoritmo = AStar(grafo, origen, destino)
        resultado = algoritmo.search()
        if resultado:
            path, cost = resultado
            print(f"Camino más corto entre {origen} y {destino}: {' → '.join(path)} (Coste: {cost})")
        else:
            print(f"No se encontró ruta entre {origen} y {destino}")

grafo = crear_grafo()
ejecutar_busquedas(grafo)

"""


#Ejercicio 7
def reset_graph(grafo):
    for nodo in grafo.nodes:
        nodo.parent = None
        nodo.heuristic_value = -1
        nodo.distance_from_start = inf

reset_graph(grafo)
algoritmo = AStar(grafo, 'A', 'E')
resultado = algoritmo.search()

if resultado:
    path, cost = resultado
    print("Ruta encontrada por A*:", " → ".join(path))
    print("Coste total:", cost)
else:
    print("No se encontró ruta entre A y E")



