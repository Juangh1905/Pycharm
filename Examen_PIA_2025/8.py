from graph import Node, Graph
import networkx as nx

def crear_grafo():
    redAutobuses = Graph()


    redAutobuses.add_node(Node('Plaza Mayor', (0, 1)))
    redAutobuses.add_node(Node('Estación', (2, 0)))
    redAutobuses.add_node(Node('Instituto', (2, -1)))
    redAutobuses.add_node(Node('Polideportivo', (0, -1)))



    redAutobuses.add_edge("Plaza Mayor", "Estación")
    redAutobuses.add_edge("Estación", "Instituto")
    redAutobuses.add_edge("Instituto", "Polideportivo")
    redAutobuses.add_edge("Polideportivo", "Plaza Mayor")

    return redAutobuses


redAutobuses = crear_grafo()
print(redAutobuses.are_connected("Plaza Mayor", "Instituto"))
print(redAutobuses.are_connected("Estación", "Polideportivo"))

for nodo in redAutobuses.nodes:
    print("Nombre:", nodo.value)
    print("Número de conexiones:", nodo.number_of_neighbors())
    print("Paradas conectadas:")
    for vecino in nodo.extend_node():
        print(vecino.value)
    print()


















