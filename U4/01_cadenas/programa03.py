# Programa 03: Formato con str.format y f-strings
nombre = "Silvia"
curso = "2º DAW"
anno = 2026

# Muestra con str.format()
mensaje_format = "Hola, mi nombre es {}, estoy en el curso {} en el año {}.".format(nombre, curso, anno)
print(mensaje_format)

# Muestra con f-strings
mensaje_fstring = f"Hola, mi nombre es {nombre}, estoy en el curso {curso} en el año {anno}."
print(mensaje_fstring)

# Resultado de una operación matemática con un f-string
num1, num2 = 15, 27
print(f"El resultado de sumar {num1} + {num2} es {num1 + num2}")