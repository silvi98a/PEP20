# Programa 07: Copia y actualización
colores = {"rojo", "verde", "azul"}

copia_colores = colores.copy()
print(f"ID original: {id(colores)}")
print(f"ID copia: {id(copia_colores)}")

otros_colores = {"amarillo", "morado"}
print(f"Antes de update(): {colores}")

colores.update(otros_colores)
print(f"Después de update(): {colores}")