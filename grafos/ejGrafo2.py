from graph import Node, Graph
import matplotlib.pyplot as plt



# 3º ejemplo: grafo con 7 nodos y 8 aristas
nodos=[Node('A', (1,2)),
       Node('B', (2,3)),
       Node('C', (3,4)),
       Node('D', (4,2)),
       Node('E', (2,1)),
       Node('F', (3,3)),
       Node('G', (3,1))]

miGrafo2 = Graph()
for nodo in nodos:
    miGrafo2.add_node(nodo)

miGrafo2.add_edge('A', 'B', 2)
miGrafo2.add_edge('A', 'E', 1)
miGrafo2.add_edge('B', 'E', 3)
miGrafo2.add_edge('C', 'F', 2)
miGrafo2.add_edge('D', 'F', 1)
miGrafo2.add_edge('D', 'G', 4)
miGrafo2.add_edge('E', 'G', 1)
miGrafo2.add_edge('F', 'G', 5)

# Dibujar aristas
edges = [
    ('A', 'B'),
    ('A', 'E'),
    ('B', 'E'),
    ('C', 'F'),
    ('D', 'F'),
    ('D', 'G'),
    ('E', 'G'),
    ('F', 'G')
]

plt.title('Ruta al destino')
x=[]
y=[]
for nodo in nodos:
    x.append(nodo.x)
    y.append(nodo.y)

plt.scatter(x,y)
plt.show()
