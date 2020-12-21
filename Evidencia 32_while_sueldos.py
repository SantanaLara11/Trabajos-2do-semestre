n=int(input("Cuantos empleados hay en la empresa: "))
x=1
conta1=0
conta2=0
gastos=0

while x<=n:
    sueldo=float(input("Ingresa el sueldo del empleado: "))
    if sueldo<=300:
        conta1=conta1 + 1
    else:
        conta2=conta2 + 1
    gastos=gastos + sueldo
    x=x + 1

print(f"La cantidad de empleados que hay con sueldos entre 100 y 300 es: {conta1}")
print(f"La cantidad de empleados con sueldos mayor a 300 es: {conta2}")
print(f"Los gastos de la empresa son: {gastos}")
