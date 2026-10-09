from math import sin, cos, sqrt, pow, radians

print("¿Qué operación quieres hacer?")
print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números")

opcion = int(input("Elige una opción (1-4): "))

if opcion == 1:
    angulo = float(input("Introduce el ángulo en grados: "))
    resultado = sin(radians(angulo))
    print(f"El seno de {angulo}º es {resultado}")
elif opcion == 2:
    angulo = float(input("Introduce el ángulo en grados: "))
    resultado = cos(radians(angulo))
    print(f"El coseno de {angulo}º es {resultado}")
elif opcion == 3:
    numero = float(input("Introduce un número: "))
    resultado = sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {resultado}")
elif opcion == 4:
    base = float(input("Introduce la base: "))
    exponente = float(input("Introduce el exponente: "))
    resultado = pow(base, exponente)
    print(f"{base} elevado a {exponente} es {resultado}")
else:
    print("Opción no válida")