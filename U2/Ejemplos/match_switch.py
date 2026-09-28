print("Introduce tu edad: ")
edad = int(input())

match edad:
    case 10:
        print("No puedes ver la película")

    case 9:
        print("Has tenido suerte, es gratis")
    
    case 8:
        print("Nada")

    case _: 
        print("Adiós")

    # El case _: es que si no se pone nada, saldrá por defecto (default)
