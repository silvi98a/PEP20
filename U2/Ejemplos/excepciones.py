print("Introduce tu edad: ")


try:
    n = int(input())

    if n>5:
        print("Hola")
    else:
        print(10/n)

except ValueError:
    print("Algo ha ido mal")
except ZeroDivisionError:
    print("Algo ha ido mal")
else:
    print("No ha habido ninguna excepción") #cuando no hay ninguna excepción
finally:
    print("Siempre") #se usa cuando se trabaja con bases de datos para cerrar
                    # la concexión