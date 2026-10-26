import sys

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

if (len(sys.argv) < 2 or sys.argv is None):
    print('Uso: saludar <nombre> <apellido>')
else:
    nombre = sys.argv[1]
    apellido = sys.argv[2]
    print(f"Hola {nombre} {apellido}")