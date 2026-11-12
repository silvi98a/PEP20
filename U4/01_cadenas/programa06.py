# Programa 06: Slicing e iteración
cadena = "Python"

# Extraer "Pyt"
sub_pyt = cadena[:3]
print(f"Subcadena 'Pyt': {sub_pyt}")

# Posiciones pares con slicing ::2
pares = cadena[::2]
print(f"Caracteres en posiciones pares: {pares}")

# Invertir cadena
invertida = cadena[::-1]
print(f"Cadena invertida: {invertida}")

# Recorrido carácter por carácter
print("Recorrido carácter por carácter:")
for char in cadena:
    print(char)