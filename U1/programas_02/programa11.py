hh = int(input("Introduce la hora de salida (HH): "))
mm = int(input("Introduce los minutos de salida (MM): "))
ss = int(input("Introduce los segundos de salida (SS): "))
n = int(input("Introduce la duración del viaje en segundos: "))

segundos_totales = hh * 3600 + mm * 60 + ss + n
segundos_totales = segundos_totales % 86400

hh_llegada = segundos_totales // 3600
mm_llegada = (segundos_totales % 3600) // 60
ss_llegada = segundos_totales % 60

print("Hora de llegada:", hh_llegada, ":", mm_llegada, ":", ss_llegada)