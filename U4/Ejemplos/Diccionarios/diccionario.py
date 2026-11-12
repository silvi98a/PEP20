# Los diccionarios son desordenados

diccionario = {1: "Harry potter", 2: "Willo", 3: "Matrix"}
print(diccionario)

diccionario1 = {"almeria": 22.5, "granada": 23.7, "malaga": 21.9}
print(diccionario1)

persona = {
    "nombre": "Juana",
    "apellidos": "García",
    "edad": 105,
    "pais": "España",
    "lenguajes": ["JavaScript", "Java", "SQL", "C", "Python"],
    "direccion": {"calle": "Alcala", "numero": 33},
}
print(persona)


persona1 = {
    "nombre": "Luis",
    "apellidos": "García",
    "edad": 30,
    "pais": "España",
    "lenguajes": ["JavaScript", "Java", "SQL", "C", "Python"],
    "direccion": {"calle": "Alcala", "numero": 33},
}

print(persona1["nombre"])  # imprimen lo mismo
print(persona1.get("nombre"))

persona1["altura"] = 1.8
persona1["altura"] = 2
persona1["nombre"] = "Ana"

print(persona1)

print(len(persona1))  # sale 7 porque se le ha añadido altura en la línea 32
print(persona1.keys())
print(persona1.values())

print(persona1.items())  # me da una lista de las tuplas ¿?¿?¿ confirmar esto
