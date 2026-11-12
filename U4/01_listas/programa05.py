# Programa 05: Ordenación y manejo de Referencias
# Ordenación modficable vs no modificable
cadenas = ["zara", "antonio", "beatriz"]
cadenas.sort()
print(f"Lista original ordenada con sort(): {cadenas}")

original = ["zara", "antonio", "beatriz"]
ordenada = sorted(original)
print(f"Original sin modificar: {original}")
print(f"Nueva lista con sorted(): {ordenada}")

# Concatenación
lista1 = [1, 2]
lista2 = [3, 4]
concatenada = lista1 + lista2
print(f"Concatenación con +: {concatenada}")

# Ampliar la primera lista
lista1.extend(lista2)
print(f"Lista 1 ampliada con extend(): {lista1}")

# Diferencia de copia (asignación directa)
copia = original
print(f"ID de original: {id(original)}")
print(f"ID de copia: {id(copia)}")