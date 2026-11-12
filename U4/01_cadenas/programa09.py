# Programa 09: Unicode y ASCII
emoji = "🐍"
codigo_ord = ord(emoji)
codigo_hex = hex(codigo_ord)
print(f"Emoji: {emoji} -> Código ord(): {codigo_ord}, en Hexadecimal: {codigo_hex}")

# Crear carácter a partir de código numérico
caracter_creado = chr(65)
print(f"Carácter con chr(65): {caracter_creado}")

# Imprimir caracteres ASCII del 48 al 57 (dígitos) en una sola línea
print("Caracteres ASCII del 48 al 57:", end=" ")
for i in range(48, 58):
    print(chr(i), end=" ")
print()  # Salto de línea final