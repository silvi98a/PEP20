millas = float(input("Introduce un número de millas: "))
km = float(input("Introduce un número de kilómetros: "))

millas_a_km = round(millas * 1.61, 2)
km_a_millas = round(km / 1.61, 2)

print(millas, "millas son", millas_a_km, "km")
print(km, "km son", km_a_millas, "millas")
