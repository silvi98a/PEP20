# Programa 06: Concatenación, repetición y copia
t1 = (1, 2)
t2 = (3, 4)

concatenada = t1 + t2
repetida = t1 * 2

print(f"Concatenación: {concatenada}")
print(f"Repetición: {repetida}")

copia = concatenada
print(f"ID de concatenada: {id(concatenada)}")
print(f"ID de copia: {id(copia)}")
print(f"¿Apuntan al mismo objeto?: {concatenada is copia}")