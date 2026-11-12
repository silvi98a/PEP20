# Programa 05: Función mysplit() personalizada
def mysplit(cadena):
    # Si la cadena está vacía o solo contiene espacios, devuelve lista vacía
    if not cadena or cadena.isspace():
        return []
    
    palabras = []
    palabra_actual = ""
    
    for char in cadena:
        if char == " ":
            if palabra_actual:
                palabras.append(palabra_actual)
                palabra_actual = ""
        else:
            palabra_actual += char
            
    # Añadir la última palabra si quedó pendiente
    if palabra_actual:
        palabras.append(palabra_actual)
        
    return palabras

# Pruebas de la función
texto_prueba1 = "Hola mundo desde Python"
print(f"Prueba 1 ('{texto_prueba1}'):")
print(mysplit(texto_prueba1))

texto_prueba2 = "   Espacios   al   principio y final   "
print(f"\nPrueba 2 ('{texto_prueba2}'):")
print(mysplit(texto_prueba2))

texto_prueba3 = ""
print(f"\nPrueba 3 (Cadena vacía):")
print(mysplit(texto_prueba3))