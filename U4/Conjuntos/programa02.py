# Programa 02: Añadir y eliminar elementos
frutas = {"manzana", "pera", "plátano"}

frutas.add("naranja")
print(f"Tras add('naranja'): {frutas}")

frutas.remove("pera")
print(f"Tras remove('pera'): {frutas}")

# discard no da error si el elemento no existe
frutas.discard("kiwi")
print(f"Tras discard('kiwi') (inexistente): {frutas}")

elemento_eliminado = frutas.pop()
print(f"Elemento eliminado con pop(): {elemento_eliminado}")
print(f"Conjunto final: {frutas}")