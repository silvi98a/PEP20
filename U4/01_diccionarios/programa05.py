# Programa 05: Recorrido de diccionarios
configuracion = {"servidor": "localhost", "puerto": 8080, "modo": "debug"}

print("Recorriendo claves:")
for clave in configuracion:
    print(f"- {clave}")

print("\nRecorriendo valores:")
for valor in configuracion.values():
    print(f"- {valor}")

print("\nRecorriendo claves y valores (items):")
for clave, valor in configuracion.items():
    print(f"- {clave}: {valor}")
