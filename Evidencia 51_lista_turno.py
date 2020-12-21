sueldosmañana=[]
print("Sueldos turno mañana: ")

for x in range (4):
    valor=float(input("Ingresa sueldo: "))
    sueldosmañana.append(valor)

sueldostarde=[]
print("Sueldos turno tarde: ")

for x in range (4):
    valor=float(input("Ingresa sueldo: "))
    sueldostarde.append(valor)

print(f"Turno mañana: {sueldosmañana}")
print(f"Turno tarde: {sueldostarde}")
