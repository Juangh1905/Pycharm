import math
import random
class Punto:
    """
    Esta clase permite representar un punto en el espacio 2D
    Tiene como métodos
     blah blah
     blah blah
     blah blah
    """
    ## Python -> constructor se __init__
    def __init__(self,x,y):
        self.x=x
        self.y=y

    # destructor
    def __del__(self):
        #print("Punto "+str(self.x)+","+str(self.y)+" se ha destruido destruido!!")
        pass

    def saluda(self,nombre):
        print("Hola,"+nombre+
              ", soy un punto("+str(self.x)+","+str(self.y)+"):"+str(type(self)))

    def distancia_euclidia(self, otro):
        return math.sqrt(  (self.x-otro.x)**2 + (self.y-otro.y)**2 )

    def cuadrante(self):
        """
        Función ficticia que retorna un número dependiendo del cuadrante
        """
        if self.x >= 0:
            if self.y >=0:
                return 1
            else:
                return 3
        else:
            if self.y >=0:
                return 0
            else:
                return 2

    def manhattan(self,otro):
        return abs(self.x-otro.x)+abs(self.y-otro.y)

    def __add__(self, other):
        return Punto(self.x+other.x,self.y+other.y)

    def __str__(self):
        return "Punto("+str(self.x)+","+str(self.y)+")"

    @staticmethod
    def sumar(a,b):
        return a+b

    @classmethod
    def punto_aleatorio(cls):
        return cls(random.randrange(1,10),random.randrange(2,20))

class Punto3d(Punto):
    def __init__(self,x,y,z):
        self.z=z
        super().__init__(x,y)

    def __str__(self):
        return "Punto3d("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def __del__(self):
        pass
        #print("Punto " + str(self.x) + "," + str(self.y) + ","+ str(self.z) + " se ha destruido destruido!!")

    def distancia_euclidia(self, otro):
        d_super=super().distancia_euclidia(otro)
        return math.sqrt(d_super**2+(self.z-otro.z)**2)

"""
p=Punto3d(1,2,3)
print(p.distancia_euclidia(Punto3d(2,2,2)))
print(type(p))


punto1=Punto(2,3)
punto2=Punto(5,7)
d=punto2.distancia_euclidia(punto1)
print("el cuadrante del punto 2 es: ",punto2.cuadrante())
print("la distancia de manhattan de ",punto1," al ",punto2,"es ",punto1.manhattan(punto2))
punto1.saluda("Iván")
punto2.saluda("Pedro")



#print(punto1.__doc__)
#print(punto1.cuadrante.__doc__)

print((punto1+punto2).saluda("Iván"))


print(Punto.sumar(Punto(2,3),Punto(4,5)))
print(Punto.punto_aleatorio())
p1=Punto(2,3)
del p1
print(p1.cuadrante())
"""