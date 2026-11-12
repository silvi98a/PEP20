# Programa 02: Mutabilidad y manipulación simple
mi_lista01 = [10, "Hola", True, 3.14]

# Modificar el tercer elemento (índice 2)
mi_lista01[2] = False

# Añadir un elemento al final
mi_lista01.append("Nuevo elemento")

# Insertar una cadena en la segunda posición (índice 1)
mi_lista01.insert(1, "Python")

# Recorrer y mostrar elementos
print("Elementos de la lista:")
for elemento in mi_lista01:
    print(elemento)