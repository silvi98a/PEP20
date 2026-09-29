num = int(input("Dame un número entre 1 y 10: "))

while num<1 or num>10: #mientras que num sea menor que 1 o mayor que 10
    print("Tienes que poner un número entre 1 y 10.")
    num = int(input("Dame un número entre 1 y 10: "))

print("Bien. Has escogido un número entre 1 y 10.")