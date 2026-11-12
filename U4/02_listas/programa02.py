# Programa 02: Temperaturas mínimas y máximas de 5 días (Lista 2D)
temperaturas = []

print("Introduce las temperaturas de 5 días:")
for i in range(5):
    print(f"\nDía {i + 1}:")
    t_min = float(input("  Temperatura mínima: "))
    t_max = float(input("  Temperatura máxima: "))
    temperaturas.append([t_min, t_max])

# 1. Temperatura media de cada día
print("\n--- Temperatura media de cada día ---")
for i, (t_min, t_max) in enumerate(temperaturas, 1):
    media = (t_min + t_max) / 2
    print(f"Día {i}: {media:.2f}ºC")

# 2. Días con menos temperatura (menor temperatura mínima global)
minimas = [d[0] for d in temperaturas]
menor_temp = min(minimas)
dias_menor_temp = [i + 1 for i, t in enumerate(temperaturas) if t[0] == menor_temp]
print(f"\nDía(s) con menor temperatura ({menor_temp}ºC): {dias_menor_temp}")

# 3. Buscar días que coincidan con una temperatura máxima introducida
buscar_max = float(input("\nIntroduce una temperatura máxima a buscar: "))
dias_coincidentes = [i + 1 for i, t in enumerate(temperaturas) if t[1] == buscar_max]

if dias_coincidentes:
    print(f"Día(s) cuya temperatura máxima coincide con {buscar_max}ºC: {dias_coincidentes}")
else:
    print(f"Información: Ningún día tiene una temperatura máxima de {buscar_max}ºC.")