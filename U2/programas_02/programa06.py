continuar = "s"

while continuar == "s":
    numero = int(input("Introduce un número entre 1 y 10: "))
    while numero < 1 or numero > 10:
        numero = int(input("Número incorrecto. Introduce un número entre 1 y 10: "))

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

    continuar = input("¿Quieres otro número? (s/n): ")

print("Fin")
