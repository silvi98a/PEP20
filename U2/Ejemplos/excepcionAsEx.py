print("Introduce tu edad: ")

try:
    n = int(input())

    if n>5:
        print("Hola")
    else:
        print(10/n)

except Exception as ex:
    print(ex)

#No es una buena práctica porque esto captura el error
#de manera general y es mejor hacerlo individual.