# Programa 09: Diccionarios anidados
# Diccionario persona con direccion anidada
persona = {
    "nombre": "Elena",
    "edad": 30,
    "direccion": {
        "calle": "Gran Vía",
        "numero": 42,
        "ciudad": "Madrid"
    }
}

# Acceso a un elemento anidado (número de la calle)
print(f"Número de la calle: {persona['direccion']['numero']}")

# Diccionario familia con varios miembros
familia = {
    "padre": {"nombre": "Juan", "edad": 50},
    "madre": {"nombre": "María", "edad": 48},
    "hijo": {"nombre": "Pablo", "edad": 20}
}

print("\nDatos de la familia:")
for rol, info in familia.items():
    print(f"- {rol.capitalize()}: {info['nombre']}, {info['edad']} años")