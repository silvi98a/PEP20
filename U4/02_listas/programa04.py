# Programa 04: Operaciones con dos listas de palabras (sin repeticiones)
lista1 = ["manzana", "pera", "plátano", "manzana", "kiwi", "uva"]
lista2 = ["pera", "naranja", "kiwi", "uva", "naranja", "melocotón"]

# Eliminar elementos repetidos en cada lista individualmente
lista1 = list(set(lista1))
lista2 = list(set(lista2))

print(f"Lista 1 (sin repetidos): {lista1}")
print(f"Lista 2 (sin repetidos): {lista2}")

# 1. Palabras que aparecen en las dos listas (Intersección)
comunes = [p for p in lista1 if p in lista2]
print(f"\nPalabras que aparecen en las dos listas: {comunes}")

# 2. Palabras que aparecen en la primera, pero no en la segunda
solo_lista1 = [p for p in lista1 if p not in lista2]
print(f"Palabras solo en la primera lista: {solo_lista1}")

# 3. Palabras que aparecen en la segunda, pero no en la primera
solo_lista2 = [p for p in lista2 if p not in lista1]
print(f"Palabras solo en la segunda lista: {solo_lista2}")

# 4. Palabras que aparecen en ambas listas (Unión sin repetir)
ambas_unidas = list(set(lista1 + lista2))
print(f"Palabras que aparecen en ambas listas (unión): {ambas_unidas}")