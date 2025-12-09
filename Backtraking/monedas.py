def busca_combinaciones(monedas, objetivo, combinacion, soluciones):
    # Caso base: si la suma actual es igual al objetivo → guardamos la combinación
    if sum(combinacion) == objetivo:
        soluciones.append(combinacion[:])  # [:] = copia de la lista, no referencia
        return

    # Caso de corte: si la suma se pasa del objetivo → no seguimos
    if sum(combinacion) > objetivo:
        return

    # Paso recursivo: probar cada moneda
    for moneda in monedas:
        combinacion.append(moneda)  # anotar (añadir moneda)
        busca_combinaciones(monedas, objetivo, combinacion, soluciones)  # explorar
        combinacion.pop()  # desanotar (quitar moneda para retroceder)


# Datos iniciales
monedas = [1, 2, 5, 4]
objetivo = 5
soluciones = []

busca_combinaciones(monedas, objetivo, [], soluciones)

# Mostrar resultados
for s in soluciones:
    print(s)
