nombres=[]
notas=[]

for x in range(3):
    nom=input("Ingresa el nombre del alumno: ")
    nombres.append(nom)
    
    no1=int(input("Ingresa la primer nota: "))
    no2=int(input("Ingresa la segunda nota: "))
    notas.append([no1,no2])
    
for x in range(3):
    print(nombres[x], notas[x][0], notas[x][1])