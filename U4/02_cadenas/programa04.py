# Programa 04: Cifrado y descifrado César clásico
def cifrar_cesar(texto):
    cifrado = ""
    for char in texto:
        if char.isalpha():
            if char == 'Z':
                cifrado += 'A'
            else:
                cifrado += chr(ord(char) + 1)
        else:
            cifrado += char
    return cifrado

def descifrar_cesar(texto_cifrado):
    descifrado = ""
    for char in texto_cifrado:
        if char.isalpha():
            if char == 'A':
                descifrado += 'Z'
            else:
                descifrado += chr(ord(char) - 1)
        else:
            descifrado += char
    return descifrado

# Prueba de las funciones
mensaje = "AVE CAESAR"
mensaje_cifrado = cifrar_cesar(mensaje)
mensaje_descifrado = descifrar_cesar(mensaje_cifrado)

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado: {mensaje_cifrado}")
print(f"Mensaje descifrado: {mensaje_descifrado}")