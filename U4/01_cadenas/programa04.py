# Programa 04: Conversión y cadenas crudas
entero = 100
decimal = 45.67
booleano = True

# Conversión a cadena
str_entero = str(entero)
str_decimal = str(decimal)
str_booleano = str(booleano)

print(f"Tipos convertidos a cadena: '{str_entero}', '{str_decimal}', '{str_booleano}'")

# Conversión de cadena a entero y decimal
cad_entero = "50"
cad_decimal = "3.14"

num_entero = int(cad_entero)
num_decimal = float(cad_decimal)

print(f"Cadena a int: {num_entero} (Tipo: {type(num_entero)})")
print(f"Cadena a float: {num_decimal} (Tipo: {type(num_decimal)})")

# Cadena cruda (raw string)
cadena_cruda = r"C:\Users\Nombre\Documentos\archivo.txt"
print(f"Cadena cruda: {cadena_cruda}")