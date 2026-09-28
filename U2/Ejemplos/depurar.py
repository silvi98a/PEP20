numero_secreto = 42

num_intentos = 1

# Leer el intento del usuario como un número entero
intento_usuario = int(input("Por favor, introduce un número (tienes 4 oportunidades): "))

while intento_usuario != numero_secreto and num_intentos < 5:
    print("Incorrecto.")
    intento_usuario = int(input("Por favor, introduce un número: "))
    num_intentos = num_intentos + 1

if intento_usuario == numero_secreto:
    print("¡Correcto!")
else:
    print("Incorrecto. Fin del juego.")
