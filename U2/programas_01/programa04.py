print("Pon tu nota")
nota = int(input())

match nota:
    case 0 | 1 | 2 | 3 | 4:
        print("Insuficiente.")
    case 5:
        print("Suficiente.")
    case 6:
        print("Bien.")
    case 7 | 8:
        print("Notable.")
    case 9 | 10:
        print("Sobresaliente.")
    case _:
        print("Error: la nota no es válida.")
# El case _: si no se pone nada de los valores que hay
# en los otros case (1,2 .. 10), saldrá por defecto el case _
