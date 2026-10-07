# Variable global (se puede leer desde cualquier función)
contador = 10


def mostrar_global():
    # Solo lee la variable global, no la modifica
    print(f"Dentro de mostrar_global, contador vale {contador}")  # contador vale 10


def crear_local():
    # Este "contador" es LOCAL: no es la global, solo se llama igual
    contador = 99
    print(
        f"Dentro de crear_local, contador local vale {contador}"
    )  # al meterla dentro, vale 99. Fuera valdría 10


def modificar_global():
    # Con "global" le decimos a Python que use la variable de fuera
    global contador
    contador = contador + 1  # cojo el contador que vale 10 y le sumo 1
    print(f"Dentro de modificar_global, contador vale {contador}")  # 11

    # Al usar global contador, la función modifica la variable global de verdad, así que el nuevo valor se mantiene para el resto del programa.


def variable_solo_local():
    dentro = "Soy una variable local" # solo se ve aquí dentor
    print(f"Dentro de variable_solo_local: {dentro}")






print("PROBANDO")
print(f"Fuera de las funciones, contador vale {contador}")

print("\n 1. Leer una variable global ")
mostrar_global()

print("\n 2. Variable local con el mismo nombre ")
crear_local()
print(f"Fuera, contador sigue valiendo {contador}")

print("\n 3. Modificar la variable global ")
modificar_global()
print(f"Fuera, contador ahora vale {contador}")

print("\n 4. Variable que solo existe dentro de la función ")
variable_solo_local()
# print(secreto)   <- Si quitas el #, da NameError porque "secreto" es local
