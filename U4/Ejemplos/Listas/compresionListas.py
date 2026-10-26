# <expresion> for <elemento> in <lista> if <condicional>

# Crear una lista con 5 cadenas:
lista = ["Hola" for i in range(5)]
print(lista)


lista2 = [i * 2 for i in range(5)]  # 0, 2, 4, 6, 8
print(lista2)

#convertir palabras a mayusculas
palabras = ["hola", "mundo", "python"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)

#Crear una lista con los números pares de los 10 primeros números
listaPar = [i for i in range(1,11) if i%2 == 0]
print(listaPar)