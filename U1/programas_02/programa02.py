a = 6
print(type(a))
print(type(6))

b = a
print(type(6))
print(type(b))

print(a is b)
print(a is not b)

a = "Hola"
print(type(a))
print(type("Hola"))

print(isinstance(a, str))
print(isinstance(b, int))
