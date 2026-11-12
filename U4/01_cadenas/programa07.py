# Programa 07: Métodos de cadena
cad = " Hola Mundo "
print(f"Original: '{cad}'")

print(f"upper(): '{cad.upper()}'")
print(f"lower(): '{cad.lower()}'")
print(f"capitalize(): '{cad.capitalize()}'")
print(f"title(): '{cad.title()}'")

# Eliminar espacios
sin_espacios = cad.strip()
print(f"strip(): '{sin_espacios}'")

# Reemplazar
reemplazada = sin_espacios.replace("Mundo", "Python")
print(f"replace(): '{reemplazada}'")

# Dividir en palabras
palabras = reemplazada.split()
print(f"split(): {palabras}")

# Unir lista de palabras
unidas = " - ".join(palabras)
print(f"join(): '{unidas}'")