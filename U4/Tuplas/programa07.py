# Programa 07: Desempaquetado y empaquetado de argumentos
# Desempaquetado simple
tupla_tres = (10, 20, 30)
a, b, c = tupla_tres
print(f"Desempaquetado: a={a}, b={b}, c={c}")

# Desempaquetado extendido
primero, *medio, ultimo = (1, 2, 3, 4, 5)
print(f"Extendido: primero={primero}, medio={medio}, último={ultimo}")

# Función media(*args)
def media(*args):
    return sum(args) / len(args) if args else 0

print(f"Media de (10, 20, 30): {media(10, 20, 30)}")
print(f"Media de (5, 5, 5, 5, 10): {media(5, 5, 5, 5, 10)}")