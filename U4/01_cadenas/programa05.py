# Programa 05: Operaciones básicas
cad1 = "Hola"
cad2 = "Mundo"

# Concatenación
concatenada = cad1 + " " + cad2
print(f"Concatenación: {concatenada}")

# Repetición
repetida = cad1 * 3
print(f"Repetición: {repetida}")

# Comparación lexicográfica
str_a = "Ana"
str_b = "Bernardo"
if str_a > str_b:
    print(f"'{str_a}' es mayor que '{str_b}' lexicográficamente.")
else:
    print(f"'{str_b}' es mayor que '{str_a}' lexicográficamente.")

# Pertenencia con 'in'
texto = "Programación en Python"
subcadena = "Python"
if subcadena in texto:
    print(f"La subcadena '{subcadena}' sí está presente en el texto.")
else:
    print(f"La subcadena '{subcadena}' no está presente en el texto.")