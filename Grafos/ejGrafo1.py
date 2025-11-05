from graph import Node, Graph
import matplotlib.pyplot as plt

# un grafo dirigido, con conexion del nodo B al nodo A, con peso 3
# dirigido (no hay conexión de nodo A a B)
# b -(3)>a
nodoA=Node('A', (1,2))
nodoB=Node('B', (2,2), [(nodoA, 3)]) #B conecta con A con coste 3

miGrafo = Graph()
miGrafo.add_node(nodoA)
miGrafo.add_node(nodoB)

print(miGrafo)
print("¿Estan conectados A y B?", miGrafo.are_connected('A', 'B'))
print("¿Estan conectados B y A?", miGrafo.are_connected('B', 'A'))

print('A'>'B')

# 2º ejemplo: grafo con 4 nodos y algunas aristas
nodos=[Node('A', (1,2)),Node('B', (2,2)),Node('C', (3,4)), Node('D', (-2,-2))]

miGrafo2 = Graph()
for nodo in nodos:
    miGrafo2.add_node(nodo)

miGrafo2.add_edge('A', 'B', 5)
miGrafo2.add_edge('D', 'C', 8)

print("Conectados D y C:", miGrafo2.are_connected('D', 'C'))
print("Conectados A y D:", miGrafo2.are_connected('A', 'D'))

plt.title('Ruta al destino')
x=[]
y=[]
for nodo in nodos:
    x.append(nodo.x)
    y.append(nodo.y)

plt.scatter(x,y)
plt.show()