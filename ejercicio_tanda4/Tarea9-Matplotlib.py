import csv
import matplotlib.pyplot as plt
import numpy as np
"""

x=np.random.normal(loc=10, scale=3, size=100)
print(x)
plt.hist(x, bins=50)
plt.show()



#Ejercicio 1

with open("/home/iabd/Descargas/archive/Books_Data_Clean.csv") as f:
    linea = f.readline()
    while linea != "":
        print(linea, end="")
        linea = f.readline()

#Ejercicio 2
f = open("/home/iabd/Descargas/archive/Books_Data_Clean.csv")
reader = csv.reader(f)
next(reader)
for linea in reader:
    print(linea)


#Ejercicio 3
with open("/home/iabd/Descargas/archive/Books_Data_Clean.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))


#Ejercicio 4
with open("/home/iabd/Descargas/archive/Books_Data_Clean.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = f.readline()
    for row in reader:
        print(headers + np.matrix(row))


#Ejercicio 5 Book Name,  units sold, sale price
with open("/home/iabd/Descargas/archive/Books_Data_Clean.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        nombre = fila.get("Book Name", "")
        rating = fila.get("Book_average_rating", "")
        unidades = fila.get("units sold", "")
        precio = fila.get("sale price", "")

        print(f" {nombre} |  Rating: {rating} |  Vendidos: {unidades} | Precio: {precio}")
        
#Ejercicio 6

precios = np.array([15.99, 22.50, 9.99, 18.75, 12.00, 30.00])
ratings = np.array([4.5, 3.8, 4.2, 4.0, 5.0, 3.5])
vendidas = np.array([12599, 2250, 999, 19875, 21200, 30000])
tamanos = (vendidas//100)
colores = np.where(ratings > 4, 'green', 'red')
titulos =  ['Caperucita', 'El cazador', 'Los 3 cerditos', 'Pinocho', 'La casa', 'La tortuga y la liebre']
for xi, yi, titulo in zip(precios,ratings, titulos):
    plt.text(xi,yi,s=titulo, ha='center', va='bottom')

plt.scatter(x=precios, y=ratings, s=tamanos, c=colores, alpha=0.3, edgecolors='k')
plt.show()


"""







