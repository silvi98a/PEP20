# Programa 02: Conversión entre listas y tuplas
lista_juegos = ["Zelda", "Mario", "Minecraft", "FIFA", "Pokemon"]
print(f"Original (lista): {type(lista_juegos)} -> {lista_juegos}")

tupla_juegos = tuple(lista_juegos)
print(f"Convertido (tupla): {type(tupla_juegos)} -> {tupla_juegos}")

lista_nuevamente = list(tupla_juegos)
print(f"Reconvertido (lista): {type(lista_nuevamente)} -> {lista_nuevamente}")