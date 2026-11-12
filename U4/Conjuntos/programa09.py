# Programa 09: Conjuntos inmutables (frozenset)
conjunto_normal = {1, 2, 3}
conjunto_inmutable = frozenset([4, 5, 6])

print(f"Tipo normal: {type(conjunto_normal)}, Contenido: {conjunto_normal}")
print(f"Tipo frozenset: {type(conjunto_inmutable)}, Contenido: {conjunto_inmutable}")

# Intentar añadir un elemento generaría AttributeError (frozenset no tiene método add)
# conjunto_inmutable.add(7) -> Da error

# Usar frozenset como clave de un diccionario
diccionario = {frozenset([1, 2]): "Valor asociado"}
print(f"Diccionario con frozenset como clave: {diccionario}")
