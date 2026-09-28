import random

print("1. Piedra")
print("2. Papel")
print("3. Tijera")
opc = int(input("Seleccione una opción: "))

maquina = random.randrange(1, 4)
print("La máquina ha elegido:", maquina)

if opc == maquina:
    print("Empate.")
elif opc==1 and maquina==3: #piedra vs tijera
    print("Has ganado.")
elif opc==2 and maquina==1: #papel vs piedra
    print("Has ganado.")
elif opc==3 and maquina==2: #tijera vs papel
    print("Has ganado.")
else:
    print("Has perdido.")

# simplificado también se puede poner así, en un SÓLO elif
#elif (opc == 1 and maquina == 3) or (opc == 2 and maquina == 1) or (opc == 3 and maquina == 2):
