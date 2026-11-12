# Programa 07: Combinación y copia de diccionarios
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}

# Combinar con el operador |
combinado = d1 | d2
print(f"Diccionario combinado (|): {combinado}")

# Actualizar uno con update()
d1.update(d2)
print(f"d1 actualizado con update(): {d1}")

# Copia y verificación de IDs
copia = d1.copy()
print(f"ID de d1: {id(d1)}")
print(f"ID de copia: {id(copia)}")
print(f"¿Son distintos objetos?: {d1 is not copia}")