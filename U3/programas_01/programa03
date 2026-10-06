import math

seguir = True


def calcular_area_circulo(radio):
    area = (radio * radio) * math.pi
    return area


# def calcular_area_circulo(radio):
#   return (radio * radio) * math.pi


def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area


while seguir == True:
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")
    opc = int(input("Introduce una opción: "))

    match opc:
        case 1:
            print("1. Calcular el área de un círculo")
            radio = float(input("Dame el radio del circulo: "))
            resultado = calcular_area_circulo(radio)
            print(f"El área del círculo es {resultado:.2f}")

        case 2:
            print("2. Calcular el área de un triángulo")
            baseTri = float(input("Dame la base del triangulo: "))
            hTri = float(input("Dame la altura del triangulo: "))
            resultado = calcular_area_triangulo(baseTri, hTri)
            print(f"El área del triángulo es {resultado:.2f}")

        case 3:
            print("3. Calcular el área de un rectángulo")
            baseRec = float(input("Dame la base del rectangulo: "))
            hRec = float(input("Dame la altura del rectangulo: "))
            resultado = calcular_area_rectangulo(baseRec, hRec)
            print(f"El área del rectángulo es {resultado:.2f}")

        case 4:
            print("Programa terminado.")
            seguir = False


# Con coma (la más simple)
# print("El área del círculo es", resultado)

# Con f-string (la más recomendada)
# print(f"El área del círculo es {resultado}")

# Con f-string y redondeo a 2 decimales
# print(f"El área del círculo es {resultado:.2f}")
