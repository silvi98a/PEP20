# Programa 05: Teoría de conjuntos (operaciones básicas)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Operadores
print(f"Unión (A | B): {A | B}")
print(f"Intersección (A & B): {A & B}")
print(f"Diferencia (A - B): {A - B}")
print(f"Diferencia simétrica (A ^ B): {A ^ B}")

# Métodos
print(f"Unión (método): {A.union(B)}")
print(f"Intersección (método): {A.intersection(B)}")
print(f"Diferencia (método): {A.difference(B)}")
print(f"Diferencia simétrica (método): {A.symmetric_difference(B)}")