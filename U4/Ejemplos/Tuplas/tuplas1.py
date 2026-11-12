#Pasar una tupla a una lista
tupla = (4, 5, "hola")

lista = list(tupla)

for e in lista:
    print(e)

lista[1]=10 #Esto se puede hacer porque se ha pasado a una lista
print(lista[1])