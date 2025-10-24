from puntos import Punto


class NotAPointException(Exception):
    pass


class Rectangulo:
    """
    La clase rectángulo va a tener los siguientes métodos:
    - constructor para inicializar un rectángulo a partir de 2 puntos
    - calcular perímetro
    - calcular área
    - __str__
    - __add__ -> devuelve la suma de sus áreas
    """
    def __init__(self,p1,p2):
        if type(p1)!=Punto and type(p2)!=Punto:
            raise NotAPointException
        self.p1=p1
        self.p2=p2

    def calcular_area(self):
        lado1=abs(self.p1.x-self.p2.x)
        lado2=abs(self.p1.y-self.p2.y)
        return lado1*lado2

    def perimetro(self):
        lado1 = abs(self.p1.x - self.p2.x)
        lado2 = abs(self.p1.y - self.p2.y)
        return 2*(lado1 + lado2)

    def __str__(self):
        return "Rectangulo("+str(self.p1)+","+str(self.p2)+")"

    def __add__(self,other):
        return self.calcular_area()+other.calcular_area()

r1=Rectangulo(Punto(1,2),Punto(3,4))
print("El area de ",r1, " es ",r1.calcular_area())
r2=Rectangulo(Punto(5,8),Punto(10,20))
print("El area de ",r2, " es ",r2.calcular_area())
print(r1+r2)

