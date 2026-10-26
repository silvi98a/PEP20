lista1 = ["Hola", "Adios", 1, 89, True]
print(lista1)

del lista1[1]
print(lista1)

del lista1[1:4] #borra todo menos el primero
print(lista1) 

#lista1.pop()
#print(lista1)

lista2 = ["Hola", "Adios", 1, 89, True]

lista2.remove(1)
print(lista2)

for e in lista2:
    print(e)

for i in range(len(lista1)):
    print(lista2[i])