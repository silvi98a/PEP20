# Programa 04: Eliminación y búsqueda
lista = ["manzana", "pera", "plátano", "naranja", "kiwi", "pera"]

# Eliminar el cuarto elemento (índice 3) usando del
del lista[3]
print(f"Tras eliminar el cuarto elemento: {lista}")

# Eliminar un elemento usando remove()
lista.remove("plátano")
print(f"Tras eliminar 'plátano': {lista}")

# Verificar si un elemento pertenece a la lista
existe = "manzana" in lista
print(f"¿'manzana' está en la lista?: {existe}")

# Mostrar el índice de un elemento
indice = lista.index("pera")
print(f"Índice de 'pera': {indice}")

# Número de ocurrencias de un elemento
ocurrencias = lista.count("pera")
print(f"Número de veces que aparece 'pera': {ocurrencias}")