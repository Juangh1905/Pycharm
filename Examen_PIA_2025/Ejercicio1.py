import matplotlib.pyplot as plt
"""
#Ejercicio 1
inventario = {
    "manzanas": 25,
    "naranjas": 18,
    "plátanos": 30,
    "peras": 12
}

producto= input("Introduce el nombre de un producto: ")

if producto in inventario:
    print("El producto existe en el inventario")
    unidades = inventario[producto]
    print("Hay ", unidades, " unidades de", producto )
else:
    print("El producto no existe en el inventario")


#Ejercicio 2
def reverse(lista):
    palabras_reves = []
    for palabra in lista:
        palabras_reves.append(palabra[::-1])
    return palabras_reves

lista=['en','un','lugar','de','la','mancha']
revertido = reverse(lista)
print(revertido)
"""

#Ejercicio 3
def notas(lista_notas):
    resultado = []
    for nota in lista_notas:
        if nota >= 9:
            resultado.append('sobresaliente')
        elif nota >= 5:
            resultado.append('apto')
        else:
            resultado.append('no apto')
    return resultado
lista_notas = [10, 8, 6, 4, 9, 3, 7]
examenes = notas(lista_notas)
print(examenes)

"""
#ejercicio 4
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_pares = [num for num in numeros if num % 2 == 0]
print(numeros_pares)

numeros_cuadrado = [num**2 for num in numeros]
print(numeros_cuadrado)

matriz = [numeros for i in range(10)]
print(matriz)


#Ejercicio 5
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

fila_sumas = [sum(fila) for fila in matriz]
print(fila_sumas)

diag_principal = [matriz[0][0], matriz[1][1], matriz[2][2]]
print(diag_principal)

pares_matriz = [num for fila in matriz for num in fila if num % 2 == 0]
print(pares_matriz)


#Ejercicio 6
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
x = matriz[0]
y = [sum(fila) for fila in matriz]
plt.scatter(x, y)
plt.show()


#Ejercicio 7
class Coche:
    def __init__(self, marca, modelo, anio, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = velocidad

    def acelerar(self, cantidad):
        self.velocidad += cantidad

    def frenar(self, cantidad):
        self.velocidad -= cantidad
        if self.velocidad < 0:
            self.velocidad = 0

    def mostrar_info(self):
        print("Marca:", self.marca, " Modelo:", self.modelo, " Año:", self.anio, " Velocidad:", self.velocidad, "km/h")


coche1 = Coche("Toyota", "Yaris", 2004, 0)
coche2 = Coche("Renault", "Clio", 2010, 0)

coche1.acelerar(50)
coche2.acelerar(80)

coche1.frenar(20)
coche2.frenar(100)

coche1.mostrar_info()
coche2.mostrar_info()

"""



