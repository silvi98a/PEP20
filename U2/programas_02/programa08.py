import random

secreto = random.randrange(1, 21)
numero = int(input("Adivina el número (1-20): "))

while numero != secreto:
    if secreto > numero:
        print("El número es mayor")
    else:
        print("El número es menor")
    numero = int(input("Prueba otra vez: "))

print("¡Has acertado!")