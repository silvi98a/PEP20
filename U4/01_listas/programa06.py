# Programa 06: Listas y cadenas
texto = "Programación en Python facil"

# Usando split()
lista_split = texto.split()
print(f"Lista con split(): {lista_split}")

# Usando partition()
lista_partition = list(texto.partition("en"))
print(f"Lista con partition(): {lista_partition}")

# Crear cadena a partir de una lista separada por guiones
palabras = ["Hola", "mundo", "Python"]
cadena_guiones = "-".join(palabras)
print(f"Cadena unida por guiones: {cadena_guiones}")