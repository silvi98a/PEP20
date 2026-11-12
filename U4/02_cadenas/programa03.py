# Programa 03: Análisis de iniciales y palabras que comienzan por minúscula
texto = input("Introduce una cadena de caracteres: ")
palabras = texto.split()

# Primera letra de cada palabra escrita en mayúsculas (formando siglas)
siglas = "".join(p[0].upper() for p in palabras if p)

# Palabras que comienzan por minúscula
minusculas = [p for p in palabras if p and p[0].islower()]

print(f"Texto original: {texto}")
print(f"Primera letra de cada palabra (siglas): {siglas}")
print(f"Palabras que comienzan por minúscula: {minusculas}")