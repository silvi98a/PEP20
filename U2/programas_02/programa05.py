numero = int(input("Introduce un número entre 1 y 10: "))

while numero < 1 or numero > 10:
    print("Número no válido. Debe estar entre 1 y 10.")
    numero = int(input("Introduce un número entre 1 y 10: "))

for i in range(1, numero + 1):
    print(i)
