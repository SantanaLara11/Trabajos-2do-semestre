sueldos=[]

for x in range(5):
    valor=int(input("Ingresa el sueldo: "))
    sueldos.append(valor)
    
print(f"Lista sin ordenar de los sueldos: {sueldos}")

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print(f"Sueldos de la lista ordenada: {sueldos}")
                    