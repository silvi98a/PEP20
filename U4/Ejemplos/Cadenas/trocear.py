cadena = "Hola qué tal"
# el valor final es n-1 IMPORTANTE!!
print(cadena[0:2])
print(cadena[0:4])
print(cadena[2:4])

print(cadena[0:6:2])  # Salta de dos en dos

print(cadena[0 : len(cadena) : 2])  # Muestra el índice par

print(len(cadena))  # longitud de la cadena

print(cadena[len(cadena) - 1])  # siempre es -1
