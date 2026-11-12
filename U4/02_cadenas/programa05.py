# Programa 05: Mejorando el cifrado César (desplazamiento 1-25, mayúsculas/minúsculas y caracteres no alfabéticos intactos)
def cifrar_cesar_mejorado(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Definimos el límite base según si es mayúscula o minúscula
            limite = ord('A') if char.isupper() else ord('a')
            # Aplicamos desplazamiento cíclico de 26 letras
            cifrado_char = chr((ord(char) - limite + desplazamiento) % 26 + limite)
            resultado += cifrado_char
        else:
            resultado += char
    return resultado

# Programa principal
texto_usuario = input("Introduce una línea de texto para cifrar: ")

# Validación de la entrada del valor de cambio (rango 1..25)
while True:
    try:
        desplazamiento = int(input("Introduce un valor de cambio (número entero del 1 al 25): "))
        if 1 <= desplazamiento <= 25:
            break
        else:
            print("Error: El número debe estar estrictamente en el rango de 1 a 25.")
    except ValueError:
        print("Error: Debes introducir un número entero válido.")

texto_cifrado = cifrar_cesar_mejorado(texto_usuario, desplazamiento)
print(f"Texto cifrado: {texto_cifrado}")