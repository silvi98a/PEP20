# Programa 02: Reemplazo de todos los dígitos por un carácter introducido por teclado
texto = input("Introduce una cadena de texto: ")
caracter = input("Introduce el carácter de reemplazo (ej. X): ")

# Recorremos la cadena y reemplazamos si es un dígito
resultado = "".join(caracter if c.isdigit() else c for c in texto)

print(f"Resultado: {resultado}")