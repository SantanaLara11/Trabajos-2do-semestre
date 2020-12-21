aprobados=0
reprobados=0

for f in range(10):
    notas=int(input("Ingresa la nota: "))
    
    if notas>=7:
        aprobados=aprobados + 1
    else:
        reprobados=reprobados + 1

print(f"La cantidad de aprobados es: {aprobados}")
print(f"La cantidad de reprobados es: {reprobados}")
