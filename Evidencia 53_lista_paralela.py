nombres=[]
edades=[]

for x in range(5):
    nombre=input("Ingresa el nombre de la persona: ")
    nombres.append(nombre)
    
    edad=int(input("Ingresa la edad: "))
    edades.append(edad)

print("Nombre de las personas mayores de edad:")

for x in range (5):
    if edades[x]>=18:
        print(nombres[x])
    
