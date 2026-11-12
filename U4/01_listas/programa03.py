# Programa 03: Slicing y reverso
lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice desde el índice 2 hasta el 5 (excluido)
sub_lista = lista_original[2:6]
print(f"Slice del 2 al 5: {sub_lista}")

# Elementos en posiciones pares usando incremento de 2
pares_posicion = lista_original[::2]
print(f"Elementos en posiciones pares: {pares_posicion}")

# Reverso con slicing [::-1]
lista_inversa_slicing = lista_original[::-1]
print(f"Invertida con slicing: {lista_inversa_slicing}")

# Reverso con el método reverse() (modifica la lista original)
lista_original.reverse()
print(f"Invertida con reverse(): {lista_original}")