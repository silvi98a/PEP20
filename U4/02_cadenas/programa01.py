# Programa 01: Extracción de usuario y contraseña de una cadena
cadena = "usuario:root|contraseña:123456"

# Dividimos la cadena por el separador '|' y luego cada parte por ':'
partes = cadena.split('|')
usuario = partes[0].split(':')[1]
contrasena = partes[1].split(':')[1]

print(f"Cadena original: {cadena}")
print(f"Usuario: {usuario}")
print(f"Contraseña: {contrasena}")