def suma_peso(mochila):
    suma = 0
    for peso, valor in mochila:
        suma += peso
    return suma

def suma_valor(mochila):
    suma = 0
    for peso, valor in mochila:
        suma += valor
    return suma

def es_opcion_aceptable(mochila, objeto, peso_max):
    """
    :param mochila:
    :param objeto: tupla peso,valor
    :param peso_max:
    :return:
    """
    return suma_peso(mochila) + objeto[0] <= peso_max

def compara_mochila(mochila1, mochila2):
    """
    TODO
    :param mochila1:
    :param mochila2:
    :return: True si mochila1 tiene más valor que mochila2
    """
    return suma_valor(mochila1) > suma_valor(mochila2)

def copia_mochila(mochila_final, mochila):
    """
    TODO
    copia en mochila_final el contenido de mochila:
        vacía mochila_final y copia todos los elementos de mochila

    :param mochila_final:
    :param mochila:
    :return: None
    """
    mochila_final.clear()
    mochila_final.extend(mochila)

# backtracking
def optimiza_mochila(mochila, mochila_optima, items, peso_max, paso=0):
    for i in range(len(items)):
        objeto = items[i]
        if es_opcion_aceptable(mochila, objeto, peso_max):  # se si me paso o no me paso del peso
            # anotar
            mochila.append(objeto)  # añadir elemento a mochila

            # crear nueva lista sin el objeto actual para evitar modificar la original
            nuevos_items = items[:i] + items[i+1:]

            # acabo de generar una solucion, veo si es la mejor
            if compara_mochila(mochila, mochila_optima):  # si mochila es mejor que mochila optima
                copia_mochila(mochila_optima, mochila)

            # optimizar
            optimiza_mochila(mochila, mochila_optima, nuevos_items, peso_max, paso + 1)

            # desanotar
            mochila.pop()
"""

# backtracking con trazas
def optimiza_mochila(mochila, mochila_optima, items, peso_max, paso=0):
    tab = "    " * paso  # tabulación para mostrar el nivel
    for i in range(len(items)):
        objeto = items[i]
        if es_opcion_aceptable(mochila, objeto, peso_max):
            mochila.append(objeto)
            print(f"{tab}Añado item {objeto} → mochila actual: {mochila}")

            nuevos_items = items[:i] + items[i+1:]

            if compara_mochila(mochila, mochila_optima):
                copia_mochila(mochila_optima, mochila)
                print(f"{tab}✅ Mejor solución hasta ahora: {mochila_optima} (valor: {suma_valor(mochila_optima)}, peso: {suma_peso(mochila_optima)})")

            optimiza_mochila(mochila, mochila_optima, nuevos_items, peso_max, paso + 1)

            mochila.pop()
"""

# ejecución principal
mochila = []  # mochila provisional que vamos generando en cada estado nuevo
mochila_optima = []  # mochila optima
items = [(12, 4), (2, 2), (1, 2), (4, 10), (1, 1)]
peso_max = 15

optimiza_mochila(mochila, mochila_optima, items, peso_max)

print("La mochila óptima vale " + str(suma_valor(mochila_optima)) + " con peso " + str(suma_peso(mochila_optima)))
print(mochila_optima)
