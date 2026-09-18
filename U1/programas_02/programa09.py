ra1 = int(input("Introduce la calificación de RA1: "))
ra2 = int(input("Introduce la calificación de RA2: "))
ra3 = int(input("Introduce la calificación de RA3: "))

media = ra1 * 0.20 + ra2 * 0.60 + ra3 * 0.20

print("La media final del módulo es:", media)

"""
Otra manera de hacerlo
ra1 = ra1 * 20 / 100
ra2 = ra2 * 60 / 100
ra3 = ra3 * 20 / 100

media = ra1 + ra2 + ra3
"""