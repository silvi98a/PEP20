# Programa 09: Tuplas multidimensionales y mutabilidad
# Tabla 3x3 (tupla de tuplas)
tabla = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Elementos de la tabla 3x3:")
for fila in tabla:
    for elemento in fila:
        print(elemento, end=" ")
    print()

# Tupla que contiene listas (mutabilidad interna)
tupla_con_listas = ([1, 2], [3, 4])
print(f"\nTupla original con listas: {tupla_con_listas}")

# Modificamos la lista interna (la tupla en sí no cambia, pero su contenido mutable sí)
tupla_con_listas[0][0] = 99
print(f"Tupla tras modificar la lista interna: {tupla_con_listas}")