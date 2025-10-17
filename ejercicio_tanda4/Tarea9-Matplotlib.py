import matplotlib.pyplot as plt
import numpy as np

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















