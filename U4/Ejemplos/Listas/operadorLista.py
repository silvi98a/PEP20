lista1 = ["Hola", "Adios", 1, 89, True]
lista2 = [3,4]

for e1, e2 in zip (lista1, lista2):
    print(e1, e2)

print(lista1.index(1))

if 1 in lista1:
    print("El 1 está en la lista")

if 2 not in lista1:
    print("El 2 no está en la lista")

print(len(lista1))
print(lista1.index("Hola"))


lista3 = ["Hola", "Adios", "1", "aa"]
lista3.sort() #Ordenar. Tener cuidado si no son del mismo tipo (int y str)
print(lista3)

lista4 = [1231, 1, 12, 543243, 123]
lista4.sort()
print(lista4)

lista5 = sorted(lista2)
print(lista3)

lista2.extend(lista3)
print(lista2)

lista1 = lista2
print(lista1)
print(lista2)
