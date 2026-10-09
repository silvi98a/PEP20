# imports de la librería estándar

# imports de librerías de terceros

# imports de módulos propios
import programa01


# Definición de funciones principales
def main():
    """Función principal del programa"""
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print(f"Suma: {programa01.suma(a, b)}")
    print(f"Resta: {programa01.resta(a, b)}")
    print(f"Multiplicación: {programa01.multiplicacion(a, b)}")
    print(f"División: {programa01.division(a, b)}")


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()


# Orden de los imports: primero la librería estándar, luego las de terceros y al final los módulos propios. Es una convención de PEP 8 para que el código sea legible y ordenado.
# def main(): agrupa todo el programa en una función. Lleva un docstring ("""...""") que documenta qué hace.
# if __name__ == "__main__": es la diferencia más importante:
# Si ejecuto el archivo directamente (python main.py), __name__ vale "__main__" y se ejecuta main().
# Si otro archivo lo importa, __name__ vale el nombre del módulo, así que main() no se ejecuta.
# Ventaja de la versión 1: el archivo se puede importar desde otro sin que arranque el programa por sorpresa, y las funciones se pueden reutilizar o probar por separado.
# Con la versión 2: si hiciera import main, se ejecutaría todo el código y empezaría a pedir números por pantalla.
