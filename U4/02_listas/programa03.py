# Programa 03: Conteo de palabras en una lista
# Creamos una lista de palabras de ejemplo
palabras = ["gato", "perro", "casa", "gato", "auto", "perro", "gato", "sol"]
print(f"Lista de palabras: {palabras}")

palabra_buscada = input("Introduce la palabra que deseas buscar: ")
conteo = palabras.count(palabra_buscada)

print(f"La palabra '{palabra_buscada}' aparece {conteo} veces en la lista.")