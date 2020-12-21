x=1
conta1=0
conta2=0

while x<=10:
    nota=int(input("Ingresa tu nota: "))
    if nota>=7:
        conta1=conta1+1
    else:
        conta2=conta2+1
    x=x+1

print(f"La cantidad de alumnos con notas menores o iguales a 7 es: {conta1}")
print(f"La cantidad de alumnos con notas menores a 7 es: {conta2}")