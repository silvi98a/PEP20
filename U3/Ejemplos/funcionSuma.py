def suma(a, b, *, c):
    return a + b + c


print(suma(2, 8, c=4))
# al poner el * en la función, obliga a poner sí o sí el parámetro.

# al c=4 se le llama parámetro con nombre.
