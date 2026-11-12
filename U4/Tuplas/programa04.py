# Programa 04: Recorrido e iteración múltiple con tuplas
tupla = ("Python", "Java", "C++", "JavaScript")

print("Recorrido simple:")
for lenguaje in tupla:
    print(lenguaje)

print("\nRecorrido con enumerate():")
for i, lenguaje in enumerate(tupla):
    print(f"Índice {i}: {lenguaje}")