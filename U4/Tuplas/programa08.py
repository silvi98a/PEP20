# Programa 08: Tuplas y cadenas
texto = "Programación en Python muy sencilla"

# Split a lista y conversión a tupla
tupla_palabras = tuple(texto.split())
print(f"Tupla desde cadena: {tupla_palabras}")

# Join de tupla a cadena separada por guiones
cadena_guiones = "-".join(tupla_palabras)
print(f"Unida por guiones: {cadena_guiones}")

# Partition (devuelve tupla)
resultado_partition = texto.partition("Python")
print(f"Resultado partition(): {resultado_partition}")