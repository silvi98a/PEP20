# Programa 08: Compresión de listas
# Lista con 30 veces la palabra "Vacío"
lista_vacio = ["Vacío" for _ in range(30)]
print(lista_vacio)

print(f"Lista 'Vacío' (longitud {len(lista_vacio)}): {lista_vacio[:5]}...")

# Lista con los 10 primeros números pares
primeros_pares = [i * 2 for i in range(10)]
print(f"Primeros 10 números pares: {primeros_pares}")