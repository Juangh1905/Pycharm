import json

#escribir un json con el contenido de un diccionario
x={"alumno":"juan", "nota": 8}
print(type(x),x)

cadena_x = json.dumps(x) #vuelca un diccionario a formato texto
print(cadena_x)

#leer un diccionario desde un fichero json
with open('mi_fichero_json.txt', "w") as fichero:
    cadena=fichero.read()

x_original=json.loads(cadena)
print(x_original, type(x_original))