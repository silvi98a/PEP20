# Programa 01: Contar apariciones de cada palabra en una cadena
cadena = input("Introduce una cadena de texto: ")

# Convertimos a minúsculas para que no distinga entre mayúsculas y minúsculas
palabras = cadena.lower().split()
diccionario_frecuencia = {}

for palabra in palabras:
    # Contamos cuántas veces aparece cada palabra
    diccionario_frecuencia[palabra] = palabras.count(palabra)

print("Apariciones de cada palabra:")
print(diccionario_frecuencia)