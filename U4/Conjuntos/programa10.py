# Programa 10: Aplicación práctica con conjuntos
lista_palabras = ["python", "java", "python", "c++", "java", "ruby"]
print(f"Lista original con duplicados: {lista_palabras}")

# Convertir a conjunto para eliminar duplicados
unicos = set(lista_palabras)

# Pedir al usuario una palabra
palabra_usuario = input("Introduce una palabra a buscar: ")
if palabra_usuario in unicos:
    print(f"La palabra '{palabra_usuario}' SÍ está en el conjunto de únicos.")
else:
    print(f"La palabra '{palabra_usuario}' NO está en el conjunto de únicos.")

print(f"Conjunto ordenado de palabras únicas: {sorted(unicos)}")
