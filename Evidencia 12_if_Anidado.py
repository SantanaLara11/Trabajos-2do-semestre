"""Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:
Si el promedio es >=7 mostrar "Aprobado"
Si el promedio es >=4 y <7 mostrar "Regular"
Si el promedio es <4 mostrar "Reprobado". """

cali1=int(input("Ingresa primer calificación: "))
cali2=int(input("Ingresa segunda calificación: "))
cali3=int(input("Ingresa tercera calificación: "))

promedio=(cali1+cali2+cali3)/3

if promedio>=7:
    print("Aprobado")

else:
    if promedio>=4:
        print("Regular")
    else:
        print("Reprobado")