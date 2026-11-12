# Programa 05: Métodos y pertenencia
tupla = (1, 2, 3, 2, 4, 2, 5)

print(f"Índice del primer '2': {tupla.index(2)}")
print(f"Número de veces que aparece el '2': {tupla.count(2)}")
print(f"¿Está el 3?: {3 in tupla}")
print(f"¿Está el 10 (not in)?: {10 not in tupla}")