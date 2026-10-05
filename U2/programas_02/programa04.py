# bucle infinito con break
while True:
    numero = int(input("Introduce un número: "))
    if numero == 45:
        print("¡Has dejado el bucle con éxito!")
        break

# sin break, el while controla la condición de salida
numero = int(input("Introduce un número: "))
while numero != 45:
    numero = int(input("Introduce un número: "))
print("¡Has dejado el bucle con éxito!")
