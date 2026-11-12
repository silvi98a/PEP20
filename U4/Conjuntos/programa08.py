# Programa 08: Comprensión de conjuntos
conjunto_1_10 = {x for x in range(1, 11)}
cuadrados = {x**2 for x in range(1, 11)}
pares_1_20 = {x for x in range(1, 21) if x % 2 == 0}

print(f"Números del 1 al 10: {conjunto_1_10}")
print(f"Cuadrados del 1 al 10: {cuadrados}")
print(f"Números pares del 1 al 20: {pares_1_20}")