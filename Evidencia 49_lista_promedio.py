sueldos=[]
suma=0

for x in range(5):
    valor=float(input("Ingrese el sueldo del operario: "))
    sueldos.append(valor)
    suma=suma + valor

print(f"La lista de sueldos es: {sueldos}")

promedio=suma/5
print(f"El promedio de los sueldos es: {promedio}")

   
    
