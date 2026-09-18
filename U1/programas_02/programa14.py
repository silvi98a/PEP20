bytes_totales = int(input("Introduce el número de bytes: "))

#decimal (SI)
gb = bytes_totales // 1000000000
resto = bytes_totales % 1000000000
mb = resto // 1000000
resto = resto % 1000000
kb = resto // 1000
b = resto % 1000
print(bytes_totales, "bytes en sistema decimal (SI):", gb, "GB,", mb, "MB,", kb, "KB,", b, "bytes")

#binario (IEC)
gib = bytes_totales // (1024**3)
resto = bytes_totales % (1024**3)
mib = resto // (1024**2)
resto = resto % (1024**2)
kib = resto // 1024
bb = resto % 1024
print(bytes_totales, "bytes en sistema binario (IEC):", gib, "GiB,", mib, "MiB,", kib, "KiB,", bb, "bytes")