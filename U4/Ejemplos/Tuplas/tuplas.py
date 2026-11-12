#Repaso LISTAS
lista = [5, 3, "hola", "sss"]  # Lista -> secuencia de objetos ordenados
print(lista)  # también es MUTABLE (se puede modificar)

for e in lista:  # recorrer con un for.
    print(e)

lista[0] = 45
print(lista[0])


tupla = (4, 5, "hola")
print(tupla[1])

for i in tupla:
    print(i)

print(len(tupla))

print(tupla[2:3])

#tupla[0]=9     #ESTO CON LAS TUPLAS NO SE PUEDE HACER
                #Porque las tuplas son INMUTABLES.