dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

if mes==2: #febrero
    maximo=28
elif mes==4 or mes==6 or mes==9 or mes==11: #los que acaban en 30
    maximo=30
else: 
    maximo=31

# comprobar que el día está entre 1 y el máximo, con el mes entre 1 y 12
if mes>=1 and mes<=12 and dia>=1 and dia<=maximo: 
    print("La fecha es correcta.")
else:
    print("La fecha no es correcta.")