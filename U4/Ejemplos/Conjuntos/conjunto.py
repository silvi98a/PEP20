#Es una estructura de datos MUTABLE que alamacena objetos únicos y NO ordenados
#Los elementos del conjunto son objetos INMUTABLES

# EL conjunto -> Mutable. Los elementos de dentro del conjunto -> Inmutables

lista = [3,4,[3,4],("hola", 2)]

tupla = (3,2,[4,6])

tupla[2][0] = 10 # esto coge el 4 (que es una lista) de la tupla.
print(tupla)

#CONJUNTO
conjunto1 = {4,4,6,"hola"}
conjunto2 = {4,4,4,4,4,4,6,"hola"}
print(conjunto1)
print(conjunto2)

#En los print sale lo mismo ya que si se repite un valor, solo sale una vez.

print(len(conjunto1))

conjunto1.add(8) #Puedo añadir
conjunto1.remove(4) #Puedo quitar
                    #Pero NO PUEDO modificar ningún elemento
print(conjunto1)

print(4 in conjunto1) #da false

for e in conjunto1:
    print(e)

lista = sorted(conjunto1) #genero una lista del conjunto y le digo que me la ordene