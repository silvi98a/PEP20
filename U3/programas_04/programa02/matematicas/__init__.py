# Fichero __init__.py del paquete matematicas
# Se ejecuta automáticamente la primera vez que se importa el paquete.

# 1) Metadatos del paquete
__version__ = "1.0"
__author__ = "Tu nombre"

# 2) Importar las funciones más usadas para poder acceder a ellas directamente:
#    from matematicas import suma   (en vez de from matematicas.operaciones import suma)
from .operaciones import suma, resta, multiplicacion, division
from .figuras import area_rectangulo, area_triangulo, area_circulo

# 3) Definir qué se importa con: from matematicas import *
__all__ = [
    "suma",
    "resta",
    "multiplicacion",
    "division",
    "area_rectangulo",
    "area_triangulo",
    "area_circulo",
]

# 4) Código de inicialización (se ejecuta una sola vez al importar el paquete)
print(f"[Paquete matematicas v{__version__} cargado]")
