# Devuelve el número en binario (cadena)
def a_binario(n):
    return bin(n)[2:]


# Devuelve el número en hexadecimal (cadena)
def a_hexadecimal(n):
    return hex(n)[2:]


# Convierte un texto en entero. Devuelve None si no es válido
def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        print("Error: el texto no es un número entero válido")
        return None
