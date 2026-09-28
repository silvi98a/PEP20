print("Dime un número par")
par = int(input())

if par % 2 == 0:
    print("Ahora dame el número impar")
    impar = int(input())
    if impar % 2 == 0:
        print("El número" ,impar, "no es impar.")
else:
    print("El número" ,par, "no es par.")