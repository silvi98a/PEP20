print("Introduce un número: ")
n = int(input())

while n > 0:
    print(n)
    n = n-1
    if n == 6:
        break

else:
    print("No se ha ejecutado el break.")