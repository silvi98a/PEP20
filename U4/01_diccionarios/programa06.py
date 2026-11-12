# Programa 06: Eliminación de elementos
datos = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Original: {datos}")

# Eliminar con del
del datos["a"]
print(f"Tras eliminar 'a' con del: {datos}")

# Eliminar con pop() y mostrar el valor eliminado
eliminado = datos.pop("b")
print(f"Valor eliminado con pop('b'): {eliminado}")
print(f"Diccionario tras pop: {datos}")

# Vaciar con clear()
datos.clear()
print(f"Tras clear(): {datos}")

# Reasignar a {}
datos = {}
print(f"Reasignado a {{}}: {datos}")