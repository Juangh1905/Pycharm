import networkx as nx
import matplotlib.pyplot as plt

miGrafo = nx.Graph()

miGrafo.add_node('A', pos=(0, 1))
miGrafo.add_node('B', pos=(2, 2))
miGrafo.add_node('C', pos=(1, 0))
miGrafo.add_node('D', pos=(3, 0))
miGrafo.add_node('E', pos=(4, 1))
miGrafo.add_node('F', pos=(6, 0))
miGrafo.add_node('G', pos=(6, 2))
miGrafo.add_node('H', pos=(7, 1))  # Nodo H (aislado)

miGrafo.add_edge('A', 'B', length=5)
miGrafo.add_edge('A', 'C', length=2)
miGrafo.add_edge('B', 'C', length=1)
miGrafo.add_edge('B', 'E', length=4)
miGrafo.add_edge('B', 'D', length=2)
miGrafo.add_edge('C', 'D', length=7)
miGrafo.add_edge('D', 'E', length=1)
miGrafo.add_edge('E', 'G', length=12)
miGrafo.add_edge('E', 'F', length=15)
miGrafo.add_edge('F', 'G', length=1)

# Posiciones y etiquetas
pos = nx.get_node_attributes(miGrafo, 'pos')
etiquetas_aristas = nx.get_edge_attributes(miGrafo, 'length')

# Dibujar grafo con estilo personalizado
plt.figure(figsize=(10, 7))
nx.draw_networkx_edges(miGrafo, pos, edge_color='gray', width=2)
nx.draw_networkx_nodes(miGrafo, pos, node_color='white', edgecolors='black', linewidths=1.5, node_size=400)
nx.draw_networkx_labels(miGrafo, pos, font_size=12)
nx.draw_networkx_edge_labels(miGrafo, pos, edge_labels=etiquetas_aristas, font_color='black', font_size=9)

plt.title("Representación del Grafo con NetworkX (Ejercicio 2)")
plt.axis('equal')
plt.grid(True)
plt.show()

