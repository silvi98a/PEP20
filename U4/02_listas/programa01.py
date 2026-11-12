# Programa 01: Lectura de números hasta negativo, máximo y pares
numeros = []

print("Introduce números (introduce un número negativo para terminar):")
while True:
    num = int(input("Número: "))
    if num < 0:
        break
    numeros.append(num)

if numeros:
    print(f"\nNúmero máximo de la lista: {max(numeros)}")
    
    # Filtrar números pares
    pares = [n for n in numeros if n % 2 == 0]
    print(f"Números pares de la lista: {pares}")
else:
    print("No se introdujo ningún número válido.")