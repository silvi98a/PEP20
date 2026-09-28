import random

dado1J1 = random.randrange(1, 7)
dado2J1 = random.randrange(1, 7)
dado1J2 = random.randrange(1, 7)
dado2J2 = random.randrange(1, 7)

totalJ1 = dado1J1 + dado2J1
totalJ2 = dado1J2 + dado2J2

maxJ1 = max(dado1J1, dado2J1) #el max se queda con el dado más alto
maxJ2 = max(dado1J2, dado2J2)

print("Jugador 1:", dado1J1, dado2J1, "-> total", totalJ1)
print("Jugador 2:", dado1J2, dado2J2, "-> total", totalJ2)

if totalJ1>totalJ2:
    print("Gana el jugador 1.") #comparo los totales. Si son distintos, hay ganador
elif totalJ2>totalJ1:
    print("Gana el jugador 2.")
elif maxJ1>maxJ2:
    print("Gana el jugador 1.") #comparo los máximos en el caso de que no haya ganador
elif maxJ2>maxJ1:
    print("Gana el jugador 2.")
else:
    print("Empate.")


