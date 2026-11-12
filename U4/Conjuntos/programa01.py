# Programa 01: Creación de conjuntos
conjunto_enteros = {1, 2, 3, 4, 5}
conjunto_cadenas = {"manzana", "pera", "plátano"}
conjunto_vacio = set()

print(f"Conjunto de enteros: {conjunto_enteros}")
print(f"Conjunto de cadenas: {conjunto_cadenas}")
print(f"Tipo del conjunto vacío: {type(conjunto_vacio)}")

# Comprobación de que no permite duplicados
duplicados = {1, 2, 2, 3, 3, 3, 4}
print(f"Conjunto con elementos repetidos (elimina duplicados): {duplicados}")