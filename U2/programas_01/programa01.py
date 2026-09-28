print("Dame un número par")
par = int(input())

print("Dame un número impar")
impar = int(input())

if par % 2 == 0 and impar % 2 != 0:
    print("El primer número es par " ,par, " y el segundo número impar es " ,impar)
else:
    if par % 2 != 0:
        print("El número" ,par, "no es un número par.")
    if impar % 2 == 0:
        print("El número" ,impar, "no es un número impar")