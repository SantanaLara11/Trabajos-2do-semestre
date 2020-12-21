cantidad=0

n=int(input("Cuantos valores ingresara: "))

for f in range(n):
    valor=int(input("Ingresa el valor: "))
    
    if valor>=1000:
        cantidad= cantidad + 1

print(f"La cantidad de valores ingresados mayores o iguales a 1000 son: {cantidad}")