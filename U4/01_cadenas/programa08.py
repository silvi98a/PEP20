# Programa 08: Búsqueda y conteo
texto = "programación en Python"

# Buscar posición
posicion = texto.find("Python")
print(f"Posición de 'Python': {posicion}")

# Contar apariciones de "o"
conteo_o = texto.count("o")
print(f"Número de veces que aparece la letra 'o': {conteo_o}")

# Verificar inicio y fin
comienza = texto.startswith("pro")
termina = texto.endswith("on")

print(f"¿Comienza por 'pro'?: {comienza}")
print(f"¿Termina por 'on'?: {termina}")