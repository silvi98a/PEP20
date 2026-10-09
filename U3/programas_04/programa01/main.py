# imports de la librería estándar

# imports de librerías de terceros

# imports de módulos propios
from matematicas import operaciones, figuras


# Definición de funciones principales
def main():
    # Función principal del programa
    print("1. Operaciones matemáticas")
    print("2. Cálculo de áreas geométricas")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print("Suma:", operaciones.suma(a, b))
        print("Resta:", operaciones.resta(a, b))
        print("Multiplicación:", operaciones.multiplicacion(a, b))
        if b != 0:
            print("División:", operaciones.division(a, b))
    elif opcion == "2":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        radio = float(input("Radio: "))
        print("Rectángulo:", figuras.area_rectangulo(base, altura))
        print("Triángulo:", figuras.area_triangulo(base, altura))
        print("Círculo:", figuras.area_circulo(radio))
    else:
        print("Opción no válida")


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    main()

# Si borro estas dos últimas líneas, el programa no hace nada (no se llama a main)
# Va enlazado con el def main() de arriba: el def la define y esto la llama
# El if __name__ sirve para que se ejecute main() solo cuando se ejecuta el fichero
# directamente, no cuando otro fichero lo importa
