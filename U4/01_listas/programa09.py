# Programa 09: Listas multidimensionales
# Creación usando un bucle for tradicional
pares_for = []
impares_for = []
for i in range(100):
    pares_for.append(i * 2)
    impares_for.append(i * 2 + 1)

multidimensional_for = [pares_for, impares_for]

# Creación usando compresión de listas
multidimensional_comp = [
    [i * 2 for i in range(100)],
    [i * 2 + 1 for i in range(100)]
]

# Recorrer y mostrar por pantalla
print("--- Números pares ---")
for numero in multidimensional_comp[0]:
    print(numero, end=" ")
print("\n\n--- Números impares ---")
for numero in multidimensional_comp[1]:
    print(numero, end=" ")
print()