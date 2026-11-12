# Programa 02: Cálculo de la media de notas de alumnos usando diccionarios y tuplas
alumnos = {}

print("Introduce alumnos y calificaciones (nombre vacío para terminar):")
while True:
    nombre = input("Nombre del alumno: ").strip()
    if not nombre:
        break
    
    try:
        nota = float(input(f"Calificación de {nombre}: "))
    except ValueError:
        print("Error: La calificación debe ser un número.")
        continue
    
    # Si el alumno ya existe, añadimos la nota a su tupla existente
    if nombre in alumnos:
        alumnos[nombre] += (nota,)
    else:
        alumnos[nombre] = (nota,)

print("\n--- Promedio de calificaciones por alumno ---")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"- {nombre}: {promedio:.2f} (Notas: {notas})")