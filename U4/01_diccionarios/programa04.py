# Programa 04: Pertenencia, longitud y métodos básicos
producto = {"id": 101, "nombre": "Teclado", "precio": 45.50, "stock": 15}

# Pertenencia con in y not in
print(f"¿Existe la clave 'precio'?: {'precio' in producto}")
print(f"¿No existe la clave 'descuento'?: {'descuento' not in producto}")

# Número total de elementos
print(f"Total de elementos (len): {len(producto)}")

# Mostrar keys, values e items
print(f"Claves: {producto.keys()}")
print(f"Valores: {producto.values()}")
print(f"Pares (items): {producto.items()}")