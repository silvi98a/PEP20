suma = 0
cantidad = 0

while True:
    n = int(input("Número: "))
    if n == 0:
        break
    suma += n
    cantidad += 1

print("Suma:", suma)
print("Media:", suma / cantidad)



# sin break

suma = 0
cantidad = 0

n = int(input("Número: "))
while n != 0:
    suma += n
    cantidad += 1
    n = int(input("Número: "))

print("Suma:", suma)
print("Media:", suma / cantidad)
