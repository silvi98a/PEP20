def saludar(*args):
    print(args[0])
    print(args[1])
    print(args[2])

saludar("Juan", "Garcia", "1DAW")


# Si lo hago con el for siguiente, es mejor ya que puedo poner lo que yo quiera
# No es limitado como el anterior que le estoy poniendo [0]....
def saludar1(*args):
    for a in args:
        print(a)


saludar1("Juan", "sss")

saludar1("Juan", "sss", "fdfewfw", "vdfver")
# le pongo los argumentos que yo quiera
