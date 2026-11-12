# Programa 06: Relaciones entre conjuntos
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s3 = {6, 7, 8}

print(f"¿s1 es subconjunto de s2? (issubset): {s1.issubset(s2)}")
print(f"¿s2 es superconjunto de s1? (issuperset): {s2.issuperset(s1)}")
print(f"¿s1 y s3 son disjuntos? (isdisjoint): {s1.isdisjoint(s3)}")