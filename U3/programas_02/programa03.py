import platform
import os

print("Procesador:", platform.processor())
print("Sistema operativo:", platform.system(), platform.release())
print("Versión:", platform.version())
print("Nombre del host:", platform.node())
print("Directorio actual:", os.getcwd())