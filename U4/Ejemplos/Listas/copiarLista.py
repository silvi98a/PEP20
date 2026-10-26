lista1 = ["Hola", "Adios", "gg", "aa"]
lista2 = [1231, 1, 12, 543243, 123]

lista1 = (
    lista2.copy()
)  # esto crea un objeto nuevo, copiando los elementos de otra lista.
print(lista1)


lista1.reverse()
print(lista1)

lista_nueva=list(reversed(lista1))
print(lista_nueva)
