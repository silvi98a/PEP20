# Programa 01: Creación de diccionarios
diccionario_vacio = {}
diccionario_literales = {"nombre": "Ana", "edad": 25, "país": "España"}
diccionario_constructor = dict(nombre="Luis", edad=30, país="México")

print(f"Diccionario vacío: {diccionario_vacio} | Tipo: {type(diccionario_vacio)}")
print(f"Diccionario con llaves: {diccionario_literales} | Tipo: {type(diccionario_literales)}")
print(f"Diccionario con dict(): {diccionario_constructor} | Tipo: {type(diccionario_constructor)}")