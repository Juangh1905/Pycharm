#Conjuntos
frutas1 = set(["kiwi", "manzana", "pera", "kiwi"])
frutas2 = set(["melocoton", "manzana", "melon"])


print(frutas1, type(frutas1))
frutas3=frutas1.union(frutas2)

print(frutas3, type(frutas3))

if "manzana" in frutas3:
    print("lo q sea")

#Tuplas
tupla=(1,2,3)
print(tupla, type(tupla))

#desempaquetar -> unpacking
variable1, variable2, variable3 = tupla
print(variable1, variable2, variable3)

x,y = 3,4

def funcion_que_devuelve_3_valores():
    return 'aaa','3', 'chocolate'

x,y,z = funcion_que_devuelve_3_valores()
print(x,y,z)

y,_,z = funcion_que_devuelve_3_valores()
print(y,z)

def funcion_que_devuelve_100_valores():
    return tuple([i for i in range(100)])
x,_,_,_,y,z,*_ = funcion_que_devuelve_100_valores()
print(x,y,z)


#zip -> union
vector_alumnos=['paco', 'pepe', 'pedro', 'maria']
vector_notas=[10,8,3,6]
for alumno, notas in zip(vector_alumnos, vector_notas):
    print(alumno, '-->', notas)
