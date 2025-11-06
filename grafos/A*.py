from graph import Node, Graph

# Crear grafo
miGrafo = Graph()

# Añadir nodos con coordenadas
miGrafo.add_node(Node('S', (1, 1)))
miGrafo.add_node(Node('B', (1, 2)))
miGrafo.add_node(Node('C', (1, 4)))
miGrafo.add_node(Node('D', (2, 1)))
miGrafo.add_node(Node('E', (2, 2)))
miGrafo.add_node(Node('F', (2, 3)))
miGrafo.add_node(Node('G', (2, 4)))
miGrafo.add_node(Node('H', (3, 1)))
miGrafo.add_node(Node('I', (3, 4)))
miGrafo.add_node(Node('J', (4, 1)))
miGrafo.add_node(Node('K', (4, 2)))
miGrafo.add_node(Node('L', (4, 4)))
miGrafo.add_node(Node('T', (4, 3)))

# Añadir aristas con pesos (length)
miGrafo.add_edge('S', 'B', 4)
miGrafo.add_edge('S', 'D', 4)
miGrafo.add_edge('B', 'E', 3)
miGrafo.add_edge('D', 'E', 3)
miGrafo.add_edge('D', 'H', 3)
miGrafo.add_edge('H', 'J', 2)
miGrafo.add_edge('J', 'K', 1)
miGrafo.add_edge('K', 'T', 2)  # antes vacío
miGrafo.add_edge('E', 'F', 2)
miGrafo.add_edge('F', 'G', 3)
miGrafo.add_edge('G', 'C', 2)  # antes vacío
miGrafo.add_edge('G', 'I', 2)
miGrafo.add_edge('I', 'L', 1)
miGrafo.add_edge('L', 'T', 2)  # antes vacío


