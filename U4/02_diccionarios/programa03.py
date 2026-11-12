# Programa 03: Gestión de agenda de contactos
agenda = {}

while True:
    print("\n--- MENÚ AGENDA ---")
    print("1. Añadir / Modificar contacto")
    print("2. Eliminar contacto")
    print("3. Mostrar agenda completa")
    print("4. Buscar contacto")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "1":
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el número de teléfono: ")
        agenda[nombre] = telefono
        print(f"Contacto '{nombre}' guardado correctamente.")
        
    elif opcion == "2":
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto '{nombre}' eliminado.")
        else:
            print("El contacto no existe en la agenda.")
            
    elif opcion == "3":
        if agenda:
            print("\n--- Agenda ordenada por nombre ---")
            # Ordenamos por las claves (nombres) alfabéticamente
            for nombre in sorted(agenda):
                print(f"- {nombre}: {agenda[nombre]}")
        else:
            print("La agenda está vacía.")
            
    elif opcion == "4":
        nombre = input("Introduce el nombre a buscar: ")
        if nombre in agenda:
            print(f"Teléfono de {nombre}: {agenda[nombre]}")
        else:
            print(f"El contacto '{nombre}' no existe en la agenda.")
            
    elif opcion == "5":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Elige un número del 1 al 5.")