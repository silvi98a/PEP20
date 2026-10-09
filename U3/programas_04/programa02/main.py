# imports de la librería estándar

# imports de librerías de terceros

# imports de módulos propios
# Gracias al __init__.py se importan directamente las funciones del paquete
import matematicas
from matematicas import suma, resta, multiplicacion, division
from matematicas import area_rectangulo, area_triangulo, area_circulo


# Definición de funciones principales
def main():
    # Función principal del programa
    print("Versión del paquete:", matematicas.__version__)
    print("1. Operaciones matemáticas")
    print("2. Cálculo de áreas geométricas")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print("Suma:", suma(a, b))
        print("Resta:", resta(a, b))
        print("Multiplicación:", multiplicacion(a, b))
        if b != 0:
            print("División:", division(a, b))
    elif opcion == "2":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        radio = float(input("Radio: "))
        print("Rectángulo:", area_rectangulo(base, altura))
        print("Triángulo:", area_triangulo(base, altura))
        print("Círculo:", area_circulo(radio))
    else:
        print("Opción no válida")


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    main()
