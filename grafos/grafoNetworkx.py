import networkx as nx
import matplotlib.pyplot as plt

miGrafo = nx.Graph()
miGrafo.add_node('A', pos = (1,2))
miGrafo.add_node('B', pos = (2,3))
miGrafo.add_node('C', pos = (3,4))
miGrafo.add_node('D', pos = (4,2))
miGrafo.add_node('E', pos = (2,1))
miGrafo.add_node('F', pos = (3,3))
miGrafo.add_node('G', pos = (3,1))

miGrafo.add_edge('A', 'B', length = 2)
miGrafo.add_edge('A', 'E', length = 1)
miGrafo.add_edge('B', 'E', length = 3)
miGrafo.add_edge('G', 'E', length = 6)
miGrafo.add_edge('G', 'F', length = 5)
miGrafo.add_edge('G', 'D', length = 4)
miGrafo.add_edge('F', 'D', length = 1)
miGrafo.add_edge('F', 'C', length = 2)

# Obtener posiciones
pos = nx.get_node_attributes(miGrafo, 'pos')

# Obtener etiquetas
etiquetas = nx.get_edge_attributes(miGrafo, 'length')

# Dibujar grafo
nx.draw_networkx_edge_labels(miGrafo, pos, edge_labels=etiquetas)
nx.draw_networkx(miGrafo, pos)
plt.show()
