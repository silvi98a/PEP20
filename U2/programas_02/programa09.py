import random

banca = random.randrange(17, 22)
puntos = 0
seguir = "s"

while seguir == "s":
    puntos += random.randrange(1, 6)
    print("Llevas", puntos)
    seguir = input("¿Otra carta? (s/n): ")

print("Banca:", banca)
if puntos <= 21 and puntos > banca:
    print("Ganas")
else:
    print("Pierdes")
