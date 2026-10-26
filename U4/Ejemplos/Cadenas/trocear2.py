a = 1
b = 2
cadena = "Hola"
cadena1 = "pepe el pepero"
if "a" in cadena:
    print("La a está dentro de la cadena")
else:
    print("La a no está dentro de la cadena")

if "b" in cadena:
    print("La b está dentro de la cadena")
else:
    print("La b no está dentro de la cadena")

for c in cadena:  # Recorre la cadena de caracteres elemento a elemento
    print(c)

# cadena[0]="T" # no deja porque es inmutable

print(cadena[0])

print(len(cadena))

print(cadena.lower())
print(cadena.upper())
print(cadena.replace("a", "XXX"))
print(cadena1.find("pepero"))  # devuelve el índice en el que está
