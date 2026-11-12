# Programa 02: Acceso a elementos
persona = {"nombre": "Carlos", "edad": 28, "profesión": "Ingeniero"}

# Acceso con corchetes
print(f"Nombre (con corchetes): {persona['nombre']}")
print(f"Edad (con corchetes): {persona['edad']}")

# Acceso con get()
print(f"Profesión (con get): {persona.get('profesión')}")
print(f"Teléfono (con valor por defecto): {persona.get('telefono', 'No disponible')}")

# Acceso a una clave inexistente con get() (devuelve None por defecto)
print(f"Clave inexistente con get(): {persona.get('email')}")