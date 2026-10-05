# Bucle for SIN continue
print("for sin continue:")
for i in range(0, 11):
    if i % 2 == 0:
        print(i)

# Bucle for CON continue
print("\nfor con continue:")
for i in range(0, 11):
    if i % 2 != 0:
        continue  # si es impar, salta a la siguiente iteración
    print(i)

# Bucle while SIN continue
print("\nwhile sin continue:")
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# Bucle while CON continue
print("\nwhile con continue:")
i = -1
while i < 10:
    i += 1  # se incrementa al principio para que continue no provoque un bucle infinito
    if i % 2 != 0:
        continue  # si es impar, salta a la siguiente iteración
    print(i)
