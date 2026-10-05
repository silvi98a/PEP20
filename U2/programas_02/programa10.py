import random

banca = random.randrange(17, 22)
jugadores = int(input("Número de jugadores: "))

for j in range(1, jugadores + 1):
    print("\nJugador", j)
    puntos = 0
    seguir = "s"

    while seguir == "s":
        puntos += random.randrange(1, 6)
        print("Llevas", puntos)
        seguir = input("¿Otra carta? (s/n): ")

    if puntos <= 21 and puntos > banca:
        print("Jugador", j, "gana a la banca")
    else:
        print("Jugador", j, "pierde")

print("\nLa banca tenía", banca)
