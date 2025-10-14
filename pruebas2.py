lambda lista_parametros: expresion

lambda x: x**2

lista_parametros = [9,2,7,4,5]
print(sorted(lista_parametros))

lista = [{"nombre":"Ruben", "nota": 7},
         {"nombre":"Juan", "nota": 6},
         {"nombre":"Ram", "nota": 4},
         {"nombre":"Adrian", "nota": 8}, ]

#print(sorted(lista, key=lambda x: x["nota"]))
#print(sorted(lista, key=lambda x: x["nota"], reverse=True))

#lista_filtrada= list(filter(lambda x: x["nota"]>5, lista))
#print(lista_filtrada)

iterable=map(lambda x: {**x, "nota":x["nota"]*1.1}, lista)
for i in iterable:
   print(i)