# Programa 08: Comprensión de diccionarios
# Frecuencia de elementos en una lista
palabras = ["ana", "luis", "ana", "pedro", "luis", "ana"]
frecuencia = {p: palabras.count(p) for p in palabras}
print(f"Frecuencia de palabras: {frecuencia}")

# Números del 1 al 5 con sus cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"Diccionario de cuadrados: {cuadrados}")