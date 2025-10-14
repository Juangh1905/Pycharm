""" from pydantic import BaseModel
from typing import List

class Empleado(BaseModel):
    nombre: str
    edad: int
    nominas: List[float]

paco=Empleado(nombre="Paco", edad=49,nominas=[1900,2000,1000,2500])

print(paco) "


edad=int(input("Edad: "))
if edad<18:
    print("El edad es menor de 18")
    print("otra cosa")
    print("otra cosa más")
else:
    print("El edad es mayor de 18")


for c in [1,'a',3.4,'hola']:
    print(c)

for c in range(20):
    print(c)

lista2 = [numeros for numeros in [2,202,2]]
lista3 = [ i+2 for i in range(1, 101) ]

print(lista3)

#sacar una lista con un "list comprehension" de los 100 primeros pares pero -1 en los múltiplos de 4
lista4 = [ -1 if n%4==0 else n for n in range(2,202,2) ]
#print(lista4)

x=list(range(20))
#print(x)

listaArrays = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
#print(listaArrays)


m= [ [ j for j in range(0,10)] for i in range() ]
print(m)

#for i in range(0,3):
#print(m[i])


lista8 = [i for i in range(100)]
# Añadir un único elemento al final de la lista
lista8.append(101)

# Añadir varios elementos al final de la lista
lista8.extend([101, 102, 103])

# Insertar un elemento en una posición específica
lista8.insert(0, 'aaaa')  # Inserta 'aaaa' al inicio de la lista



#hacer un pop -> extraer el primer elemento de una lista (get+remove)
lista1= [10,20,30,10,40,50,10,60,70,80,80]
print(lista1.pop(0))
print(lista1)


#eliminar todas las instancias de un elemento de la lista
lista1= [10,20,30,10,40,50,10,60,70,80,80]
elemento=10
encontrado=True
while encontrado:
    try:
        lista1.remove(elemento)
    except ValueError:
        encontrado=False



def suma(x, y):
    pass
print(suma("4","6"))


#Programar la suma de las matrices x e y
def suma(x, y):
    resultado = []
    for i in range(len(x)):           # recorre filas
        fila = []
        for j in range(len(x[0])):    # recorre columnas
            fila.append(x[i][j] + y[i][j])
        resultado.append(fila)
    return resultado


x = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
]

y = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]

print(suma(x, y))



def resumir(m1):

    Recorre una matriz y devuelve la suma de cada una de sus filas
    :param m1: la matriz bidimensional
    :return: una lista con la suma de todas las filas

    Por ejemplo:
    [[1,2,3],
    [4,5,6],
    [1,2,3]] -> [6,15,6]


def resumir(m1):

    #Recibe una matriz bidimensional y devuelve una lista
    #con la suma de cada una de sus filas.

    resultado = []
    for fila in m1:
        resultado.append(sum(fila))
    return resultado

# Ejemplo de uso
x = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

print(resumir(x))  # Imprime: [6, 15, 6]



#Multiplicación de matrices
# Definimos las matrices
A = [
    [1, 2, 3],
    [4, 5, 0],
    [3, 0, 2]
]

B = [
    [0, 1, 2],
    [0, 1, 4],
    [1, 2, 1]
]

# Verificamos que se puedan multiplicar
if len(A[0]) != len(B):
    raise ValueError("No se pueden multiplicar las matrices")

# Creamos la matriz resultado vacía
C = []

# Recorremos las filas de A
for i in range(len(A)):
    fila_resultado = []
    # Recorremos las columnas de B
    for j in range(len(B[0])):
        suma = 0
        # Sumamos los productos de la fila i de A y la columna j de B
        for k in range(len(A[0])):
            suma += A[i][k] * B[k][j]
        fila_resultado.append(suma)
    C.append(fila_resultado)

# Mostramos el resultado
for fila in C:
    print(fila)

"""





