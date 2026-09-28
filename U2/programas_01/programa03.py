print("Dame dos números para dividirlos.")
n1 = int(input())
n2 = int(input())

try:
    print(n1/n2)
except ZeroDivisionError:
    print("No se puede dividir entre 0.")