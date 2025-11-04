"""
import matplotlib.pyplot as plt
import numpy as np

pesos = np.array([80, 75, 120, 55, 70, 60])
alturas = np.array([160, 170, 180, 190, 120, 165])
colores = np.array(['r', 'b', 'g', 'y', 'm', 'c'])

plt.ylim(0, 200)
plt.scatter(x=pesos, y=alturas, c=colores, edgecolors='k', marker='x')
plt.scatter(x=pesos + 1, y=alturas + 1, c='b')
plt.show()



"""
#import matplotlib.pyplot as plt
#import numpy as np

x = np.arange(-100, 100, 10)           # 20 valores
y = x**2
colores = np.arange(0, 20, 1)          # 20 colores
tamanos = [i for i in range(0, 200, 10)]  # 20 tamaños
texto = [i for i in range(0, 200, 10)]

# Scatter plot con mapa de color
plt.scatter(x, y, c=colores, s=tamanos, cmap='plasma_r')
plt.colorbar(label='Barra Color')  # Barra de color

# Añadir texto a cada punto
for xi, yi, textoi in zip(x, y, texto):
    plt.text(xi, yi, s=textoi, ha='center', va='bottom', fontsize=8)

plt.xlabel("Eje X")
plt.ylabel("Eje Y (x²)")
plt.title("Scatter plot con etiquetas adaptadas")
plt.show()




