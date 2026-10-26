lista1 = ["Hola", "Adios", 1, 89, True]
lista2 = [] #lista vacia, se recomienda esta opción en vez de la siguiente
# lista3 = list() #una lista vacia, mejor usar la anterior.

print(lista1[0]) #da lo mismo
print(lista1[-5]) #da lo mismo

print(lista1[4]) #da lo mismo
print(lista1[-1]) #da lo mismo


lista3=lista1[1:3] #le paso el array de lista1 del elemento 1 al 3
print(lista3)

print(len(lista3))

lista1.append("Nuevo") #añadir elemento a una lista
print(lista1)

lista1 += ["Otro nuevo"] # es lo mismo que poner lista1.append("Otro nuevo")

lista1.insert(1, "hhhhh") #desplaza el resto de elementos
lista1[0] = "dddd"


print(lista1)

lista1[2:4] = ["jjj", "999"] # reemplaza una sección específica de la lista (lista1) por los nuevos elementos de la lista de la derecha
print(lista1)